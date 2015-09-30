class Null(object):
    """
    Object is a Harsh Null.
    
    Object can be assigned and initialised.
    Will the always raise TypeError.
    """
    
    def __init__(self, *args, **kwargs):
        return

    # object calling
    def __call__(self, *args, **kwargs):
        raise TypeError("Object is Null.")

    # attribute handling
    def __getattr__(self, name):
        raise TypeError("Object is Null.")
        
    def __setattr__(self, name, value):
        raise TypeError("Object is Null.")
        
    def __delattr__(self, name):
        raise TypeError("Object is Null.")

    # misc.
    def __repr__(self):
        raise TypeError("Object is Null.")
    
    def __str__(self):
        raise TypeError("Object is Null.")
    
    def __dir__(self):
        raise TypeError("Object is Null.")
    
    # math
    def __add__(self, other):
        raise TypeError("Object is Null.")
        
    def __sub__(self, other):
        raise TypeError("Object is Null.")
        
    def __radd__(self, other):
        raise TypeError("Object is Null.")
        
    def __rsub__(self, other):
        raise TypeError("Object is Null.")
        
    def __cmp__(self, other):
        raise TypeError("Object is Null.")
        
    def __nonzero__(self):
        raise TypeError("Object is Null.")
