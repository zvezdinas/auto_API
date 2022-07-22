import unittest
import my_lib.my_func
import docx
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import uuid

from selenium.webdriver.support import expected_conditions as ec


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        s = Service(r"C:\Users\a.zvezdin\Documents\PYTHON\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        #self.driver = webdriver.Chrome(executable_path=r"C:\Users\a.zvezdin\Documents\PYTHON\chromedriver.exe")

        self.driver.implicitly_wait(5)

    def test_case(self):
        # Вход в приложение
        myuuid = uuid.uuid4()
        print(myuuid)
        myuuid = str(myuuid)
        print(myuuid)

        driver = self.driver
        url = "http://localhost:83/"
        # Логин/пароль
        name = "Supervisor"
        passw = "!IteSupervisor123!"
        # Авторизация
        my_lib.my_func.login(driver, url, name, passw)
        my_lib.my_func.open_work_place(driver, "ITSM Box")
        my_lib.my_func.open_section(driver, "Обращения")



        document = docx.Document("Обращения.docx")
        table = document.tables[0]
        # table_size = len(table.rows)
        for col in range(220):

            proish = table.rows[col].cells[0].text
            opis = table.rows[col].cells[1].text
            tema = table.rows[col].cells[2].text
            otvetstv = table.rows[col].cells[3].text
            gr_otvet = table.rows[col].cells[4].text
            service = table.rows[col].cells[5].text
            servise_item = table.rows[col].cells[6].text
            contact = table.rows[col].cells[7].text



            my_lib.my_func.page_lock(driver)
            my_lib.my_func.click_button(driver, "Добавить обращение")

            my_lib.my_func.enter_list_value(driver, "CaseContact", contact)
            time.sleep(2)
            my_lib.my_func.enter_list_value(driver, "ServicePact Сервисный договор", servise_item)
            my_lib.my_func.enter_list_value(driver, 'ServiceItem Сервис', service)
            my_lib.my_func.enter_list_value(driver, 'Влияние', '2-й уровень: значительное')
            my_lib.my_func.enter_list_value(driver, 'CaseGroup Группа ответственных', gr_otvet)
            my_lib.my_func.enter_list_value(driver, 'CaseOwner Ответственный', otvetstv)

            my_lib.my_func.enter_value_input(driver, 'Тема', tema)
            my_lib.my_func.enter_value_textarea(driver, 'Описание', opis)
            my_lib.my_func.enter_list_value(driver, 'Origin Происхождение', proish)

            my_lib.my_func.click_button(driver, "Сохранить")
            my_lib.my_func.page_lock(driver)
            time.sleep(1)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
