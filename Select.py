import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales
#Variables globales
tiempo=3
ruta="imagenes/Select/"
def test_select1(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context = browser.new_context(
        viewport={'width': 1500, 'height': 800}
        # record_video_dir="Videos/Checkbox/"
    )
    page = context.new_page()
    page.goto("https://testingqarvn.com.es/combobox/")

    page.set_default_timeout(5000)


    #Creando nuestro objeto de tipo funciones globales
    Funcion=Funciones_Globales(page)
    Funcion.validarTitulo("ComboBox | TestingQaRvn")
    #time.sleep(1)
    # page.mouse.wheel(0,400)
    Funcion.Scroll_xy(0,800,1)
    Funcion.Esperar(1)
    #Nombres
    Funcion.Texto_img("//input[contains(@id,'wsf-1-field-45')]","Sasha",ruta+"Nombre.png",tiempo)
    Funcion.Texto("//input[contains(@id,'wsf-1-field-46')]", "Dog", tiempo)
    Funcion.Texto("//input[contains(@id,'wsf-1-field-47')]", "sashitadog@gmail.com", tiempo)
    Funcion.Texto("//input[contains(@id,'wsf-1-field-48')]", "300000111", tiempo)
    Funcion.Texto("//textarea[contains(@id,'wsf-1-field-49')]", "Direccion de sashita", tiempo)

    #Checkbox
    Funcion.Scroll_xy(0,700)
    Funcion.Click("//label[contains(@id,'wsf-1-label-50-row-2')]", tiempo)
    Funcion.Click_img("//label[contains(@id,'wsf-1-label-51-row-2')]",ruta+"Radio.png", tiempo)

    #ComboBox
    Funcion.Combo_value_img("//select[contains(@id,'wsf-1-field-53')]", "Linux",ruta+"linux.png", tiempo)
    Funcion.Combo_label_img("//select[contains(@id,'wsf-1-field-53')]", "Mac",ruta+"Mac.png", tiempo)

    #Submit
    Funcion.Click("//button[contains(@id,'wsf-1-field-52')]", tiempo)





    context.close()
    browser.close()