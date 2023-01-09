"""uniq test_one -Dc
uniq: вывод всех повторяющихся строк и числа повторений не имеет смысла
"""

import argparse
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from lib import cat

if __name__ == '__main__':
    exit(main())