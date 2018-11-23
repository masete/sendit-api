# sendit-api
Bootcamp 14

## Badges

[![Build Status](https://travis-ci.org/masete/sendit-api.svg?branch=develop)](https://travis-ci.org/masete/sendit-api) [![Maintainability](https://api.codeclimate.com/v1/badges/4ea459fea6b2ed0cdc66/maintainability)](https://codeclimate.com/github/masete/sendit-api/maintainability) [![Coverage Status](https://coveralls.io/repos/github/masete/sendit-api/badge.svg?branch=develop)](https://coveralls.io/github/masete/sendit-api?branch=develop)



## Features 

- Create a parcel delivery order
- Get all parcel delivery orders
- Get a specific parcel delivery order
- Cancel a parcel delivery order
- Get parcels by user id


## API Endpoints

| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| GET | /api/v1/parcel |Fetch all parcel delivery orders|
| GET | api/v1/parcel/&lt;parcel_id&gt; | Fetch a specific parcel delivery order |
| GET | api/v1/users | Fetches all users |
| GET | api/v1/users/&lt;user_id&gt; |parcel | Fetch all parcel delivery orders by a specific user |
| POST | /api/auth/signup | User signup |
| POST | /api/auth/login | Login |
| PUT | /api/v1/parcel/&lt;parcel_id&gt; /cancel | Cancel parcel |

**Getting started with the app**

**Modules and tools used to build the endpoints**

* [Python 3.6](https://docs.python.org/3/)

* [Flask](http://flask.pocoo.org/)


## Installation

Create a new directory and initialize git in it. Clone this repository by running
```sh
$ git clone URL   which in this case is https://github.com/masete/sendit-api.git
```
Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using
```sh
$ virtualenv venv
```
Activate the virtual environment
```sh
$ cd venv/scripts/activate
```
Install the dependencies in the requirements.txt file using pip
```sh

$ pip install -r requirements.txt
```
Populate the requirements.txt using

$ pip freeze  >  requirements.txt
```sh
Start the application by running
```
$ python run.py
```sh

 
The APP is hosted on heroku, checkout this Link: https://sendit-ma.herokuapp.com/

## Author
Masete Nicholas @masete


Hope you had a nice ride
