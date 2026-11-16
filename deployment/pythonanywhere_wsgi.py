"""Copy into the PythonAnywhere EU Web app WSGI configuration.
No password or token belongs in this file.
"""
import sys
from pathlib import Path

account = Path.home()
root = account / 'qbert-web'
sys.path.insert(0, str(root / 'server'))
from hosted_wsgi import create_application

# Beginner EU accounts use their username as the assigned subdomain.
# Check the actual hostname in Web before reloading the application.
application = create_application(
    root / 'site',
    account / 'qbert-data' / 'leaderboard.sqlite3',
    f'https://{account.name}.eu.pythonanywhere.com',
    'https://eruggie.github.io/',
)
