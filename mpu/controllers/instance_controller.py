from mpu.controllers.config_controller import ConfigData
import subprocess

class InstanceController:
  """A controller to operate virtualization interface"""

  def cmd_run_bg(self,cmds):
    """run command without showing output and return output"""
    return str(subprocess.run(cmds.split(" "), stdout=subprocess.PIPE).stdout.decode("utf-8"))

  def cmd_run(self,cmds):
    """run command without hidding output (and no returning output)"""
    return str((subprocess.run(cmds.split(" ")).stdout or b"").decode("utf-8"))

  def cmd_run_disp(self,cmds):
    """run command and display it as a format: 
      CMD: [cmd_str]
    """
    print("CMD: ", cmds)
    self.cmd_run(cmds)

  def __init__(self) -> None:
    pass

  def init_process(self) -> None:
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
