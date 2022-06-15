import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase


# python -m pytest -s tests\test_update_analytics_order.py -k test_correct_delta_f_demo


# Тестирование загрузки справочника "Значения аналитического признака "Заказ""

class TestUpdateAnalyticsOrder(BaseCase):

# Авторизация и получение необходимых cookie и headers

    def setup(self):
        env = 'http://localhost:83'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "Supervisor"
        }
        self.url = "http://localhost:83/0/rest/SapErpIntegrationService/v1/UpdateAnalyticsOrder"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)


    """
    def test_correct_delta_f_demo(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
         "row": "4",
         "AUFNR":"main test code 1",
         "AUART":"IteAOKind 1",
         "ERNAM":"IteAOAuthor 1",
         "ERDAT":"01.01.01",
         "AENAM":"IteAOLastChangeAuthor 1",
         "AEDAT":"01.01.01",
         "KTEXT":"IteAOShortText 1",
         "BUKRS":"IteBUCode 1",
         "WERKS":"ItePlantCode 1",
         "GSBER":"IteAOBusinessArea 1",
         "KOKRS":"IteAOControllingUnit 1",
         "KOSTV":"IteCSCode 1",
         "STORT":"IteAOLocation 1",
         "SOWRK":"IteAOPlantLocation 1",
         "ASTKZ":"1",
         "PHAS0":"1",
         "PHAS1":"1",
         "PHAS2":"1",
         "PHAS3":"1",
         "CYCLE":"IteRealEntryCSCode 1",
         "deleted": ""
      }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        print(response.text)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"
    """


# Загрузка справочника в режиме полной выгрузки (delta = "F") корректный запрос

    def test_correct_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 1",
                    "AUART": "IteAOKind 1",
                    "ERNAM": "IteAOAuthor 1",
                    "ERDAT": "01.01.01",
                    "AENAM": "IteAOLastChangeAuthor 1",
                    "AEDAT": "01.01.01",
                    "KTEXT": "IteAOShortText 1",
                    "BUKRS": "IteBUCode 1",
                    "WERKS": "ItePlantCode 1",
                    "GSBER": "IteAOBusinessArea 1",
                    "KOKRS": "IteAOControllingUnit 1",
                    "KOSTV": "IteCSCode 1",
                    "STORT": "IteAOLocation 1",
                    "SOWRK": "IteAOPlantLocation 1",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 1",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"


# Загрузка справочника в режиме обновления (delta = "D", deleted == "") корректный запрос
    def test_correct_delta_d_without_x(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 2",
                    "AUART": "IteAOKind 2",
                    "ERNAM": "IteAOAuthor 2",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 2",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 2",
                    "BUKRS": "IteBUCode 2",
                    "WERKS": "ItePlantCode 2",
                    "GSBER": "IteAOBusinessArea 2",
                    "KOKRS": "IteAOControllingUnit 2",
                    "KOSTV": "IteCSCode 2",
                    "STORT": "IteAOLocation 2",
                    "SOWRK": "IteAOPlantLocation 2",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 2",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Загрузка справочника в режиме обновления - деактивация записи (delta = "D", deleted == "X") корректный запрос

    def test_correct_delta_d_with_x(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 2",
                    "AUART": "IteAOKind 2",
                    "ERNAM": "IteAOAuthor 2",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 2",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 2",
                    "BUKRS": "IteBUCode 2",
                    "WERKS": "ItePlantCode 2",
                    "GSBER": "IteAOBusinessArea 2",
                    "KOKRS": "IteAOControllingUnit 2",
                    "KOSTV": "IteCSCode 2",
                    "STORT": "IteAOLocation 2",
                    "SOWRK": "IteAOPlantLocation 2",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 2",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Проверка граничных значений полей "currentPage" и "pageCount" ("currentPage":"1", "pageCount":"3",)

    def test_boundary_values_p1_c3(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 3",
                    "AUART": "IteAOKind 3",
                    "ERNAM": "IteAOAuthor 3",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 3",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3",
                    "BUKRS": "IteBUCode 3",
                    "WERKS": "ItePlantCode 3",
                    "GSBER": "IteAOBusinessArea 3",
                    "KOKRS": "IteAOControllingUnit 3",
                    "KOSTV": "IteCSCode 3",
                    "STORT": "IteAOLocation 3",
                    "SOWRK": "IteAOPlantLocation 3",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 3",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Проверка граничных значений полей "currentPage" и "pageCount" ("currentPage":"3", "pageCount":"3",)
    def test_boundary_values_p3_c3(self):
        json_data = {
            "currentPage": "3",
            "pageCount": "3",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 4",
                    "AUART": "IteAOKind 4",
                    "ERNAM": "IteAOAuthor 4",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 4",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 4",
                    "BUKRS": "IteBUCode 4",
                    "WERKS": "ItePlantCode 4",
                    "GSBER": "IteAOBusinessArea 4",
                    "KOKRS": "IteAOControllingUnit 4",
                    "KOSTV": "IteCSCode 4",
                    "STORT": "IteAOLocation 4",
                    "SOWRK": "IteAOPlantLocation 4",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 4",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Проверка граничных значений полей "currentPage" и "pageCount" -- выход из диапазона ("currentPage":"4", "pageCount":"3",)

    def test_boundary_values_p4_c3(self):
        json_data = {
            "currentPage": "4",
            "pageCount": "3",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 2",
                    "AUART": "IteAOKind 2",
                    "ERNAM": "IteAOAuthor 2",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 2",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 2",
                    "BUKRS": "IteBUCode 2",
                    "WERKS": "ItePlantCode 2",
                    "GSBER": "IteAOBusinessArea 2",
                    "KOKRS": "IteAOControllingUnit 2",
                    "KOSTV": "IteCSCode 2",
                    "STORT": "IteAOLocation 2",
                    "SOWRK": "IteAOPlantLocation 2",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 2",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Номер страницы превышает количество страниц", f"The value of 'MESSAGE' is not correct"
        assert obj['status'] == 400, f"The status is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "AUFNR")

    def test_null_aufnr_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "",
                    "AUART": "IteAOKind 5",
                    "ERNAM": "IteAOAuthor 5",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 5",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 5",
                    "BUKRS": "IteBUCode 5",
                    "WERKS": "ItePlantCode 5",
                    "GSBER": "IteAOBusinessArea 5",
                    "KOKRS": "IteAOControllingUnit 5",
                    "KOSTV": "IteCSCode 5",
                    "STORT": "IteAOLocation 5",
                    "SOWRK": "IteAOPlantLocation 5",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 5",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - AUFNR", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "AUART")

    def test_null_auart_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 6",
                    "AUART": "",
                    "ERNAM": "IteAOAuthor 6",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 6",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 6",
                    "BUKRS": "IteBUCode 6",
                    "WERKS": "ItePlantCode 6",
                    "GSBER": "IteAOBusinessArea 6",
                    "KOKRS": "IteAOControllingUnit 6",
                    "KOSTV": "IteCSCode 6",
                    "STORT": "IteAOLocation 6",
                    "SOWRK": "IteAOPlantLocation 6",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 6",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - AUART", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "ERNAM")

    def test_null_ernam_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 7",
                    "AUART": "IteAOKind 7",
                    "ERNAM": "",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 7",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 7",
                    "BUKRS": "IteBUCode 7",
                    "WERKS": "ItePlantCode 7",
                    "GSBER": "IteAOBusinessArea 7",
                    "KOKRS": "IteAOControllingUnit 7",
                    "KOSTV": "IteCSCode 7",
                    "STORT": "IteAOLocation 7",
                    "SOWRK": "IteAOPlantLocation 7",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 7",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - ERNAM", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "ERDAT")

    def test_null_erdat_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 8",
                    "AUART": "IteAOKind 8",
                    "ERNAM": "IteAOAuthor 8",
                    "ERDAT": "",
                    "AENAM": "IteAOLastChangeAuthor 8",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 8",
                    "BUKRS": "IteBUCode 8",
                    "WERKS": "ItePlantCode 8",
                    "GSBER": "IteAOBusinessArea 8",
                    "KOKRS": "IteAOControllingUnit 8",
                    "KOSTV": "IteCSCode 8",
                    "STORT": "IteAOLocation 8",
                    "SOWRK": "IteAOPlantLocation 8",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 8",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - ERDAT", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "AENAM")

    def test_null_aenam_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 9",
                    "AUART": "IteAOKind 9",
                    "ERNAM": "IteAOAuthor 9",
                    "ERDAT": "01.01.20",
                    "AENAM": "",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 9",
                    "BUKRS": "IteBUCode 9",
                    "WERKS": "ItePlantCode 9",
                    "GSBER": "IteAOBusinessArea 9",
                    "KOKRS": "IteAOControllingUnit 9",
                    "KOSTV": "IteCSCode 9",
                    "STORT": "IteAOLocation 9",
                    "SOWRK": "IteAOPlantLocation 9",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 9",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - AENAM", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "AEDAT")

    def test_null_aedat_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 10",
                    "AUART": "IteAOKind 10",
                    "ERNAM": "IteAOAuthor 10",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 10",
                    "AEDAT": "",
                    "KTEXT": "IteAOShortText 10",
                    "BUKRS": "IteBUCode 10",
                    "WERKS": "ItePlantCode 10",
                    "GSBER": "IteAOBusinessArea 10",
                    "KOKRS": "IteAOControllingUnit 10",
                    "KOSTV": "IteCSCode 10",
                    "STORT": "IteAOLocation 10",
                    "SOWRK": "IteAOPlantLocation 10",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 10",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - AEDAT", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KTEXT")

    def test_null_ktext_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 11",
                    "AUART": "IteAOKind 11",
                    "ERNAM": "IteAOAuthor 11",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 11",
                    "AEDAT": "31.12.21",
                    "KTEXT": "",
                    "BUKRS": "IteBUCode 11",
                    "WERKS": "ItePlantCode 11",
                    "GSBER": "IteAOBusinessArea 11",
                    "KOKRS": "IteAOControllingUnit 11",
                    "KOSTV": "IteCSCode 11",
                    "STORT": "IteAOLocation 11",
                    "SOWRK": "IteAOPlantLocation 11",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 11",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KTEXT", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "BUKRS")

    def test_null_bukrs_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 12",
                    "AUART": "IteAOKind 12",
                    "ERNAM": "IteAOAuthor 12",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 12",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 12",
                    "BUKRS": "",
                    "WERKS": "ItePlantCode 12",
                    "GSBER": "IteAOBusinessArea 12",
                    "KOKRS": "IteAOControllingUnit 12",
                    "KOSTV": "IteCSCode 12",
                    "STORT": "IteAOLocation 12",
                    "SOWRK": "IteAOPlantLocation 12",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 12",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - BUKRS", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "WERKS")

    def test_null_werks_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 13",
                    "AUART": "IteAOKind 13",
                    "ERNAM": "IteAOAuthor 13",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 13",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 13",
                    "BUKRS": "IteBUCode 13",
                    "WERKS": "",
                    "GSBER": "IteAOBusinessArea 13",
                    "KOKRS": "IteAOControllingUnit 13",
                    "KOSTV": "IteCSCode 13",
                    "STORT": "IteAOLocation 13",
                    "SOWRK": "IteAOPlantLocation 13",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 13",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - WERKS", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "GSBER")

    def test_null_gsber_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 14",
                    "AUART": "IteAOKind 14",
                    "ERNAM": "IteAOAuthor 14",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 14",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 14",
                    "BUKRS": "IteBUCode 14",
                    "WERKS": "ItePlantCode 14",
                    "GSBER": "",
                    "KOKRS": "IteAOControllingUnit 14",
                    "KOSTV": "IteCSCode 14",
                    "STORT": "IteAOLocation 14",
                    "SOWRK": "IteAOPlantLocation 14",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 14",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - GSBER", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KOKRS")

    def test_null_kokrs_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 15",
                    "AUART": "IteAOKind 15",
                    "ERNAM": "IteAOAuthor 15",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 15",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 15",
                    "BUKRS": "IteBUCode 15",
                    "WERKS": "ItePlantCode 15",
                    "GSBER": "IteAOBusinessArea 15",
                    "KOKRS": "IteAOControllingUnit 15",
                    "KOSTV": "IteCSCode 15",
                    "STORT": "IteAOLocation 15",
                    "SOWRK": "IteAOPlantLocation 15",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 15",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KOKRS", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "KOSTV")

    def test_null_kostv_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 16",
                    "AUART": "IteAOKind 16",
                    "ERNAM": "IteAOAuthor 16",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 16",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 16",
                    "BUKRS": "IteBUCode 16",
                    "WERKS": "ItePlantCode 16",
                    "GSBER": "IteAOBusinessArea 16",
                    "KOKRS": "IteAOControllingUnit 16",
                    "KOSTV": "",
                    "STORT": "IteAOLocation 16",
                    "SOWRK": "IteAOPlantLocation 16",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 16",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - KOSTV", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "STORT")

    def test_null_stort_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 17",
                    "AUART": "IteAOKind 17",
                    "ERNAM": "IteAOAuthor 17",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 17",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 17",
                    "BUKRS": "IteBUCode 17",
                    "WERKS": "ItePlantCode 17",
                    "GSBER": "IteAOBusinessArea 17",
                    "KOKRS": "IteAOControllingUnit 17",
                    "KOSTV": "IteCSCode 17",
                    "STORT": "",
                    "SOWRK": "IteAOPlantLocation 17",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 17",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - STORT", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "SOWRK")

    def test_null_sowrk_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 18",
                    "AUART": "IteAOKind 18",
                    "ERNAM": "IteAOAuthor 18",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 18",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 18",
                    "BUKRS": "IteBUCode 18",
                    "WERKS": "ItePlantCode 18",
                    "GSBER": "IteAOBusinessArea 18",
                    "KOKRS": "IteAOControllingUnit 18",
                    "KOSTV": "IteCSCode 18",
                    "STORT": "IteAOLocation 18",
                    "SOWRK": "",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 18",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - SOWRK", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "ASTKZ")

    def test_null_astkz_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 19",
                    "AUART": "IteAOKind 19",
                    "ERNAM": "IteAOAuthor 19",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 19",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 19",
                    "BUKRS": "IteBUCode 19",
                    "WERKS": "ItePlantCode 19",
                    "GSBER": "IteAOBusinessArea 19",
                    "KOKRS": "IteAOControllingUnit 19",
                    "KOSTV": "IteCSCode 19",
                    "STORT": "IteAOLocation 19",
                    "SOWRK": "IteAOPlantLocation 19",
                    "ASTKZ": "",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 19",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - ASTKZ", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "PHAS0")

    def test_null_phas0_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 20",
                    "AUART": "IteAOKind 20",
                    "ERNAM": "IteAOAuthor 20",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 20",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 20",
                    "BUKRS": "IteBUCode 20",
                    "WERKS": "ItePlantCode 20",
                    "GSBER": "IteAOBusinessArea 20",
                    "KOKRS": "IteAOControllingUnit 20",
                    "KOSTV": "IteCSCode 20",
                    "STORT": "IteAOLocation 20",
                    "SOWRK": "IteAOPlantLocation 20",
                    "ASTKZ": "1",
                    "PHAS0": "",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 20",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - PHAS0", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "PHAS1")

    def test_null_phas1_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 21",
                    "AUART": "IteAOKind 21",
                    "ERNAM": "IteAOAuthor 21",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 21",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 21",
                    "BUKRS": "IteBUCode 21",
                    "WERKS": "ItePlantCode 21",
                    "GSBER": "IteAOBusinessArea 21",
                    "KOKRS": "IteAOControllingUnit 21",
                    "KOSTV": "IteCSCode 21",
                    "STORT": "IteAOLocation 21",
                    "SOWRK": "IteAOPlantLocation 21",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 21",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - PHAS1", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "PHAS2")

    def test_null_phas2_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 22",
                    "AUART": "IteAOKind 22",
                    "ERNAM": "IteAOAuthor 22",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 22",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 22",
                    "BUKRS": "IteBUCode 22",
                    "WERKS": "ItePlantCode 22",
                    "GSBER": "IteAOBusinessArea 22",
                    "KOKRS": "IteAOControllingUnit 22",
                    "KOSTV": "IteCSCode 22",
                    "STORT": "IteAOLocation 22",
                    "SOWRK": "IteAOPlantLocation 22",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "",
                    "PHAS3": "1",
                    "CYCLE": "IteRealEntryCSCode 22",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - PHAS2", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "PHAS3")

    def test_null_phas3_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 23",
                    "AUART": "IteAOKind 23",
                    "ERNAM": "IteAOAuthor 23",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 23",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 23",
                    "BUKRS": "IteBUCode 23",
                    "WERKS": "ItePlantCode 23",
                    "GSBER": "IteAOBusinessArea 23",
                    "KOKRS": "IteAOControllingUnit 23",
                    "KOSTV": "IteCSCode 23",
                    "STORT": "IteAOLocation 23",
                    "SOWRK": "IteAOPlantLocation 23",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "",
                    "CYCLE": "IteRealEntryCSCode 23",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - PHAS3", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "CYCLE")

    def test_null_cicle_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 24",
                    "AUART": "IteAOKind 24",
                    "ERNAM": "IteAOAuthor 24",
                    "ERDAT": "01.01.20",
                    "AENAM": "IteAOLastChangeAuthor 24",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 24",
                    "BUKRS": "IteBUCode 24",
                    "WERKS": "ItePlantCode 24",
                    "GSBER": "IteAOBusinessArea 24",
                    "KOKRS": "IteAOControllingUnit 24",
                    "KOSTV": "IteCSCode 24",
                    "STORT": "IteAOLocation 24",
                    "SOWRK": "IteAOPlantLocation 24",
                    "ASTKZ": "1",
                    "PHAS0": "1",
                    "PHAS1": "1",
                    "PHAS2": "1",
                    "PHAS3": "1",
                    "CYCLE": "",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - CYCLE", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"



# Загрузка уже существующей записи (изменение записи) в режиме полной выгрузки (delta = "F") корректный запрос

    def test_changing_an_existing_record_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 2",
                    "AUART": "IteAOKind 2 (new)",
                    "ERNAM": "IteAOAuthor 2 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 2 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 2 (new)",
                    "BUKRS": "IteBUCode 2 (new)",
                    "WERKS": "ItePlantCode 2 (new)",
                    "GSBER": "IteAOBusinessArea 2 (new)",
                    "KOKRS": "IteAOControllingUnit 2 (new)",
                    "KOSTV": "IteCSCode 2 (new)",
                    "STORT": "IteAOLocation 2 (new)",
                    "SOWRK": "IteAOPlantLocation 2 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "0",
                    "PHAS1": "0",
                    "PHAS2": "0",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 2 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Загрузка уже существующей записи (запись актуальна) в режиме полной выгрузки (delta = "F") корректный запрос

    def test_changing_actual_record_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 2",
                    "AUART": "IteAOKind 2 (new)",
                    "ERNAM": "IteAOAuthor 2 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 2 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 2 (new)",
                    "BUKRS": "IteBUCode 2 (new)",
                    "WERKS": "ItePlantCode 2 (new)",
                    "GSBER": "IteAOBusinessArea 2 (new)",
                    "KOKRS": "IteAOControllingUnit 2 (new)",
                    "KOSTV": "IteCSCode 2 (new)",
                    "STORT": "IteAOLocation 2 (new)",
                    "SOWRK": "IteAOPlantLocation 2 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "0",
                    "PHAS1": "0",
                    "PHAS2": "0",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 2 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Запись актуальна", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "I", f"The value of 'TYPE' is not correct"


# Загрузка уже существующей записи (Изменение записи) в режиме обновления (delta = "D") корректный запрос

    def test_changing_an_existing_record_delta_d(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 3",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Загрузка уже существующей записи (запись актуальна) в режиме обновления (delta = "D") корректный запрос

    def test_changing_actual_record_delta_d(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 3",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Изменений в обновляемой записи не обнаружено", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "I", f"The value of 'TYPE' is not correct"

# Деактивация существующей записи в режиме обновления (delta = "D") корректный запрос

    def test_deactivate_record_delta_d(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 3",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Деактивация существующей записи в режиме полной выгрузки (delta = "F") корректный запрос

    def test_deactivate_record_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 4",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"

# Деактивация несуществующей записи в режиме полной выгрузки (delta = "D") корректный запрос

    def test_deactivate_not_exist_record_delta_d(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 33",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
                    "deleted": "X"
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Удаляемая запись отсутствует в справочнике", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Запрос с некорректным параметром (delta = "М")

    def test_uncorrect_delta(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "М",
            "item": [
                {
                    "row": "1",
                    "AUFNR": "main test code 3",
                    "AUART": "IteAOKind 3 (new)",
                    "ERNAM": "IteAOAuthor 3 (new)",
                    "ERDAT": "02.02.20",
                    "AENAM": "IteAOLastChangeAuthor 3 (new)",
                    "AEDAT": "31.12.21",
                    "KTEXT": "IteAOShortText 3 (new)",
                    "BUKRS": "IteBUCode 3 (new)",
                    "WERKS": "ItePlantCode 3 (new)",
                    "GSBER": "IteAOBusinessArea 3 (new)",
                    "KOKRS": "IteAOControllingUnit 3 (new)",
                    "KOSTV": "IteCSCode 3 (new)",
                    "STORT": "IteAOLocation 3 (new)",
                    "SOWRK": "IteAOPlantLocation 3 (new)",
                    "ASTKZ": "0",
                    "PHAS0": "1",
                    "PHAS1": "0",
                    "PHAS2": "1",
                    "PHAS3": "0",
                    "CYCLE": "IteRealEntryCSCode 3 (new)",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Режим выгрузки справочника не идентифицирован", f"The value of 'MESSAGE' is not correct"



