# Built-Budget-API
Proof of concept Get Built Budget API

## Core Technologies:

* Docker
* Flask
* Python >=3.7
* SqlAlchemy + Alembic
* Marshmallow
* Pipenv
* PyTest

## Acceptance Criteria:
* Create a restful API using Built Core Technologies
	- CRUD endpoint for a “Budget Item” using SQLAlchemy (improvise on the fields, but want to see some critical thinking)
	- example leveraging marshmallow schema for validation & serialization
	- example query / migration using SQLAlchemy
	- Testing

* Create a docker-compose to orchestrate the following
	- Flask API from Step 1
	- localstack/localstack
	- MySql >= 5.7 (Docker) https://hub.docker.com/_/mysql
	- Sample Postman collection to your API (you can include the collection.json in Github) -> https://www.postman.com/
	- Demonstrate connectivity between your docker network and localstack using Kinesis (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html)
	- Light record of time spent / decisions made

## Project Record
- Create repo and clone local 
```
git clone git@github.com:hyattdrew11/Built-Budget-API.git
```
- setup virtual environment and requirements
```
cd Built-Budget-API

virtualenv env

source env/bin/activate

python -V

touch requirements.txt

pip install Flask

pip install Flask-SQLAlchemy

pip install mysqlclient

pip install flask-migrate

pip install flask-marshmallow

pip install -U flask-sqlalchemy marshmallow-sqlalchemy

```
- Write some code and setup project base structure
- Initilize the db and migrations
```
flask db init
```
- Migrate the BudgetItem Table
```
flask db migrate -m "Budget Item Table"
flask db upgrade
```
