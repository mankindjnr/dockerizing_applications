# Running Dockerized Applications (Django | Postgres | FastAPI)

---

- Install Docker and Docker Compose
- create a parent directory to hold the different projects
- cd into the parent directory
- create a django project [django-admin startproject project_name]
- create a fastapi project [mkdir fastapi_project]
- cd to each project and create a Dockerfile

1. djangoapp/Dockerfile
2. fastapiapp/Dockerfile

- create a docker-compose.yml file in the parent directory
- run `docker-compose up --build` to build and run the containers

## Access the applications

- ### locally
  - Django: http://localhost:8000
  - FastAPI: http://localhost:8001
- ### on a network
  - Django: http://<host_ip>:8000
  - FastAPI: http://<host_ip>:8001

---

Rebuild a single service

```bash
docker-compose up --build <service_name>
```

After rebuilding, you need to restart the fastapi service for the changes to take effect. You can do this with the up command and the --no-deps flag to prevent dependencies from also being restarted:

```bash
docker-compose up --no-deps fastapi
```

These commands will rebuild and restart only the fastapi service, leaving the rest of your Docker Compose stack untouched.

---

In Docker, a volume is a mechanism for persisting data generated by and used by Docker containers. It's essentially a directory on the host machine that is linked to a directory in the Docker container.

In the provided `docker-compose.yml` file, the line `- ./django_app:/app` under `volumes` is creating a volume. Here's what it does:

- `./django_app`: This is the path to the directory on the host machine. The `.` indicates that the `django_app` directory is in the same directory as the `docker-compose.yml` file.

- `:/app`: This is the path in the Docker container where the host directory will be mounted.

So, any changes made in the `django_app` directory on the host machine will be reflected in the `/app` directory in the Docker container, and vice versa. This is particularly useful during development, as it allows you to change your application's code without having to rebuild the Docker image.
