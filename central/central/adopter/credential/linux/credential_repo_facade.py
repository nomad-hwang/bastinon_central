import grp
import os
import pwd
import warnings

from pydantic import BaseModel

credential_error = {
    "NP": "user has no password set",
    None: "user has no password set",
    "!": "user has no password set",
    "": "user has no password set",
    "LK": "account is locked",
    "*": "account is locked",
    "!!": "password has expired",
}


class LinuxLocalCredentialOpitons(BaseModel):
    group_name: str = "tunnel_user_group"
    shell: str = "/bin/true"  # TODO: Maybe we should use /bin/false or /sbin/nologin


class LinuxUserCredential(BaseModel):
    username: str
    password: str | None = None
    error: str | None = None


""" 
This class is a facade for the credential repo.
Only for prototyping purpose. Really should not be used in production.
"""


class LinuxCredentialFacade(object):
    def __init__(
        self, options: LinuxLocalCredentialOpitons = LinuxLocalCredentialOpitons()
    ):
        self._options = options

        if os.geteuid() != 0:
            raise PermissionError("This module requires root previledge")
        warnings.warn(f"Use {self.__class__.__name__} only for prototyping")
        self._creat_group()

    def _creat_group(self) -> None:
        try:
            grp.getgrnam(self._options.group_name)
        except KeyError:
            os.system(f"sudo groupadd {self._options.group_name}")

    def _create_user(self, username: str, password: str) -> str | None:
        # https://unix.stackexchange.com/questions/14312/how-to-restrict-an-ssh-user-to-only-allow-ssh-tunneling#comment19210_14313
        if self._user(username) is not None:
            return "user already exists"
        cmd = f"useradd -M -s {self._options.shell} {username} -G {self._options.group_name}"
        if self.__cmd(cmd):
            return "user creation failed"
        self._change_password(username, password)
        return None

    def _change_password(self, username: str, password: str):
        if self._user(username) is None:
            raise ValueError("user does not exist")
        if self.__cmd(f"echo {username}:{password} | sudo chpasswd"):
            raise ValueError("password change failed")

    def _get_user(self, username: str) -> tuple[str | None, str | None]:
        if user := self._user(username) is None:
            return None, None
        user = pwd.getpwnam(username)
        return user.pw_name, user.pw_passwd

    def _user(self, username: str):
        try:
            return pwd.getpwnam(username)
        except KeyError:
            return None

    def __cmd(self, cmd: str) -> int:
        return os.system(cmd)
