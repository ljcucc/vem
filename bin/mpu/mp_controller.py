from dataclasses import dataclass
import os
import subprocess
import json

from dataclasses import dataclass

@dataclass
class InstanceInfo:
  name: str
  disk: str

class MPController:
  def __init__(self) -> None:
    pass

  def cmd_run_bg(self,cmds):
    return str(subprocess.run(cmds.split(" "), stdout=subprocess.PIPE).stdout.decode("utf-8"))

  def cmd_run_bg(self,cmds):
    return str(subprocess.run(cmds.split(" ")).stdout.decode("utf-8"))
  
  def list_vm(self):
    vms = []

    obj = json.loads(self.cmd_run_bg("multipass list --format json"))
    for vm in obj["list"]:
      vms.append(vm["name"])
    
    return vms
  
  def info_vm(self, name):
    self.cmd_run(f"multipass info {name}")