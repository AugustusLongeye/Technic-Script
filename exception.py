class Error(Exception):
    """
    Base Error for custom exceptions.
    """
    
    def __init__(self, *values):
        """
        Store own values
        """
        self.values = values
        
    def __str__(self):
        """
        Return list of all values.
        """
        ret_val = []
        for value in values:
            ret_val += value
        return ret_val
    
    def __repr__(self):
        """
        Wrapper for __str__.
        """
        return self.__str__()
    
class IllegalArgError(Error):
    """
    Exception to raise when illegal char present
    in given arg.
    
    IllegalArgError(illegal_char, arg)
    """
    def __str__(self):
        """
        Returns formatted string of char/arg.
        """
        return ("Illegal character {0} in {1} argument."
                .format(self.values[0], self.values[1]))
    
class ModuleMissingError(Error):
    """
    Exception to raise when module not found.
    
    ModuleMissingError(module_name)
    """
    def __str__(self):
        """
        Returns formatted strong of module name.
        """
        return("Module {0} missing! Reinstall script!"
               .format(self.values[0]))
    
class ConfigAccessError(Error):
    """
    Wrapper for IOError, used to pass additional
    informaton including link to GitHub config.txt
    and reminder to check i/o permissions.
    
    ConfigAccesssError(exception)
    """
    def __str__(self):
        """
        Formatted string of original exception
        and web address.
        """
        web_address="https://github.com/AugustusLongeye/Technic-Script-2/blob/master/config.txt"
        return("Config file missing. \nRedownload from {0}. \n"
               "If config file present, check permissions! \n"
               "See exception for more details: \n{1}"
               .format(web_address, self.values[0]))
    
class InvalidPathError(Error):
    """
    Exception to raise when path not valid.
    Wrapper for exception.
    
    InvalidPathError(path, exception)
    """
    def __str__(self):
        """
        Returns formatted string of path and exception.
        """
        return("Path {0} Invalid, check path exists and "
               "script has permissions to access it! \n"
               "See Exception for more details: \m{1}"
               .format(self.values[0], self.values[1]))