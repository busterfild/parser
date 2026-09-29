from selenium import webdriver
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
with file.open('r+') as f:
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
time.sleep(1)
driver.get(new_url)

