class Logger(object):
    """
    Basic logging module.
    
    Accepts messages by direct calling,
    prints all messages to terminal and
    saves copy to stack. If passed an
    exception or requested will dump
    stack to file/terminal and exit.
    
    Supports silent, quiet, normal,
    verbose, and debug level logging.
    """
    
    from os import getcwd
    
    level = {"silent":0,
             "quiet":1,
             "normal":2,
             "verbose":3,
             "debug":4}
    
    current_log_level = ""
    script_location = ""
    stack = []
    
    def __init__(self, current_level = 2):
        """
        Set params, get location of self.
        """
        self.current_log_level = current_level
        self.__call__("Logger initialised.", self.level["debug"])
        self.__call__("Logger level set at Debug", self.level["debug"])
        self.script_location = self.getcwd
        self.__call__("Script location: {0}".format(self.script_location),
                      self.level["debug"])
    
    def __call__(self, message = "", level=level["normal"]):
        """
        Log when message level is LOWER 
        than global logging level. Also 
        add all messages to stack.
        """
        
        #TODO log to file/console
        
        self.stack.append(message)
        if level <= self.current_log_level:
            print(message)
            
    def log(*args, **kwargs):
        """
        You wanna log with logger.log()
        rather than logger()?!
        I ain't gonna' stop you!
        
        Wrapper for __call__.
        """
        self.__call__(args, kwargs)
            
    def error(self, message, exception=""):
        """
        Log exception and dumps current
        stack to file.
        """
        self.stack.append("ERROR: " + message)
        if exception:
            self.stack.append("EXCEPTION: " + exception)
        self.__call__("Stack saved to " + repr(dump_path), 
                      self.level["silent"])
        self.dump_stack(out="file")

    def dump_stack(self, out="file", path=""):
        """
        Dump current stack to console or file, 
        will default to dumping to file.
        kwarg out can be either "file" or
        "terminal" to direct output.
        
        Raise IOError if unable to create dump
        file.
        """
        if out is "terminal":
            print(self.stack)
        if out is "file":
            from datetime import datetime as time
            now = time.now().strftime("%Y-%m-%d_%H.%M.%s")
            if path:
                path = path + "dump.{0}.txt".format(now)
            else:
                path = script_location + "dump.{0}.txt".format(now)
            try:
                with open(path, "w") as file:
                    for line in self.stack:
                        file.write(line + "\n")
            except IOError as e:
                raise e
                    
    def set_log_level(self, level):
        """
        Set logger's current log level.
        """
        self.current_log_level = level