from mpu.controllers.args_controller import ArgsController
from mpu.controllers.instance_controller import InstanceController
from ..command import Command, CmdInfo
from ..controllers.engine.mp_controller import MPController
from ..controllers.config_controller import ConfigController

class RemoveCommand(Command):
  def __init__(self, ic:InstanceController) -> None:
    super().__init__(CmdInfo("rm", "remove current folder's instance totally"))
    self.mpc = ic
  
  def run(self, args:ArgsController):
    """remove currnet folder instance"""
    cc = ConfigController()
    cd = cc.convData(cc.read()) # cd: Config Data

    self.mpc.remove_vm(cd.name)
    print("process finished!")