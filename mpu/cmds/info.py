from mpu.controllers.args_controller import ArgsController
from ..command import CmdInfo, Command
from ..mp_controller import MPController

class InfoCommand(Command):
  """Command 'info' class"""

  def __init__(self) -> None:
    super().__init__(CmdInfo("info", "Get info of instance (aka. multipass info)"))
    self.mpc = MPController()

  def run(self, args:ArgsController):
    self.mpc.info_vm()