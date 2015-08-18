# Imports
from folder import Folder
from config import Config
from logger import Logger
import exception
import shutil
from os import getcwd
from sys import argv


# Inits
config = Config()
config.parse_args(argv)
log = Logger(current_level = config.get_value("log_level"),
             output = config.get_value("log_location"),
             output_style = config.get_value("output_style"))
folder = {}
working_dir = Folder(getcwd()+"/working_dir")
working_dir.add_subdirs({"bin":"bin", 
                         "config":"config", 
                         "mods":"mods"})

def init():
    log("Initialising folders.....")
    
    for key, value in config.kwargs.items():
        if "dir" in key:
            if "master" in key:
                conti
            folder[key] = Folder(value, name=key)

    folder["master_dir"].add_subdirs({
                "mods":config.get_value("master_mods"),
                "client_mods":config.get_value("master_client_mods"),
                "config":config.get_value("master_config"),
                "bin":config.get_value("master_bin")})
    folder["minecraft_dir"].add_subdirs({
                "mods":"mods",
                "config":"config"})
    log("Done!")
    
    if config.get_flag("no-backup"):
        command_chain.pop(0)
        
def debug_log():
    log("Working Directory: " + str(working_dir), log.level["debug"])
    log(config.print_state(), log.level["debug"])
    for key, val in folder.iteritems():
        log(val.print_state(), log.level["debug"])


# Operation Methods
def backup():
    log("Backing up pack.....")
    
    backup_name = ""
    if "{" in config.get_value("backup_name"):
        backup_name = config.get_value("backup_name").format(log.now)
    else:
        backup_name = config.get_value("backup_name")
        
    shutil.move(folder["web_dir"] + config.get_value("pack_name"),
         folder["backup_dir"] + backup_name)
    log("Pack moved to " + folder["backup_dir"] + backup_name,
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
                                  dst=folder["minecraft_dir"]
                                      .subdirs["mods"]),
        log.level["verbose"])
    log(folder["master_dir"].copy(subdir="config", 
                                  dst=folder["minecraft_dir"]
                                      .subdirs["config"]),
        log.level["verbose"])
    
    log("Done!")
    log("Copying files to client.....")
    
    log(folder["master_dir"].copy(subdir="mods",
                                  dst=working_dir.subdirs["mods"]),
        log.level["verbose"])
    log(folder["master_dir"].copy(subdir="client_mods",
                                  dst=working_dir.subdirs["mods"]),
        log.level["verbose"])
    log(folder["master_dir"].copy(subdir="config",
                                  dst=working_dir.subdirs["config"]),
        log.level["verbose"])
    log(folder["master_dir"].copy(subdir="bin",
                                  dst=working_dir.subdirs["bin"]),
        log.level["verbose"])
    
    log("Done!")
    
def zip_pack():
    log("Zipping pack from current working directory.....")
    
    working_dir.zip(config.kwargs["pack_name"])
    
    log("Done!")

def move_pack():
    log("Moving zip to web directory.....")
    
    shutil.move(working_dir() + config.get_value("pack_name") + ".zip", 
         folder["web_dir"])
    
    log("Done!")

def clean_up():
    log("Removing working dir and all contents.....")
    
    working_dir.wipe(reinit=False)
    
    log("Done!")


# Main
command_chain=[backup, purge, sync, zip_pack, move_pack, clean_up]

if __name__ == "__main__":
    try:
        init()
        if debug in log.get_log_level():
            debug_log()
        for command in command_chain:
            command()
    except Error as e:
        #Catch all custom errors, ignore all else.
        if "debug" in log.get_log_level():
            raise
        else:
            log.error("Exception occured, see log for details.", e)