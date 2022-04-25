from mpu.controllers.instance_controller import InstanceController


class DockerController(InstanceController):
  """A instance controller by using Docker"""

  def is_running(self): 
    result = self.cmd_run_bg("""docker info --format \"{{json . }}\"""")
    return not "ServerErrors" in result
  
  def info_vm(self, name):
    if not self.is_running():
      print("dockerd currently not running")

  def list_vm(self):
    if not self.is_running():
      return []