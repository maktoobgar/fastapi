# A Simple API

## Requirements
<p align="left">
    <a href="https://www.python.org/downloads/">
        <img alt="Python" src="https://img.shields.io/static/v1?label=Python&message=v3.8.5&color=blue&logo=python&logoColor=blue&style=for-the-badge">
    </a>
    <a href="https://www.python.org/downloads/">
        <img alt="Python" src="https://img.shields.io/pypi/v/fastapi?color=red&label=fastapi&logo=fastapi&logoColor=red&style=for-the-badge">
    </a>
</p>

## About

This repository is one of the two repositories in this organization which is an implementation for comparing how fast adonisjs and fastapi can handle requests.\
This repository is fastapi side.

## Installation

Just for saving time, I'm writing all needed lines to install requirements for api down here.

```
pyhton3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt
uvicorn main:app --reload
```