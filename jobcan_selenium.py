import argparse
import os

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# ログイン情報を読み出し
# get credentials
credentials_path = os.path.dirname(__file__) + '/credentials.txt'
f = open(credentials_path)
credentials = f.read().split('\n')
f.close()

login_id = credentials[0]
login_pw = credentials[1]

# 引数取得
# get args
parser = argparse.ArgumentParser()
parser.add_argument('action_type',
                    choices=['start', 'end', 'start-rest', 'end-rest'])
args = parser.parse_args()
args_action_type = args.action_type
print("action_type = " + args_action_type)

# 初期設定 (ローカルで動作させる前提)
# initialize selenium webdriver
options = webdriver.ChromeOptions()
print('Starting a new session of Google Chrome')
driver = webdriver.Chrome(options=options)

# 待機時間
# wait time setting
driver.implicitly_wait(5)
max_wait_seconds = 10

# ジョブカンにアクセス
# accessing jobcan
print('Connecting to the first page of jobcan')
driver.get('https://id.jobcan.jp/users/sign_in')

# Googleのログインに進む
# proceed to google auth
WebDriverWait(driver, max_wait_seconds).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, "google")))
driver.find_element_by_class_name("google").click()

# GoogleのログインID入力画面
# typing id
login_id_xpath = '//*[@id="identifierNext"]'
WebDriverWait(driver, max_wait_seconds).until(
    expected_conditions.presence_of_element_located((By.XPATH, login_id_xpath)))
print('Entering login name')
driver.find_element_by_name("identifier").send_keys(login_id)
driver.find_element_by_xpath(login_id_xpath).click()

# Googleのパスワード入力画面
# typing password
login_pw_xpath = '//*[@id="passwordNext"]'
WebDriverWait(driver, max_wait_seconds).until(
    expected_conditions.presence_of_element_located((By.XPATH, login_pw_xpath)))
print('Entering password')
driver.find_element_by_name("password").send_keys(login_pw)
driver.find_element_by_xpath(login_pw_xpath).click()

# ジョブカンログイン後の初期画面
# jobcan's first view after login
jobcan_link_class_name = "jbc-app-link"
WebDriverWait(driver, max_wait_seconds).until(
    expected_conditions.presence_of_all_elements_located)
print('Login successful!')
driver.find_element_by_class_name(jobcan_link_class_name).click()
driver.switch_to.window(driver.window_handles[-1])
print('Proceeding to another window')

# 勤怠入力画面
# jobcan's view that shows timecard button
jobcan_element_id_dict = {
    "start": 'adit-button-work-start',
    "end": 'adit-button-work-end',
    "start-rest": 'adit-button-rest-start',
    "end-rest": 'adit-button-rest-end'
}
jobcan_element_id = jobcan_element_id_dict[args_action_type]

WebDriverWait(driver, max_wait_seconds).until(
    expected_conditions.presence_of_all_elements_located)
driver.find_element_by_id(jobcan_element_id).click()

# 打刻結果の取得
# get results
server_status = driver.find_element_by_xpath('//*[@id="clock"]').text

while('通信中' in server_status):
    server_status = driver.find_element_by_xpath('//*[@id="clock"]').text

print('----------------')
print(server_status)
print('----------------')

# ブラウザを終了する
# quit browser
print('Terminating Google Chrome')
driver.quit()
