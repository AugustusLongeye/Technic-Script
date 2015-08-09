# Imports
from folder import Folder
from config import Config
from logger import Logger
from os import getcwd
from sys import argv

# Inits
working_dir = Folder(getcwd())
working_dir.add_subdirs({"bin":"bin", 
                         "config":"config", 
                         "mods":"mods"})
config = Config()
config.parse_args(argv)
log = Logger(working_dir,
             config.get_value("log_level"),
             config.get_value("log_location"),
             config.get_value("output_style"))

# Debug logging
log("Working Directory: " + working_dir, log.level["debug"])
log(config.print_state(), log.level["debug"])

# Initialize paths
for key, value in config.kwargs.items():
    if "dir" in key:
        folder[key] = Folder(value)

folder["master_directory"].add_subdirs({
                "mods":config.get_value("master_mods"),
                "client_mods":config.get_value("master_client_mods"),
                "config":config.get_value("master_config"),
                "bin":config.get_value("master_bin")})

# Operation Methods
def backup():
    pass

def purge():
    pass

def sync():
    pass

def zip_pack():
    log("Zipping pack from current working directory.")
    working_dir.zip(config.kwargs["pack_name"])
    log("Pack zipped!")

def move_packs():
    pass

def clean_up():
    log("Removing working dir and all contents....")
    working_dir.wipe(reinit=False)
    log("Working dir removed.")
