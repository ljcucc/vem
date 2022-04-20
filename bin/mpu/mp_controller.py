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
  
  def list_vm(self):
    jsons = str(subprocess.run(["multipass", "list", "--format","json"], stdout=subprocess.PIPE).stdout.decode("utf-8"))
    vms = []

    obj = json.loads(jsons)
    for vm in obj["list"]:
      vms.append(vm["name"])
    
    return vms