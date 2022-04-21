from dataclasses import dataclass

from mpu.controllers.args_controller import ArgsController

class Command:
  """Empty command tmeplate class"""
  def __init__(self, info) -> None:
    self.info = info
  
  def run(self, args:ArgsController):
    """undefined run function, which will run custom command code after overrided."""
    print("not defined")

@dataclass
class CmdInfo:
  """CmdInfo structure which will store help info about command"""
  name:str
  description:str = "no description"

  def title_help(self):
    """Get line help formatted string."""
    return self.name.ljust(10) + self.description


@dataclass
class CommandManager:
  """managing multiple commands"""
  cmds:list

  def indexOf(self, name):
    """get the index of command in command sequence"""
    for index, item in enumerate(self.cmds):
      if(item.info.name == name): return index
  
    return -1
  
  def exec(self, name, args:ArgsController):
    """execute command by using name"""
    if(self.indexOf(name) == -1):
      raise Exception("Command name not found")

    self.cmds[self.indexOf(name)].run(args)