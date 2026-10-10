from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from settings import test
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml
from pathlib import Path
import time










option = input("Do You want enable detach?\n Y/n: ")
options = test(option)



#selection of years for the filter
input_year_from = input("since what year: ")
input_year_to = input("to what year: ")



driver = webdriver.Chrome(options = options)
url = "https://animego.me"
driver.get(url)






names = []



soup = BeautifulSoup(driver.page_source, 'lxml')


find_section = soup.find('section', class_ = 'container-xxl carousel-section season-section position-relative overflow-hidden')
find_name = find_section.find_all('div', class_ = "ani-grid__item-title h5 fw-normal mb-1")



for i in find_name:
    names.append(i.get_text(strip = True))


#writing anime's names in .txt file
file = Path.cwd() / "anime_of_this_season.txt"
if not file.is_file():
    file.touch()
with file.open('r+', encoding = 'utf-8') as f:
    for name in names:
        if name in "anime_of_this_season.txt":
            continue
        f.write(name + '\n')


#open menu
menu = driver.find_element(By.CSS_SELECTOR, 'button.icon-burger')
menu.click()
#find new url by XPath
header = menu.find_element(By.XPATH, '//nav/a[1]')




new_url = header.get_attribute('href')
driver.get(new_url)

filter_find = driver.find_element(By.ID, 'filterBtn')
filter_find.click()




#setup filter

wait = WebDriverWait(driver, 10)
year_from = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/div[1]/div/input[1]')))
click_year_from = year_from.send_keys(input_year_from)
year_to = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/div[1]/div/input[2]')))
click_year_to = year_to.send_keys(input_year_to)


#choosing genre
genre_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Жанры")]')))
genre_button.click()


romance = wait.until(EC.element_to_be_clickable((By.ID, 'checkGenreromance')))
romance.click()

close_filter = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mmenuSidebar"]/div[1]/button')))
close_filter.click()
time.sleep(1)
driver.get(driver.current_url)


#scroll
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        load_more_href = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="anime-list-results"]/div/div[2]/div[2]/a')))
        load_more_href.click()
    except TimeoutException:
        print("this element does not exist")
    finally:
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



soup = BeautifulSoup(driver.page_source, 'lxml')




parsing_romance_page = soup.find('div', id = 'content-container')
parsing_romance = parsing_romance_page.find_all('a', class_ = 'text-line-clamp')




names_romance = []
for i in parsing_romance:
    names_romance.append(i.get_text())
    


anime_romantics = Path.cwd() / 'anime_romance.txt'

if not anime_romantics.is_file():
    anime_romantics.touch()
with anime_romantics.open('r+', encoding = 'utf-8') as f:
    for name in names_romance:
        if name in 'anime_romance.txt':
            continue
        f.write(name + '\n')