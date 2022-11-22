# FactoryMethod
from abc import ABC, abstractmethod, abstractproperty


# フレームワーク側
# Factory ->(creates) Product
class IFactory(ABC):

    def __init__(self):
        self.registered_owners = []

    def create(self, owner):
        self._owner = owner
        # プロダクトの作成
        product = self._create_product()
        # プロダクトの登録
        self._register_product(product)
        return product

    @abstractmethod
    def _create_product(self):
        pass

    @abstractmethod
    def _register_product(self, product):
        pass


# ファクトリークラス
# 具体的作成者
class CarFactory(IFactory):

    def _create_product(self):
        return Car(self._owner)

    def _register_product(self, product):
        self.registered_owners.append(product.owner)


# ファクトリークラス
# 具体的作成者
class ShipFactory(IFactory):

    def _create_product(self):
        return Ship(self._owner)

    def _register_product(self, product):
        self.registered_owners.append(product.owner)


# フレームワーク側
class IProduct(ABC):

    def __init__(self, owner):
        self._owner = owner

    @abstractmethod
    def use(self):
        pass

    @abstractproperty
    def owner(self):
        pass


# 具体的な製品
class Car(IProduct):

    def use(self):
        print('{}: 車を運転します'.format(self._owner))

    @property
    def owner(self):
        return self._owner


# 具体的な製品
class Ship(IProduct):

    def use(self):
        print('{}: 船を運転します'.format(self._owner))

    @property
    def owner(self):
        return self._owner


car_factory = CarFactory()
ship_factory = ShipFactory()

yamadaCar = car_factory.create('yamada')
satoCar = car_factory.create('sato')
yamadaShip = ship_factory.create('yamada')
satoShip = ship_factory.create('sato')

yamadaCar.use()
satoCar.use()
yamadaShip.use()
satoShip.use()

print(car_factory.registered_owners)
print(ship_factory.registered_owners)
