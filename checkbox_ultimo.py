import re
from playwright.sync_api import Playwright, sync_playwright, expect

# pytest --slowmo 2000  --headed checkbox_ultimo.py
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")
    page.get_by_label("Toggle").click()
    page.locator("li").filter(has_text=re.compile(r"^Desktop$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Notes").get_by_role("img").first.click()
    page.locator("li").filter(has_text=re.compile(r"^Downloads$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Word File.doc").get_by_role("img").first.click()
    page.locator("li").filter(has_text=re.compile(r"^Documents$")).get_by_label("Toggle").click()
    page.locator("li").filter(has_text=re.compile(r"^WorkSpace$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Veu").get_by_role("img").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
