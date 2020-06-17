from openpyxl import load_workbook
from selenium import webdriver
from time import sleep
from random import randint
from tqdm import tqdm


def sleepTime():
    time = int(randint(2, 7))
    for i in tqdm(range(time)):
        sleep(1)
    return


# Work Whith Requests
from authKey import facebookLogin, facebookPassword

browser = webdriver.Chrome()
# load browser

browser.get('https://www.instagram.com')
print('Page Load . . .')
sleepTime()

select = browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
select.send_keys(facebookLogin)
print('Login Enter . . . ')
sleepTime()

select = browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
select.send_keys(facebookPassword)
print('Password Enter . . . ')
sleepTime()

submitAuthInstagrsm = browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[4]/button')
submitAuthInstagrsm.click()
print('Auth is OK! ')
sleepTime()

# Проверка на наличие присутствия окна "Сохранить данные для входа"

saveDataEnter = None
saveDataEnter = None

try:
    saveDataEnter = browser.find_element_by_xpath('//section/main/div/div/div/div/button').click()
    print(saveDataEnter)
    print('There are # Сохранить данные для входа? #')
    print('Предложение - Сохранить данные для входа -- Отключено')
    print('Go Next')
    print()
except:

    if saveDataEnter is not None:
        pressNotNow = browser.find_element_by_xpath('//section/main/div/div/div/div/button').click()
    else:
        pass

sleepTime()

# Проверка на наличие присутствия окна "Включить уведомления"

try:
    saveDataEnter = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    print(saveDataEnter)
    print('There are # Включить уведомления #')
    print('Предложение - Включить уведомления -- Отключено')
    print('Go Next')
    print()
except:
    if saveDataEnter is not None:
        pressNotNow = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    else:
        pass


sleepTime()


workBook = load_workbook('keywords.xlsx', read_only=False)
sheet = workBook['Лист1']

cellCount = 0

for row in sheet.values:
    for value in row:
        cellCount += 1

        literaCell = 'A'
        numberCell = str(cellCount)
        cellIndex = literaCell + numberCell
        cell = sheet[cellIndex].value

        hasTag = str(('#' + cell)).replace(' ', '')
        try:
            findHashTag = browser.find_element_by_xpath('//section/nav/div[2]/div/div/div[2]/input')
            findHashTag.send_keys(hasTag)

            sleep(3)

            nunberOfPublications = browser.find_element_by_xpath(
                '//section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[2]/span/span').text

            print(cellCount, hasTag, nunberOfPublications)

            findHashTag = browser.find_element_by_xpath('//section/nav/div[2]/div/div/div[2]/input').clear()
            sleep(randint(2, 5))
        except:
            findHashTag = browser.find_element_by_xpath('//section/nav/div[2]/div/div/div[2]/input').clear()
            exceptions = "Not Find HashTag"
            print(cellCount, hasTag, exceptions)

print('Parsing was done !')