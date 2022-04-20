import os
from os import path
from ..command import Command, CmdInfo

class PkgCommand(Command):
  def __init__(self):
    super().__init__(
      CmdInfo("pkg", "manage package of VM instance")
    )