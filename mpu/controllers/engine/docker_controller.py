# from mpu.controllers.instance_controller import InstanceController
from mpu.controllers import *
# from mpu import *

class DockerInit:
  """init process for docker instance"""
  def __init__(self) -> None:
    print("\n--- docker init process ---", end="\n")
    self.image_id = input("* docker image: (ubuntu) ") or "ubuntu"
  
class DockerController(InstanceController):
  """A instance controller by using Docker"""

  def init_process(self) -> None:
    DockerInit()

  def is_running(self): 
    """check docker is running or not"""
    result = self.cmd_run_bg("""docker info --format \"{{json . }}\"""")
    return not "ServerErrors" in result
  
  def info_vm(self, name):
    if not self.is_running():
      print("dockerd currently not running")

  def list_vm(self):
    if not self.is_running():
      return []
  
  def launch_vm(self, config: ConfigData):
      return super().launch_vm(config)