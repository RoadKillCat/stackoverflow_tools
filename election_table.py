import requests
from bs4 import BeautifulSoup

t = requests.get("https://stackoverflow.com/election").text
s = BeautifulSoup(t, 'lxml')
names = [t.a.text for t in s.find_all(class_='user-details')]
votes = [t.text for t in s.find_all(class_='vote-count-post')]

assert len(names) == len(votes)

for name, vote in sorted(zip(names, votes), key=lambda p: int(p[1])):
    print(name.ljust(max(len(n) for n in names)), vote)
