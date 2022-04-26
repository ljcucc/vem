from mpu.command import *

class ConfigCommand(Command):
  def __init__(self) -> None:
    super().__init__(
      CmdInfo("config", "udpate or read config to or from VM instance")
    )