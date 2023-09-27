import re
import time
import random
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

# Variables globales
tiempo = 0.3
ruta = "imagenes/Calendarios/"


def test_Calendarios(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context = browser.new_context(
        viewport={'width': 1500, 'height': 800}
        # record_video_dir="Videos/Checkbox/"
    )
    page = context.new_page()
    page.goto("https://testingqarvn.com.es/calendarios/")

    page.set_default_timeout(5000)

    numA2 = random.sample(range(1, 100000), 6)
    numA3 = random.sample(range(1, 100000), 6)

    # Creando nuestro Objeto de tipo Funciones Globales
    Funciones = Funciones_Globales(page)
    Funciones.validarTitulo("Calendarios | TestingQaRvn")
    # time.sleep(1)
    # page.mouse.wheel(0, 400)
    Funciones.Scroll_xy(0, 400)
    Funciones.Esperar(tiempo)

    # nombre
    Funciones.Texto_img("//*[@id='wsf-1-field-66']", "Sasha" + str(numA2[0]), ruta + "Nombre" + str(numA2[0]) + ".png",
                tiempo)
    Funciones.Texto("//*[@id='wsf-1-field-67']", "Dog", tiempo)
    Funciones.Texto("//*[@id='wsf-1-field-68']", "sashita@gmail.com", tiempo)
    Funciones.Texto_img("//input[contains(@id,'wsf-1-field-69')]", "5544" + str(numA3[0]), ruta + "Tel.png", tiempo)
    Funciones.Texto("//textarea[contains(@id,'wsf-1-field-70')]", "Demo de la Dirección", tiempo)

    # checkbox
    Funciones.Scroll_xy(0, 700)
    Funciones.Click("//label[contains(@id,'wsf-1-label-71-row-3')]", tiempo)
    Funciones.Click_img("//label[contains(@id,'wsf-1-label-72-row-1')]", ruta + "Radio.png", tiempo)

    # ComboBox
    Funciones.Combo_value_img("//select[contains(@id,'wsf-1-field-73')]", "Linux", ruta + "Combo.png", tiempo)

    # Metodo Random
    numA = random.sample(range(1, 4), 1)
    print(numA[0])

    if numA[0] == 1:
        print("Es el uno")
        Funciones.Combo_label_img("//select[contains(@id,'wsf-1-field-75')]", "Ubuntu", ruta + "Combo2.png", tiempo)
    elif numA[0] == 2:
        print("es el dos")
        Funciones.Combo_label_img("//select[contains(@id,'wsf-1-field-75')]", "Debian", ruta + "Combo2.png", tiempo)
    elif numA[0] == 3:
        print("es el tres")
        Funciones.Combo_label_img("//select[contains(@id,'wsf-1-field-75')]", "Read Hat", ruta + "Combo2.png", tiempo)

        #Calendario
        Funciones.Texto("//input[contains(@id,'wsf-1-field-79')]", "Septiembre 25, 2023",tiempo)

        Funciones.Texto("//input[contains(@id,'wsf-1-field-78')]","Septiembre 25, 2023")

        #Hacer click en otra area y perder el foco
        #Funciones.mouseXY(0,50)
        #page.mouse.click(0,60) #x.y
        #Funcion para dar click al teclado en la opción TAB
        Funciones.Tab(3)
        #page.keyboard.press("Tab")
        Funciones.Esperar(3)



        # Submit
        Funciones.Click("//button[contains(@id,'wsf-1-field-77')]", tiempo)

        # Validar Confirmación
        Funciones.validarNotificacion_img("//p[contains(.,'Gracias por tu encuesta.')]", "Gracias", ruta + "Respuesta.png", tiempo)

        # validar url
        Funciones.validarUrl("https://testingqarvn.com.es/calendarios/", tiempo)

        Funciones.Esperar(2)
        context.close()
        browser.close()


