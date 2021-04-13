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
		* see app/routes.py
	- example leveraging marshmallow schema for validation & serialization
		* see app/routes.py line 42
	- example query / migration using SQLAlchemy
		* see  app/routes.py
		* see migrations directory for migrations
	- Testing
		* see unit_tests/run_test.py

* Create a docker-compose to orchestrate the following
	- Flask API from Step 1
	- localstack/localstack
	- MySql >= 5.7 (Docker) https://hub.docker.com/_/mysql
	- Sample Postman collection to your API (you can include the collection.json in Github) -> https://www.postman.com/
	- Demonstrate connectivity between your docker network and localstack using Kinesis (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html)
	- Light record of time spent / decisions made

## Setup

Assumes you have Docker, Python 3.7, and Virtualenv installed. Also assumes you have an existing AWS Kinesis data stream created and your AWS CLI setup with correct permissions to interact with the Kinesis service. 
```
git clone git@github.com:hyattdrew11/Built-Budget-API.git

cd Built-Budget-API

docker-compose build

docker-compose up
```
## Project Record
Wed. April 8 - Apx. 4 hours work

- Reorient to SQL Alchemy 
- Build project layout
- Build base models
- Read Marshmallow docs as I have never used it before
- Revamp schema definitions for field validation and relationship models
- Run migrations
- Build rest url endpoints and logic
- Test with Postman
- Play with jQuery just to appreciate why we don't use it anymore
- Dive into Docker documentation

Thurs April 9 - Apx. 4 hours work

- Code cleanup
- Wrestle with Docker as I haven't touched it in many months
- Test API with Postman 
- Write unit tests - read pytest basic docs first

## Notes 4-7-2021 - 4-8-2021

- I am still working with unit tests and have begun to explore AWS Kinesis connectivity. 
- I could have just done a basic schema & CRUD for budget items, but that did not make sense in a business context to me as these items would need to be associated with a customer or account in a production environment. Honestly doing a crash course in Marshmallow was quite enjoyable and I see the value in it. It simplifies the validation and serialization from caller and responder in the API. 
- The most time consuming part of this project has been Docker. I do not have a ton of exposure to it. I understand it at a high level, but just need more practice with Docker and BASH. 

## Notes 4-13-2021
- Implemented basic connectivity to an AWS Kinesis data stream by putting data to the stream upon new customer creation in the REST api. I'm not sure how this would look in a production environment, I am assuming IAM roles, but configured my AWS CLI tools with my personal account to test my implementation. 
- I do not feel like I have a full understanding on model / schema definitions with SQL ALchemy and Marshmallow, but was able to implement basic field validation for a new customers email address. Feel like I just need a bit more time with the documentation and perhaps a resource to bounce questions off.