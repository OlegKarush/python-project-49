
install: # инициализировать виртуальное окружение
	poetry install

brain-games: # запускает brain-games
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint: # checking the code for compliance with standards
	poetry run flake8 brain_games
