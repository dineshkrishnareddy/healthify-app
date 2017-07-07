# healthify-app

***
## External Dependencies 
-----

* <a href="https://apscheduler.readthedocs.io/en/latest/" target="_blank">APScheduler Documentation</a> (To schedule task)
* <a href="https://github.com/dalelotts/angular-bootstrap-datetimepicker" target="_blank">Angular Date Time Picker</a> (To select date and time from UI)


## Install and Running Application
-----

* Install prerequisites

```
$ pip install requirements.txt
```

* Run migrations

```
$ python manage.py migrate
```

* Run application

```
$ python manage.py runserver
```


## Demo
-----

Please check <a href="https://healthify-app.herokuapp.com/" target="_blank">DEMO</a> for further details


## Limitations
-----

* For now we are using only images which are hosted in external server. So for image_url please specify external image url
* As we don't have users table to execute query given by user, we just created a function ```send_notification``` only using notification_payload. So its a dummy function


