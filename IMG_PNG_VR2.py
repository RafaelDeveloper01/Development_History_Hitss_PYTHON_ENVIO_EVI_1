#librerias de chrome para selenium y algunas mas de ayuda
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#unaopcion_para_enviar_msj_al_Wsp_(no usada)
import pywhatkit
#control local
import keyword
import pyautogui as pa
#numero o valor aleatorio
import random
#retraso
import time
#libreria_tiempo y suma de tiempo a la hora actual
from datetime import datetime, timedelta
import pytz
import os
from selenium.common.exceptions import NoSuchElementException
import glob
import subprocess
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
############################################################################################################################
#### INSTANCIA PRINCIPAL DE CHROME ###
# Crear una instancia de ChromeOptions----------------------
options = Options()
# Agregar la ruta de la extensión a las opciones de Chrome--
options.add_argument("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\CHROME_EXT_EXE\\chromedriver.exe")
# Abrir el navegador completo-------------------------------
options.add_argument("--start-maximized")
# Inicializar el controlador de Chrome con las opciones-----
driver = webdriver.Chrome(options=options)
############################################################################################################################
driver.get("pagina_1")
time.sleep(5)
pa.click(x=300, y=300)
time.sleep(2)
pa.typewrite('user', interval=0.1)  # Ajusta el intervalo según tus necesidades
# Presionar la tecla Enter
pa.press('tab')
time.sleep(2)
#LLAMAR A UN ARCHIVO TXT
ruta_archivo="C:/Automatizacion_PYTHON_ENTORNO_IMG/BOT_IMAGEN_2_VR/Contraseñas/Contraseña.txt"
subprocess.Popen(["notepad.exe",ruta_archivo])
time.sleep(2)
pa.hotkey('ctrl', 'e')
time.sleep(2)
pa.hotkey('ctrl', 'c')
time.sleep(2)
pa.hotkey('alt','f4')
time.sleep(5)
# Escribir la segunda credencial sin cambiar las mayúsculas y minúsculas
pa.hotkey('ctrl','v')
time.sleep(2)
pa.press('enter')
time.sleep(10)
#Cliclear el buscador
try:
    # Espera hasta que el elemento sea clickable
    toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnFilters")))
    toglee1.click()
    time.sleep(4)
except NoSuchElementException:
    print("El elemento 'btnFilters' no se encontró. Tomando una captura de pantalla.")
    driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_1.jpg")

except Exception as e:
    print(f"Se produjo un error: {str(e)}. Tomando una captura de pantalla.")
    driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_1.jpg")
else:
    try:
        # Espera hasta que el elemento sea clickable
        toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sltFilters_ul"]/li[3]/a')))
        toglee1.click()

        # Puedes aplicar la misma lógica de WebDriverWait para otros elementos
        toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "txtSearch")))
        toglee1.send_keys("cod")
        pa.press("enter")
        time.sleep(15)
        driver.execute_script("document.body.style.zoom = '70%'")
        time.sleep(2)
        # Toma captura a toda la pantalla en mención y guarda la imagen en una carpeta específica
        driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_1.jpg")
    except Exception as e:
        print(f"Se produjo un error durante la ejecución posterior: {str(e)}. Tomando una captura de pantalla.")
        driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_1.jpg")
time.sleep(5)
############################################################################################################################
############################################################################################################################
driver.get("pagina_2")
time.sleep(5)
pa.click(x=300, y=300)
time.sleep(2)
pa.typewrite('user', interval=0.1)  # Ajusta el intervalo según tus necesidades
# Presionar la tecla Enter
pa.press('tab')
time.sleep(2)
#LLAMAR A UN ARCHIVO TXT
ruta_archivo="C:/Automatizacion_PYTHON_ENTORNO_IMG/BOT_IMAGEN_2_VR/Contraseñas/Contraseña.txt"
subprocess.Popen(["notepad.exe",ruta_archivo])
time.sleep(2)
pa.hotkey('ctrl', 'e')
time.sleep(2)
pa.hotkey('ctrl', 'c')
time.sleep(2)
pa.hotkey('alt','f4')
time.sleep(5)
# Escribir la segunda credencial sin cambiar las mayúsculas y minúsculas
pa.hotkey('ctrl','v')
time.sleep(2)
pa.press('enter')
time.sleep(10)
#Cliclear el buscador
try:
    # Espera hasta que el elemento sea clickable
    toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnFilters")))
    toglee1.click()
    time.sleep(4)
except NoSuchElementException:
    print("El elemento 'btnFilters' no se encontró. Tomando una captura de pantalla.")
    driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_2.jpg")

except Exception as e:
    print(f"Se produjo un error: {str(e)}. Tomando una captura de pantalla.")
    driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_2.jpg")
else:
    try:
        # Espera hasta que el elemento sea clickable
        toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sltFilters_ul"]/li[3]/a')))
        toglee1.click()

        # Puedes aplicar la misma lógica de WebDriverWait para otros elementos
        toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "txtSearch")))
        toglee1.send_keys("cod")
        pa.press("enter")
        time.sleep(15)
        driver.execute_script("document.body.style.zoom = '70%'")
        time.sleep(2)
        # Toma captura a toda la pantalla en mención y guarda la imagen en una carpeta específica
        driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_2.jpg")
    except Exception as e:
        print(f"Se produjo un error durante la ejecución posterior: {str(e)}. Tomando una captura de pantalla.")
        driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_2.jpg")
time.sleep(5)
############################################################################################
#############################################################################################
driver.get("pagina_3")
time.sleep(5)
pa.click(x=300, y=300)
time.sleep(2)
pa.typewrite('user', interval=0.1)  # Ajusta el intervalo según tus necesidades
# Presionar la tecla Enter
pa.press('tab')
time.sleep(2)
#LLAMAR A UN ARCHIVO TXT
ruta_archivo="C:/Automatizacion_PYTHON_ENTORNO_IMG/BOT_IMAGEN_2_VR/Contraseñas/Contraseña.txt"
subprocess.Popen(["notepad.exe",ruta_archivo])
time.sleep(2)
pa.hotkey('ctrl', 'e')
time.sleep(2)
pa.hotkey('ctrl', 'c')
time.sleep(2)
pa.hotkey('alt','f4')
time.sleep(5)
# Escribir la segunda credencial sin cambiar las mayúsculas y minúsculas
pa.hotkey('ctrl','v')
time.sleep(2)
pa.press('enter')
time.sleep(10)
#Cliclear el buscador
try:
    # Espera hasta que el elemento sea clickable
    toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnFilters")))
    toglee1.click()
    time.sleep(4)
except NoSuchElementException:
    print("El elemento 'btnFilters' no se encontró. Tomando una captura de pantalla.")
    driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_3.jpg")

except Exception as e:
    print(f"Se produjo un error: {str(e)}. Tomando una captura de pantalla.")
    driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_3.jpg")
else:
    try:
        # Espera hasta que el elemento sea clickable
        toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sltFilters_ul"]/li[3]/a')))
        toglee1.click()

        # Puedes aplicar la misma lógica de WebDriverWait para otros elementos
        toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "txtSearch")))
        toglee1.send_keys("cod")
        pa.press("enter")
        time.sleep(15)
        driver.execute_script("document.body.style.zoom = '70%'")
        time.sleep(2)
        # Toma captura a toda la pantalla en mención y guarda la imagen en una carpeta específica
        driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_3.jpg")
    except Exception as e:
        print(f"Se produjo un error durante la ejecución posterior: {str(e)}. Tomando una captura de pantalla.")
        driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_3.jpg")
time.sleep(5)
##############################################################################################################
##############################################################################################################


# Abrir la primera página
driver.get("pagina_4")
time.sleep(5)
pa.click(x=300, y=300)
time.sleep(2)
pa.typewrite('user', interval=0.1)  # Ajusta el intervalo según tus necesidades
# Presionar la tecla Enter
pa.press('tab')
time.sleep(2)
#LLAMAR A UN ARCHIVO TXT
ruta_archivo="C:/Automatizacion_PYTHON_ENTORNO_IMG/BOT_IMAGEN_2_VR/Contraseñas/Contraseña.txt"
subprocess.Popen(["notepad.exe",ruta_archivo])
time.sleep(2)
pa.hotkey('ctrl', 'e')
time.sleep(2)
pa.hotkey('ctrl', 'c')
time.sleep(2)
pa.hotkey('alt','f4')
time.sleep(5)
# Escribir la segunda credencial sin cambiar las mayúsculas y minúsculas
pa.hotkey('ctrl','v')
time.sleep(2)
pa.press('enter')
time.sleep(10)
#Cliclear el buscador
try:
    # Espera hasta que el elemento sea clickable
    toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnFilters")))
    toglee1.click()
    time.sleep(4)
except NoSuchElementException:
    print("El elemento 'btnFilters' no se encontró. Tomando una captura de pantalla.")
    driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_4.jpg")

except Exception as e:
    print(f"Se produjo un error: {str(e)}. Tomando una captura de pantalla.")
    driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_4.jpg")
else:
    try:
        # Espera hasta que el elemento sea clickable
        toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sltFilters_ul"]/li[3]/a')))
        toglee1.click()

        # Puedes aplicar la misma lógica de WebDriverWait para otros elementos
        toglee1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "txtSearch")))
        toglee1.send_keys("cod")
        pa.press("enter")
        time.sleep(15)
        driver.execute_script("document.body.style.zoom = '70%'")
        time.sleep(2)
        # Toma captura a toda la pantalla en mención y guarda la imagen en una carpeta específica
        driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_4.jpg")
    except Exception as e:
        print(f"Se produjo un error durante la ejecución posterior: {str(e)}. Tomando una captura de pantalla.")
        driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP\\Img_4.jpg")
time.sleep(5)
driver.close()
time.sleep(5)
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
#####################################################ENVIO_WSP###
#CARPETA_ORIGEN_GUARDA_ARCHIVOS_de a ca sacare los archivos que enviare por wsp
carpeta_imagenes = "C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_2_VR\\IMG_ENVIO_WSP"

#################################### INSTANCIA SECUNDARIA DE CHROME PARA WSP__inicio##########################################

# Ruta al perfil de Chrome que deseas utilizar(dependencia_aparte)
profile_path = r"C:\Users\Orlando\AppData\Local\Google\Chrome\User Data\Default"

# Configurar las opciones del navegador para utilizar el perfil
options.add_argument("--user-data-dir=" + profile_path)

# Reutilizar la instancia de Chrome con el perfil seleccionado(Profile 1)
driver = webdriver.Chrome(options=options)
time.sleep(5)

#################################### INSTANCIA SECUNDARIA DE CHROME PARA WSP__fin##########################################

#Seleccion_link
driver.get("https://web.whatsapp.com/")
time.sleep(35)

#Seleccionar la barra buscadora de wsp y buscar el nombre del grupo
Click_wsp = driver.find_element(By.CSS_SELECTOR, "div._3gYev > div > div._1EUay > div._2vDPL > div > div.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt.qh0vvdkp > p")
Click_wsp.click()
#Name_grup
Click_wsp.send_keys("equipo")
Click_wsp.send_keys(Keys.ENTER)
time.sleep(3)

#Bucle para el envio consecutivo de las img alojadas en una carpeta
for imagen in os.listdir(carpeta_imagenes):
    ruta_imagen = os.path.join(carpeta_imagenes, imagen)
    #selecionar lo adjunto
    attachment_button = driver.find_element(By.XPATH,'//div[@title="Adjuntar"]')
    attachment_button.click()
    time.sleep(3)
    #elegir el tipo de archivo que se desea enviar
    file_input = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    file_input.send_keys(ruta_imagen)
    time.sleep(3)
    #selecion de icono (adjuntador"+"")
    send_button = driver.find_element(By.XPATH,'//span[@data-icon="send"]')
    send_button.click()
    time.sleep(3)
time.sleep(5)
msj = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
msj.send_keys("Se envia la validacion")
time.sleep(3)
msj.send_keys(Keys.ENTER)
time.sleep(8)
driver.close()
time.sleep(5)