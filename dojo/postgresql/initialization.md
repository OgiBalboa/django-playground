## Initialization
* sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
* sudo su - postgres
* psql
* CREATE DATABASE dbname;
* CREATE USER myprojectuser WITH PASSWORD 'password';
    * ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    * ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
    * ALTER ROLE myprojectuser SET timezone TO 'UTC';
    * GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
    * \q
    * exit
* pip install django psycopg2
* setting.py : 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```