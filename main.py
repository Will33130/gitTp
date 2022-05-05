import requests
s = requests.session()

def getAge(name):
    path = "https://api.agify.io?name=" + name
    r = s.get(path).json()
    print(r.get("age"))

textinput = input("rentrez votre nom : \n")

getAge(textinput)