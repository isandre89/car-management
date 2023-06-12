# Car Management System

## Description

This is a car management system that allows you to add, edit, delete and view cars.

## Pre-requisites

- docker >= 24.0.2
- docker-compose >= 1.29.2
- make >= 4.2.1
- pipenv >= 2022.7.4

## Installation

Clone the repository

```bash
git clone git@github.com:isandre89/car-management.git
```

Run the following command to build the docker image

```bash
make build
```

Run the following command to start the docker container and to run the migrations

## Usage

```bash
make up-d
```

Run the following command to shut down the docker container

```bash
make down
```

Run the following command to shut down the docker container and to erase de database

```bash
make clean
```

Run the following command to run the tests

```bash
make tests
```

Run the following command to check the logs

```bash
make logs
```
