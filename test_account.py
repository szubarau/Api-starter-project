import requests
import json
import pytest
from faker import Faker
from client import Client


@pytest.fixture()
def client():
    return Client()


@pytest.fixture()
def generation_user():
    fake = Faker("en_US")
    return {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()
    }


data = [
    # short login
    {
        "login": "l",
        "email": "email@mail.net",
        "password": "012345"
    },
    # invalid email
    {
        "login": "Username",
        "email": "emailemail.com",
        "password": "012345"
    },
    # short password
    {
        "login": "Username",
        "email": "email@mail.net",
        "password": "1"
    }

]


@pytest.mark.parametrize('data', data)
def test_post_v1_account(data, client):
    response = client.register_user(data)
    assert response.status_code == 400, f"The status code of the server must be 200"

