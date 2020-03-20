#! /usr/bin/python3.5

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from browser import facebook_sign_in


# Brings in the return data from the sign in
driver = facebook_sign_in()

'''
    Asks for a filename to open
    Filename is to store it for later use to save data
    to the file.
'''

print('Please write your filename: ')
filename = input()
# Makes sure thats the correct name or file type to save.
print('Is ' + filename + ' correct?')
proceed = input()
# Starts the process of saving the name.
while True:
    if proceed == 'yes':
        break
    else:
        print('Please write your filename: ')
        filename = input()
        print('Is ' + filename + ' correct?')
        proceed = input()
        continue
filename = filename

# Beginning function to search one keyword at a time


def keyword_search():
    # Beginning function to search one keyword at a time

    base = 'https://www.facebook.com/search/top/?q='
    keywords = ('gemstone',
                'gemstones',
                'gems',
                'gemstonejewllery'
                )
    keyword = keywords[0]

    for keyword in keywords:
        search = str(base+keyword)
        driver.get(search)
        with open(filename, 'a') as f:
            print('Writing Keyword')
            f.write('Keyword-Word: ' + keyword + '\n' + '\n')
            print('Finished Writing Keyword.')
        keyword = keywords[+1]
        keyword_data()


def scroll_Down():
    # Scroll down function for scrolling the page down all the way due
    # to Javascript loading

    SCROLL_PAUSE_TIME = 2
    elem = driver.find_element_by_tag_name("html")
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to almost the bottom of the page
        driver.execute_script("window.scrollTo(0, (document.body.scrollHeight-400));")

        # Time Taken to Load the page
        sleep(SCROLL_PAUSE_TIME)
        # Scrolling Up & Down to load more Data
        elem.send_keys(Keys.HOME)
        sleep(1)
        elem.send_keys(Keys.END)
        sleep(1)

        # Calculate the new scrolling height and then compare it to old height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        else:
            last_height = new_height

def keyword_data():
    # Functon to print out the name of the group and the
    # URL to the groups page
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div/div/div[1]/div/a').click()
    sleep(3)
    scroll_Down()
    sleep(3)
    # Store the information for the groups name
    group_names = driver.find_elements_by_css_selector("div._401d > div > div._4bl9 > div > div._5aj7 > div._4bl9 > div > div > div > a")
    name = group_names[0]
    for name in group_names:
        with open(filename, 'a') as f:
            print('Writing Group Name to file..')
            f.write(name.text + '\n' + '\n')
            print('Finished writing group name to file.')
            name = group_names[+1]






keyword_search()
