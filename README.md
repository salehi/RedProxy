# MITM attack on frontends with api calls
***NOTICE***: This is only for ethical hacking in RedTeams.

***NOTICE***: You are the one who is responsible for legal issues, this is only source code, its not for production or enterprise usage.



##Intro:
How many of your employees take care about their cyber security?

Are you interested in this topic? 

![keepcalm](https://raw.githubusercontent.com/salehi/RedProxy/master/keep-calm.png)

If you are interested to this subject, just setup this project and create a full proxy of frontend-backend stack. This code will do A Man In The Middle Attack , thats it.

`(THEIR) UPSTREAM <-> (OUR) Nginx Reverse Proxy <-> Target Users`

## Install the requirements
```pip install -r requirements.txt```

We need a redis server also, just install it :)

##Configuration steps:

1. Setup ssl in the nginx configurations or by SSL-Termination.
2. Change example.com and api.example.com to the upstream domain.
3. Check ```https://api.our-domain.com/djangoadmin/```
4. Create a superuser with ```python manage.py createsuperuser```
5. Run the celery worker ```celery -A redproxy.celery worker -l INFO```
6. Run this projcet ```uvicorn redproxy.asgi:application```
7. Try to do some deceptive actions, sending mail from an unknown sender, sms, etc, to make targets use our-domain.com instead of the original.

You are done! know set a meeting with the weak points of security and tell them do NOT be a VICTIM.

Good Luck :)

![redteam](https://raw.githubusercontent.com/salehi/RedProxy/master/redteam.png)