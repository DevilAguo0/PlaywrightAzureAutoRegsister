# 1.set finger UA
# 2.proxy
# 3.sms api
# 4 begin regs
from playwright.sync_api import sync_playwright
import time
import sys
import json
from fake_useragent import UserAgent
""""
Process:
1.set finger UA
2.proxy
3.sms api
4 begin regs
"""


def BuildEnvironment():
    pass

def InputIpinfo():
    if sys.version_info[0] == 2:
        import six
        from six.moves.urllib import request

        opener = request.build_opener(
            request.ProxyHandler(
                {
                    'http': 'http://lum-customer-hl_cb5d20e6-zone-data_center-route_err-pass_dyn-country-us:ci05b32ry9z6@zproxy.lum-superproxy.io:22225',
                    'https': 'http://lum-customer-hl_cb5d20e6-zone-data_center-route_err-pass_dyn-country-us:ci05b32ry9z6@zproxy.lum-superproxy.io:22225'}))
        print(opener.open('http://lumtest.com/myip.json').read())
    if sys.version_info[0] == 3:
        import urllib.request

        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler(
                {
                    'http': 'http://lum-customer-hl_cb5d20e6-zone-data_center-route_err-pass_dyn-country-us:ci05b32ry9z6@zproxy.lum-superproxy.io:22225',
                    'https': 'http://lum-customer-hl_cb5d20e6-zone-data_center-route_err-pass_dyn-country-us:ci05b32ry9z6@zproxy.lum-superproxy.io:22225'}))
        print(opener.open('http://lumtest.com/myip.json').read())
        proxyinfo = opener.open('http://lumtest.com/myip.json').read()
        proxyinfo_dict = json.loads(proxyinfo)

    return proxyinfo_dict


def SetProxy(ipinfo):
    IP = ipinfo["ip"]
    ProxyUserName = "lum-customer-hl_cb5d20e6-zone-data_center-ip-" + IP
    print(ProxyUserName)
    proxy = {

        "server": 'http://zproxy.lum-superproxy.io:22225',
        "username": ProxyUserName,
        "password": 'ci05b32ry9z6'
    }
    return proxy


def BeginRgs(playwright):
    # Initialize variables
    email = "bordalesserb@hotmail.com"
    passwd = "vL63GQ50"
    EnterKey = "Enter"

    # Begin create azure account

    page = context.new_page()
    page.goto('https://azure.microsoft.com/en-us/free/')
    print("page=%s" % page)
    tryFreeseletor = "#main > div.section.section--gray100 > div > div > div:nth-child(3) > a"
    # page.wait_for_selector(tryFreeseletor)
    page.click(tryFreeseletor, force=True)
    # page.waitForloadState('load')
    # time.sleep(100)
    # beginFreeseletor = "#main > div.section.section--gray100 > div > div > div:nth-child(3) > a"
    # page.wait_for_selector(beginFreeseletor)
    # page.click(beginFreeseletor)
    page.wait_for_load_state('load')
    page.wait_for_selector("#i0116")
    # email = input("Please input your email:")
    # passwd = input('Please input your password:')
    page.fill("#i0116", email)
    page.press("#i0116", EnterKey)
    page.wait_for_selector("#idSIButton9")
    time.sleep(3)  # TODO
    page.fill("#i0118", passwd)
    page.press("#i0118", EnterKey)
    page.press("#idSIButton9", EnterKey)
    page.wait_for_selector('#signup-button')
    PhoneNumber = input("Please input your phone number:")
    page.fill("#work-phone-input", PhoneNumber)
    page.click("#send-text-message-button")
    SmsCode = input("Please input sms code:")
    time.sleep(1000)


if __name__ == '__main__':
    with sync_playwright() as playwright:
        print("init browser...")
        chromiumBrowerType = playwright.chromium
        ipinfo = InputIpinfo()
        print("set Proxy...")
        proxy = SetProxy(ipinfo)
        browser = chromiumBrowerType.launch(headless=False,proxy=proxy)
        windows = playwright.devices['iPad Pro 11 landscape']


        # print("get UA...")
        # try:
        #     ua=UserAgent()
        #     UA=ua.chrome
        #     print(UA)
        # except Exception as error:
        #     print(error)
        context = browser.new_context(
            **windows,

            locale='en-US',
            geolocation={'longitude':ipinfo['geo']['longitude'], 'latitude':ipinfo['geo']['latitude']},
            permissions=['geolocation'],
            # user_agent=UserAgent().chrome,
            # user_agent=str(''),
            ignore_https_errors=True,
            # proxy=proxy,
            timezone_id=ipinfo['geo']['tz'],
        )

        BeginRgs(playwright)
