import requests
import json


def repoApi(id):
    response1 = requests.get("https://api.github.com/users/{}/repos".format(id))
    obj = response1.json()
    #print(response1)
    if(response1.status_code == 200):
        print("List of Repos for user {}". format(id))
        list = []
        output = []
        for x in obj:
            list.append( x["name"])
        #print(list)
        for y in list:
            response2 = requests.get("https://api.github.com/repos/{}/{}/commits".format(id,y))
            if(response2.status_code == 200):
                num = len(response2.json())
                #print(num)
                s = "Repo:{} : Number of Commits: {}".format(y, num)
                #print(s)
                output.append(s)
            else:
                s = "Repo {} is empty".format(y)
                output.append(s)
                print(response2.json())
        print output
        return output
    else:
        print(response1.json())
def checkRepo(id, repo):
    response = requests.get("https://api.github.com/repos/{}/{}/commits".format(id,repo))
    return len(response.json)
 