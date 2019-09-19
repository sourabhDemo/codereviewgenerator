# coding=utf-8
import datetime
from datetime import timedelta
import json
from collaboratorAPI import CollaboratorAPI
from collaboratorConstants import *
from gitAPI import GitAPI

# variables
codeCollaboratorAPI = CollaboratorAPI()
gitApi = GitAPI()
endDate = datetime.datetime.strptime(sinceDate, "%m-%d-%Y") + timedelta(days=7)
startDate = sinceDate


if reviewMode == "datewise":
    while untilDate != "" or endDate <= datetime.datetime.now():
        # git section
        concatedIds = gitApi.getcommitids(startDate, endDate)
        print("Git commit Ids count: " + str(len(concatedIds)))

        # Collaborator API section
        title = "Review from " + str(startDate) + " to " + str(endDate.strftime("%m-%d-%Y"))
        print("Title: " + title)

        codeCollaboratorAPI.generatereview(title, concatedIds)

        tmpDate = endDate
        startDate = tmpDate
        if startDate < datetime.datetime.now():
            endDate = datetime.datetime.strptime(tmpDate.strftime("%m-%d-%Y"), "%m-%d-%Y") + timedelta(days=7)
        else:
            endDate = datetime.datetime.now()

if reviewMode == "commitwise":
    concatedIdsGroupByStoryId = gitApi.getcommitidsgroupbystoryid(sinceDate, [])
    for record in concatedIdsGroupByStoryId:
        title = "Review for Story " + record['key']
        codeCollaboratorAPI.generatereview(title, record['value'])

if reviewMode == "storywiseofdiff":
    commitIdsWithReviews = gitApi.getcommitidwithreview()
    concatedIdsGroupByStoryId = gitApi.getcommitidsgroupbystoryid(sinceDate, commitIdsWithReviews)
    for record in concatedIdsGroupByStoryId:
        title = "Review for Story " + record['key']
        codeCollaboratorAPI.generatereview(title, record['value'])
