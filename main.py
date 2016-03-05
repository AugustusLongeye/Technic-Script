# Imports
import exception
import shutil
from os import getcwd
from sys import argv

try:
    from folder import Folder
    from config import Config
    from logger import Logger
    from harsh_null import Null
    from CLUI import *
    from GUI import *
except ImportError as e:
    raise exception.ModuleMissingError(e)


# Inits
config = Config()
config.parse_args(argv)
log = Logger(current_level = config.get_value("log_level"),
             output_loc = config.get_value("log_location"),
             output_style = config.get_value("output_style"))
master_dir = Null()
working_dir = Null()
server_dir = Null()
web_dir = Null()
backup_dir = Null()
folders = Null()

def init():
    log("Initialising folders.....")
    
    global master_dir, working_dir, server_dir, web_dir, backup_dir
    global folders
    
    working_dir = Folder(getcwd()+"/working_dir",
                         name = "Working Directory")
    working_dir.add_subdirs({"bin":"bin", 
                             "config":"config", 
                             "mods":"mods"})
    
    master_dir = Folder(config.get_value("master_dir"),
                        name = "Master Directory")
    master_dir.add_subdirs({
            "mods":config.get_value("master_mods"),
            "client_mods":config.get_value("master_client_mods"),
            "config":config.get_value("master_config"),
            "bin":config.get_value("master_bin")})
    
    server_dir = Folder(config.get_value("server_dir"),
                           name = "Server Directory")
    server_dir.add_subdirs({
            "mods":"mods",
            "config":"config"})
    
    web_dir = Folder(config.get_value("web_dir"),
                     name = "Web Directory")
    
    backup_dir = Folder(config.get_value("backup_dir"), 
                        name = "Backup Directory")
    
    folders = [master_dir, working_dir, server_dir, web_dir, backup_dir]
    
    log("Done!")
    
    if config.get_flag("no-backup"):
        command_chain.pop(0)
        
def debug_log():
    log("Working Directory: " + str(working_dir), log.level["debug"])
    log(config.print_state(), log.level["debug"])
    for val in folders:
        log(val.print_state(), log.level["debug"])

# Main
if __name__ == "__main__":
    if config.get_value("headless"):
        do_clui()
    else:
        do_GUI()