### PROJECT DESCRIPTION

- This project uses trained machine learning model to make predictions on churn of customers in telecommunication industry
- This is a dockerized project running on Django (native server) and Postgresql database engine
- The visualizations of analysis of the data are employed in the web application

### PROJECT RUNNING STEPS

1) Install docker and docker-compose on your system
2) Run command -> sudo docker-compose up

### IMPORTANT COMMANDS

1) To create super/administrative user -> sudo docker-compose exec web  python3 manage.py createsuperuser
2) To make migrations -> sudo docker-compose exec web python3 manage.py make migrations
3) To execute migration -> sudo docker-compose exec web python3 manage.py migrate
4) To create an app inside project -> sudo docker-compose exec web python3 manage.py startapp prediction
3) Stop docker service -> sudo docker-compose down