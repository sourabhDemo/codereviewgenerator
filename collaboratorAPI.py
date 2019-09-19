import requests
import json
import os
import subprocess
from collaboratorConstants import *


class CollaboratorAPI:
    def createreview(self, title):
        commandCreateReview["args"]["title"] = title
        arguments = [commandSession, commandCreateReview]
        print(json.dumps(arguments))
        response = requests.post(apiEndPoint, data=json.dumps(arguments), headers=tokenHeaders)
        print(response.content)
        return response.content

    def addcodereview(self, reviewid, changelist):
        for changeId in changelist:
            print("Processing id: " + changeId)
            subprocess.run(["ccollab", "--no-browser", "--quiet", "--scm", "git", "addchangelist", reviewid, changeId], shell=True, cwd=repoPath)

    def generatereview(self, title, concatedIds):
        createReviewResponse = json.loads(self.createreview(title))
        reviewId = createReviewResponse[1]["result"]["reviewId"]
        print("Review Id: " + str(reviewId))

        # Add Code reviews to Review
        self.addcodereview(str(reviewId), concatedIds)
        print("Commits added to Review " + str(reviewId))
