# TODO app
A simple TODO application written in DRF

# Install

```bash
  docker-compose up --build
```

Swagger URL: http://localhost:8000/api/v1/swagger

# Note
Чтобы email уведомления работали, нужно указать настройки для EMAIL_HOST_USER и EMAIL_HOST_PASSWORD. Если celery не работает внутри докера, то закомментируйте ENTRYPOINT ["./entrypoint.sh"] внутри Dockerfile
