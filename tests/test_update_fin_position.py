import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase


# python -m pytest -s tests\test_update_fin_position.py -k test_correct_delta_f_demo


# Тестирование загрузки справочника "Значения аналитического признака "Финансовая позиция""

class TestUpdateFinPosition(BaseCase):

# Авторизация и получение необходимых cookie и headers

    def setup(self):
        env = 'http://localhost:83'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "Supervisor"
        }
        self.url = "http://localhost:83/0/rest/SapErpIntegrationService/v1/UpdateFinPosition"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)



    def test_correct_delta_f_demo(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "4",
                    "FIPEX": "main test code 1",
                    "BEZEI": "",
                    "TEXT1": "",
                    "DATAB": "",
                    "DATBIS": "",
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



# Загрузка справочника в режиме полной выгрузки (delta = "F") корректный запрос

    def test_correct_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "4",
                    "FIPEX": "main test code 1",
                    "BEZEI": "IteFPName 1",
                    "TEXT1": "IteFPDescription 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
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
                    "row": "4",
                    "FIPEX": "main test code 2",
                    "BEZEI": "IteFPName 2",
                    "TEXT1": "IteFPDescription 2",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
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
                    "row": "4",
                    "FIPEX": "main test code 2",
                    "BEZEI": "IteFPName 2",
                    "TEXT1": "IteFPDescription 2",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
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
                    "row": "4",
                    "FIPEX": "main test code 3",
                    "BEZEI": "IteFPName 3",
                    "TEXT1": "IteFPDescription 3",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
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
                    "row": "4",
                    "FIPEX": "main test code 4",
                    "BEZEI": "IteFPName 4",
                    "TEXT1": "IteFPDescription 4",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
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
                    "row": "4",
                    "FIPEX": "main test code 1",
                    "BEZEI": "IteFPName 1",
                    "TEXT1": "IteFPDescription 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Номер страницы превышает количество страниц", f"The value of 'MESSAGE' is not correct"
        assert obj['status'] == 400, f"The status is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "FIPEX")

    def test_null_fipex_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "4",
                    "FIPEX": "",
                    "BEZEI": "IteFPName 1",
                    "TEXT1": "IteFPDescription 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - FIPEX", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"

# Проверка возможности создания записи без обязательных полей режим "F" (пустой "BEZEI")

    def test_null_bezei_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "4",
                    "FIPEX": "main test code 1",
                    "BEZEI": "",
                    "TEXT1": "IteFPDescription 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - BEZEI", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "TEXT1")

    def test_null_text1_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "4",
                    "FIPEX": "main test code 1",
                    "BEZEI": "IteFPName 1",
                    "TEXT1": "",
                    "DATAB": "01.01.20",
                    "DATBIS": "31.12.21",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - TEXT1", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "DATAB")

    def test_null_datab_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "4",
                    "FIPEX": "main test code 1",
                    "BEZEI": "IteFPName 1",
                    "TEXT1": "IteFPDescription 1",
                    "DATAB": "",
                    "DATBIS": "31.12.21",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - DATAB", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Проверка возможности создания записи без обязательных полей режим "F" (пустой "DATBIS")

    def test_null_datbis_value_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "4",
                    "FIPEX": "main test code 1",
                    "BEZEI": "IteFPName 1",
                    "TEXT1": "IteFPDescription 1",
                    "DATAB": "01.01.20",
                    "DATBIS": "",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        for result in obj['result']:
            assert result['MESSAGE'] == "Обязательно для заполнения - DATBIS", f"The value of 'MESSAGE' is not correct"
            assert result['TYPE'] == "E", f"The value of 'TYPE' is not correct"


# Загрузка уже существующей записи (изменение записи) в режиме полной выгрузки (delta = "F") корректный запрос

    def test_changing_an_existing_record_delta_f(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "F",
            "item": [
                {
                    "row": "4",
                    "FIPEX": "main test code 4",
                    "BEZEI": "IteFPName 4 (new)",
                    "TEXT1": "IteFPDescription 4 (new)",
                    "DATAB": "02.02.20",
                    "DATBIS": "30.10.21",
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
                    "row": "4",
                    "FIPEX": "main test code 4",
                    "BEZEI": "IteFPName 4 (new)",
                    "TEXT1": "IteFPDescription 4 (new)",
                    "DATAB": "02.02.20",
                    "DATBIS": "30.10.21",
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
                    "row": "4",
                    "FIPEX": "main test code 3",
                    "BEZEI": "IteFPName 3 (new)",
                    "TEXT1": "IteFPDescription 3 (new)",
                    "DATAB": "02.02.20",
                    "DATBIS": "30.10.21",
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
                    "row": "4",
                    "FIPEX": "main test code 3",
                    "BEZEI": "IteFPName 3 (new)",
                    "TEXT1": "IteFPDescription 3 (new)",
                    "DATAB": "02.02.20",
                    "DATBIS": "30.10.21",
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
                    "row": "4",
                    "FIPEX": "main test code 3",
                    "BEZEI": "IteFPName 3 (new)",
                    "TEXT1": "IteFPDescription 3 (new)",
                    "DATAB": "02.02.20",
                    "DATBIS": "30.10.21",
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
                    "row": "4",
                    "FIPEX": "main test code 4",
                    "BEZEI": "IteFPName 4 (new)",
                    "TEXT1": "IteFPDescription 4 (new)",
                    "DATAB": "02.02.20",
                    "DATBIS": "30.10.21",
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
                    "row": "4",
                    "FIPEX": "main test code 17",
                    "BEZEI": "IteFPName 4 (new)",
                    "TEXT1": "IteFPDescription 4 (new)",
                    "DATAB": "02.02.20",
                    "DATBIS": "30.10.21",
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
                    "row": "4",
                    "FIPEX": "main test code 4",
                    "BEZEI": "IteFPName 4 (new)",
                    "TEXT1": "IteFPDescription 4 (new)",
                    "DATAB": "02.02.20",
                    "DATBIS": "30.10.21",
                    "deleted": ""
                }
            ]
        }
        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        obj = json.loads(response.text)
        assert obj['error'] == "Режим выгрузки справочника не идентифицирован", f"The value of 'MESSAGE' is not correct"
        assert obj['status'] == 400, f"The status is not correct"



