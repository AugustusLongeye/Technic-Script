class Config(object):
    
    from os import getcwd
    from exception import IllegalArgError
    from exception import ConfigMissingError
    
    kwargs = {}
    flags = []
    illegal_chars = ";*?<>|()\"\'"
    
    def __init__(self):
        lines = ""
        try:
            with open(self.getcwd() + "/config.txt", "r") as config_file:
                lines = [line.strip() for line in config_file]
        except IOError as e:
            raise ConfigMissingError(e)
        for line in lines:
            for char in self.illegal_chars:
                if char in line and "#" not in line:
                    raise IllegalArgError(ch)
            if "#" in line:
                clean_arg = ""
                for char in line:
                    if char is "#":
                        break
                    else:
                        clean_arg += char
                clean_arg.strip()
                lines.append(clean_arg)
            elif ":" in line:
                key, value = line.split(":")
                self.kwargs[key] = value
            elif "-" in line:
                line.strip("-")
                self.flags.append(line)
            else:
                pass
                
    def get_value(self, key):
        if key in self.kwargs:
            return self.kwargs[key]
        else:
            return False
        
    def set_flag(self, flag):
        self.flags.append(flag)
        
    def set_config_value(self, key, value):
        self.kwargs[key] = value

    def flag_present(self, flag):
        if flag in self.flags:
            return True
        else:
            return False
    
    def print_state(self, log):
        log("===================")
        log("Config Module - Start Dump")
        log("Module loaded, config.txt read.")
        log("-----")
        log("KWARGS: ")
        for key, value in self.kwargs.items():
            log("{0}: {1}".format(key, value))
        log("-----")
        if self.flags:
            log("FLAGS: ")
            for flag in self.flags:
                log(flag)
        else:
            log("No Flags found.")
        log("-----")
        log("Config Module - End Dump")
        log("===================")