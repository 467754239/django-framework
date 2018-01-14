import os
from config.base import *

if os.environ.get('DJANGO_DEVELOPMENT') == "Production":
    from config.production import *
else:
    from config.develop import *
