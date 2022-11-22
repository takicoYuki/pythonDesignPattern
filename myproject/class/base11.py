#ファイル入力
import subprocess
import re

filePath = '\pythonDesignPattern\myproject\resources\input.csv'
fileName = 'input.csv'

def existenceCheckOsCmd(filepath,fileName):
  #cmdのデフォルト文字コード cp932
  result = subprocess.run(["ls"], cwd=filepath,stdout=subprocess.PIPE, shell=True).stdout.decode("cp932")
  print(result)
  if fileName in result:
    return True
  else:
    return False

def getCurrentDir():

  result = subprocess.run(['cd'],stdout=subprocess.PIPE,shell=True).stdout.decode("cp932")
  return re.sub('\r\n','',result)

if existenceCheckOsCmd(getCurrentDir() + filePath, fileName):
  f = open(getCurrentDir() + filePath + fileName,mode='r',encoding='utf-8')
  line = f.read() #全体の読み込み
  print(line)
else:
  print('ファイルが存在しません path = {}'.format(getCurrentDir() + filePath))
