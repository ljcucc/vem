import os
from os import path
import json

from ..command import Command, CmdInfo
from ..mp_controller import MPController
from ..controllers.config_controller import ConfigController

import random
import string
rand_char = lambda y: ''.join(random.choice(string.ascii_letters) for x in range(y))

class InitCommand(Command):
  """Command 'init' class"""
  def __init__(self):
    super().__init__(CmdInfo("init", "create a VM instance for current folder"))
    self.config = {}
    self.mpc = MPController()

  def run(self):
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
    current_folder = os.getcwd()
    config = {
      "version": 1,
      "name": os.path.basename(current_folder).lower().replace("_","-"),
      "disk": "10G",
      "dir": current_folder
    }
    config['name'] = input(f"* environment name: ({config['name']}) ") or config['name']
    while True:
      rid = rand_char(6)
      name = rid+config['name']
      if(not self.mpc.exists(name)):
        config['name'] = rand_char(6)+"-"+config['name']
        break

    config['disk'] = input(f"* disk size: ({config['disk']}) ") or config['disk']

    print()
    print(json.dumps(config, indent=4))

    confirm = input("\nIs this OK? (yes) ")
    if not (len(confirm) > 0 and (confirm[0].lower() == 'y' or confirm[0] == '\n')):
      print("canceled")
      exit(1)

    return config
  
  def read_config(self):
    cc = ConfigController()

    print(f"\n[1/1] init VM instance in {cc.current_folder} ...")

    if(not cc.exists()):
      print("config file not exists...")
      self.config = self.prompt_config()
      cc.write(self.config)
    else:
      print("config file exists, read from config file...")
      self.config = cc.read()
    
  def launch(self):
    cc = ConfigController()
    self.mpc.launch_vm(cc.convData(self.config))