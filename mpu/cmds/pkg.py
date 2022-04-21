import os
from os import path

from mpu.controllers.args_controller import ArgsController
from ..command import Command, CmdInfo

class PkgCommand(Command):
  """Command 'pkg' class"""

  def __init__(self):
    super().__init__(
      CmdInfo("pkg", "manage package of VM instance")
    )
  
  def run(self, args: ArgsController):
    func = args.down_level().title()