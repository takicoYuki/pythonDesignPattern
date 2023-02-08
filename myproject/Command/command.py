from abc import ABC, abstractclassmethod
from enum import Enum

# Enumを使って定数をまとめる
class CommandNumber(Enum):

  LIGHT = 0
  TV = 1
  GAME = 2

# Receiver -> commandが実行するクラス
class TV:

  def __init__(self, name):
    self.__name = name

  def on_tv(self):
    print(f'TV: {self.__name}をonにします')

  def off_tv(self):
    print(f'TV: {self.__name}をoffにします')

class Light:

  def __init__(self, name):
    self.__name = name

  def on_light(self):
    print(f'LIGHT: {self.__name}をonにします')

  def off_light(self):
    print(f'LIGHT: {self.__name}をoffにします')

class Game:

  def __init__(self, name):
    self.__name = name

  def on_game(self):
    print(f'GAME: {self.__name}をonにします')

  def off_game(self):
    print(f'GAME: {self.__name}をoffにします')

# Command
class Command(ABC):

  # Receiverをここで使用する
  @abstractclassmethod
  def execute(self):
    pass

  @abstractclassmethod
  def undo(self):
    pass

# ConcreteCommand
class NoCommand(Command):

  def execute(self):
    pass

  def undo(self):
    pass

class LightOnCommand(Command):

  def __init__(self, light: Light):
    self.__light = light

  def execute(self):
    self.__light.on_light()

  def undo(self):
    self.__light.off_light()


class LightOffCommand(Command):

  def __init__(self, light: Light):
    self.__light = light

  def execute(self):
    self.__light.off_light()

  def undo(self):
    self.__light.on_light()

class TvOnCommand(Command):

  def __init__(self, tv: TV):
    self.__tv = tv

  def execute(self):
    self.__tv.on_tv()

  def undo(self):
    self.__tv.off_tv()

class TvOffCommand(Command):

  def __init__(self, tv: TV):
    self.__tv = tv

  def execute(self):
    self.__tv.off_tv()

  def undo(self):
    self.__tv.on_tv()

class GameOnCommand(Command):

  def __init__(self, game: Game):
    self.__game = game

  def execute(self):
    self.__game.on_game()

  def undo(self):
    self.__game.off_game()

class GameOffCommand(Command):

  def __init__(self, game: Game):
    self.__game = game

  def execute(self):
    self.__game.off_game()

  def undo(self):
    self.__game.on_game()

# Invoker
class RemoteController:

  def __init__(self):
    self.__on_commands = [NoCommand()] * len(CommandNumber)
    self.__off_commands = [NoCommand()] * len(CommandNumber)
    # undoCommandの追加
    self.__undo_command = NoCommand()

  def set_command(self, number, on_command: Command, off_command: Command):
    self.__on_commands[number] = on_command
    self.__off_commands[number] = off_command

  def on_command(self, number):
    self.__on_commands[number].execute()
    # 直近のコマンドをundoに追加する
    self.__undo_command = self.__on_commands[number]

  def off_command(self, number):
    self.__off_commands[number].execute()
    # 直近のコマンドをundoに追加する
    self.__undo_command = self.__off_commands[number]

  def undo_command(self):
    self.__undo_command.undo()


# Receiver
light = Light('My Light')
tv = TV('REGZA')
game = Game('Nintendo')

# ConcreteCommand
light_on_command = LightOnCommand(light)
light_off_command = LightOnCommand(light)
tv_on_command = TvOnCommand(tv)
tv_off_command = TvOffCommand(tv)
game_on_command = GameOnCommand(game)
game_off_command = GameOffCommand(game)

# Invoker
remote_controller = RemoteController()
remote_controller.set_command(CommandNumber.LIGHT.value, light_on_command, light_off_command)
remote_controller.set_command(CommandNumber.TV.value, tv_on_command, tv_off_command)
remote_controller.set_command(CommandNumber.GAME.value, game_on_command, game_off_command)

# Commandの実行
remote_controller.on_command(CommandNumber.LIGHT.value)
remote_controller.on_command(CommandNumber.GAME.value)
remote_controller.on_command(CommandNumber.TV.value)
remote_controller.undo_command()
remote_controller.on_command(CommandNumber.LIGHT.value)
