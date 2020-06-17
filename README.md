# Accounts&Transactions service
Accounts&Transactions service was created for providing accounts' transactions information

## Installation
- First of all install [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/)
- Build project from root directory: `sudo docker build .`
- Start service: `sudo docker-compose up`
- Run all migrations from web container: `docker-compose exec web python manage.py migrate`
- Finally, go to the url: [http://localhost:8000/](http://localhost:8000/)

**Port 8000 must be available!**    

If you want to stop project, just run: `sudo docker-compose down`
