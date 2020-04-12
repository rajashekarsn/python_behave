from selenium import webdriver


def before_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser = webdriver.Chrome('/home/shanmukh/Python-3.7.3/chromedriver')
        context.browser.implicitly_wait(3)


def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser.quit()
