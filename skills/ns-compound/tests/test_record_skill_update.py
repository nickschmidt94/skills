"""Run with python3 -m unittest discover -s tests from the skill directory."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/record_skill_update.py'


class VersionRecordingTests(unittest.TestCase):
    def run_record(self, metadata, changelog=None):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        content = '---\nname: example\ndescription: Example\n' + metadata + '\n---\n\nKeep this body.\n'
        (root / 'SKILL.md').write_text(content)
        if changelog is not None:
            (root / 'CHANGELOG.md').write_text(changelog)
        result = subprocess.run([sys.executable, str(SCRIPT), str(root), '--summary', 'Preserve behavior', '--date', '2026-09-07'], capture_output=True, text=True)
        return root, content, result

    def test_patch_preserves_body_and_history(self):
        old = '# Changelog\n\n## 1.2.3 - 2026-09-01\n\n- Earlier behavior.\n'
        root, original, result = self.run_record('metadata:\n  version: "1.2.3"', old)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((root / 'SKILL.md').read_text(), original.replace('1.2.3', '1.2.4'))
        log = (root / 'CHANGELOG.md').read_text()
        self.assertIn('## 1.2.4 - 2026-09-07', log)
        self.assertTrue(log.endswith(old.split('\n\n', 1)[1]))

    def test_initial_version(self):
        root, _, result = self.run_record('')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('version: "1.0.0"', (root / 'SKILL.md').read_text())

    def test_unsupported_or_duplicate_versions_leave_files_unchanged(self):
        for metadata in ['metadata:\n  version: "1.2.3" # release', 'metadata:\n    version: "1.2.3"', 'metadata:\n  version: "1.2.3"\n  version: "2.0.0"', 'metadata: {version: "1.2.3"}']:
            with self.subTest(metadata=metadata):
                root, original, result = self.run_record(metadata)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual((root / 'SKILL.md').read_text(), original)
                self.assertFalse((root / 'CHANGELOG.md').exists())

    def test_changelog_conflict_leaves_skill_unchanged(self):
        old = '# Changelog\n\n## 1.2.4 - 2026-09-07\n\n- Existing entry.\n'
        root, original, result = self.run_record('metadata:\n  version: "1.2.3"', old)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((root / 'SKILL.md').read_text(), original)
        self.assertEqual((root / 'CHANGELOG.md').read_text(), old)


if __name__ == '__main__':
    unittest.main()
