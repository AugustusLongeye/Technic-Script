# Imports
from folder import Folder
from config import Config
from logger import Logger
import exception
from os import getcwd
from sys import argv
from shutil import move


# Inits
config = Config()
config.parse_args(argv)
log = Logger(getcwd(),
             config.get_value("log_level"),
             config.get_value("log_location"),
             config.get_value("output_style"))
command_chain=[backup, purge, sync, zip_pack, move_pack, clean_up]


def init():
    log("Working Directory: " + working_dir, log.level["debug"])
    log(config.print_state(), log.level["debug"])
    
    log("Initialising folders.....")
    working_dir = Folder(getcwd())
    working_dir.add_subdirs({"bin":"bin", 
                             "config":"config", 
                             "mods":"mods"})
    
    for key, value in config.kwargs.items():
        if "dir" in key:
            folder[key] = Folder(value)

    folder["master_dir"].add_subdirs({
                "mods":config.get_value("master_mods"),
                "client_mods":config.get_value("master_client_mods"),
                "config":config.get_value("master_config"),
                "bin":config.get_value("master_bin")})
    folder["minecraft_dir"].addsubdir({
                "bin":"bin",
                "config":"config"})
    log("Done!")
    
    if config.get_flag("no-backup"):
        command_chain.pop(0)


# Operation Methods
def backup():
    log("Backing up pack.....")
    backup_name = ""
    if "{" in config.get_value("backup_name"):
        backup_name = config.get_value("backup_name").format(log.now)
    else:
        backup_name = config.get_value("backup_name")
    move(folder["web_dir"]() + config.get_value("pack_name"),
         folder["backup_dir"]() + backup_name)
    log("Pack moved to " + folder["backup_dir"]() + backup_name,
        log.level["verbose"])
    log("Done!")

def purge():
    log("Clearing up old files.....")
    folder["minecraft_dir"].wipe_subdirs()
    working_dir.wipe()
    log("Done!")

def sync():
    log("Copying files to server.....")

    log(folder["master_dir"].copy(subdir="mods", 
                                  folder["minecraft_dir"].subdir["config"])
        log.level["verbose"])
    log(folder["master_dir"].copy(subdir="config", 
                                  folder["minecraft_dir"].subdir["config"])
        log.level["verbose"])
    log("Done!")
    
    log("Copying files to client.....")
    log(folder["master_dir"].copy(subdir="mods",
                                  working_dir.subdir["mods"])
        log.level["verbose"])
    log(folder["master_dir"].copy(subdir="client_mods",
                                  working_dir.subdir["mods"])
        log.level["verbose"])
    log(folder["master_dir"].copy(subdir="config",
                                  working_dir.subdir["config"])
        log.level["verbose"])
    log(folder["master_dir"].copy(subdir="bin",
                                  working_dir.subdir["bin"])
        log.level["verbose"])
    log("Done!")
    
def zip_pack():
    log("Zipping pack from current working directory.....")
    working_dir.zip(config.kwargs["pack_name"])
    log("Done!")

def move_pack():
    log("Moving zip to web directory.....")
    move(working_dir() + pack_name + ".zip", folder["web_dir"]())
    log("Done!")

def clean_up():
    log("Removing working dir and all contents.....")
    working_dir.wipe(reinit=False)
    log("Done!")


# Main
if __name__ == "__main__":
    try:
        init()
        for command in command_chain:
            command()
    except Error as e:
        #Catch all custom errors, ignore all else.
        if "4" or "debug" in log.get_log_level():
            raise
        else:
            log.error("Exception occured, see log for details.", e)