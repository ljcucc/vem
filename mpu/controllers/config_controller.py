import os
from os import path
import json
from dataclasses import dataclass, field
import dataclasses
from typing import List

def dataclass_from_dict(classname, d):
  try:
    fieldtypes = {f.name:f.type for f in dataclasses.fields(classname)}
    return classname(**{f:dataclass_from_dict(fieldtypes[f],d[f]) for f in d})
  except:
    return d # Not a dataclass field

@dataclass
class ConfigData:
  """Config data dataclass"""

  version:int  = 1
  """version of ConfigData"""

  name: str = ""
  """name of the env (instance)"""

  disk: str = "10G"
  """disk space size"""

  recorded:bool = True 
  """enable this will record every command you type from 'exec'"""

  dir:str = ""
  """dir name"""

  pm_cli = "apt-get"
  """package manager cli name (or path)"""

  packages:list =  field(default_factory=lambda:[])
  """installed packages list"""
    
  @staticmethod
  def fromDict(d:dict):
    """convert dict to config data"""
    return dataclass_from_dict(ConfigData, d)

  def toDict(self) -> dict:
    """convert config data to dict"""
    return dataclasses.asdict(self)
  
  def toJsons(self) -> str:
    """convert config data to json string"""
    return json.dumps(self.toDict())

class ConfigController:
  """Controller for config file"""
  def __init__(self) -> None:
    self.current_folder = os.getcwd()
    """the folder that program currently running at (user execution)"""

    self.config_path = path.join(self.current_folder, "mpconfig.json")
    """string path to config file"""

  def exists(self) -> bool:
    """check config file is exists or not"""
    return path.exists(self.config_path)

  def write(self, config):
    """deprecated: write all config object to file"""
    print(config)

    with open(self.config_path, '+w') as jsonf:
      json.dump(config ,jsonf, indent=4)
  
  def read(self):
    """deprecated: read out all config from file"""

    with open(self.config_path) as jsonf:
      return json.load(jsonf)

  def setConfig(self, cd:ConfigData):
    """write all config data object to file"""
    self.write(cd.toDict())
    
  def getConfig(self) -> ConfigData:
    """get config data object from file"""
    return self.convData(self.read())
  
  def convData(self, config):
    """return a dataclass from dict object"""

    cd = ConfigData.fromDict(config)
    return cd