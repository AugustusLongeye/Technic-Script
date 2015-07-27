class Folder(object):
    """
    Folder object to hold reference and behaviours of a given path.

    Folder holds a main path with an optional
    list of subdirs. Path is checked and touched
    before use. Includes methods to deal with
    contents of self in relation to other Folder
    objects, such as copying or wiping self.
    
    Maintains an internal list of all obejects
    in own path as a generator to use when needed.
    """
    
    import os
    from exceptions import IllegalArgError
    from exceptions import InvalidPathError

    path = None
    subdirs = {}
    illegal_chars = ";*?<>|()\"\'"
    last_err = None
    contents = ["""GENERATOR"""]
    
    def __init__(self, path):
        """
        Set path var, check for illegal chars.
        """
        for char in self.illegal_chars:
            if char in path:
                raise IllegalArgError(char, path)
        self.path = path

    def touch(self, path):
        """
        Test path location is read/writeable.
        
        Raise InvalidPathError if not.
        """
        try:
            self.os.makedirs(path)
        except OSError as e:
            if not self.os.path.isdir(path):
                raise self.InvalidPathError(path, e)
        else:
            return True
    
    def add_subdir(self, key, value):
        """
        Add single subdirectory to subdirs list.
        """
        self.subdirs[key] = self.path + value
    
    def add_subdirs(self, subdirs):
        """
        Add list of subdirectories to subdirs list.
        """
        for key, value in subdirs.items():
            self.subdirs[key] = self.path + value
    
    def __call__(self):
        """
        Call Folder instance to return self.path as string.
        """
        return self.path
    
    def __add__(self, other):
        """
        Add other to self.
        
        If other is valid folder object return new
        Folder with other.path appended to self.path,
        and other.subdirs appended to self.subdirs.
        
        If other is valid string, return new Folder
        with str appended to self.path, and same subdirs
        as self.subdirs.
        """
        if isinstance(other, type(self)):
            return Folder(self.path + other.path,
                           subdirs=self.subdirs.update(other.subdirs))
        elif isinstance(other, str):
            return Folder(self.path + other,
                           subdirs=self.subdirs)
        
    def print_state(self):
        """
        Return list of current class state.
        Includes main path and any subdirs.
        """
        to_log = []
        to_log += "==================="
        to_log += "Folder Instance {0} - Start Dump".format(self.path)
        to_log += "Module loaded, path initialised"
        to_log += "-----"
        to_log += "Path created with location {0}".format(self.path)
        to_log += "-----"
        if subdirs:
            to_log += "Loaded Sub-Directories: "
            for key, value in self.subdirs.items():
                to_log += "{0}: {1}".format(key, value)
        else:
            to_log += "No Sub-Directories found."
        to_log += "-----"
        to_log += "Folder Instance- End Dump"
        to_log += "==================="
        return to_log
   
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