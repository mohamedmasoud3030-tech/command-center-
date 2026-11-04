"""Self-contained tests for the skill contract gate."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("skill_gate", HERE / "skill_gate.py")
skill_gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skill_gate)


class SkillGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        folder = self.root / "skills" / "financial-correctness"
        folder.mkdir(parents=True)
        self.sample = "---\nname: financial-correctness\ndescription: Use when changing payments or balances.\n---\n# Rules\n"
        (folder / "SKILL.md").write_text(self.sample, encoding="utf-8")
        self.cases = self.root / "skills" / "activation-cases.json"
        self.valid = [
            {"id": "positive", "prompt": "Fix the balance of a cash refund", "expected": ["financial-correctness"], "excluded": []},
            {"id": "negative", "prompt": "Change a footer spelling mistake", "expected": [], "excluded": ["financial-correctness"]},
        ]
        self.cases.write_text(json.dumps(self.valid), encoding="utf-8")

    def check(self, **kwargs):
        return skill_gate.audit(self.root, self.cases, **kwargs)[0]

    def test_valid_canary_contract(self):
        self.assertEqual(self.check(), [])

    def test_missing_positive_is_rejected(self):
        self.cases.write_text(json.dumps(self.valid[1:]), encoding="utf-8")
        self.assertTrue(any("positive" in issue for issue in self.check()))

    def test_unknown_skill_is_rejected(self):
        invalid = self.valid + [{"id": "unknown", "prompt": "More than eight chars of input", "expected": ["imaginary"], "excluded": []}]
        self.cases.write_text(json.dumps(invalid), encoding="utf-8")
        self.assertTrue(any("unknown skill" in issue for issue in self.check()))

    def test_duplicate_prompt_is_rejected(self):
        self.cases.write_text(json.dumps(self.valid + self.valid), encoding="utf-8")
        self.assertTrue(any("duplicate prompt" in issue for issue in self.check()))

    def test_same_expected_and_excluded_is_rejected(self):
        invalid = self.valid + [{"id": "overlap", "prompt": "Should a refund be classified this way", "expected": ["financial-correctness"], "excluded": ["financial-correctness"]}]
        self.cases.write_text(json.dumps(invalid), encoding="utf-8")
        self.assertTrue(any("overlap" in issue for issue in self.check()))

    def test_malformed_values_fail_cleanly(self):
        malformed = self.valid + [{"id": ["bad"], "prompt": "Long enough to validate", "expected": [{"bad": "type"}], "excluded": []}]
        self.cases.write_text(json.dumps(malformed), encoding="utf-8")
        issues = self.check()
        self.assertTrue(any("invalid id" in issue for issue in issues))
        self.assertTrue(any("unknown skill" in issue for issue in issues))

    def test_mismatched_name_is_rejected(self):
        path = self.root / "skills" / "financial-correctness" / "SKILL.md"
        path.write_text(self.sample.replace("name: financial-correctness", "name: other"), encoding="utf-8")
        self.assertTrue(any("mismatched name" in issue for issue in self.check()))

    def test_downstream_drift_is_detected(self):
        downstream = self.root / "project" / ".agents" / "skills" / "financial-correctness"
        downstream.mkdir(parents=True)
        target = downstream / "SKILL.md"
        target.write_text(self.sample, encoding="utf-8")
        self.assertEqual(self.check(downstream=downstream.parent, required=["financial-correctness"]), [])
        target.write_text(self.sample + "modified", encoding="utf-8")
        self.assertTrue(any("drift" in issue for issue in self.check(downstream=downstream.parent)))

    def test_required_missing_downstream_fails(self):
        downstream = self.root / "project" / ".agents" / "skills"
        downstream.mkdir(parents=True)
        self.assertTrue(any("missing" in issue for issue in self.check(downstream=downstream, required=["financial-correctness"])))

    def test_case_validation_does_not_claim_agent_execution(self):
        errors, notices, count = skill_gate.audit(self.root, self.cases)
        self.assertEqual((errors, count), ([], 1))
        self.assertTrue(any("NOT executed" in note for note in notices))


if __name__ == "__main__":
    unittest.main()
