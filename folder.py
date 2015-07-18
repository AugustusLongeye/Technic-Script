class Folder(object):    
    from os import chdir
    import subprocess as s
    
    def __init__(self):
        pass

    def run(self, command):
        output = self.s.check_output(command,
                                     stderr=self.s.STDOUT,
                                     shell=False)
        return output

    def copy(self, src, dst):
        return self.run(["cp", src, dst,])

    def wipe(self, src):
        return self.run(["rm", "-rf", src,])

    def rsync(self, src, dst):
        return self.run(["rsync", "-a", src, dst,])

    def zip(self, location, zip_name, folders):
        if not zip_name.endswith(".zip"):
            zip_name += ".zip"
        self.chdir(location)
        return self.run(["zip", "-r", zip_name] + folders)

    def move(self, src, dst):
        return self.run(["mv", "-f", src, dst,])