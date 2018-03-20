import requests, time
from bs4 import BeautifulSoup

stem = 'https://stackoverflow.com'

user_id = '7434365'

def get_num_pages(user):
    url = 'https://stackoverflow.com/search?&page=1&tab=Newest&q=user%3a'+user+'%20is%3aanswer'
    sp = soupify(url)
    return int(sp.find_all('span', class_="page-numbers")[-3].text)

def get_answer_links(user, page):
    page = str(page)
    url = 'https://stackoverflow.com/search?&page='+page+'&tab=Newest&q=user%3a'+user+'%20is%3aanswer'
    sp = soupify(url)
    global s
    s = sp
    lnks = [stem+b.find('a')['href'] for b in sp.find_all(class_='result-link')]
    return lnks

def get_answer_text(url):
    sp = soupify(url)
    return sp.find(id='answer-'+url.split('#')[-1]).find(class_='post-text').text


def soupify(url):
    return BeautifulSoup(requests.get(url).text, 'lxml')

div_l = 64

pages = get_num_pages(user_id)
time.sleep(2)
with open('stack_answers.txt', 'w') as f:
    for p in range(1, pages):
        print('~'*div_l+'page '+str(p)+'~'*div_l)
        for i,l in enumerate(get_answer_links(user_id, p)):
            ans = get_answer_text(l)
            #f.write('\n'+l.ljust(200, '~')+'\n')
            f.write('\n'+'~'*250+'\n'+l+'\n'+'~'*250+'\n')
            f.write(ans)
            print('~'*div_l+'ansr '+str(i)+'~'*div_l)
            print(ans)
