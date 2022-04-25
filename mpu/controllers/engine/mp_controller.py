from dataclasses import dataclass
import os
import json

from dataclasses import dataclass

from mpu.controllers.instance_controller import InstanceController

from ..config_controller import ConfigData

@dataclass
class InstanceInfo:
  name: str
  disk: str

class MPController(InstanceController):
  """AKA, MultiPass-Controller"""
  def __init__(self) -> None:
    pass
 
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
    self.cmd_run_disp(f"multipass delete {name}")
    self.cmd_run_disp(f"multipass purge")

  def exec(self, name, cmd):
    """run a command to a instance"""
    self.cmd_run_disp(f"multipass exec {name} -- {cmd}")

  def exists(self, name):
    """check a instance is exists or not by using name of it"""
    return name in self.list_vm()

  def launch_vm(self, config:ConfigData):
    """launch command alt of multipass"""
    self.cmd_run_disp(f"multipass launch --name {config.name} --disk {config.disk}")