#!C:\Users\liuwenwu\PycharmProjects\pycobertura\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pycobertura==0.10.5','console_scripts','pycobertura'
__requires__ = 'pycobertura==0.10.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pycobertura==0.10.5', 'console_scripts', 'pycobertura')()
    )
