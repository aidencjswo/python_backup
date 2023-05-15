from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False, channel="msedge")
context = browser.new_context()

page = context.new_page()

page.goto("https://mandloh.tistory.com/manage/posts/")


page.wait_for_selector("#login-form")
