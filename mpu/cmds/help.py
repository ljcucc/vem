from mpu.command import *

class HelpCommand(Command):
  def __init__(self, cm:CommandManager) -> None:
    super().__init__(
      CmdInfo("help", "display help")
    )
    self.cm = cm
  
  def run(self, args: ArgsController):
    print(self.cm.disp_help())
  