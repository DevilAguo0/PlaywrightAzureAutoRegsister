from playwright.sync_api import sync_playwright
import time
import azurefuto
with sync_playwright() as p:
    proxy=azurefuto.SetProxy()
    chromiumBrowserType = p.chromium
    print("chromiumBrowserType=%s" % chromiumBrowserType)
    browser = chromiumBrowserType.launch(headless=False,proxy=proxy)
    # chromiumBrowserType=<BrowserType name=chromium executable_path=/Users/limao/Library/Caches/ms-playwright/chromium-857950/chrome-mac/Chromium.app/Contents/MacOS/Chromium>
    print("browser=%s" % browser)
    # browser=<Browser type=<BrowserType name=chromium executable_path=/Users/limao/Library/Caches/ms-playwright/chromium-857950/chrome-mac/Chromium.app/Contents/MacOS/Chromium> version=90.0.4430.0>
    page = browser.new_page()
    print("page=%s" % page)
    # page=<Page url='about:blank'>
    # page.goto("https://whoer.net/")
    page.goto('https://portal.azure.com/')
    print("page=%s" % page)
    # # page=<Page url='https://www.baidu.com/'>
    # page.screenshot(path=f'example_chromium.png')
    tryFreeSeletor="#main > div.section.section--gray100 > div > div > div:nth-child(3) > a"
    page.wait_for_selector(tryFreeSeletor)
    page.click(tryFreeSeletor)
    time.sleep(100)