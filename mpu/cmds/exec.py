from cmd import Cmd
from mpu.command import Command, CommandManager, CmdInfo
from mpu.controllers.args_controller import ArgsController
from mpu.controllers.instance_controller import InstanceController
from mpu.controllers.engine.mp_controller import MPController
from mpu.controllers.config_controller import ConfigController

class ExecCommand(Command):
  """Execute command dirctly into instance"""

  def __init__(self, ic:InstanceController) -> None:
    super().__init__(
      CmdInfo("exec", "(Not recommend to do this) Execute a command to instance")
    )
    self.ic = ic
  
  def run(self, args: ArgsController):
    """run command into instance"""
    name = ConfigController().getConfig().name

    self.ic.exec(name, args.source())

class RunCommand(ExecCommand):
  """Execute command dirctly into instance"""

  def __init__(self, ic) -> None:
    super().__init__(ic)
    self.info = CmdInfo("run", "same as exec")