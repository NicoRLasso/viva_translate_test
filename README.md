# Viva Translate POC

In this repository live the POC for the backend job at Viva Translate 


## Docker

for running the solution

'''
docker-compose build  
'''

for running the migrations
'''
docker-compose run --rm django python manage.py migrate
'''
for create a SuperUSer
'''
docker-compose run --rm django python manage.py createsuperuser --email admin@example.com --username admin
'''

for start the solution 
'''
docker-compose up
'''

