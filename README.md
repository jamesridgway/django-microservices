# Django Microservices
This is a basic and crude project that is design to illustrate some of the concepts behind microservices.

What this project does:

* Specifically this looks to demonstrate the use of correlation IDs and fish tagging.

What this project does NOT do:

* This was put together very quickly, in about an hour and a half. It is not perfect and shortcuts were made.
* This is not a definitive example of what a microservice should be (that is an entirely complicated topic in its own right)

## Microservices
This project contains two microservices:

* Store - an online store where customers place orders
* Warehouse - a warehouse system where the warehouse team can manage orders that have been placed.

The Store system uses an HTTP API call to Warehouse to create an order.

## Correlation IDs
Correlation IDs are designed to tie together log lines that relate to the same context. For example, if a web request is received, all log statements related to the handling of that requesst could contain a correlation ID which is value that can be used to allow you to distinguish these logs from the logs of other requests.

Correlation IDs are often randomly generated.

## Fish Tagging
Fish tagging is a way of using Correlation IDs to chain requests together from different systems.

Instead of generation a Correlation ID at random, an upstream system could set the Correlation ID for the downstream system to use. This allows log messages to be traced between systems where different systems are handling part of the same request.

## This Example
Run the project using docker compose:

    docker-compose up --build


In this project there is a frontend Store system that can accessed from:

    http://0.0.0.0:8000/orders/new/

The store will send a POST request to warehouse to create an order. The API URL is as follows:

    POST http://0.0.0.0:9000/api/orders/

Warehouse will return a response saying that the order was created or failed to be created. Orders starting with an `F` will fail.

Both projects use `django-cid` to provide the correlation ID tagging. I recommend referring to their docs for specific instructions on how to set this up.

In short, for both Store and Warehouse `settings.py` was modified to:

1. Add `django-cid` to the list of installed apps
2. Add the `django-cid` middleware
3. Define a `LOGGING` config that uses the `django-cid` library

Store, sets a `X-Correlation-Id` header in the API request that is sent to Warehouse. `X-Correlation-Id` is the default header that `django-cid` will looks for and will use to set the correlation ID if it is supplied.

As a result, we can see that `e078265e-3e49-424e-8139-619ad7072b38` is the correlation ID which is used to tie together the related log lines between the two systems:

[ TODO - picture ]
