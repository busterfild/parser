from selenium.webdriver.chrome.options import Options



def test(option):
    agree = True
    option = option.strip().lower()
    if option == 'n':
        agree = False
    options = Options()
    options.add_experimental_option('detach', agree)
    return options