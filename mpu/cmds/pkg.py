import os
from os import path

from mpu.controllers.args_controller import ArgsController
from ..command import Command, CmdInfo, CommandManager

class UninstallCommand(Command):
  """'pkg uninstall'"""
  def __init__(self) -> None:
    super().__init__(
      CmdInfo("uninstall", "Uninstall a package from instance")
    )

class InstallCommand(Command):
  """'pkg install'"""
  def __init__(self) -> None:
    super().__init__(
      CmdInfo("install", "Install a package to instance")
    )

class ListCommand(Command):
  """'pkg list'"""
  def __init__(self) -> None:
      super().__init__(
        CmdInfo("list", "List all installed packages on a instance")
      )

class PkgCommand(Command):
  """Command 'pkg' class"""

  def __init__(self):
    super().__init__(
      CmdInfo("pkg", "manage package of VM instance")
    )

    self.cm = CommandManager([
      UninstallCommand(),
      InstallCommand()
    ])
  
  def run(self, args: ArgsController):
    """while pkg command executed"""
    if not args.isValidCmd():
      print(self.cm.disp_help(usage="""vem pkg <command> [...options]"""))
    func = args.down_level().title()
