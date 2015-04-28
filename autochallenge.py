import sched, time, mechanize, requests, random
from datetime import datetime
from bs4 import BeautifulSoup

# Username + password
LOGIN = ""
PASSWORD = ""

# Oppoennts list
OPPONENTS = [
    "CCCodingBad",
    #"oponennt",
    #"names",
    #"here"
    ]

def auth():
    browser = mechanize.Browser()
    browser.open("http://theaigames.com/competitions/warlight-ai-challenge-2")

    browser.select_form(nr=0)

    browser.form['login'] = LOGIN
    browser.form['password'] = PASSWORD

    browser.submit()

    return browser

def get_opponent():
    name = random.choice(OPPONENTS)
    return "http://theaigames.com/competitions/warlight-ai-challenge-2/game/challenge/" + name + "/new"

def challenge(s, browser, link):
    current_time = datetime.now()
    print ('Challenged %d:%d:%d\n' % (current_time.hour, current_time.minute, current_time.second))
    print ('Link: ', link)
    browser.open(link)
    s.enter(305, 1, challenge, (s, browser, link ))
    s.run()

def main():
    browser = auth()

    link = get_opponent()
    s = sched.scheduler(time.time, time.sleep)
    s.enter(5, 1, challenge, (s, browser, link,))
    s.run()

if __name__ == "__main__":
    main ()
