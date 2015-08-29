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
    from exception import NoDstError

    __illegal_chars = ";*?<>|()\"\'"

    
    def __init__(self, path, name=None):
        """
        Set path var, check for illegal chars,
        touch path to varify access rights.
        
        Raise InvalidPathError if no access.
        """
        self.subdirs = {}
        self.__last_err = None
        if name:
            self.__name = name
        else:
            self.__name = path
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
        if self.touch(self.path + value + "/"):
            self.subdirs[key] = self.path + value + "/"
    
    def add_subdirs(self, subdirs):
        """
        Add list of subdirectories to subdirs list.
        """
        for key, value in subdirs.items():
            if self.touch(self.path + value + "/"):
                self.subdirs[key] = self.path + value + "/"
    
    def __call__(self):
        """
        Call Folder instance to return self.path as string.
        """
        return self.path
    
    def __add__(self, other):
        """
        Add other to self.

        If other is valid string, return String
        with str appended to self.path.
        """
        try:
            return self.path + other
        except Exception as e:
            raise e
            
    # Methods to alter content
    def copy(self, dst=None, subdir=None, log=True):
        """
        Copy contents of self to dst recursively.
        If log, return list of files copied.
        """
        if not dst:
            raise NoDstError()
        if subdir:
            path = self.subdirs[subdir]
        elif not subdir:
            path = self.path
        to_log = self.dir_util.copy_tree(path, dst)
        if log:
            return to_log

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
        
    def wipe(self, reinit=True, path=None):
        """
        Wipe self, removes all contents recursively.
        If reinit, retouch path when done.
        """
        if path is None:
            paht = self.path
        self.shutil.rmtree(self.path, ignore_errors = True)
        if reinit:
            try:
                return self.touch()
            except InvalidPathError:
                raise
                
    def wipe_subdirs(self, reinit=True):
        """
        Wipe subdirs of self, remove all contents.
        If reinit will touch each subdir when done.
        Will not wipe contents of self, only subdirs.
        """
        for key in self.subdirs:
            try:
                self.wipe(path=self.subdirs[key], reinit=reinit)
            except InvalidPathError:
                raise
    
    # Representation Methods
    def print_state(self):
        """
        Return list of current class state.
        Includes main path and any subdirs.
        """
        to_log = []
        to_log.append("===================")
        if self.__name:
            to_log.append("Folder Instance {0} - Start Dump".format(self.__name))
        else:
            to_log.append("Folder Instance {0} - Start Dump".format(self.path))
        to_log.append("Module loaded, path initialised")
        to_log.append("-----")
        to_log.append("Path created with location {0}".format(self.path))
        to_log.append("-----")
        if self.subdirs:
            to_log.append("Loaded Sub-Directories: ")
            for key, value in self.subdirs.items():
                to_log.append("{0}: {1}".format(key, value))
            to_log.append("-----")
        else:
            to_log.append("No Sub-Directories found.")
            to_log.append("-----")
        if self.__last_err:
            to_log.append("Last Error:")
            to_log.append(self.__last_err)
            to_log.append("-----")
        to_log.append("Folder Instance- End Dump")
        to_log.append("===================")
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