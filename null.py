class Null(object):
    """
    Object is Null.
    
    Object will accept all params, calls,
    and supports most builtin behaviour.
    Will always return None.
    """
    from inspect import isclass
    
    def __init__(self, *args, **kwargs):
        """Ignore parameters."""
        return None

    # object calling
    def __call__(self, *args, **kwargs):
        """Ignore method calls."""
        return self

    # attribute handling
    def __getattr__(self, name):
        """Ignore attribute requests."""
        return self
    def __setattr__(self, name, value):
        """Ignore attribute setting."""
        return self
    def __delattr__(self, name):
        """Ignore deleting attributes."""
        return self

    # misc.
    def __repr__(self):
        """Return a string representation."""
        return "<Null>"
    def __str__(self):
        """Convert to a string and return it."""
        return """Null"""
    def __dir__(self):
        return self
    
    # math
    def __add__(self, other):
        """Return only other"""
        return other
    def __sub__(self, other):
        """Return negative other"""
        return -other
    def __radd__(self, other):
        """Return only other"""
        return other
    def __rsub__(self, other):
        """Return negative other"""
        return -other
    def __cmp__(self, other):
        """Only return True if other is Null"""
        if isinstance(self, type(other)):
            return 0
        else:
            return -1
    def __nonzero__(self):
        """Always return False"""
        return False
