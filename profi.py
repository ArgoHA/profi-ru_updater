from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText


def send_email(task):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    me = '<your email (from)>'
    you = '<your email (to)>'
    server.login(me, '<your_email_password(from)>')
    msg = MIMEText(task + url)
    msg['Subject'] = 'Новое задание!'
    msg['From'] = me
    msg['To'] = you
    server.sendmail(me, [you], msg.as_string())
    server.quit()


url = 'https://profi.ru/backoffice/n.php'
main_key = {'Умн'}  # Needed words here

driver = webdriver.Chrome()
driver.get(url)

login = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/form/div/div[1]/div[1]/label/span/input')
login.send_keys('<your_login>')

time.sleep(0.1)

passw = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/form/div/div[1]/div[2]/label/span/input')
passw.send_keys('<your_password>')

click = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/form/a')
click.click()

time.sleep(2)

page = driver.page_source

soup = bs(page, 'html.parser')
known_tasks = []

while True:
    for block in soup.find_all(class_='order_block_wrapper'):
        task_key = block.find(class_='subjects').get_text().title()
        name = block.find(class_='client-info order_block__client-info').get_text().replace('\n', ' ')
        task_stack = (task_key, name)
        for key in main_key:
            if task_stack not in known_tasks and key in task_key:
                known_tasks.append(task_key)
                send_email(str(''.join(task_stack)))
            known_tasks.append(task_stack)

    time.sleep(60)
    driver.get(url)
    page = driver.page_source
    soup = bs(page, 'html.parser')
