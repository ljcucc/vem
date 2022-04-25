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
  
  def disp_help(self):
    """return help docs string"""

    return """
using 
    """
 
  def run(self, args: ArgsController):
    if not args.isValidCmd():
      print(self.disp_help())
    func = args.down_level().title()
