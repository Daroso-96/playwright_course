import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright


class Funciones_Globales:
      def __init__(self, page):
          self.page=page

      def Esperar(self,tiempo=1):
           time.sleep(tiempo)


      def Scroll_xy(self, x,y,tiempo=1):
          self.page.mouse.wheel(x,y)
          time.sleep(tiempo)

      def Texto(self, selector, texto, tiempo=1):
          t = self.page.locator(selector)
          expect(t).to_be_visible()
          expect(t).to_be_enabled()
          expect(t).to_be_empty()
          t.highlight()
          t.fill(texto)
          time.sleep(tiempo)


      def Texto_img(self, selector, texto,ruta,tiempo=1):
          t = self.page.locator(selector)
          expect(t).to_be_visible()
          expect(t).to_be_enabled()
          expect(t).to_be_empty()
          t.highlight()
          t.fill(texto)
          self.page.screenshot(path=ruta)
          time.sleep(tiempo)

