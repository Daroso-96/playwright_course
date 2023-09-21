import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright


# pytest --slowmo 2000  --headed checkbox.py

def test_checkbox(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    # context=browser.new_context()
    context = browser.new_context(record_video_dir="Videos/Checkbox")
    context = browser.new_context(
        viewport={'width': 1500, 'height': 800}
    )

    page = context.new_page()
    # page.set_viewport_size({"width": 600, "height": 700})
    page.goto("https://testpages.eviltester.com/styled/basic-html-form-test.html")
    expect(page).to_have_title("HTML Form Elements")

    # Tiempo de Espera
    page.set_default_timeout(8000)

    che1=page.locator("//input[@value='rd3']")
    expect(che1).to_be_visible()
    che1.click()
    # #Segundo
    # page.locator("(//button[contains(@aria-label,'Toggle')])[2]").click()
    # #tercera opción
    # page.locator("text=Commands").click()

    # page.locator("[aria-label=Toggle]").click()
    # Segundo
    # page.locator("[aria-label=Toggle]").nth(1).click()

    # tercero
    # page.locator("text=Commands").click()
    # page.locator("text=NotesCommands >> svg").nth(2).click()

    # Cerrar Context y Navegador
    context.close()
    browser.close()