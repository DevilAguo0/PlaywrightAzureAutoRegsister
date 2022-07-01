from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    chromiumBrowerType=p.chromium
    print("chromiumBrowerType=%s" % chromiumBrowerType)
    browser = chromiumBrowerType.launch(headless=False)
    print("browser=%s" % browser)
    page=browser.new_page()
    print("page=%s" % page)
    page.goto('https://signup.azure.com.api/user/login')
    print("page=%s" % page)
    page.screenshot(path=f'example_chromium.png')
    page.click("#main > div.section.section--gray100 > div > div > div:nth-child(3) > a")
    # browser.close()
    time.sleep(1000)