# Builderパターン
from abc import ABC, abstractproperty


# Product
# 建物
class SetMeal:

    @property
    def main_dish(self):
        return self.__main_dish

    @main_dish.setter
    def main_dish(self, main_dish):
        self.__main_dish = main_dish

    @property
    def side_dish(self):
        return self.side_dish

    @side_dish.setter
    def side_dish(self, side_dish):
        self.__side_dish = side_dish

    def __str__(self):
        return f'メインディッシュ: {self.main_dish}, サイドディッシュ: {self.side_dish}'


# Builderインタフェース
# 設計図
class SetMealBuilder(ABC):

    def __init__(self):
        self.__set_meal = SetMeal()

    @abstractproperty
    def product(self):
        pass

    @abstractproperty
    def build_main_dish(self):
        pass

    @abstractproperty
    def build_side_dish(self):
        pass


# 作成
# 作成工程
class SanmmaSetBuilder(SetMealBuilder):

    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self.__set_meal

    def build_main_dish(self):
        self.__set_meal.main_dish = 'サンマ'

    def build_side_dish(self):
        self.__set_meal.side_dish = 'お味噌汁'


# 作成工程
class PastSetBuilder(SetMealBuilder):

    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self.__set_meal

    def build_main_dish(self):
        self.__set_meal.main_dish = 'パスタ'

    def build_side_dish(self):
        self.__set_meal.side_dish = 'スープ'


# Directorはどのビルダーを使っているか意識していない
# 作成管理
class Director:

    def __init__(self, builder: SetMealBuilder):
        self.__builder = builder

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder):
        self.__builder = builder

    def build(self):
        self.__builder.build_main_dish()
        self.__builder.build_side_dish()


sanmaBuilder = SanmmaSetBuilder()
pastaBuilder = PastSetBuilder()

director = Director(sanmaBuilder)
director.build()
print(director.builder.product)
