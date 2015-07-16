class Path(object):
    import os
    
    logger = None
    path = None
    subdirs = {}
    illegal_chars = ";*?<>|"
    
    def __init__(self, path, logger):
        self.logger = logger
        for char in path:
            if char in self.illegal_chars:
                self.logger.error("Illegal character present " +
                                  "in " + path + " argument!")
        self.path = path

    def touch(self, path):
        try:
            self.os.makedirs(path)
        except OSError as exception:
            if not self.os.path.isdir(path):
                self.log.error("Invalid File Path.\n",
                               repr(exception))
    
    def add_subdir(self, key, value):
        self.subdirs[key] = self.path + value
    
    def add_subdirs(self, subdirs):
        for key, value in subdirs.items():
            self.subdirs[key] = self.path + value
    
    def __call__(self):
        return self.path
    
    def __add__(self, other):
        if isinstance(other, PathObj):
            return PathObj(self.path + other.path,
                           self.logger,
                           subdirs=self.subdirs.update(other.subdirs))
        elif isinstance(other, str):
            return PathObj(self.path + other,
                           self.logger,
                           subdirs=self.subdirs)
        
    def print_state(self, log):
        log("===================")
        log("Path Instance {0} - Start Dump".format(self.path))
        log("Module loaded, path initialised")
        log("-----")
        log("Path created with location {0}".format(self.path))
        log("-----")
        if subdirs:
            log("Loaded Sub-Directories: ")
            for key, value in self.subdirs.items():
                log("{0}: {1}".format(key, value))
        else:
            log("No Sub-Directories found.")
        log("-----")
        log("Path Instance- End Dump")
        log("===================")