# Note Taker

## Overview

This is a command line application written in python that takes notes and stores them in a PostgreSQL Database

- [Note Taker](#note-taker)
  - [Overview](#overview)
  - [Technical Requirements](#techincal-requirements)
    - [Technologies Used](#technologies-used)
    - [Dependencies](#dependencies)

## Technical Requirements

### Technologies Used

1. Python 3 - the primary language used to develop the app
2. PostgreSQL - A SQL-based database for storing notes

### Dependencies

1. `pip` - to install and manage packages and dependencies of the project
2. `pipenv` - to isolate dependencies locally to a project and setup a virtual dev environment
3. `peewee` - to connect to and manipulate the PostgreSQL Database
4. `pyinstaller` - to generate a single-file build of the app

**Special Mention** - `colors.py` - a module to easily insert BASH color codes into python `print()`'s.
[From dnmellen on github](https://gist.github.com/dnmellen/5584007)

To set up a development environment:

`git clone` this repository, enter `pipenv shell` to enter the **virtual environment**, then `pipenv install` to install all project dependencies.

run `python3 app/db/seed.py` to seed the database and `python3 app/app.py` to start the app.
