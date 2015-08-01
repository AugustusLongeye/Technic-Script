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
    
    __current_log_level = ""
    script_location = ""
    __stack = []
    __to_file = False
    __bulk_log = False
    __log_file = ""
    
    def __init__(self, current_level = 2, output="terminal",
                 output_style="live"):
        """
        Set params, get location of self.
        
        current_level can be 0 for no logging, up
        to 4 for debug logging.
        
        output is terminal or file.
        
        output_style can be live or bulk. Live
        will print in real time, bulk will wait
        until termination and print all content.
        """
        if output == "file":
            self.__to_file = True
        if output_style == "bulk":
            self.__bulk_log = True
        self.__current_log_level = current_level
        self.__call__("Logger initialised.", self.level["debug"])
        self.__call__("Logger level set at Debug", self.level["debug"])
        self.script_location = self.getcwd
        self.__call__("Script location: {0}".format(self.script_location),
                      self.level["debug"])
        self.__log_file = self.script_location + "/log.txt"
    
    def __call__(self, message = "", level=level["normal"]):
        """
        Log when message level is LOWER 
        than global logging level. Also 
        add all messages to stack.
        """
        if not message:
            return
        if hasattr(message, "__iter__"):
        # Will intentionally fail for str, only want to iter
        # on lists or the like, not strings.
            for line in message:
                self.__call__(message, level)
        self.__stack.append(message)
        if level <= self.__current_log_level:
            if not self.__bulk_log:
                if self.__to_file:
                    self.__write(message)
                else:
                    print(message)
            
    def log(*args, **kwargs):
        """
        You wanna log with log.log()
        rather than log()?!
        I ain't gonna' stop you!
        
        Wrapper for __call__.
        """
        self.__call__(args, kwargs)
        
    def __write(self, message):
        """
        Write given line to log file.
        Write safely such that file is
        opened/closed after each operation.
        
        To write bulk data use _bulk_write
        """
        with open(self.__log_file, "w") as log_file:
            log_file.write(message)
        
    def __bulk_write(self):
        """
        Write list to file as single bulk.
        
        Accept list and print line-by-line.
        Used to shutn IO time to end of script
        rather than during runtime.
        """
        with open(self.__log_file, "w") as log_file:
            for line in self.__stack:
                log_file.write(line)
            
    def error(self, message, exception=""):
        """
        Log exception and dumps current
        stack to file.
        """
        self.__stack.append("ERROR: " + message)
        if exception:
            self.__stack.append("EXCEPTION: " + exception)
        self.__call__("Stack saved to " + self.__log_file, 
                      self.level["silent"])
        self.dump_stack(out="file")

    def dump_stack(self, out="file"):
        """
        Dump current stack to console or file, 
        will default to dumping to file.
        kwarg out can be either "file" or
        "terminal" to direct output.
        
        Raise IOError if unable to create dump
        file.
        """
        if out is "terminal":
            print(self.__stack)
        if out is "file":
            from datetime import datetime as time
            now = time.now().strftime("%Y-%m-%d_%H.%M.%s")
            if path:
                path = path + "dump.{0}.txt".format(now)
            else:
                path = script_location + "dump.{0}.txt".format(now)
            try:
                with open(self.__log_file, "w") as file:
                    for line in self.__stack:
                        file.write(line + "\n")
            except IOError as e:
                raise e
                    
    def set_log_level(self, level):
        """
        Set logger's current log level.
        """
        self.__current_log_level = level