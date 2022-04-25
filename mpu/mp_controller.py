from dataclasses import dataclass
import os
import subprocess
import json

from dataclasses import dataclass

from .controllers.config_controller import ConfigData

@dataclass
class InstanceInfo:
  name: str
  disk: str

class MPController:
  """AKA, MultiPass-Controller"""
  def __init__(self) -> None:
    pass

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
  
  def list_vm(self):
    """return all instances list object"""
    vms = []

    obj = json.loads(self.cmd_run_bg("multipass list --format json"))
    for vm in obj["list"]:
      vms.append(vm["name"])
    
    return vms
  
  def info_vm(self, name):
    """print info of a instance"""
    self.cmd_run(f"multipass info {name}")
  
  def remove_vm(self, name):
    """remove vm instance"""
    self.cmd_run(f"multipass delete {name}")
    self.cmd_run(f"multipass purge")

  def exec_vm(self, name):
    """run a command to a instance"""

  def exists(self, name):
    """check a instance is exists or not by using name of it"""
    return name in self.list_vm()

  def launch_vm(self, config:ConfigData):
    """launch command alt of multipass"""
    self.cmd_run_disp(f"multipass launch --name {config.name} --disk {config.disk}")