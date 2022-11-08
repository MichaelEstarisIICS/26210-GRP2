import pytest 
import json
from requests import get

def get_ip():
    ip = get('https://api.ipify.org').text
    return ip

def test_get_ip(): 
    ip = get_ip()
    loc = get('https://ipapi.co/'+ip+'/json/')
    for key, val in loc.json().items():
        assert key != None
        assert val != None

#def test_get_info():


#def test_get_choice():