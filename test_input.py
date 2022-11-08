import pytest 
import json
from requests import get

def get_ip():
    ip = get('https://api.ipify.org').text
    return ip

#get IP Address Info
def get_ip_info(ip):
    loc = get('https://ipapi.co/'+ip+'/json/')
    return loc

#get Choice
def get_choice():
    choice = input('Enter number of choice: ') 
    return choice

def test_get_ip(): 
    ip = get_ip()
    loc = get('https://ipapi.co/'+ip+'/json/')
    for key, val in loc.json().items():
        assert key != None
        assert val != None

#def test_get_info():


#def test_get_choice():