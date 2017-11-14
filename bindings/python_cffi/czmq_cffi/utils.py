################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
try:
    from . import native
    lib = native.lib
    ffi = native.ffi
except ImportError:
    from . import dlopen
    lib = dlopen.lib
    ffi = dlopen.ffi

def rebind (_lib, _ffi):
    """Rebind Lib and CompiledFFi objects for given package. Lib object MUST expose all functions
       required by the classes. This is default for zproject based projects"""
    global lib
    global ffi
    lib = _lib
    ffi = _ffi

try:
    text_type = unicode  # Python 2
    binary_type = str
except NameError:
    text_type = str      # Python 3
    binary_type = bytes


def to_bytes(s):
    return s if isinstance(s, binary_type) else text_type(s).encode("utf-8")


def to_unicode(s):
    return s if isinstance(s, text_type) else binary_type(s).decode("utf-8")


def to_strings (s):
    """Convert Python native list types to zlist_t of strings"""
    if issubclass (s.__class__, (list, set, frozenset, tuple)):
        foo = lib.zlist_new ()
        for item in s:
            lib.zlist_append (foo, to_bytes (item))
        return foo
    return None
################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
