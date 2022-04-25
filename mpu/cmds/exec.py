from cmd import Cmd
from mpu.command import Command, CommandManager, CmdInfo
from mpu.controllers.args_controller import ArgsController
from mpu.mp_controller import MPController
from mpu.controllers.config_controller import ConfigController

class ExecCommand(Command):
  def __init__(self) -> None:
    super().__init__(
      CmdInfo("exec", "(Not recommend to do this) Execute a command to instance")
    )
  
  def run(self, args: ArgsController):
    """run command into instance"""
    ic = MPController()
    name = ConfigController().getConfig().name

    ic.exec(name, args.source())

class RunCommand(ExecCommand):
  def __init__(self) -> None:
    super().__init__()
    self.info = CmdInfo("run", "same as exec")