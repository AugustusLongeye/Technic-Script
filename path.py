class Path(object):
    import os
    from exceptions import IllegalArgError
    from exceptions import InvalidPathError

    path = None
    subdirs = {}
    illegal_chars = ";*?<>|()\"\'"
    last_err = None
    
    def __init__(self, path):
        # Sifts for illegal chars, sets path
        for char in self.illegal_chars:
            if char in path:
                raise IllegalArgError(char, path)
        self.path = path

    def touch(self, path):
        # Tests path exists and is read/writeable
        try:
            self.os.makedirs(path)
        except OSError as e:
            if not self.os.path.isdir(path):
                raise self.InvalidPathError(path, e)
        else:
            return True
    
    def add_subdir(self, key, value):
        # Adds single subdir
        self.subdirs[key] = self.path + value
    
    def add_subdirs(self, subdirs):
        # Adds list of subdirs
        for key, value in subdirs.items():
            self.subdirs[key] = self.path + value
    
    def __call__(self):
        # Returns true if folder read/writeable
        # Else returns false and saves exception
        # to last_err.
        try:
            self.touch(self.path)
        except InvalidPathError as e:
            self.last_err = e
            return False
        else:
            return True
    
    def __add__(self, other):
        # If other is path, appends other to self
        # and appends other.subdirs to self.subdirs
        if isinstance(other, PathObj):
            return PathObj(self.path + other.path,
                           subdirs=self.subdirs.update(other.subdirs))
        # If other is string, appends other to
        # self.subdirs
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
   
    def copy(self, dst, dupes="ignore"):
        #copy contents of self to dst
        #overwright/rename/ignore
        
    def move(self, dst, dupes="ignore"):
        #move contents of self to dst
        #overwright/rename
        
    def zip(self, name, dst=None):
        #zip contents of self to name.zip
        #if no dst provided, place zip in self
        
    def wipe(self, recursive=True):
        #remove contents of self
        #if recursive true remove all folders
        
    def sync(self, dst):
        #only copy changed/no present contents
        #of self to dst. All same ignored.
        pass