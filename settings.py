from selenium.webdriver.chrome.options import Options



def driver_options(option, input_browser):
    agree = True
    option = option.strip().lower()
    if option == 'n':
        agree = False
    options = Options()
    if input_browser == "chromium":
        options.add_experimental_option('detach', agree)
        return options
    elif input_browser == "firefox":
        options.add_experimental_option('--detach', agree)
        return options
    