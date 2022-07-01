from playwright.sync_api import sync_playwright
import time
import sys
import json
import azurefuto

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
    IP = proxyinfo_dict["ip"]

ProxyUserName = "lum-customer-hl_cb5d20e6-zone-data_center-ip-" + IP
print(ProxyUserName)
proxy = {

    "server": 'http://zproxy.lum-superproxy.io:22225',
    "username": ProxyUserName,
    "password": 'ci05b32ry9z6'

}
with sync_playwright() as playwright:
    chromiumBrowerType = playwright.chromium
    browser = chromiumBrowerType.launch(headless=False, proxy=proxy)
    azurefuto.BeginRgs(playwright,browser)
