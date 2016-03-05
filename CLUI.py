# Operation Methods
def backup():
    log("Backing up pack.....")
    
    backup_name = ""
    if "{" in config.get_value("backup_name"):
        backup_name = config.get_value("backup_name").format(log.now())
    else:
        backup_name = config.get_value("backup_name")
    backup_name += ".zip"
    
    try:    
        shutil.move(web_dir + config.get_value("pack_name") + ".zip",
                    backup_dir + backup_name)
        log("Pack moved to " + str(backup_dir) + backup_name,
            log.level["verbose"])
    except IOError as e:
        # if the file doesn't exist, pass.
        if e.errno is 2:
            log("No file to backup, skipping!")
            pass
        else:
            raise e
            
    log("Done!")

def purge():
    log("Clearing up old files.....")
    
    server_dir.wipe_subdirs()
    working_dir.wipe()
    
    log("Done!")

def sync():
    log("Copying files to server.....")

    log(master_dir.copy(subdir="mods", 
                        dst=server_dir.subdirs["mods"]),
        log.level["verbose"])
    log(master_dir.copy(subdir="config", 
                        dst=server_dir.subdirs["config"]),
        log.level["verbose"])
    
    log("Done!")
    log("Copying files to client.....")
    
    log(master_dir.copy(subdir="mods",
                        dst=working_dir.subdirs["mods"]),
        log.level["verbose"])
    log(master_dir.copy(subdir="client_mods",
                        dst=working_dir.subdirs["mods"]),
        log.level["verbose"])
    log(master_dir.copy(subdir="config",
                        dst=working_dir.subdirs["config"]),
        log.level["verbose"])
    log(master_dir.copy(subdir="bin",
                        dst=working_dir.subdirs["bin"]),
        log.level["verbose"])
    
    log("Done!")
    
def zip_pack():
    log("Zipping pack from current working directory.....")
    
    working_dir.zip(config.kwargs["pack_name"])
    
    log("Done!")

def move_pack():
    log("Moving zip to web directory.....")
    
    shutil.move(working_dir + config.get_value("pack_name") + ".zip", 
                str(web_dir))
    
    log("Done!")

def clean_up():
    log("Removing working dir and all contents.....")
    
    working_dir.wipe(reinit=False)
    
    log("Done!")
    
command_chain=[backup, purge, sync, zip_pack, move_pack, clean_up]

def do_clui():
    try:
        init()
        if "debug" in log.get_log_level():
            debug_log()
        for command in command_chain:
            command()
    except exception.Error as e:
        #Catch all custom errors, ignore all else.
        if "debug" in log.get_log_level():
            raise
        else:
            log.error("Exception occured, see log for details.", e)