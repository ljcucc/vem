from mpu.controllers.config_controller import ConfigData


class PMController:
  """PackageManagerController: A controller to return, build package manager commands"""

  target:list = ["multipass", "ubuntu"]
  """target list that command supports"""

  def __init__(self) -> None:
    pass
  
  def install(self,pkg_name) -> list:
    """get installation command string"""
    return [
      f"sudo apt-get update"
      f"sudo apt-get -y install {pkg_name}"
    ]
  
  def uninstall(self, pkg_name) -> list:
    """get uninstallation command string"""
    return [
      f"sudo apt-get -y uninstall {pkg_name}"
      "sudo apt-get autoremove"
    ]

class AptGet(PMController):
  def __init__(self) -> None:
    super().__init__("apt-get")

class PackagesController:
  """A controller to install, uninstall package by using PMController"""
  def __init__(self, pmc:PMController) -> None:
    self.pmc = pmc
    """PMController"""

  def resolve(self, config: ConfigData):
    """resolving (installing package from config.packages) packages and install"""
    for package in config.packages:
      self.install(package)

  def install(self, package_name:str):
    """Install package by a package name (str)"""
    for cmd in self.pmc.install():
      

  def uninstall(self, package_name:str):
    """Uninstall package by a package name (str)"""