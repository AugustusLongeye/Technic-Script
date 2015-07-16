class Logger(object):
    from os import getcwd
    
    level = {"silent":0,
             "quiet":1,
             "normal":2,
             "verbose":3,
             "debug":4}
    
    current_log_level = level["normal"]
    
    script_location = ""
    
    stack = []
    
    def __init__(self, current_level = 2):
        self.current_log_level = current_level
        self.__call__("Logger initialised.", self.level["debug"])
        self.__call__("Logger level set at Debug", self.level["debug"])
        self.script_location = self.getcwd
        self.__call__("Script location: {0}".format(self.script_location),
                      self.level["debug"])

    def __le__(self, other):
        if value <= other.value:
            return True
        else:
            return False
    
    def __call__(self, message = "", level=level["normal"]):
        self.stack.append(message)
        if level <= self.current_log_level:
            print(message)
            
    def error(self, message, exception=""):
        self.stack.append("ERROR: " + message)
        if exception:
            self.stack.append("EXCEPTION: " + exception)
        self.__call__("Stack saved to " + repr(dump_path), 
                      self.level["silent"])
        self.dump_stack(out="file")

    def dump_stack(self, out="terminal", path=""):
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
            except Exception as e:
                exit(repr(e))
                    
    def set_log_level(self, level):
        self.current_log_level = level