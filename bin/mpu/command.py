from dataclasses import dataclass

class Command:
  def __init__(self, info) -> None:
    self.info = info
  
  def run(self):
    print("not defined")

@dataclass
class CmdInfo:
  name:str
  description:str = "no description"

  def title_help(self):
    return self.name.ljust(10) + self.description


@dataclass
class CommandManager:
  cmds:list

  def indexOf(self, name):
    for index, item in enumerate(self.cmds):
      if(item.info.name == name): return index
  
    return -1
  
  def exec(self, name):
    if(self.indexOf(name) == -1):
      raise Exception("Command name not found")

    self.cmds[self.indexOf(name)].run()