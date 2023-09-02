import re
from playwright.sync_api import Page, expect

def test_dos(page: Page):
    page.goto("https://demoqa.com/")
    expect(page).to_have_title(("DEMOQA"))
    #boton uno
    #boton_uno = page.locator("text =Elements")
    boton_uno = page.locator("text =Elements").click()
    page.screenshot(path = "imagenes/boton_uno.png")
    #boton_uno.click()
    #page.screenshot(path = "imagenes/boton_uno_click.png")
    page.locator("text=Text Box").click()
    page.screenshot(path='imagenes/boton_dos_click.png')