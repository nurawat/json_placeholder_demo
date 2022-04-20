# JSON Placeholder API Crawler

This CLI tool uses data from https://jsonplaceholder.typicode.com and combines the data to form a simple count of each of the action that is performed by the users.

## Pre-requisites
Should have python installed.

## Development Setup
```shell
$ userstat
```
## Setup Guide
```shellCancel changes
# Create a Python Virtual Environment for managing package
$ python3 -m venv .venv
$ pip install --upgrade pip
$ source .venv/bin/activate

# Install Dependencies
$ python -m pip install --editable .

> You are all set to use the CLI 

# Create the traefik config file
$ userstat --help
Usage: userstat [OPTIONS]

Options:
  -o, --output [csv|table]  Sets default output format for configuration files
  --help                    Show this message and exit.

Default Output type will be table.
```
## Usage
``` shell
userstat -o [csv|table]
```
> Tool will return the Below columns and data about them.


* ID
* Name
* User_Name
* Email
* Todo-Count
* Post-Count
* Comment-Count
