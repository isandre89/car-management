build:
	@docker-compose build

migrations:
	@docker-compose run car_management python manage.py makemigrations
	@docker-compose run car_management python manage.py migrate
	@docker-compose restart car_management

up-d:
	@docker-compose up -d
	@make migrations

up:
	@docker-compose up

down:
	@docker-compose down

stop:
	@docker-compose stop

clean:
	@make down
	@rm car_management/db.sqlite3

logs:
	@docker-compose logs -f

tests:
	@export DJANGO_SETTINGS_MODULE=car_management.settings && cd car_management && pytest
	@cd ..
	

