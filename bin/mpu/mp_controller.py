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
  def __init__(self) -> None:
    pass

  def cmd_run_bg(self,cmds):
    return str(subprocess.run(cmds.split(" "), stdout=subprocess.PIPE).stdout.decode("utf-8"))

  def cmd_run(self,cmds):
    return str((subprocess.run(cmds.split(" ")).stdout or b"").decode("utf-8"))

  def cmd_run_disp(self,cmds):
    print("CMD: ", cmds)
    self.cmd_run(cmds)
  
  def list_vm(self):
    vms = []

    obj = json.loads(self.cmd_run_bg("multipass list --format json"))
    for vm in obj["list"]:
      vms.append(vm["name"])
    
    return vms
  
  def info_vm(self, name):
    self.cmd_run(f"multipass info {name}")
  
  def remove_vm(self, name):
    self.cmd_run(f"multipass delete {name}")
    self.cmd_run(f"multipass purge")

  def exists(self, name):
    return name in self.list_vm()

  def launch_vm(self, config:ConfigData):
    self.cmd_run_disp(f"multipass launch --name {config.name} --disk {config.disk}")