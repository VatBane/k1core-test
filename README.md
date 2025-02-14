## Overview

Simple applications that reads last block for BTC and ETH 
cryptocurrencies

## Setup

To start application you need perform several steps in next order:

- Run database instance with:
``docker-compose -f ./services/postgres/postgres.yaml up -d``
- Go to ``localhost:5050``, authorize with ``admin@admin.com | root``
- Connect database: right-click Servers->Register->Server, 
set any name what you want, in Connection tab Host ``main-db``, user|pass ``root|root``
- Create 2 databases: in my case ``currency-test`` and ``default-test``
because separated db for every app
- Run redis service with 
``docker-compose -f ./services/redis/redis.yaml up -d``
- Build application with 
``docker build -t test-app .``
- Run ``docker-compose up -d``
- Go to ``localhost:8100/docs`` to see API (maybe will need to wait a little)

### Additional:
- To access admin panel: ``docker exec -it application bash`` 
-> ``python manage.py createsuperuser``
- Go to ``localhost:8101/admin`` to see admin panel

## Not finished tasks

- Both BTC and ETH reading from BlockChair 
because I had issues visiting CoinMarketCap 
(Some JS error, idk)
- Auth is not implemented at all, because I didn't
deal with Django auth services and didn't fully 
understand some custom solutions
- Didn't create script to fully automatically setup environment,
especially databases

## Possible improvements

- implement authentication with JWT, 
probably with SSO like Keycloak
- improve architecture, there is a little mess
when mixing 2 frameworks
- create run script to automate application startup
- add views, because Django is quite good with views operating
