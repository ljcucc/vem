from dataclasses import dataclass

from mpu.controllers.args_controller import ArgsController
from mpu.controllers.instance_controller import InstanceController

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

  def disp_help(self, usage="vem <command> [...options]"):
    description = ("""
usage: 
"""
+"  "+usage
+
"""

Available commands:
""")

    for cmd in self.cmds:
      description += "  " + (cmd.info.title_help()) + "\n"
  
    return description

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
  
  def run(self, args:ArgsController) -> bool:
    """run command by args. accept ArgsController, if command not found returns False"""
    func_name = args.command_head()
    if(self.indexOf(func_name) == -1):
      print(f"command \"{func_name}\" not found")
      return False
    self.exec(func_name, args = args.down_level())
    return True