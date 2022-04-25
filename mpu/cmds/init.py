import os
from os import path
import json

from mpu.controllers.args_controller import ArgsController

from ..command import Command, CmdInfo
from ..mp_controller import MPController
from ..controllers.config_controller import ConfigController, ConfigData

import random
import string
rand_char = lambda y: ''.join(random.choice(string.ascii_letters) for x in range(y))

class InitCommand(Command):
  """Command 'init' class"""
  def __init__(self):
    super().__init__(CmdInfo("init", "create a VM instance for current folder"))
    self.config = {}
    self.mpc = MPController()

  def run(self, args:ArgsController):
    """while command is executed"""
    self.read_config()
    self.launch()
  
  def read_options(self):
    # import argparse

    # my_parser = argparse.ArgumentParser()
    # # my_parser.add_argument('init', action='store', type=int, nargs=3)
    # my_parser.add_argument('-y', action='store')

    # args = my_parser.parse_args()
    a=0

    # print(args)
  
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
      print(self.config)
    
  def launch(self):
    """launch a instance by using MPController"""
    cc = ConfigController()
    self.mpc.launch_vm(cc.convData(self.config))