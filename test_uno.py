import re
from playwright.sync_api import Page, expect

def test_uno(page:Page):
    page.goto('https://playwright.dev/')
    expect(page).to_have_title(re.compile("apps")) #Con esta función le estamos diciendo que espere ese parametro
    button_uno=page.locator("text=Get started")
    expect(button_uno).to_have_attribute("href", "/docs/intro")
    page.screenshot(path="imagenes/test_uno.png")
    button_uno.click()

    #Tomar screenshot
    page.screenshot(path="imagenes/test_uno_final.png")
    expect(page).not_to_have_url(re.compile(".*docs/intro"))


