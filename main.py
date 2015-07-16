# Imports
from path import Path
from config import Config
from logger import Logger
from os import getcwd

# Globals
path = {}
working_dir = getcwd()
config = Config()
log = Logger(working_dir)
log.set_current_level(log.level[config.get_value("log_level")])

# Debug logging
log("Working Directory: " + working_dir, log.level["debug"])
log("Kwargs: ", log.level["debug"])
for key, value in config.kwargs.items():
    log("{0}: {1}".format(key, value), log.level["debug"])
log("Flags: ", log.level["debug"])
for value in config.flags:
    log(flag, log.level["debug"])

# Initialize paths
for key, value in config.kwargs.items():
    if "directory" in key:
        path[key] = Path(value, log)
        
master_subdirs = {"mods":config.get_value("master_mods"),
                  "client_mods":config.get_value("master_client_mods"),
                  "config":config.get_value("master_config"),
                  "bin":config.get_value("master_bin")}
path["master_directory"].add_subdirs(master_subdirs)

