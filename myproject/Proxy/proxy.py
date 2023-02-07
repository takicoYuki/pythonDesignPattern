
from abc import ABC, abstractclassmethod
import time

class APICaller(ABC):

  @abstractclassmethod
  def request(self):
    pass

class RealAPICaller(APICaller):

  # 処理の重いコンストラクタとする
  def __init__(self, url):
    self.__url = url
    time.sleep(5)

  def request(self):
    print("APIを呼び出す")
    return

# Proxy
class RealAPICallerProxy(APICaller):

  def __init__(self, url):
    self.__url = url

  # プライベートメソッド
  def __check_access(self):
    print("アクセスに成功しました")
    return True

  # プライベートメソッド
  def __write_log(self):
    print('ログを出力します')

  def request(self):
    if self.__check_access():
      # Proxyなので実際の処理はこのクラスでは行わない
      real_api_caller = RealAPICaller(self.__url)
      real_api_caller.request()
      self.__write_log()

proxy = RealAPICallerProxy("https://google.com")
proxy.request()
