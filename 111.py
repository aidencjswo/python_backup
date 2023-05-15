from playwright.sync_api import Playwright, sync_playwright
import time
time.sleep(3)

browser = Playwright.chromium.launch(headless=False)

context = browser.new_context


print(browser)