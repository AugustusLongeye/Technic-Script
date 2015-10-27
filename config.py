class Config(object):
    """
    Read and store config data from a config.txt file
    
    Reads data from a config.txt file,
    parses and catches illegal chars. Once
    data processed will store in kwargs and
    flags variables.
    
    Can be passed additional list of args
    (such as command line) which are added
    to kwargs and flags as needed.
    
    Will always raise IllegalArgError if
    illegal character found. Will look for
    config.txt in same dir, will raise
    ConfigAccessError if not found.
    """
    
    from os import getcwd
    from exception import IllegalArgError
    from exception import ConfigAccessError
    from exception import MissingConfigError

    extra_args_added = False
    kwargs = {}
    flags = []
    illegal_chars = ";*?<>|()\"\'"
    config_file_web_path  = "https://github.com/AugustusLongeye/Technic-Script-2/blob/master/config.txt"
    __config_name = "/config.txt"
    
    def __init__(self):
        """
        Open config file and parse content.
        Assign kwargs & flags as appropreate, 
        stripping ", - and comments.
        
        Raise IllegalArgError if any illegal
        characters found.
        """
        lines = ""
        try:
            with open(self.getcwd() + self.__config_name, "r") as config_file:
                lines = [line.strip() for line in config_file]
        except IOError as e:
            raise self.ConfigAccessError(e, self.config_file_web_path)
        for line in lines:
            line.strip("\"")
            self.validate(line)
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
                self.kwargs[key.strip()] = value.strip()
            elif "-" in line:
                line.strip("-")
                self.flags.append(line.strip())
            else:
                pass
    
    def parse_args(self, args):
        """
        Parse and overwrite/create  kwargs & args
        as necessary to kwargs and flags. Return 
        full log of all args added.
        
        Raise IllegalArgError if any illegal
        characters found.
        """
        self.extra_args_added = True
        to_log = []
        for arg in args:
            self.validate(arg)
        for arg in args:
            arg.lower()
            arg.strip("\"")
            if "=" in arg:
                key, value = arg.split("=")
                self.kwargs[key] = value
                to_log.append("- kwarg {0}:{1} added".format(key, value))        
            elif "-" in arg:
                arg = arg.strip("-")
                self.flags.append(arg)
                to_log.append("- arg {0} added".format(arg))
        return to_log
                
    def get_value(self, key):
        """
        Return value of given key or false
        if key not found.
        """
        if key in self.kwargs:
            return self.kwargs[key]
        else:
            raise self.MissingConfigError(key, self.config_file_web_path)
        
    def set_flag(self, flag):
        """
        Set a given flag to return True
        """
        self.flags.append(flag)
        
    def set_config_value(self, key, value):
        """
        Set a given kwarg to value
        """
        self.kwargs[key] = value

    def get_flag(self, flag):
        """
        Return True if flag present
        or False if not
        """
        if flag in self.flags:
            return True
        else:
            return False
    
    def validate(self, arg):
        """
        Test given string for illegal character.
        
        Raise IllegalArgError if any illegal
        characters found.
        """
        if '#' in arg:
            return True
        for char in self.illegal_chars:
            if char in arg:
                raise self.IllegalArgError(char, arg)
        return True
    
    def print_state(self):
        """
        Return list of data associated with file:
        Current KWARGS & FLAGS, if extra args added
        after init, with formatting.
        """
        to_log = []
        to_log.append("===================")
        to_log.append("Config Module - Start Dump")
        to_log.append("Module loaded, config.txt read.")
        if self.extra_args_added:
            to_log.append("Additional args added after config load")
        to_log.append("-----")
        to_log.append("KWARGS: ")
        for key, value in self.kwargs.items():
            to_log.append("{0}: {1}".format(key, value))
        to_log.append("-----")
        if self.flags:
            to_log.append("FLAGS: ")
            for flag in self.flags:
                to_log.append(flag)
        else:
            to_log.append("No Flags found.")
        to_log.append("-----")
        to_log.append("Config Module - End Dump")
        to_log.append("===================")
        return to_log