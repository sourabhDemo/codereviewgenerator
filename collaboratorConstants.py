import datetime
from datetime import timedelta
from gitConstants import *

tokenHeaders = {'Content-Type': 'application/json'}

apiEndPoint = ''

title = ""

deadLine = datetime.datetime.now() + timedelta(days=3)

commandSession = {"command": "SessionService.authenticate", "args": {"login": userAccount, "ticket": ""}}

commandCreateReview = {"command": "ReviewService.createReview",
                        "args": {
                                "creator": userAccount,
                                "title": title,
                                "deadline": deadLine.strftime('%Y-%m-%dT%H:%M:%SZ'),
                                "templateId": "",
                                "customFields": [
                                        {"name": "Summary", "value": ["Please check the JDK version that we use."]}
                                                ]
                                }
                        }
