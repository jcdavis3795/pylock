from pathlib import Path
import os

TEST_DIR = Path(os.path.expanduser('~/.pylock/tests'))

TEST_MASTER_PASS_FILE = os.path.join(TEST_DIR, 'test_master.json')
TEST_MASTER_KEY_FILE = os.path.join(TEST_DIR, 'test_master.key')

TEST_PASS_FILE = os.path.join(TEST_DIR, 'test_pylock.json')
TEST_PASS_KEY_FILE = os.path.join(TEST_DIR, 'test_pylock.key')
