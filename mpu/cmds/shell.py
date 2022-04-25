from mpu.command import *

class ShellCommand(Command):
  def __init__(self) -> None:
    super().__init__(
      CmdInfo("shell", """enter instance shell to execute command (not recommended to do that)""")
    )