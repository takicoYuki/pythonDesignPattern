class DataBase():

    __instance = None
    __database_url = None

    # コンストラクタ
    def __init__(self):
        self.__database_url = None

    def  __new__(cls):
        if cls.__instance is None:
            # インスタンスが作成されていない場合
            # super()で基底クラスに作成する。
            cls.__instance = super().__new__(cls)
        return cls.__instance

    # getter
    @property
    def database_url(self):
        return self.__database_url

    # setter
    @database_url.setter
    def database_url(self,database_url):
        self.__database_url = database_url

    def connect(self):
        # databaseに接続する
        pass


# インスタンスを作成する
a = DataBase()
b = DataBase()

# idの比較
print(id(a),id(b))

a.database_url = '128.1.1.1:5678'

# 同じdatabase_urlが表示される
print(a.database_url)
print(b.database_url)
