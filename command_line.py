class CMD_Line():
    
    from exception import IllegalArgError
    
    logger = ""
    config = ""
    
    def __init__(self, logger, config, args):
        self.logger = logger
        self.config = config
        self.check_args(args)
        self.split_assign_args(args)
    
    def split_assign_args(args):
        for arg in args:
            arg.lower()
            arg.strip("\"")
            if "=" in arg:
                key, value = arg.split("=")
                self.config.kwargs[key] = value
                self.logger("- kwarg {0}:{1} added".format(key, value),
                            self.logger.level["debug"])
            elif "-" in arg:
                arg = arg.strip("-")
                self.config.flags.append(arg)
                self.logger("- arg {0} added".format(arg),
                            self.logger.level["debug"])

    def sanitize_kwargs(kwargs):
        for char in self.config.illegal_chars:
            for arg in args:
                if char in arg:
                    raise IllegalArgError(arg, char)