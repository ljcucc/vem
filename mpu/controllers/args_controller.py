import sys
import copy

class ArgsController:
  def __init__(self) -> None:
    self.args = copy.deepcopy(sys.argv)
    del self.args[0]

    self.levels = []
    self.parse()
  
  def isValidCmd(self):
    print(self.levels)
    return len(self.levels) > 0
  
  def parse(self):
    while len(self.args) > 0:
      head = self.args[0]
      if(head[0] == "-"):
        break
      del self.args[0]
      self.levels.append(head)
  
  def command_head(self):
    return self.levels[0]
  
  def title(self): return self.command_head()
  
  def down_level(self):
    obj = copy.deepcopy(self)
    del obj.levels[0]