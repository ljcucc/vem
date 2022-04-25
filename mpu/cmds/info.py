from mpu.controllers.args_controller import ArgsController
from mpu.controllers.instance_controller import InstanceController
from ..command import CmdInfo, Command
from ..controllers.engine.mp_controller import MPController
from mpu.controllers.config_controller import *

class InfoCommand(Command):
  """Command 'info' class"""

  def __init__(self, ic:InstanceController) -> None:
    super().__init__(CmdInfo("info", "Get info of instance (aka. multipass info)"))
    self.mpc = ic

  def run(self, args:ArgsController):
    name = ConfigController().getConfig().name
    self.mpc.info_vm(name)