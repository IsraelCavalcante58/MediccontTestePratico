from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.amazon.com.br/ap/signin?_encoding=UTF8&openid.assoc_handle=brflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com.br%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1")

input_email = driver.find_element(By.ID, 'ap_email')
input_email.send_keys(os.environ['LOGIN'])

botao_continuar_login = driver.find_element(By.ID , 'continue')
botao_continuar_login.click()

input_password = driver.find_element(By.ID , 'ap_password')
input_password.send_keys(os.environ['SENHA'])

botao_fazer_login = driver.find_element(By.ID , 'signInSubmit')
botao_fazer_login.click()

minhas_compras = driver.find_element(By.ID , 'nav-orders')
minhas_compras.click()
sleep(5)
botao_dias = driver.find_element(By.ID, 'a-autoid-1-announce')
botao_dias.click()

botao_2021 = driver.find_element(By.ID, 'orderFilter_2')
botao_2021.click()
sleep(5)

div_pedido = driver.find_elements(By.CLASS_NAME, "a-vertical")
# print(div_pedido[0].get_attribute("innerHTML"))
div_pedido[1].click()






# sleep(2)
# driver.get("https://cliente.americanas.com.br/simple-login/?next=https%3A%2F%2Fwww.americanas.com.br%2F")
# sleep(2)
# input_email = driver.find_element(By.ID ,'email-input')
# sleep(2)
# input_email.send_keys(os.environ['LOGIN'])
# sleep(2)
# input_senha = driver.find_element(By.ID ,'password-input')
# sleep(2)
# input_senha.send_keys(os.environ['SENHA'])
# sleep(2)
# botao_login = driver.find_element(By.ID , 'login-button')
# sleep(2)
# botao_login.click()
# sleep(2)
# botao_minha_conta = driver.find_element(By.ID, "h_usr-link")
# sleep(2)
# botao_minha_conta.click()
# sleep(2)
#
#
# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source
# # driver.close()