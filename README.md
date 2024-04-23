# daily-image

A daily image.

## Scripts

### Migrations

```
docker exec -it daily-image bash -c "python manage.py makemigrations && python manage.py migrate"
```

or just `docker exec -it daily-image bash` and then

```bash
python manage.py makemigrations && python manage.py migrate
```
