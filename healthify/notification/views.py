import json
import requests
from datetime import datetime

from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()

from .models import notification

def send_notification(notification_payload):
    return True

def getDataFromDB(id):
    data = notification.objects.get(id=id)
    notification_payload = {
        'header': data.header,
        'content': data.content,
        'image_url': data.url
    }
    send_notification(notification_payload)


def checkHeader(header):
    headerLength = len(header)
    min = 20
    max = 150
    if (headerLength >= min and headerLength <= max):
        return header
    else:
        raise RuntimeError("header size must be inbetween 20 to 150")

def checkContent(content):
    contentlength = len(content)
    min = 20
    max = 300
    if (contentlength >= min and contentlength <= max):
        return content
    else:
        raise RuntimeError("content size must be inbetween 20 to 300")

def checkValidImage(path):
    r = requests.head(path)
    if (r.status_code == 200):
        return path
    else:
        raise RuntimeError("Please enter valid image")

class Notifications(View):
    def get(self, request):
        return render(request, 'notification/index.html')

class ApiNotifications(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            header = checkHeader(data.get("header", ""))
            content = checkContent(data.get("content", ""))
            url = checkValidImage(data.get("url", ""))
            notification_details = notification(
                header=header,
                content=content,
                url=url,
                scheduledTime=data.get("scheduledTime", ""),
                query=data.get("query", "")
            )
            notification_details.save()

            date_posted = data.get("scheduledTime", "")
            userDateTime = datetime.strptime(date_posted, '%Y-%m-%dT%H:%M:%S.%fZ')
            scheduler.add_job(lambda: getDataFromDB(notification_details.id), 'cron', month=userDateTime.month,
                              day=userDateTime.day, year=userDateTime.year,
                              hour=userDateTime.hour, minute=userDateTime.minute)

            response = HttpResponse(json.dumps({"data": str(notification_details)}), content_type='application/json')
            response.status_code = 200
            return response
        except Exception as e:
            response = HttpResponse(json.dumps({"error": str(e)}), content_type='application/json')
            response.status_code = 400
            return response


scheduler.start()