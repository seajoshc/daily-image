# daily-image

A daily image.

## Scripts

`python manage.py runserver`

### Migrations

```
docker exec -it daily-image-web-1 sh "python manage.py makemigrations && python manage.py migrate"
```

or just `docker exec -it daily-image-web-1 sh` and then

```bash
python manage.py makemigrations && python manage.py migrate
```

### Update daily image cronjob

To create a scheduled job in Django, you can use the Django-extensions management command `runscript` in combination with a task scheduler like cron (on Unix-based systems) or Task Scheduler (on Windows). Here's a step-by-step plan:

1. Install Django-extensions by adding it to your `requirements.txt` file or by running `pip install django-extensions`.

2. Add `'django_extensions'` to your `INSTALLED_APPS` in `settings.py`.

3. Create a new script in your Django project. This script will contain the code to update the database record. Let's call it `update_db.py` and put it in a directory named `scripts` at the root of your project.

4. Schedule a job to run this script once per day using cron or Task Scheduler.

Here's how you can implement this:

1. Install Django-extensions:

```bash
pip install django-extensions
```

2. Add `'django_extensions'` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'django_extensions',
    # ...
]
```

3. Create a new script `update_db.py`:

```python
from django.core.management.base import BaseCommand
from myapp.models import Image  # replace with your actual model and app

class Command(BaseCommand):
    help = 'Updates database records'

    def handle(self, *args, **options):
        # replace with your actual update logic
        Image.objects.all().update(is_current_image=False)
```

4. Schedule a job to run this script once per day. If you're on a Unix-based system, you can use cron. Open your crontab file with `crontab -e` and add a new line like this:

```bash
0 0 * * * cd /path/to/your/project && python manage.py runscript update_db
```

This will run the script every day at midnight. Replace `/path/to/your/project` with the actual path to your Django project.

If you're on Windows, you can use Task Scheduler. Create a new task that runs the following command once per day:

```bash
cmd /c "cd \path\to\your\project && python manage.py runscript update_db"
```

Replace `\path\to\your\project` with the actual path to your Django project.

Please note that this is a basic example and you might need to adjust it to fit your needs. For example, you might need to activate your virtual environment before running the script, or you might need to use a different command to update your database records.
