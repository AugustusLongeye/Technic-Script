class Folder(object):    
    from os import chdir
    import subprocess
    
    log = ""
    
    def __init__(self, logger):
        self.log = logger

    def run(self, command, log_level):
        output = self.subprocess.check_output(command,
                                              stderr=self.subprocess.STDOUT,
                                              shell=False)
        self.log(output, log_level)

    def copy(self, src, dst):
        self.run(["cp",
                  src,
                  dst,],
                  self.log.level["normal"])

    def wipe(self, src):
        self.run(["rm",
                  "-rf",
                  src,],
                  self.log.level["normal"])

    def rsync(self, src, dst):
        self.run(["rsync",
                  "-a",
                  src,
                  dst,],
                  self.log.level["normal"])

    def zip(self, location, zip_name, folders):
        if not zip_name.endswith(".zip"):
            zip_name += ".zip"
        self.chdir(location)
        self.run(["zip",
                  "-r", 
                  zip_name]
                  + folders,
                  self.log.level["verbose"])

    def move(self, src, dst):
        self.run(["mv",
                  "-f",
                  src,
                  dst,],
                  self.log.level["normal"])