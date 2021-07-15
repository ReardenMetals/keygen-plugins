import inspect

from keygen.crypto_coin_factory import CoinFactory
from keygen.crypto_coin_service import CoinService


class CoinFactoryExtended(CoinFactory):
    def __init__(self):
        super().__init__()
        self.coin_services_classes = CoinFactoryExtended.__get_coin_service_classes()

    def get_available_currencies(self):
        return super().get_default_available_currencies() + self.get_default_available_currencies()

    def get_default_available_currencies(self):
        return [coin_services_class.get_currency_name() for coin_services_class in self.coin_services_classes]

    def get_coin_service(self, currency):
        coin_services_dictionary = dict((service.get_currency_name(), service) for service in self.coin_services_classes)
        if currency in coin_services_dictionary:
            return coin_services_dictionary.get(currency)()
        return super().get_coin_service(currency)

    @staticmethod
    def __get_coin_service_classes():
        plugins_module = __import__("plugins")
        classes_member_list = [member for member in dir(plugins_module)
                               if inspect.isclass(getattr(plugins_module, member))]
        classes_list = [getattr(plugins_module, class_member) for class_member in classes_member_list]
        return [clazz for clazz in classes_list if issubclass(clazz, CoinService) and clazz != CoinService]