from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

router = Router()
driver = webdriver.Chrome()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Напиши любое сообщение и твои ящики в танках будут собраны")

@router.message()
async def message_handler(msg: Message):
    url = "https://lesta.ru/shop/wotb/containers/"
    driver.get(url)
    delay = 100

    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'js-cm-login-link')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")

    myElem.click()

    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'id_login')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    login = driver.find_element(By.ID, 'id_login')
    password = driver.find_element(By.ID, 'id_password')
    logib_btn = driver.find_element(By.CLASS_NAME, 'js-auth-throbbing-element')
    login.send_keys("login@gmail.com")
    password.send_keys("password")
    logib_btn.click()

    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'cm-user-menu-link_cutted-text')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")

    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn__zero')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")

    buttons = driver.find_elements(By.CLASS_NAME, 'btn__zero')
    if (len(buttons) != 0):
        for b in buttons:
            b.click()
            try:
                confirm = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-qa='dialog_button_claim']")))
            except TimeoutException:
                print ("Loading took too much time!")
            confirm.click()
            try:
                close = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-qa='dialog_button_close']")))
            except TimeoutException:
                print ("Loading took too much time!")
            close.click()
            await msg.answer(f"Награда успешно получена!")
    else:
        await msg.answer(f"Нет наград для сбора")
    