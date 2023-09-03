import re
import time

from playwright.sync_api import Page, expect, Playwright, sync_playwright
# pytest --slowmo 500  --headed  input2.py
def test_input2(page: Page):
    page.goto('https://testingqarvn.com.es/datos-personales/')
    expect(page).to_have_title('Datos Personales | TestingQaRvn')
    #Tiempo de espera
    page.set_default_timeout(5000)

    page.locator("#wsf-1-field-21").fill("Sasha")
    page.locator("#wsf-1-field-22").fill("Dog")
    page.locator("#wsf-1-field-23").fill("sashadog@gmail.com")
    #tiempo forzado
    time.sleep(5)

    page.locator("#wsf-1-field-24").fill("300356875")
    page.locator("#wsf-1-field-28").fill("Sincelejo ciudad de sashita")
    page.locator("//button[@id='wsf-1-field-27']").click()
