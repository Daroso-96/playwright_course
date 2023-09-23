import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
#playwright codegen https://demoqa.com/checkbox
# pytest --slowmo 2000  --headed retocheckbox.py
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context(
        viewport={'width':1500, 'height':800},
        #record_video_dir="Videos/reto/"
    )
    page = context.new_page()

    page.goto("https://testingqarvn.com.es/prueba-de-campos-checkbox/")
    expect(page).to_have_title("Prueba de campos Checkbox | TestingQaRvn")
    page.mouse.wheel(0, 400)  # coordenas en x ,y
    time.sleep(2)

    page.locator("//input[@id='wsf-1-field-29']").fill("Sasha")
    #page.screenshot(path="Imagenes/texto_nombre.png")

    page.locator("//input[@id='wsf-1-field-30']").fill("Dog")
    #page.screenshot(path="Imagenes/texto_email.png")
    #scroll

    page.locator("//input[@id='wsf-1-field-31']").fill("sasha@gmail.com")
    #page.screenshot(path="Imagenes/texto_dirección.png")

    page.locator("//input[@id='wsf-1-field-32']").fill("300330330")

    page.locator("//textarea[@id='wsf-1-field-33']").fill("Dirección dos permanente demo")
    #page.screenshot(path="Imagenes/texto_dirección2.png")
     #Check manera 1
    page.mouse.wheel(0,700)
    time.sleep(1)
    """"
    che1 = page.locator("//label[@id='wsf-1-label-36-row-2']")
    expect(che1).to_be_visible()
    che1.click()
    che2 = page.locator("//label[@id='wsf-1-label-36-row-3']")
    expect(che2).to_be_visible()
    che2.click()
    """
    #Manera dos
    """""
    che1 = page.locator("//label[@id='wsf-1-label-36-row-2']")
    expect(che1).to_be_visible()
    che1.check()
    che2 = page.locator("//label[@id='wsf-1-label-36-row-3']")
    expect(che2).to_be_visible()
    che2.check()
    che2 = page.locator("//label[@id='wsf-1-label-36-row-3']")
    expect(che2).to_be_visible()
    che2.uncheck()
    assert che2.locator("//label[@id='wsf-1-label-36-row-3']").is_checked() is False
     """
    # page.locator("//label[contains(.,'PHP')]").click()
    # page.locator("//label[contains(.,'PHP')]").click()
    # time.sleep(1)
    # page.locator("//label[contains(.,'JS')]").click()

    # page.locator("//label[contains(.,'PHP')]").check()
    # page.locator("//label[contains(.,'PHP')]").uncheck()
    # time.sleep(2)
    # page.locator("//label[contains(.,'JS')]").check()
    # page.locator("//label[contains(.,'JS')]").uncheck()
    # assert page.locator("//label[contains(.,'JS')]").is_checked() is False

    # (//label[contains(@class,'wsf-label')])[7]

    for i in range(7,9):
        page.locator(f"(//label[contains(@class,'wsf-label')])[{i}]").click()


    page.locator("//button[@id='wsf-1-field-34']").click()

    """
    page.get_by_label("Toggle").click()
    page.locator("li").filter(has_text=re.compile(r"^Desktop$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Notes").get_by_role("img").first.click()
    page.locator("li").filter(has_text=re.compile(r"^Downloads$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Word File.doc").get_by_role("img").first.click()
    page.locator("li").filter(has_text=re.compile(r"^Documents$")).get_by_label("Toggle").click()
    page.locator("li").filter(has_text=re.compile(r"^WorkSpace$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Veu").get_by_role("img").first.click()
    """
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
