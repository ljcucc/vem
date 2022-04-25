from mpu.command import *

class StartCommand(Command):
  def __init__(self, ic:InstanceController) -> None:
    super().__init__(
      CmdInfo("start", "restart paused instance")
    )

    self.ic = ic
  
  def run(self, args: ArgsController):
      return super().run(args)