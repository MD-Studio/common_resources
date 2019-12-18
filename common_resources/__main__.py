# -*- coding: utf-8 -*-

import sys
import os

modulepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if modulepath not in sys.path:
    sys.path.insert(0, modulepath)

from mdstudio.runner import main
from common_resources.resources_endpoints import Common_resources

if __name__ == '__main__':
    main(Common_resources)
