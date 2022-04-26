import os
from os import path
import json

# from mpu.controllers.args_controller import ArgsController
# from mpu.controllers.instance_controller import InstanceController
# from mpu.controllers.packages_controllers import AptGet, PMController, PackagesController

from mpu.command import *
# from ..controllers.engine.mp_controller import MPController
# from ..controllers.config_controller import ConfigController, ConfigData

from mpu.controllers import *

import random
import string

from mpu.controllers.engine.docker_controller import DockerController
rand_char = lambda y: ''.join(random.choice(string.ascii_letters) for x in range(y))

class InitCommand(Command):
  """Command 'init' class"""
  def __init__(self, ic:InstanceController):
    super().__init__(CmdInfo("init", "create a VM instance for current folder"))
    self.config = {}
    self.mpc = ic

  def run(self, args:ArgsController):
    """while command is executed"""
    self.read_config()
    self.launch()
  
  def read_options(self):
    """parse args option"""
  
  def prompt_config(self):
    """Prompt user to input config file."""

    # Init config object
    current_folder = os.getcwd()
    config = ConfigData(
      name = os.path.basename(current_folder).lower().replace("_","-"), 
      dir = current_folder
    )

    # Prompt instance name
    config.name = input(f"* environment name: ({config.name}) ") or config.name
    while True:
      rid = rand_char(6)
      name = rid+config.name
      if(not self.mpc.exists(name)):
        config.name = rand_char(6)+"-"+config.name
        break

    # Prompt disk name
    config.disk = input(f"* disk size: ({config.disk}) ") or config.disk

    # Prompt package manager
    config.pm_cli = input(f"* package manager: ({config.pm_cli}) ") or config.pm_cli

    # Choose virtualization engine
    while True:
      print(f"\nengine options: {engine_options}")
      engine = input(f"* engine: ({config.engine}) ") or config.engine
      if(not engine in engine_options):
        print(f"engine '{engine}' option not found. ", end="\n")
        continue
      
      break

    if engine == "docker":
      self.mpc = DockerController()

    self.mpc.init_process()

    # Display final config
    print()
    print(json.dumps(config.toDict(), indent=4))

    # Confirm config before write to file
    confirm = input("\nIs this OK? (yes) ")
    if not (len(confirm) > 0 and (confirm[0].lower() == 'y' or confirm[0] == '\n')):
      print("canceled")
      exit(1)

    return config
  
  def read_config(self):
    """read config object from file or user's input."""
    cc = ConfigController()

    print(f"\n[1/1] init VM instance in {cc.current_folder} ...")

    if(not cc.exists()):
      print("config file not exists...")
      self.config = self.prompt_config()
      cc.setConfig(self.config)
    else:
      print("config file exists, read from config file...")
      self.config = cc.getConfig()
      # print(self.config)
    
  def launch(self):
    """launch a instance by using MPController"""

    # Create VM instance
    cc = ConfigController()
    self.mpc.launch_vm(cc.convData(self.config))

    # Init instance
    self.pmc:PMController = AptGet()
    self.pc = PackagesController(self.pmc, self.mpc, cc)
    self.pc.resolve()
