import os
import subprocess
from django.utils import timezone
from django.conf import settings

def create_backup():
    db_settings = settings.DATABASES['default']
    database_name = 'task'  # Database name as 'task'
    user = 'root'  # Username as 'root'
    password = 'root'  # Password as 'root'

    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    backup_file_name = f'db_backup_{timestamp}.sql'
    backup_file_path = os.path.abspath(os.path.join(settings.BACKUP_DIR, backup_file_name))

    # Use the `mysqldump` path from settings
    mysqldump_path = settings.MYSQLDUMP_PATH

    # Construct the command
    command = [
        mysqldump_path,
        f'--user={user}',
        f'--password={password}',
        '--databases',
        database_name,
        f'--result-file={backup_file_path}',
    ]

    try:
        subprocess.run(command, check=True)
        return backup_file_path
    except subprocess.CalledProcessError:
        return None