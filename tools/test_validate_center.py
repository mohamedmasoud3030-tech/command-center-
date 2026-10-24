import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest


class ValidationTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location('validator', Path(__file__).with_name('validate-center.py'))
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ('AGENTS.md', 'PROJECTS.md', 'README.md', 'skills/README.md', 'prompts/START-HERE.md', 'reports/handoffs/INDEX.md'):
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text('# Document\n', encoding='utf-8')
        p = self.root / 'skills/example/SKILL.md'
        p.parent.mkdir()
        p.write_text('---\nname: example\ndescription: Use when reviewing work.\n---\n# Skill\n', encoding='utf-8')

    def test_valid_center(self):
        self.assertEqual(self.module.validate(self.root), [])

    def test_missing_required_document(self):
        (self.root / 'PROJECTS.md').unlink()
        self.assertTrue(any('PROJECTS.md' in e for e in self.module.validate(self.root)))

    def test_broken_relative_link(self):
        (self.root / 'README.md').write_text('[bad](missing.md)\n', encoding='utf-8')
        self.assertTrue(any('missing.md' in e for e in self.module.validate(self.root)))

    def test_external_and_anchor_links_are_not_network_checked(self):
        (self.root / 'README.md').write_text('[web](https://example.com) [section](#title)\n', encoding='utf-8')
        self.assertEqual(self.module.validate(self.root), [])

    def test_wrong_skill_name(self):
        p = self.root / 'skills/example/SKILL.md'
        p.write_text('---\nname: wrong\ndescription: Use when testing.\n---\n', encoding='utf-8')
        self.assertTrue(any('name' in e for e in self.module.validate(self.root)))

    def test_deleted_historical_doc_is_rejected(self):
        p = self.root / 'reports/history.md'
        p.write_text('preserve me', encoding='utf-8')
        def git(*args):
            subprocess.run(['git', '-C', str(self.root), *args], check=True, capture_output=True)
        git('init', '-q')
        git('add', '.')
        git('-c', 'user.name=Test', '-c', 'user.email=test@example.com', 'commit', '-qm', 'baseline')
        p.unlink()
        self.assertTrue(any('reports/history.md' in e for e in self.module.validate(self.root, 'HEAD')))

    def test_unknown_base_fails_closed(self):
        self.assertTrue(any('base' in e for e in self.module.validate(self.root, 'missing-ref')))


if __name__ == '__main__':
    unittest.main()
