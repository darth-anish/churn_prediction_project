### PROJECT DESCRIPTION

- This project uses trained machine learning model to make predictions on churn of customers in telecommunication industry
- This is a dockerized project running on Django (Gunicorn/Nginx server) and Postgresql database engine
- The visualizations of analysis of the data are employed in the web application
- The django application is hosted on AWS EC2 virtual server.
- The static files are hosted in AWS S3 buckets.

### PROJECT RUNNING STEPS

1) Install docker and docker compose on your system
2) Run command -> sudo docker compose up
3) Go to: 0.0.0.0:8000 or localhost:8000

### IMPORTANT COMMANDS

1) To create super/administrative user -> sudo docker compose exec web  python3 manage.py createsuperuser
2) To make migrations -> sudo docker-compose exec web python3 manage.py make migrations
3) To execute migration -> sudo docker compose exec web python3 manage.py migrate
4) To create an app inside project -> sudo docker compose exec web python3 manage.py startapp prediction
5) Stop docker service -> sudo docker compose down
6) Build container again (If any changes in dockerfile or yml) -> docker compose up --build
7) Collect static files (upload static files locally to aws S3) -> docker compose exec web python3 manage.py collectstatic
8) To get inside dockerised web app -> sudo docker compose exec -it web /bin/bash
9) Restart all containers -> sudo docker compose restart
    
### To connect to postgresql installed inside the docker container in your local host machine, using the following credentials
- host/address: 0.0.0.0:5432
- dbname: postgres (name of the database assigned in environment of docker.yml)
- user: postgres (user of the database assigned in environment of docker.yml)
- password:***** (password of user assigned in environment of docker.yml)
