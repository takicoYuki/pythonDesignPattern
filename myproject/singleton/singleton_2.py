# javaのsingletonのように書いてみる

class Database:

  __instance = None
  __database_url = None

  # 制御子はないため、インスタンス作成をした場合はエラーを投げる
  def __init__(self):
    raise RuntimeError('このクラスのコンストラクタは呼び出せません')

  # classmethod = public static
  # こっちからインスタンス作成をさせる
  @classmethod
  def get_instance(cls, database_url=None):
    if cls.__instance is None:
      # インスタンスがNoneの場合
      cls.__instance = cls.__new__(cls)
    if database_url:
      # database_urlがある場合
      cls.__instance.__database_url = database_url
    return cls.__instance

  @property
  def database_url(self):
    return self.__database_url

  @database_url.setter
  def database_url(self,database_url):
    self.database_url = database_url

  def connect(self):
    pass

a = Database.get_instance('128.1.1.1:5678')
b = Database.get_instance()

print(id(a),id(b))
print(a.database_url,b.database_url)
