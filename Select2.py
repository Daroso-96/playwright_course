import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales
#Variables globales

tiempo=3
ruta="imagenes/Select/"
def test_select2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context = browser.new_context(
        viewport={'width': 1500, 'height': 800}
        # record_video_dir="Videos/Checkbox/"
    )
    page = context.new_page()
    page.goto("https://testingqarvn.com.es/combobox-dependiente/")

    page.set_default_timeout(5000)


    #Creando nuestro objeto de tipo funciones globales
    Funcion=Funciones_Globales(page)
    Funcion.validarTitulo("ComboBox Dependiente | TestingQaRvn")
    #time.sleep(1)
    # page.mouse.wheel(0,400)
    Funcion.Scroll_xy(0,800,1)
    Funcion.Esperar(1)
    #Nombres
    Funcion.Texto_img("//input[contains(@id,'wsf-1-field-54')]","Sasha",ruta+"Nombre.png",tiempo)
    Funcion.Texto("//input[contains(@id,'wsf-1-field-55')]", "Dog", tiempo)
    Funcion.Texto("//input[contains(@id,'wsf-1-field-56')]", "sashitadog@gmail.com", tiempo)
    Funcion.Texto("//input[contains(@id,'wsf-1-field-57')]", "300000111", tiempo)
    Funcion.Texto("//textarea[contains(@id,'wsf-1-field-58')]", "Direccion de sashita", tiempo)

    #Checkbox
    Funcion.Scroll_xy(0,700)
    Funcion.Click("//label[contains(@id,'wsf-1-label-59-row-2')]", tiempo)
    Funcion.Click_img("//label[contains(@id,'wsf-1-label-60-row-3')]",ruta+"Radio.png", tiempo)

    # Metodo Random
    numA = random.sample(range(1, 4), 1)
    print(numA[0])
    # F.Combo_label_img("//select[contains(@id,'wsf-1-field-64')]","Mac",ruta+"Combo2.png",tiempo)

    if numA[0] == 1:
        print("Es el uno")
        Funcion.Combo_label_img("//select[contains(@id,'wsf-1-field-64')]", "Ubuntu", ruta + "Combo2.png", tiempo)
    elif numA[0] == 2:
        print("es el dos")
        Funcion.Combo_label_img("//select[contains(@id,'wsf-1-field-64')]", "Debian", ruta + "Combo2.png", tiempo)
    elif numA[0] == 3:
        print("es el tres")
        Funcion.Combo_label_img("//select[contains(@id,'wsf-1-field-64')]", "Read Hat", ruta + "Combo2.png", tiempo)

    """"
    Funcion.Combo_value_img("//select[contains(@id,'wsf-1-field-53')]", "Linux",ruta+"linux.png", tiempo)
    Funcion.Combo_label_img("//select[contains(@id,'wsf-1-field-53')]", "Mac",ruta+"Mac.png", tiempo)
    """

    #Submit
    Funcion.Click("//button[contains(@id,'wsf-1-field-62')]", tiempo)
    #Validar confirmación
    Funcion.validarNotificacion("//p[contains(.,'Gracias por tu encuesta.')]", "Gracias", tiempo)
    #Validar
    Funcion.validarUrl("https://testingqarvn.com.es/combobox-dependiente/" ,tiempo)





    context.close()
    browser.close()