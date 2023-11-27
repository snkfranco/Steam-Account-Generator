import random
import string
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored
os.system('cls')
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

ascii_art = """
    MP\"\"\"\"\"\"\"`MM M\"\"\"\"\"\"`YM M\"\"MMMMM\"\"M    MP\"\"\"\"\"\"\"`M   dP                                   MM'\"\"\"\"\"\"`M
    M  mmmmm..M M  mmmm.  M M  MMMM' .M    M  mmmmm..M   88                                   M' .mmm. `M
    M.      `YM M  MMMMM  M M       .MM    M.      `YM d8888P .d8888b. .d8888b. 88d8b.d8b.    M  MMMMMMMM .d8888b. 88d888b.
    MMMMMMM.  M M  MMMMM  M M  MMMb. YM    MMMMMMM.  M   88   88ooood8 88'  `88 88'`88'`88    M  MMM   `M 88ooood8 88'  `88
    M. .MMM'  M M  MMMMM  M M  MMMMb  M    M. .MMM'  M   88   88.  ... 88.  .88 88  88  88    M. `MMM' .M 88.  ... 88    88
    Mb.     .dM M  MMMMM  M M  MMMMM  M    Mb.     .dM   dP   `88888P' `88888P8 dP  dP  dP    MM.     .MM `88888P' dP    dP
    MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM    MMMMMMMMMMM                                        MMMMMMMMMMM
"""

# Define uma lista de tons de vermelho
red_tones = [Fore.BLUE, Fore.LIGHTBLUE_EX]

# Lista para armazenar cores atribuídas aleatoriamente
colored_ascii_art = []

for char in ascii_art:
    if char.isalpha():  # Verifica se o caractere é uma letra
        # Atribui aleatoriamente um tom de vermelho
        colored_char = random.choice(red_tones) + char
        colored_ascii_art.append(colored_char)
    else:
        colored_ascii_art.append(char)

# Imprime o texto estilizado


chrome_driver_path = './chromedriver.exe'
options = webdriver.ChromeOptions()
service = webdriver.ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

os.system('cls')
print("".join(colored_ascii_art))


logo = ''''''
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_account():
    generated = generate_random_string(10)
    email = f"{generated}@tuamaeaquelaursa.com"
    print('\n [+] O email:' + email + ' foi gerado com sucesso!')
    time.sleep(2)
    print(' [+] Iniciando Steam (create account)')

    
    driver.get('https://store.steampowered.com/join/')
    wait = WebDriverWait(driver, 20)

    wait.until(EC.title_contains("Cadastrar-se"))
    print(' [+] Pagina foi carregada com sucesso!')

    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="reenter_email"]').send_keys(email)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="i_agree_check"]').click()

    print(' [!] Aguardando resolução do captcha...')
    input()

    print(' [+] Continuando...')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="createAccountButton"]').click()

    time.sleep(1)

    driver.execute_script(f"window.open('https://tuamaeaquelaursa.com/{generated}', '_blank');")

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div/section/div/div/div').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div/section/main/center[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a').click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

    usuario = generate_random_string(10)
    senha = generate_random_string(10)
    driver.find_element(By.XPATH, '//*[@id="accountname"]').send_keys(usuario)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="reenter_password"]').send_keys(senha)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="createAccountButton"]').click()
    time.sleep(5)

    print(' -------------------------------------------------')
    print(f' [+] SUCESSO! CONTA STEAM GERADA! #{x}')
    print(f'  └ EMAIL: {email}')
    print(f'  └ USUARIO: {usuario}')
    print(f'  └ SENHA: {senha}')
    print(' -------------------------------------------------')

    time.sleep(10)

    for handle in driver.window_handles[1:]:
        driver.switch_to.window(handle)
        driver.close()

    driver.switch_to.window(driver.window_handles[0])

x = 1
for _ in range(3):
    generate_account()
    x = x + 1
    time.sleep(5)

sys.exit()
