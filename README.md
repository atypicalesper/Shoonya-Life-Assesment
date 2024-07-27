# Developed on Windows 11.

1. Clone the repository.
```sh
git clone 
```
2. Activate the virtual environment
```sh
python -m venv venv
source venv/Scripts/activate
```
3. installing dependencies
```sh
  pip install -r **requirements**.txt
```
4. Run Migration
```sh
  alembic revision -m "first migration"
```
5. Run 
```sh
  python run.py
```

