# Integration tests

import pytest
from rest_framework.test import APIClient, APIRequestFactory
from django.core.management import call_command
from django.urls import reverse

client = APIClient()
factory  =APIRequestFactory()

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        # plant the seed
        call_command('seed')

 
def test_Search_only_q(db, django_db_setup):
    """this test is to test if the search endpoint returns 200 and the data is correct"""
    # Arrange
    res = client.get('/api/search?q=Mathematics')
    # Act
    data = res.json()
    assert isinstance(data['data'], list)
    assert 200==  res.status_code