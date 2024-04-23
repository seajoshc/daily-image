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
