class SuperException(Exception):
    
    def __init__(self, *values):
        self.values = values
        
    def __str__(self):
        ret_val = ""
        for value in values:
            ret_val += value
        return ret_val
    
    def __repr__(self):
        return self.__str__()
    
class IllegalArgError(SuperException):
    #[0] is character
    #[1] is arg
    def __str__(self):
        return ("Illegal character {0} in {1} argument"
                .format(self.values[0], self.values[1]))
    
class ModuleMissingError(SuperException):
    #[0] is module name
    def __str__(self):
        return("Module {0} missing! Reinstall script!"
               .format(self.values[0]))
    
class ConfigMissingError(SuperException):
    #[0] is exception
    def __str__(self):
        web_address=""#TODO add config file path on github
        return("Config file missing. \nRedownload from {0}. \n"
               "If config file present, check permissions! \n"
               "See exception for more details: \n{1}"
               .format(web_address, self.values[0]))