build:
	sudo docker-compose build

run:
	sudo docker-compose up -d
	sudo docker-compose exec estanistml bash

down:
	sudo docker-compose -f docker-compose.yml down

teste1:
	python3 -m pytest tests/teste1.py

teste2:
	python3 -m pytest tests/teste2.py