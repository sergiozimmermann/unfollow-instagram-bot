from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import os
from dotenv import load_dotenv

# Load envs
load_dotenv()

usernameInsta = os.environ['username_instagram']
passwordInsta = os.environ['password_instagram']


# Webdriver config
driver = webdriver.Chrome()

# Open instagram and login
driver.get('https://www.instagram.com')

# Input username
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input'))
).send_keys(usernameInsta)

# Input password
driver.find_element('xpath', '//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys(passwordInsta)

# Submit button
driver.find_element('xpath', '//*[@id="loginForm"]/div[1]/div[3]/button').click()

# Wait login
input('Press enter when login completes\n')

# Enter profile
driver.get('https://www.instagram.com/' + usernameInsta)

# open follows
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//a[@href="/' + usernameInsta + '/following/"]'))
).click()

# define index number
followIndex = 0

while True:
    # Aguarda a tag <a> estar presente no DOM
    profile_element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[role="dialog"] .notranslate'))
    )[followIndex]

    # Captura o atributo href da tag <a>
    url_follower_profile = profile_element.get_attribute('href')

    print("URL do perfil:", url_follower_profile)

    # open follow profile in another tab
    driver.find_element(By.TAG_NAME, 'body').send_keys('\ue009' + 't')

    # Open a new window 
    driver.execute_script("window.open('');") 
    
    # Switch to the new window and open new URL 
    driver.switch_to.window(driver.window_handles[1]) 
    driver.get(url_follower_profile)

    # Open the following
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'section ul a'))
    )[1].click()

    # Get the first username follower
    first_follow_username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role=dialog] a span'))
    ).get_attribute('innerText')

    print(first_follow_username)

    input()

    # if user isnt following my instagram
    if(first_follow_username != usernameInsta):

        # Close dialog
        driver.find_element(By.CSS_SELECTOR, 'div[role=dialog] button').click()

        # Open dialog follow configs
        driver.find_element(By.CSS_SELECTOR, 'header section:nth-child(2) button').click()
        time.sleep(.5)

        # Unfollow
        driver.find_element(By.CSS_SELECTOR, 'div[role=dialog] div[role=button]:nth-child(8) div').click()
        time.sleep(2)
        
    # Close tab
    driver.close()

    # Switching to old tab 
    driver.switch_to.window(driver.window_handles[0])

    # Next user
    followIndex += 1

    # Wait instagram load more follows
    if (followIndex == 22):
        time.sleep(3)