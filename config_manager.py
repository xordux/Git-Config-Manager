from typing import Iterable
import configparser
import os


class config_manager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("profiles.cfg")

    def is_profile(self, profile_name: str) -> bool:
        return profile_name in self.config

    def get_properties(self, profile_name: str) -> Iterable:
        return self.config[profile_name]

    def set_profile(self, profile_name):
        for k in self.config[profile_name]:
            cmd = f"git config --global --unset {k}"
            print(cmd)
            os.system(cmd)
            target = self.config[profile_name][k]
            if target != "UNSET":
                cmd = f"git config --global {k} {target}"
                print(cmd)
                os.system(cmd)

if __name__ == "__main__":
    cfmgr = config_manager()
    cfmgr.set_profile("home")
