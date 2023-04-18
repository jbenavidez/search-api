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

 
def test_search_only_q(db, django_db_setup):
    """this test is to test if the search endpoint returns 200 and the data is correct"""
    # Arrange
    res = client.get('/api/search?q=Mathematics')
    # Act
    data = res.json()
    assert isinstance(data['data'], list)
    assert 200==  res.status_code

def test_search_q_plus_include(db, django_db_setup):
    """this test is to test if search endpoint return only data with include keyword"""

    # Arrange
    res = client.get('/api/search?include=Gutmann%20LLC&q=Mathematics')
    # Act
    data = res.json()
    # Assert
    assert data['data'][0]['company'] == 'Gutmann LLC'


def test_check_keys(db, django_db_setup):
    """this test is to test if the search endpoint return a valid list of dicts"""
    # Arrange
    test_obj ={
                'id': 60,
                'first_name': 'Tomlin',
                'last_name': 'Freddi',
                'sex': 'Female',
                'birth_date': '1939-06-17',
                'rating': 7.1,
                'primary_skills': "['Mathematics', 'Code Refactoring']",
                'secondary_skill': "['Secure Code Review', ]",
                'company': 'Mann, Stokes and Christiansen',
                'returned_count': 0,
                'active': False,
                'country': 'United States',
                'language': 'Bengali'
            }
    res = client.get('/api/search?q=Mathematics')
    # Act
    data = res.json()
    s1 = test_obj.keys()
    s2 = data['data'][0].keys()
    assert len(set(s2).difference(s1)) == 0
