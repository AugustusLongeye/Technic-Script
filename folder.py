class Folder(object):
    """
    Folder object to hold reference and behaviours of a given path.

    Folder holds a main path with an optional
    list of subdirs. Path is checked and touched
    at init. Includes methods to deal with
    contents of self in relation to other Folder
    objects, such as copying or wiping self.
    """
    
    import os
    import shutil
    from distutils import dir_util
    from exception import IllegalArgError
    from exception import InvalidPathError

    path = None
    subdirs = {}
    __illegal_chars = ";*?<>|()\"\'"
    __last_err = None
    
    def __init__(self, path):
        """
        Set path var, check for illegal chars,
        touch path to varify access rights.
        
        Raise InvalidPathError if no access.
        """
        for char in self.__illegal_chars:
            if char in path:
                raise IllegalArgError(char, path)
        if path.endswith("/"):
            self.path = path
        else:
            self.path = path + "/"
        try:
            self.touch()
        except InvalidPathError as e:
            raise e

    def touch(self, path=None):
        """
        Test path location is read/writeable,
        if path=None; test self.path.
        
        Raise InvalidPathError if cannot access.
        """
        if not path:
            path = self.path
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
    
    # Methods to alter content
    def copy(self, dst, log=True):
        """
        Copy contents of self to dst recursively.
        If log, return list of files copied.
        """
        to_log = self.dir_util.copy_tree(repr(self), dst)
        if log:
            return to_log
        else:
            return

    def move(self, dst, log=True):
        """
        Copy contents of self to dst, then
        wipe self. If log, return list of
        files moved.
        """
        to_log = self.copy(dst)
        self.wipe()
        if log:
            return to_log
        else:
            return
        
    def zip(self, archive_name, dst=None):
        """
        Zip self.path contents into name.zip.
        If dst is a path, zip file will be put there.
        Else zip will be put in self.path.
        """
        if not dst:
            archive_loc = self.path + archive_name
        else:
            archive_loc = dst + archive_name
        origin_dir = self.os.getcwd()
        self.os.chdir(self.path)
        self.shutil.make_archive(archive_loc, "zip", self.path)
        self.os.chdir(origin_dir)
        
    def wipe(self, reinit=True):
        """
        Wipe self, removes all contents recursively.
        If reinit, retouch path when done.
        """
        self.shutil.rmtree(self.path, ignore_errors = True)
        if reinit:
            try:
                return self.touch()
            except InvalidPathError as e:
                raise e
    
    # Representation Methods
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
        if not __last_err:
            to_log += "Last Error:"
            to_log += self.__last_err
        to_log += "-----"
        to_log += "Folder Instance- End Dump"
        to_log += "==================="
        return to_log      
   
    def __str__(self):
        return self.path
    
    def __repr__(self):
        return self.path
    
    def __unicode__(self):
        return self.path
    
    def __bool__(self):
        try:
            self.touch()
        except self.InvalidPathError as e:
            return False
        else:
            return True