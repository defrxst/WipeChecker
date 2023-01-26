import requests
from bs4 import BeautifulSoup
import time
from discord_webhook import DiscordWebhook
import os




hook = DiscordWebhook(url='hook url here', content='@everyone Your account has been wiped!') # or set the content as whatever u want

def main():
    os.system('cls')
    os.system('color 2') # pro hackerman stuff
    delay = 25 # time delay

    url = 'https://sky.shiiyu.moe/stats/shiiyu' # your name here
    page = requests.get(url)
    pageSoup = BeautifulSoup(page.content, 'html.parser')
    results = pageSoup.find(id='player_profile')

    while True:

        if results is None: # just checks if you have profiles (for people with only one profile)
            responseHook = hook.execute()
            print('You got wiped lol L bozo')
            time.sleep(1000)
        else:
            with open('check.txt', 'w') as f:
                f.write(results.text.strip())
                f.close()
            with open('check.txt', 'r') as f:
                if 'Tomato' in results.text: #your profile fruit
                    print('Nothing has happened, you are not wiped')
                else:
                    print('You have been wiped, sending discord message')
                    hookResponse = hook.execute()
            os.remove('check.txt') # removes the check txt so it can make a new one 
            if page.status_code != 200:
                print('403!')
                delay = 500
            elif page.status_code == 200:
                delay = 25
            
        time.sleep(delay) # sleep delay per check, don't set this too low or else u get 403 (rate limited or smth i forgor)


main() # w