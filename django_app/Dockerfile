FROM python:3.10.12

# Set the working directory in the container
WORKDIR /usr/src/djapp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/djapp/requirements.txt
# Install the dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . /usr/src/djapp/

# Install wait-for-it
ADD https://github.com/eficode/wait-for/raw/master/wait-for /wait-for
RUN chmod +x /wait-for

RUN python manage.py collectstatic --no-input

# RUN python manage.py migrate

# Command to run on container start
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# Use wait-for-it to delay execution until db is ready
CMD /wait-for db:5432 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000