class Path(object):
    import os
    from exceptions import IllegalArgError
    from exceptions import InvalidPathError

    path = None
    subdirs = {}
    illegal_chars = ";*?<>|()\"\'"
    
    def __init__(self, path):
        for char in self.illegal_chars:
            if char in path:
                raise IllegalArgError(char, path)
        self.path = path

    def touch(self, path):
        try:
            self.os.makedirs(path)
        except OSError as e:
            if not self.os.path.isdir(path):
                raise self.InvalidPathError(path, e)
    
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
                           subdirs=self.subdirs.update(other.subdirs))
        elif isinstance(other, str):
            return PathObj(self.path + other,
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