from cmd import Cmd
from mpu.command import Command, CommandManager, CmdInfo

class ExecCommand(Command):
  def __init__(self) -> None:
    super().__init__(
      CmdInfo("exec", "(Not recommend to do this) Execute a command to instance")
    )