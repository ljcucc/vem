from mpu.command import *

class StopCommand(Command):
  def __init__(self, ic:InstanceController) -> None:
    super().__init__(
      CmdInfo("stop", "stop or pause instance")
    )

    self.ic = ic
  
  def run(self, args: ArgsController):
      return super().run(args)