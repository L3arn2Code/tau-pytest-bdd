"""
This module contains step definitions for service.feature.
I uses the request package:
https://requests.readthedocs.io/
"""
import requests

from pytest_bdd import scenarios, parsers, given, then

# Shared Variables

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

# Scenarios

scenarios('../features/service.feature', example_converters = dict(phrase=str))

# Steps

@given('the DuckDuckGo is quired with "<phrase>"')
def ddg_response(phrase):
    parameters = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=parameters)
    return response

@then('the response contains results for "<phrase>"')
def ddg_response_contents(ddg_response, phrase):
    assert ddg_response.json()['Heading'].lower() == phrase.lower()

@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code