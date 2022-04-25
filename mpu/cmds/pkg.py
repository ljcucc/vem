import os
from os import path

from mpu.controllers.args_controller import ArgsController
from mpu.controllers.config_controller import ConfigController
from ..command import Command, CmdInfo, CommandManager
from mpu.mp_controller import MPController

class UninstallCommand(Command):
  """'pkg uninstall'"""
  def __init__(self) -> None:
    super().__init__(
      CmdInfo("uninstall", "Uninstall a package from instance")
    )
    self.mpc = MPController()
    self.cc = ConfigController()

  def run(self, args: ArgsController):
    pkg_name = args.title()
    config = self.cc.getConfig()
    pm_cli = config.pm_cli

    # TODO: currently only support apt-get, this will merge into PMController
    self.mpc.exec(config.name, f"sudo {pm_cli} -y uninstall {pkg_name}")
    self.mpc.exec(config.name, f"sudo {pm_cli} autoremove")

    config.packages.remove(pkg_name)
    self.cc.setConfig(config)

class InstallCommand(Command):
  """'pkg install'"""
  def __init__(self) -> None:
    super().__init__(
      CmdInfo("install", "Install a package to instance")
    )
    self.mpc = MPController()
    self.cc = ConfigController()
  
  def run(self, args: ArgsController):
    pkg_name = args.title()
    config = self.cc.getConfig()
    pm_cli = config.pm_cli

    # TODO: currently only support apt-get, this will merge into PMController
    self.mpc.exec(config.name, f"sudo {pm_cli} update")
    self.mpc.exec(config.name, f"sudo {pm_cli} -y install {pkg_name}")

    config.packages.append(pkg_name)
    print(config)
    self.cc.setConfig(config)

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
      return False
    # print(args.title())
    self.cm.exec(args.title(), args.down_level())
