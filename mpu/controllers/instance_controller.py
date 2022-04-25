from mpu.controllers.config_controller import ConfigData

class InstanceController:
  """A controller to operate virtualization interface"""
  def __init__(self) -> None:
    pass

  def list_vm(self):
    """return all instances list object"""
    pass

  def info_vm(self, name):
    """print info of a instance"""
    pass

  def remove_vm(self, name):
    """remove vm instance"""
    pass

  def exec(self, name, cmd):
    """run a command to a instance"""
    pass
  
  def exists(self, name):
    """check a instance is exists or not by using name of it"""
    pass

  def launch_vm(self, config:ConfigData):
    """launch command alt of multipass"""
    pass
