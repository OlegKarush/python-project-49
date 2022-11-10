
install: # инициализировать виртуальное окружение
	poetry install

brain-games: # запускает brain-games
	poetry run brain-games

brain-even: # запускает brain-even
	poetry run brain-even

brain-calc: # запускает brain-calc
	poetry run brain-calc

brain-gcd: # запускает brain-gcd
	poetry run brain-gcd

brain-progression: # запускает brain_progression
	poetry run brain-progression

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint: # checking the code for compliance with standards
	poetry run flake8 brain_games
