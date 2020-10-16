from typing import Iterable
import configparser
import os
import argparse


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
    parser = argparse.ArgumentParser()
    parser.add_argument("profile_name", help="Enter the name of profile you"
                        " want to apply")
    args = parser.parse_args()
    cfmgr = config_manager()
    cfmgr.set_profile(args.profile_name)
