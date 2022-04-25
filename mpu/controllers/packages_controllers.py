from mpu.controllers.config_controller import ConfigController, ConfigData
from mpu.controllers.instance_controller import InstanceController


class PMController:
  """PackageManagerController: A controller to return, build package manager commands"""

  target:list = ["multipass", "ubuntu"]
  """target list that command supports"""

  def __init__(self) -> None:
    pass
  
  def installs(self, packages:list):
    """get install packages command by pass a list[str]"""
    return [
      "sudo apt-get update",
      "sudo apt-get -y install " + (" ".join(packages))
    ]

  def install(self,pkg_name) -> list:
    """get installation command string"""
    return [
      f"sudo apt-get update",
      f"sudo apt-get -y install {pkg_name}"
    ]
  
  def uninstall(self, pkg_name) -> list:
    """get uninstallation command string"""
    return [
      f"sudo apt-get -y uninstall {pkg_name}",
      "sudo apt-get autoremove"
    ]

class AptGet(PMController):
  def __init__(self) -> None:
    super().__init__()

class PackagesController:
  """Operate packages of a instance"""
  def __init__(self, pmc:PMController, ic:InstanceController, cc:ConfigController) -> None:
    self.pmc = pmc
    self.ic = ic
    self.cc = cc
    """PMController"""

  def resolve(self):
    """resolving (installing package from config.packages) packages and install"""

    print("Resolving packages from config file...")
    self.installs(self.cc.getConfig().packages)

  def installs(self, packages:list):
    """install packages by pass a list[str]"""
    name = self.cc.getConfig().name

    for cmd in self.pmc.installs(packages):
      self.ic.exec(name, cmd)

  def install(self, package_name:str):
    """Install package by a package name (str)"""

    name = self.cc.getConfig().name

    for cmd in self.pmc.install(package_name):
      self.ic.exec(name, cmd)

  def uninstall(self, package_name:str):
    """Uninstall package by a package name (str)"""

    name = self.cc.getConfig().name
    """instance name"""

    for cmd in self.pmc.uninstall(package_name):
      self.ic.exec(name, cmd)