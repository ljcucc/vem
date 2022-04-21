import os
from os import path
import json
from xmlrpc.client import Boolean
from dataclasses import dataclass

@dataclass
class ConfigData:
  """Config data dataclass"""

  name: str
  disk: str = "10G"

class ConfigController:
  """Controller for config file"""
  def __init__(self) -> None:
    self.current_folder = os.getcwd()
    self.config_path = path.join(self.current_folder, "mpconfig.json")

  def exists(self) -> Boolean:
    """check config file is exists or not"""
    return path.exists(self.config_path)

  def write(self, config):
    """write all config object to file"""
    with open(self.config_path, '+w') as jsonf:
      json.dump(config ,jsonf, indent=4)
  
  def read(self):
    """read out all config from file"""
    with open(self.config_path) as jsonf:
      return json.load(jsonf)
  
  def convData(self, config):
    """return a dataclass from config object"""
    return ConfigData(
      name=config["name"],
      disk=config["disk"]
    )