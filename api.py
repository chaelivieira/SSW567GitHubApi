import requests
import json


def repoApi(id):
    response1 = requests.get("https://api.github.com/users/{}/repos".format(id))
    obj = response1.json()
    #print(response1.json())
    if(response1.status_code == 200):
        list = []
        for x in obj:
            list.append( x["name"])
        return list
    else:
        print(response1.json())
        return response1.json()
def getCommits(id, y):
    response2 = requests.get("https://api.github.com/repos/{}/{}/commits".format(id,y))
    if(response2.status_code == 200):
        num = len(response2.json())

        #print(response2.json())
        s = "Repo:{} : Number of Commits: {}".format(y, num)
        #print(s)
        return s
    else:
        s = "Repo {} is empty".format(y)
        return s
        #print(s)
        #print(response2.json())
def output(id):
    list = repoApi(id)
    output = []
    for y in list:
            output.append(getCommits(id,y))
    return output
if __name__ == '__main__':
    print("running tests")
    print(repoApi("chaelivieira"))
    #print(checkRepo("chaelivieira", "MARCK"))
