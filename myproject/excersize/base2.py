#例外の作成(Exceptionの継承)
class CharacterAlreadyExistException(Exception):
  pass

#全体のキャラ管理
class AllCharacters:

  all_characters = []
  alive_characters = []
  dead_characters = []

  #クラス内変数の取得のためclassMethod
  @classmethod
  def character_append(cls,name):
    if name in cls.all_characters:
      raise CharacterAlreadyExistException('キャラクター {} はすでに存在しています。'.format(name))
    cls.all_characters.append(name)
    cls.alive_characters.append(name)

  @classmethod
  def character_delete(cls,name):
    cls.alive_characters.remove(name)
    cls.dead_characters.append(name)

#キャラクタークラス
class Character:

  def __init__(self,name,hp,offense,defense):
    AllCharacters.character_append(name)
    self.name = name
    self.hp = hp
    self.offense = offense
    self.defense = defense

  def attack(self,enemy,critical = 1):
    if self.hp <= 0 :
      print('キャラクター {} はすでに死んでいます。'.format(self.name))
      return
    attack_point = self.offense - enemy.defense
    attack_point = 1 if attack_point <= 0 else attack_point
    enemy.hp -= attack_point *critical
    if enemy.hp <= 0 :
      AllCharacters.character_delete(enemy.name)

  def critical_hit(self,enemy):
    self.attack(enemy,2)

  def __str__(self):
    if self.name in AllCharacters.alive_characters:
      return '{}の体力は{}です'.format(self.name,self.hp)
    else:
      return '{}は死んでいます,体力は{}です'.format(self.name, self.hp)

character_a = Character('taro',10,10,10)
character_b = Character('jiro',10,2,2)

character_a.attack(character_b)
print(character_b)
character_a.attack(character_b)
print(character_b)

#死んでいるキャラクタ
character_b.attack(character_a)

#重複キャラ作成
try:
  character_a = Character('taro',10,10,10)
except CharacterAlreadyExistException as e:
  print(e)
