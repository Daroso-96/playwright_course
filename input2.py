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
    page.screenshot(path="imagenes/input/nombre.png")
    #Assert o validadores
    apellidos=page.locator("#wsf-1-field-22")
    #Visible
    expect(apellidos).to_be_visible()
    #enable
    expect(apellidos).to_be_enabled()
    page.locator("#wsf-1-field-22").fill("Dog")



    #Enabled
    email=page.locator("#wsf-1-field-23")
    expect(email).to_be_enabled()
    #Empty tiene que estar vacio
    expect(email).to_be_empty()
    #Contiene el ID
    expect(email).to_have_id("wsf-1-field-23")
    page.locator("//input[contains(@id,'wsf-1-field-23')]").fill("sashadog@gmail.com")
    page.screenshot(path="imagenes/input/input_correo.png")
    #tiempo forzado
    time.sleep(5)

    page.locator("#wsf-1-field-24").fill("300356875")
    page.locator("#wsf-1-field-28").fill("Sincelejo ciudad de sashita")


    page.locator("//button[@id='wsf-1-field-27']").click()
    expect(page).to_have_url(re.compile(".*datos-personales/"))
