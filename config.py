from pathlib import Path
import os

CONFIG_DIR = Path(os.path.expanduser('~/.pylock'))


MASTER_PASS_FILE = os.path.join(CONFIG_DIR, 'master.json')
MASTER_KEY_FILE = os.path.join(CONFIG_DIR, 'master.key')


PASS_FILE = os.path.join(CONFIG_DIR, 'pylock.json')
PASS_KEY_FILE = os.path.join(CONFIG_DIR, 'pylock.key')
