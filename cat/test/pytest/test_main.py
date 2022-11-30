import sys
import os

try:
    from cat.bin import main
except:
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    from bin import main


