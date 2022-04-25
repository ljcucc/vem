from mpu.command import CmdInfo, Command


class DoctorCommand(Command):
  """A command tool to help you setup and diagnosis vem"""
  def __init__(self) -> None:
      super().__init__(
        CmdInfo("doctor", "A command tool to help you setup and diagnosis vem")
      )