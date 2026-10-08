from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml
from pathlib import Path
import time



options = Options()
options.add_experimental_option('detach', True)



driver = webdriver.Chrome(options = options)
url = "https://animego.me"
driver.get(url)



names = []



soup = BeautifulSoup(driver.page_source, 'lxml')

#go to place which we need
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
input_from = year_from.send_keys("2025")
year_to = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/div[1]/div/input[2]')))
input_to = year_to.send_keys("2025")


#choosing genre
genre_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Жанры")]')))
genre_button.click()


romance = driver.find_element(By.ID, 'checkGenreromance')
romance.click()

close_filter = driver.find_element(By.XPATH, '//*[@id="mmenuSidebar"]/div[1]/button')
close_filter.click()
driver.get(driver.current_url)





soup = BeautifulSoup(driver.page_source, 'lxml')




parsing_romance_page = soup.find('div', id = 'content-container')
parsing_romance = parsing_romance_page.find_all('a', class_ = 'text-line-clamp')




names_romance = []
for i in parsing_romance:
    names_romance.append(i.get_text())
    


file = Path.cwd() / 'anime_romance.txt'

if not file.is_file():
    file.touch()
with file.open('r+', encoding = 'utf-8') as f:
    for name in names_romance:
        if name in 'anime_romance.txt':
            continue
        f.write(name + '\n')