import os
import sys

sys.path.append(os.path.dirname(__name__))

from bootstrap_app import create_app

boot_app = create_app()
boot_app.run(host='0.0.0.0', port=5010)
