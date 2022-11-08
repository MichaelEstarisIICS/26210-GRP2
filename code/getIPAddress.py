#import get function from the requests library
#requests library in order to get API from the website 
from requests import get

#get IP Address
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
    
while True:
    #get user input
    print('(1) Use own IP address')
    print('(2) Manually enter IP address')
    print('(3) Exit')
    choice = get_choice()

    if choice=='1':
        ip = get_ip()

        #print Public IPv4 Address
        print('My public IP address is: {}'.format(ip))

        #run API from ipapi.co
        #API takes an input of an IPv4 Address and gets information
        #based off of it
        loc = get('https://ipapi.co/'+ip+'/json/')
        #print (loc.json())
        for key, val in loc.json().items():
            print(key, ': ', val)
        print()
        print()
    elif choice=='2':
        ip = input('Enter IPv4 Address: ')
        print('The IPv4 Address you inputted is ' + ip)
        
        loc = get_ip_info(ip)
        print (loc.json())
        print()
        print()
    elif choice=='3':
        print()
        print('Thank you for using our application')
        print()
        break
    else:
        print('Invalid input, please try again.')
        print()
        print()


    
