import git
from xlrd import open_workbook


class GitAPI:

    def getcommitids(self, startDate, endDate):
        repo = git.Repo(repoPath)
        concatedIds = []
        concatedId = ""
        for id in repo.git.log(after=startDate, before=endDate, author=userAccount, format="%h"):
            if id == "\n":
                print(concatedId)
                concatedIds.append(concatedId)
                concatedId = ""
            if id != "\n":
                concatedId = concatedId + id

        print(concatedId)
        concatedIds.append(concatedId)
        return concatedIds

    def getcommitidsgroupbystoryid(self, sinceDate, commitIdsWithReviews):
        repo = git.Repo(repoPath)
        commitGroupByStoryId = [{'key': '', 'value': []}]
        commit = ""
        for id in repo.git.log(since=sinceDate, author=userAccount, format="%h;;%s"):
            if id == "\n":
                print(commit)
                if len(commitIdsWithReviews) > 0:
                    if commit not in commitGroupByStoryId:
                        self.assignstoryidbuckettocommit(commit, commitGroupByStoryId)
                else:
                    self.assignstoryidbuckettocommit(commit, commitGroupByStoryId)
                commit = ""
            if id != "\n":
                commit = commit + id

        print(commit)
        if commit not in commitGroupByStoryId:
            assignStoryIdBucketToCommit(commit, commitGroupByStoryId)
        return commitGroupByStoryId

    def assignstoryidbuckettocommit(self, commit, commitGroupByStoryId):
        commitSplit = commit.split(';;')
        storyId = commitSplit[1].split(':')[0]
        isStoryIdExist = False
        count = 0
        for keys in commitGroupByStoryId:
            if storyId == keys['key']:
                isStoryIdExist = True
                break
            else:
                count += 1

        if isStoryIdExist:
            commitGroupByStoryId[count]['value'].append(commitSplit[0])
        else:
            commitGroupByStoryId.append({'key': storyId, 'value': [commitSplit[0]]})

    def getcommitidwithreview(self):
        wb = open_workbook('ReviewByChangelist.xls')
        s = wb.sheets()[0]
        print('Sheet:' + s.name)
        commitIds = []
        for row in range(s.nrows):
            commitid = (s.cell(row, 0).value)[:7]
            author = (s.cell(row, 1).value)
            if author.lower() == userAccount.lower():
                commitIds.append(commitid)
        print(commitIds)
        return commitIds
