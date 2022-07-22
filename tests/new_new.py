import json
from my_lib.assertions import Assertion
from my_lib.my_requests import MyRequests
from my_lib.base_case import BaseCase

# python -m pytest -s tests\new_new.py -k test_TestUpdateInvoice
# python -m pytest -s tests\new_new.py -k TestUpdateInvoice
# python -m pytest -s test_update_invoice.py -k TestUpdateInvoice

class TestUpdateInvoice(BaseCase):
# Авторизация и получение необходимых cookie и headers
# Система ищет экземляр IteRequestForPurchaseAsset
# по условию IteRequestForPurchaseAsset.IteNumber == BNFPO_IT  &&
# IteRequestForPurchaseAsset.iteIteRequestForPurchase.IteNumber == BANFN_IT

    def setup(self):
        env = 'http://localmail.itexpert.ru:5057'
        auth_data = {
            "UserName": "Supervisor",
            "UserPassword": "!Supervisor123Test!"
        }

        self.url = "http://localmail.itexpert.ru:5057/rest/SapErpIntegrationService/v1/UpdateInvoice"
        self.jar, self.header = MyRequests.user_auth(self, auth_data, env)

    #
    def test_request_for_supply(self):
        json_data = {
            "currentPage": "1",
            "pageCount": "1",
            "delta": "D",
            "item": [
                {
                  "row": "1",
                  "BLART": "t1",
                  "BELNR": "SAP 1",         # IteInvoiceSAP (Номер СФ)
                  "GJAHR": "2021",          # IteFinYear (Финансовый год)
                  "XBLNR": "Supplier 1",    # IteInvoiceSupplier (Номер счет-фактуры)
                  "BUKRS": "1111",          # ItePayer (Организация-собственник) == (SysAdminUnit).IteBUCode (Код балансовой единицы)
                  "LIFNR": "Test code",     # IteSupplier (Поставщик) == сопоставление по Объект Контрагенты.Code
                  # "LIFNR": "Test code",   # IteConsigner (Грузоотправитель) == сопоставление по Объект Контрагенты.Code
                  "BLDAT": "01.02.2020",    # IteInvoiceDate (Дата счет-фактур)
                  "BUDAT": "01.01.2020",    # IteInvoicePostingDate (Дата проводки СФ)
                  "BUZEI": "100001",        # Деталь "ИТ-активы" IteInvoicePosSAP (Позиция в документе SAP)
                  "EBELN": "Order test",    # ItePurchaseOrder (Заказ на закупку / План МТО)
                    # (первая запись IteRequestForPurchaseAsset.IteRequestForPurchase из выборки IteRequestForPurchaseAsset.IteOrder == EBELN),
                    # если выборка пустая то (первая запись IteRequestForPurchaseAssetComponent.IteRequestForPurchase из
                    # выборки IteRequestForPurchaseAssetComponent.IteOrder == EBELN)

                  "EBELP": "10000",         # ItePurchaseOrderPos (Позиция запроса на закупку) в детале "ИТ-актив" ItePurchaseOrderPosSAP (Позиция документа закупки)
                  "MATNR": "test1705-2",
                  "WERKS": "1001",
                  "MENGE": "10.1",
                  "BSTME": "ШТ",
                  "DPROG": "01.03.2020",   # IteExpectedDate (Прогнозная дата поставки)
                  "MEINS": "qwe",
                  "MEINH": "qwe",
                  "UMREZ": "10000",
                  "UMREN": "10002",
                  "RBSTAT": "q",
                  "STBLG": "test test2",
                  "STJAH": "1000",
                  "ZZ_ZEMLI": "CodeSAP 11",     # IteConsignees (Грузополучатель) == сопоставление по Грузополучатели (IteConsignees).IteCodeConsignees
                  "NETPR": "12.5",
                  "deleted": ""
                }
            ]
        }
    # """

# # Проверка наличия ключей
#         items = ["BUKRS", "LIFNR", "ZZ_ZEMLI", "MATNR", "RBSTAT", "WERKS"]
#         exceptions =[]
#
#
#         # Проверка если пустой ключ
#         json_data_list = json_data["item"]
#         json_data_dict = json_data_list[0]
#
#         # assert json_data_dict[""] == "", f"Fields key must be correct"
#         print(json_data_dict)
#         for key, value in json_data_dict.items():
#             if key in items:
#                 if value == "":
#                     exceptions.append(key)
#                     print(exceptions)
#                 assert json_data_dict[key] != "", f"Key {exceptions} isn't empty"
#
#
#         for key, value in json_data_dict.items():
#
#             if key in items:
#                 assert key != "", f"Fields  {key} must not be empty"
#                 assert value != "", f"Fields {value} must not be empty"
#                 print(key)
#
#                     print(value)
#                     exceptions.append(key)
#                     print(exceptions)
    #
    # def test_full_value(self, items, json_data_dict):
    #
    #
    #     for i in items:
    #         print(i)
    #         if i == "":
    #             assert json_data_dict[i] != "", f"В системе не найдено соответствий для атрибутов: {i}"
    #




        response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
        Assertion.assert_code_status(response, 200)
        print(response.text)
        obj = json.loads(response.text)
        print(obj)

        # obj = json.loads(response.text)
        # for result in obj['result']:
        #     assert result['MESSAGE'] == "", f"The value of 'MESSAGE' is not correct"
        #     assert result['TYPE'] == "S", f"The value of 'TYPE' is not correct"




    # def test_request_for_supply_asset(self):
    #     json_data = {
    #         "currentPage": "1",
    #         "pageCount": "1",
    #         "delta": "D",
    #         "item": [
    #             {
    #               "row": "1",
    #               "BLART": "t1",
    #               "BELNR": "SAP 1",         # IteInvoiceSAP (Номер СФ)
    #               "GJAHR": "2021",          # IteFinYear (Финансовый год)
    #               "XBLNR": "Supplier 1",    # IteInvoiceSupplier (Номер счет-фактуры)
    #               "BUKRS": "1111",          # ItePayer (Организация-собственник) == (SysAdminUnit).IteBUCode (Код балансовой единицы)
    #               "LIFNR": "Test code",     # IteSupplier (Поставщик) == сопоставление по Объект Контрагенты.Code
    #               # "LIFNR": "Test code",   # IteConsigner (Грузоотправитель) == сопоставление по Объект Контрагенты.Code
    #               "BLDAT": "01.02.2020",    # IteInvoiceDate (Дата счет-фактур)
    #               "BUDAT": "01.01.2020",    # IteInvoicePostingDate (Дата проводки СФ)
    #               "BUZEI": "100001",        # Деталь "ИТ-активы" IteInvoicePosSAP (Позиция в документе SAP)
    #               "EBELN": "Order test",    # ItePurchaseOrder (Заказ на закупку / План МТО)
    #                 # (первая запись IteRequestForPurchaseAsset.IteRequestForPurchase из выборки IteRequestForPurchaseAsset.IteOrder == EBELN),
    #                 # если выборка пустая то (первая запись IteRequestForPurchaseAssetComponent.IteRequestForPurchase из
    #                 # выборки IteRequestForPurchaseAssetComponent.IteOrder == EBELN)
    #
    #               "EBELP": "10000",         # ItePurchaseOrderPos (Позиция запроса на закупку) в детале "ИТ-актив" ItePurchaseOrderPosSAP (Позиция документа закупки)
    #               "MATNR": "test1705-2",
    #               "WERKS": "1001",
    #               "MENGE": "10.1",
    #               "BSTME": "ШТ",
    #               "DPROG": "01.03.2020",   # IteExpectedDate (Прогнозная дата поставки)
    #               "MEINS": "qwe",
    #               "MEINH": "qwe",
    #               "UMREZ": "10000",
    #               "UMREN": "10002",
    #               "RBSTAT": "q",
    #               "STBLG": "test test2",
    #               "STJAH": "1000",
    #               "ZZ_ZEMLI": "CodeSAP 11",     # IteConsignees (Грузополучатель) == сопоставление по Грузополучатели (IteConsignees).IteCodeConsignees
    #               "NETPR": "12.5",
    #               "deleted": ""
    #             }
    #         ]
    #     }
    # # """
    #
    #     response = MyRequests.post(self.url, json=json_data, headers=self.header, cookies=self.jar)
    #     Assertion.assert_code_status(response, 200)
    #     print(response.text)
    #     obj = json.loads(response.text)
    #     print(obj)