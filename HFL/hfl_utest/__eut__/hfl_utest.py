r'''Wrapper for Ccp.h

Generated with:
C:\toolbox\waf\waf build_hfl_utest

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return int(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, )):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError as e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])
def sizeof(object):
    _size = None
    try:
        _size = ctypes.sizeof(object)
    except:
        _size = None
    return _size

# Begin libraries

_libs["C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll"] = load_library("C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll")

# 1 libraries
# End libraries

# No modules


# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 288
Signal_StMan_STMAN_STATE_RESERVED00_STATE = 0

INLINE = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 42

HWMON_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 5

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 298
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR'):
    HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR
    HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR.argtypes = []
    HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR.restype = None

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\HwCfg_Cfg.h: 4
INT_EPWM8 = 3605256

SAL_REQ_CANCELLED = 6
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

END_SEC_VAR_NOINIT_UNSPECIFIED = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 250

SAL_REQ_NOT_OK = 1
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 430
Signal_PWM_AC_L2_RD_RELACT_DUTYCYCLE_ENERGIZE = 10000

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\epwm.h: 4
EPWM8_BASE = 1

# <command-line>: 26
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Interrupt_clearACKGroup'):
    Interrupt_clearACKGroup = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].Interrupt_clearACKGroup
    Interrupt_clearACKGroup.argtypes = []
    Interrupt_clearACKGroup.restype = None

SAL_NVM_SET_BLOCK_PROTECTION = 5
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 103

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 404
Signal_PWM_AC_N_RD_RELACT_DUTYCYCLE_OPENED = 0

START_SEC_VAR_UNSPECIFIED = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 180

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 354
Signal_StMan_STMAN_SUBSTATE_FAULT_SUBSTATE = 16

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 328
Signal_StMan_STMAN_SUBSTATE_G2V_PERIPHERAL_INIT_SUBSTATE = 3

END_SEC_CONST_32BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 68

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 74
SALGetSigGroupSizeCom_FaultGroup = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 26
HFL_TX_RATE = 1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 294
Signal_StMan_STMAN_STATE_GRID_TO_VEHICLE_STATE = 3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 300
Signal_StMan_STMAN_STATE_VEHICLE_TO_GRID_STATE = 6

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 594
SALGetSigGroupSizeTempSens_Group = 0

HWMON_UNIT_TESTING_IS_ON = True
# <command-line>: 4

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 282
Signal_StMan_PFCOpState_TTP1P = 3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 47
STD_IDLE = 0

DI = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 49

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__eut__\hfl_utest\stubbed_interrupt.c: 3
try:
    _p_Interrupt_enable = (POINTER(CFUNCTYPE(UNCHECKED(None), ))).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], '_p_Interrupt_enable')
except:
    pass

float64 = c_double
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 34

SAL_USE_MODULE_COM_READ = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1667

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__eut__\hfl_utest\stubbed_driverlib.c: 25
try:
    _p_Interrupt_clearACKGroup = (POINTER(CFUNCTYPE(UNCHECKED(None), ))).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], '_p_Interrupt_clearACKGroup')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 22
SAL_REPORT_DET_ERRORS = 0

SAL_NVM_SET_RAM_BLOCK_STATUS = 6
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 103

real64_T = c_double
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 8

SAL_REQ_UNKNOWN = 255
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 412
Signal_PWM_AFE_L3_RD_RELACT_DUTYCYCLE_ENERGIZE = 10000

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 698
SALGetSigGroupSizeStMan_TstMan_Group = 0

START_SEC_VAR_NOINIT_32BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 228

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 394
Signal_RelAct_RelayStatus_ENERGIZE = 1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 400
Signal_PWM_AC_L3_RD_RELACT_DUTYCYCLE_ENERGIZE = 10000

END_SEC_PBCFG = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 119

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 366
Signal_GridEval_GRID_NO_OF_PH_MISSING_GRID = 4

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 340
Signal_StMan_STMAN_SUBSTATE_G2V_DCLINKSOFTSTART_SUBSTATE = 9

sint16 = c_short
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 21

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 290
Signal_StMan_STMAN_STATE_INIT_STATE = 1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 58
TRUE = 1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 13
MEMBER_13_SIZE = 2

START_SEC_VAR_PTR = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.c: 210

uint16_T = c_ushort
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 13

uint64 = c_ulonglong
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 31

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1392
SALGetSigGroupSizeMeas_Group = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 30
SALGetSigGroupSizeComE2E_FaultGroup = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 286
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_Main'):
    SAL_Main = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].SAL_Main
    SAL_Main.argtypes = []
    SAL_Main.restype = None

# <command-line>: 23
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'set_p_Interrupt_enable'):
    set_p_Interrupt_enable = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].set_p_Interrupt_enable
    set_p_Interrupt_enable.argtypes = [POINTER(None)]
    set_p_Interrupt_enable.restype = None

SAL_REQ_RESTORED_FROM_ROM = 7
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

SAL_REQ_PENDING = 2
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

float32_t = c_float
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 39

END_SEC_VAR_NOINIT_32BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 235

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 406
Signal_PWM_AC_N_RD_RELACT_DUTYCYCLE_ENERGIZE = 10000

# <command-line>: 25
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'set_p_Interrupt_disable'):
    set_p_Interrupt_disable = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].set_p_Interrupt_disable
    set_p_Interrupt_disable.argtypes = [POINTER(None)]
    set_p_Interrupt_disable.restype = None

SAL_NVM_REQUEST_WRITE = 1
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 103

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__eut__\hfl_utest\stubbed_driverlib.c: 3
try:
    _p_EPWM_clearEventTriggerInterruptFlag = (POINTER(CFUNCTYPE(UNCHECKED(None), ))).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], '_p_EPWM_clearEventTriggerInterruptFlag')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 348
Signal_StMan_STMAN_SUBSTATE_V2L_ACSOFTSTART_SUBSTATE = 13

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\interrupt.h: 8
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Interrupt_disable'):
    Interrupt_disable = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].Interrupt_disable
    Interrupt_disable.argtypes = []
    Interrupt_disable.restype = None

START_SEC_CONST_PTR = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 91

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 64
SALGetSigGroupSizeNM_FaultGroup = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 330
Signal_StMan_STMAN_SUBSTATE_G2V_PRECHARGE_INIT_SUBSTATE = 4

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 336
Signal_StMan_STMAN_SUBSTATE_G2V_PRECHARGE_FAIL_SUBSTATE = 7

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 626
SALGetSigGroupSizeRelAct_TstMan_Group = 0

CCP_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\Ccp.h: 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 302
Signal_StMan_STMAN_STATE_SHUTDOWN_STATE = 7

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 17
SAL_FLOAT_LOWER_RESOLUTION = 0.99

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 276
Signal_StMan_PFCOpState_STANDBY = 0

SAL_H = True
# <input>: 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 50
STD_IN = 0

YSP_DEBUG = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 62

HFL_INTERNAL_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl_Internal.h: 3

uint32 = c_uint
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 27

COMPILER_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 3

SAL_USE_MODULE_IOHWAB_SIGNALS = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 278

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 414
Signal_PWM_AFE_L3_RD_RELACT_DUTYCYCLE_HOLD = 5000

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 388
Signal_RelAct_RelayType_AFE_L3_RD = 5

START_SEC_VAR_NOINIT_16BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 213

SAL_NVM_REQUEST_READ = 0
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 103

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 402
Signal_PWM_AC_L3_RD_RELACT_DUTYCYCLE_HOLD = 5000

EPWM_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\epwm.h: 2

# <command-line>: 22
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'EPWM_clearEventTriggerInterruptFlag'):
    EPWM_clearEventTriggerInterruptFlag = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].EPWM_clearEventTriggerInterruptFlag
    EPWM_clearEventTriggerInterruptFlag.argtypes = []
    EPWM_clearEventTriggerInterruptFlag.restype = None

HWCFG_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\HwCfg_Cfg.h: 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 376
Signal_GridEval_Operation_Mode_CHARGING = 3

# <command-line>: 27
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'set_p_Interrupt_clearACKGroup'):
    set_p_Interrupt_clearACKGroup = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].set_p_Interrupt_clearACKGroup
    set_p_Interrupt_clearACKGroup.argtypes = [POINTER(None)]
    set_p_Interrupt_clearACKGroup.restype = None

END_SEC_CONST_PTR = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 102

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 342
Signal_StMan_STMAN_SUBSTATE_G2V_CHARGE_SUBSTATE = 10

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 284
Signal_StMan_PFCOpState_V2L1P = 4

sint8 = c_int8
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 17

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 23
HFL_OPERATION_MODE_MANUAL = 1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 272
Signal_StMan_PCompSamplingMode_SAMPLING_STANDBY = 1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 346
Signal_StMan_STMAN_SUBSTATE_V2L_PREPARE_TO_RUN_SUBSTATE = 12

AUTOMATIC = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 33

STD_TYPES_H = True
# <input>: 4

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 224
SALGetSigGroupSizeGridEval_Group = 0

DEM_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 744
SALGetSigGroupSizeGridEval_TstMan_Group = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 299
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_Init'):
    Hfl_Init = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].Hfl_Init
    Hfl_Init.argtypes = []
    Hfl_Init.restype = None

START_SEC_RAM_CRITICAL = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 258

SAL_REQ_INTEGRITY_FAILED = 3
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 384
Signal_RelAct_RelayType_AC_L1_RD = 3

# <command-line>: 23
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'set_p_EPWM_clearEventTriggerInterruptFlag'):
    set_p_EPWM_clearEventTriggerInterruptFlag = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].set_p_EPWM_clearEventTriggerInterruptFlag
    set_p_EPWM_clearEventTriggerInterruptFlag.argtypes = [POINTER(None)]
    set_p_EPWM_clearEventTriggerInterruptFlag.restype = None

END_SEC_VAR_16BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 157

SAL_NVM_REQUEST_INVALIDATE = 2
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 103

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 350
Signal_StMan_STMAN_SUBSTATE_V2L_RUN_SUBSTATE = 14

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 324
Signal_StMan_STMAN_SUBSTATE_OFF_SUBSTATE = 1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 616
SALGetSigGroupSizeRelAct_Group = 0

SAL_USE_MODULE_IOHWAB = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 491

START_SEC_CONST_UNSPECIFIED = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 76

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 29
HFL_INTERRUPT_ENABLED = 1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 338
Signal_StMan_STMAN_SUBSTATE_G2V_PREPARE_TO_RUN_SUBSTATE = 8

__interrupt = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 17

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 312
Signal_StMan_STMAN_STATE_RESERVED04_STATE = 12

START_SEC_CONST_8BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 31

WIN_COMPILER = True
# <command-line>: 1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 278
Signal_StMan_PFCOpState_AFE3P = 1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 42
STD_OFF = 0

START_SEC_CODE = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 298

enum_anon_11 = c_int
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 103

SAL_DET_REPORT_ERROR = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 23

SAL_USE_MODULE_COM_WRITE = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1669

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 424
Signal_PWM_AC_L1_RD_RELACT_DUTYCYCLE_ENERGIZE = 10000

END_SEC_RAM_CRITICAL = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 265

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 390
Signal_RelAct_RelayType_NUMBER_OF_RELAYS = 6

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 396
Signal_RelAct_RelayStatus_HOLD = 2

START_SEC_VAR_8BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 135

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 108
SALGetSigGroupSizeDem_FaultGroup = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 378
Signal_RelAct_RelayType_AC_L1L2_RD = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__eut__\hfl_utest\stubbed_driverlib.c: 14
try:
    _p_CPUTimer_getTimerCount = (POINTER(CFUNCTYPE(UNCHECKED(c_uint32), ))).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], '_p_CPUTimer_getTimerCount')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 28
HFL_INTERRUPT_DISABLED = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 320
Signal_StMan_STMAN_STATE_MAX = 16

SAL_COM_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 286
Signal_StMan_PFCOpState_FAULT = 5

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 52
STD_OUT = 1

END_SEC_CONST_8BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 38

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 30
E_OK = 0

SAL_SGNVALUES_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 3

uint16 = c_ushort
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 23

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 274
Signal_StMan_PCompSamplingMode_SAMPLING_ACTIVE = 2

END_SEC_VAR_PTR = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.c: 225

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\interrupt.h: 7
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Interrupt_enable'):
    Interrupt_enable = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].Interrupt_enable
    Interrupt_enable.argtypes = []
    Interrupt_enable.restype = None

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 37
STD_LOW = 0

COMPILER_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 4

SAL_EVENTS_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 3

CLA_HEADER_H = True
# <command-line>: 7

SAL_SIGNAL_SCALING_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 3

bool = c_ubyte
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 40

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\epwm.h: 6
INTERRUPT_ACK_GROUP3 = 1

# <command-line>: 25
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'set_p_CPUTimer_getTimerCount'):
    set_p_CPUTimer_getTimerCount = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].set_p_CPUTimer_getTimerCount
    set_p_CPUTimer_getTimerCount.argtypes = [POINTER(None)]
    set_p_CPUTimer_getTimerCount.restype = None

START_SEC_VAR_NOINIT_UNSPECIFIED = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 243

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1686
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_ComMain'):
    SAL_ComMain = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].SAL_ComMain
    SAL_ComMain.argtypes = []
    SAL_ComMain.restype = None

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 386
Signal_RelAct_RelayType_AC_L2_RD = 4

RTWTYPES_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 3

SAL_NVM_REQUEST_RESTORE_DEFAULTS = 3
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 103

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 360
Signal_GridEval_GRID_NO_OF_PH_ONE_PHASE = 1

END_SEC_VAR_8BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 142

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 326
Signal_StMan_STMAN_SUBSTATE_STANDBY_SUBSTATE = 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 31
def HFL_READ_FLOAT_FROM_ADDR(addr):
    return (addr[0])

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 332
Signal_StMan_STMAN_SUBSTATE_G2V_PRECHARGE_SUBSTATE = 5

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 314
Signal_StMan_STMAN_STATE_RESERVED05_STATE = 13

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 20
HFL_LOGGER_INIT = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 552
SALGetSigGroupSizeTstMan_Group = 0

SAL_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 63

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 45
STD_ACTIVE = 1

START_SEC_VAR_NOINIT_PTR = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.c: 311

ASM = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 44

sint64 = c_longlong
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 29

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 210
SALGetSigGroupSizeHwCfg_Group = 0

memcpy = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 5

GRIDEVAL_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 6

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.c: 456
for _lib in _libs.values():
    try:
        aux = (c_uint16).in_dll(_lib, 'aux')
        break
    except:
        pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 21
HFL_LOGGER_STARTED = 1

SAL_USE_MODULE_COM_SIGNALS = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 282

SAL_USE_MODULE_COM = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1665

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 426
Signal_PWM_AC_L1_RD_RELACT_DUTYCYCLE_HOLD = 5000

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1683
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_ComInit'):
    SAL_ComInit = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].SAL_ComInit
    SAL_ComInit.argtypes = []
    SAL_ComInit.restype = None

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 432
Signal_PWM_AC_L2_RD_RELACT_DUTYCYCLE_HOLD = 5000

END_SEC_VAR_UNSPECIFIED = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 187

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 398
Signal_PWM_AC_L3_RD_RELACT_DUTYCYCLE_OPENED = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 372
Signal_GridEval_Operation_Mode_PHASE_DETECTION = 1

START_SEC_PBCFG = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 110

int16_T = c_short
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 12

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 322
Signal_StMan_STMAN_SUBSTATE_INIT_SUBSTATE = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 296
Signal_StMan_STMAN_STATE_RESERVED01_STATE = 4

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 55
FALSE = 0

HFL_UNIT_TESTING_IS_ON = True
# <command-line>: 5

uint8 = c_ubyte
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 19

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 297
for _lib in _libs.values():
    if not hasattr(_lib, 'INT_E_PWM8_ISR'):
        continue
    INT_E_PWM8_ISR = _lib.INT_E_PWM8_ISR
    INT_E_PWM8_ISR.argtypes = []
    INT_E_PWM8_ISR.restype = None
    break

enum_anon_12 = c_int
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

PFCCTRL_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 2

BOARD_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\board.h: 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 40
STD_ON = 1

STATIC = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 35

uint16_t = c_ushort
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 37

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__eut__\hfl_utest\stubbed_interrupt.c: 14
try:
    _p_Interrupt_disable = (POINTER(CFUNCTYPE(UNCHECKED(None), ))).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], '_p_Interrupt_disable')
except:
    pass

BTIMEMGT_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 22
HFL_LOGGER_STOPPED = 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 754
SALGetSigGroupSizeCCP_Group = 0

# <command-line>: 23
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'set_p_ccpDaq'):
    set_p_ccpDaq = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].set_p_ccpDaq
    set_p_ccpDaq.argtypes = [POINTER(None)]
    set_p_ccpDaq.restype = None

SAL_USE_MODULE_FUNCTION_CALLS = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 286

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 150
SALGetSigGroupSizeStMan_Group = 0

HFL_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 2

uint32_t = c_uint
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 38

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 380
Signal_RelAct_RelayType_AC_L3_RD = 1

START_SEC_VAR_32BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 165

SAL_NVM_GET_ERROR_STATUS = 4
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 103

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 362
Signal_GridEval_GRID_NO_OF_PH_TWO_PHASES = 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 368
Signal_GridEval_GRID_NO_OF_PH_MAX = 5

END_SEC_CONST_16BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 53

uint32_T = c_uint
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 15

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 334
Signal_StMan_STMAN_SUBSTATE_G2V_PRECHARGE_DONE_SUBSTATE = 6

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 308
Signal_StMan_STMAN_STATE_FAULT_STATE = 10

COMPILER_GCC = True
# <command-line>: 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 12
HFL_MAX_EVENTS = 3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 46
NULL_PTR = None

END_SEC_CODE = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 306

CONST = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 38

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 760
SALGetSigGroupSizeCalib_Group = 0

int32_T = c_int
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 14

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 24
HFL_OPERATION_MODE_TRIGGERED = 2

HWCFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 4

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\epwm.h: 5
CPUTIMER1_BASE = 1

SAL_REQ_BLOCK_SKIPPED = 4
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 420
Signal_PWM_AC_L1L2_RD_RELACT_DUTYCYCLE_HOLD = 5000

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 13
HFL_LOGGER_BUFFER_SIZE = 650

SAL_USE_MODULE_APPLICATION_SIGNALS = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 274

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 408
Signal_PWM_AC_N_RD_RELACT_DUTYCYCLE_HOLD = 5000

END_SEC_VAR_32BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 172

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 374
Signal_GridEval_Operation_Mode_CONTINOUS_MONITORING = 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 316
Signal_StMan_STMAN_STATE_RESERVED06_STATE = 14

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 298
Signal_StMan_STMAN_STATE_VEHICLE_TO_LOAD_STATE = 5

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 304
Signal_StMan_STMAN_STATE_ACTIVE_DISCHARGE_STATE = 8

START_SEC_CONST_16BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 46

UNIT_TESTING_IS_ON = True
# <command-line>: 3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 300
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_MainFunction'):
    Hfl_MainFunction = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].Hfl_MainFunction
    Hfl_MainFunction.argtypes = []
    Hfl_MainFunction.restype = None

sint32 = c_int
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 25

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 270
Signal_StMan_PCompSamplingMode_SAMPLING_ON_HOLD = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 32
E_NOT_OK = 1

SAL_TYPES_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 7

EI = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 48

PLATFORM_TYPES_H = True
# <input>: 5

float32 = c_float
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 33

uint8_T = c_ubyte
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 11

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 200
SALGetSigGroupSizeClaIf_Group = 0

SAL_FUNCTION_CALL_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 3

real32_T = c_float
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 7

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 416
Signal_PWM_AC_L1L2_RD_RELACT_DUTYCYCLE_OPENED = 0

END_SEC_VAR_NOINIT_16BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 220

int8_T = c_char
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 10

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 382
Signal_RelAct_RelayType_AC_N_RD = 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 356
Signal_StMan_STMAN_SUBSTATE_MAX = 17

START_SEC_VAR_16BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 150

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 370
Signal_GridEval_Operation_Mode_INIT = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 344
Signal_StMan_STMAN_SUBSTATE_V2L_PERIPHERAL_INIT_SUBSTATE = 11

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 310
Signal_StMan_STMAN_STATE_RESERVED03_STATE = 11

END_SEC_VAR_NOINIT_PTR = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.c: 326

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1382
SALGetSigGroupSizeDerat_Group = 0

SAL_IOHWAB_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 3

SAL_APP_CFG_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 3

SAL_REQ_NV_INVALIDATED = 5
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 422
Signal_PWM_AC_L1_RD_RELACT_DUTYCYCLE_OPENED = 0

INTERRUPT_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\interrupt.h: 2

SAL_REQ_OK = 0
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 428
Signal_PWM_AC_L2_RD_RELACT_DUTYCYCLE_OPENED = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1409
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Sal_InitAppGroups'):
    Sal_InitAppGroups = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].Sal_InitAppGroups
    Sal_InitAppGroups.argtypes = []
    Sal_InitAppGroups.restype = None

START_SEC_VAR_NOINIT_8BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 198

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 410
Signal_PWM_AFE_L3_RD_RELACT_DUTYCYCLE_OPENED = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 454
SALGetSigGroupSizePComp_Group = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 352
Signal_StMan_STMAN_SUBSTATE_SHUTDOWN_SUBSTATE = 15

END_SEC_CONST_UNSPECIFIED = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 83

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 318
Signal_StMan_STMAN_STATE_BOOTLOADER_STATE = 15

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 292
Signal_StMan_STMAN_STATE_STANDBY_STATE = 2

HFL_H = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 16
SAL_FLOAT_UPPER_RESOLUTION = 1.01

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 306
Signal_StMan_STMAN_STATE_RESERVED02_STATE = 9

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 280
Signal_StMan_PFCOpState_V2G3P = 2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 35
STD_HIGH = 1

# <command-line>: 24
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'CPUTimer_getTimerCount'):
    CPUTimer_getTimerCount = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].CPUTimer_getTimerCount
    CPUTimer_getTimerCount.argtypes = []
    CPUTimer_getTimerCount.restype = c_uint32

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 283
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_Init'):
    SAL_Init = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].SAL_Init
    SAL_Init.argtypes = []
    SAL_Init.restype = None

SAL_USE_MODULE_SIGNAL_EVENTS = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 290

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 418
Signal_PWM_AC_L1L2_RD_RELACT_DUTYCYCLE_ENERGIZE = 10000

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 392
Signal_RelAct_RelayStatus_OPENED = 0

END_SEC_VAR_NOINIT_8BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 205

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 358
Signal_GridEval_GRID_NO_OF_PH_UNDEFINED = 0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 364
Signal_GridEval_GRID_NO_OF_PH_THREE_PHASES = 3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 652
SALGetSigGroupSizePComp_TstMan_Group = 0

START_SEC_CONST_32BIT = True
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 61

boolean = c_ubyte
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 15

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 945
try:
    SALComGetSignal_COMTxSignal_AM_PH_2_3_ANGLE = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_PH_2_3_ANGLE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1161
try:
    SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1274
try:
    SALComGetSignal_COMRxSignal_MA_CH_V = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_CH_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 364
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_065 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_065')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1253
try:
    SALComGetSignal_COMTxSignal_AM_ODD_CNT = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_ODD_CNT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 924
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CNT_02 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CNT_02')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 635
try:
    SAL_App_TstMan_RelAct_Signal_PWM_AC_L1_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_RelAct_Signal_PWM_AC_L1_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 809
try:
    SAL_App_Signal_Calib_STMAN_G2V_PLL_STABILIZATION_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PLL_STABILIZATION_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 33
class struct_anon_3(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 95
try:
    SAL_App_Signal_Com_MA_REQUEST_OP_Monitoring_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Com_MA_REQUEST_OP_Monitoring_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 471
try:
    SAL_App_Signal_PComp_PFC3PhaseCurrBMesFactor = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_PFC3PhaseCurrBMesFactor')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 151
try:
    SAL_App_Signal_StMan_PCompSamplingMode = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_PCompSamplingMode')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1205
try:
    SAL_App_Signal_Calib_HWMON_AC_1_65V_VS_MIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_1_65V_VS_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 225
try:
    SAL_App_Signal_GridEval_GRID_NO_OF_PH = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_GRID_NO_OF_PH')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 921
try:
    SAL_App_Signal_Calib_GRIDEVAL_INIT_DEADTIMEGRIDEVAL_THRESHOLD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_INIT_DEADTIMEGRIDEVAL_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 511
try:
    SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LA_IS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LA_IS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1077
try:
    SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_UV_DQ = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_UV_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 175
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_092 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_092')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 219
try:
    SAL_App_Signal_HwCfg_AFE_LC_IS_MaxCurrent = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_HwCfg_AFE_LC_IS_MaxCurrent')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 865
try:
    SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MAX_VALUE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MAX_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 301
try:
    SAL_App_Signal_GridEval_AC_L3_IS_RMS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_IS_RMS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 154
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_095 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_095')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1358
try:
    SALComGetSignal_COMRxSignal_MA_E2E_CNT_03 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_E2E_CNT_03')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1009
try:
    SAL_App_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_THRESHOLD = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1008
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CNT_04 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CNT_04')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 195
try:
    SAL_App_Signal_StMan_DriverPowerUpSeq_InProgress = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_DriverPowerUpSeq_InProgress')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1237
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_QT = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1337
try:
    SALComGetSignal_COMRxSignal_MA_ACT_P_PH2 = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_ACT_P_PH2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 459
try:
    SAL_App_Signal_PComp_PFC3PhaseCurrBMesOffset = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_PFC3PhaseCurrBMesOffset')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 369
try:
    SAL_App_Signal_GridEval_AC_L3L1_V_POS_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3L1_V_POS_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 393
try:
    SAL_App_Signal_GridEval_AC_L2L3_V_RMS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2L3_V_RMS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 308
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_073 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_073')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1197
try:
    SALComGetSignal_COMTxSignal_AM_NODE_ID = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_NODE_ID')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 611
try:
    SAL_App_Signal_AC_FLY_TEMP = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_AC_FLY_TEMP')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 86
try:
    SALIoHwAb_ADC_AFE_LC_IS_S1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AFE_LC_IS_S1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.c: 104
try:
    Hfl_Event = (uint16_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_Event')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 238
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_083 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_083')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 711
try:
    SAL_App_TstMan_StMan_Signal_ST_AC_N_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_ST_AC_N_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 245
try:
    SAL_App_Signal_GridEval_AC_L2_V_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2_V_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 941
try:
    SAL_App_Signal_Calib_GRIDEVAL_PH_DELTAPEAKVOLTAGE_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_PH_DELTAPEAKVOLTAGE_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 345
try:
    SAL_App_Signal_GridEval_AC_L1L2_V_POS_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1L2_V_POS_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1225
try:
    SAL_App_Signal_Calib_HWMON_AC_RLY_TEMP_QT = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_RLY_TEMP_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 531
try:
    SAL_App_Signal_PComp_CMPSS2_DACHVAL = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_CMPSS2_DACHVAL')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1097
try:
    SAL_App_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_CURRENTDELTA = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_CURRENTDELTA')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 357
try:
    SAL_App_Signal_GridEval_AC_L2L3_V_POS_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2L3_V_POS_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1302
try:
    SALComGetSignal_COMRxSignal_MA_E2E_CNT_01 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_E2E_CNT_01')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 721
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_016 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_016')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 109
try:
    SAL_App_Dem_Fault1 = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Dem_Fault1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1113
try:
    SAL_App_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_DT = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_DT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 985
try:
    SAL_App_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK02_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK02_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1281
try:
    SALComGetSignal_COMRxSignal_MA_CH_MAX_I = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_CH_MAX_I')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 47
try:
    SAL_App_Signal_ComE2E_MA_REQUEST_OP_Checksum_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_ComE2E_MA_REQUEST_OP_Checksum_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 371
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_064 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_064')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1260
try:
    SALComGetSignal_COMRxSignal_MA_E2E_CHK_02 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_E2E_CHK_02')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__datagen__\Sal_App_Cfg.c: 354
for _lib in _libs.values():
    try:
        Idx = (uint32).in_dll(_lib, 'Idx')
        break
    except:
        pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 103
try:
    SAL_App_Signal_Com_MA_MCMP_Monitoring_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Com_MA_MCMP_Monitoring_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 693
try:
    SAL_App_TstMan_PComp_Signal_ADC_AC_1_65V_VS_Value = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_ADC_AC_1_65V_VS_Value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 317
try:
    SAL_App_Signal_GridEval_AC_L1_ZC_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1_ZC_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 126
try:
    SALIoHwAb_ADC_AC_DSP_3V3_S2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_DSP_3V3_S2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1157
try:
    SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 261
try:
    SAL_App_Signal_GridEval_AC_L3_V_POS_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_V_POS_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 182
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_091 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_091')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 793
try:
    SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_DONE_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_DONE_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1301
try:
    SAL_App_Signal_Calib_PCOMP_ZERO_CURRENT_VS_X_NO_OF_SAMPLES = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_PCOMP_ZERO_CURRENT_VS_X_NO_OF_SAMPLES')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 731
try:
    SAL_App_TstMan_StMan_Signal_STMAN_STATE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_STMAN_STATE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 973
try:
    SAL_App_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMAX_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMAX_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1365
try:
    SALComGetSignal_COMRxSignal_MA_V2X_MAX_P = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_V2X_MAX_P')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 665
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_024 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_024')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 837
try:
    SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA1 = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 129
try:
    SAL_App_Dem_Fault6 = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Dem_Fault6')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1133
try:
    SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 70
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_107 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_107')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.c: 103
try:
    Hfl_DaqBuff_Index = (uint16_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_DaqBuff_Index')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 893
try:
    SAL_App_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_11KW_IS_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_11KW_IS_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 455
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_054 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_054')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1015
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CHK_04 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CHK_04')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1177
try:
    SAL_App_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_VFACTOR = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_VFACTOR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 178
class struct_anon_17(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 657
try:
    SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrAMesOffset_Value = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrAMesOffset_Value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1037
try:
    SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_OV_QT = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_OV_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 825
try:
    SAL_App_Signal_Calib_STMAN_V2L_AC_SOFTSTART_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_V2L_AC_SOFTSTART_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 749
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_012 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_012')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1309
try:
    SALComGetSignal_COMRxSignal_MA_REACT_P_PH3 = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_REACT_P_PH3')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 577
try:
    SAL_App_Signal_TstMan_Mode_Cla = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_TstMan_Mode_Cla')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 487
try:
    SAL_App_Signal_Pcomp_AC12VSMesFactor = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Pcomp_AC12VSMesFactor')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 728
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_015 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_015')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 421
try:
    SAL_App_Signal_GridEval_AC_L3L1_ZC_Max_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3L1_ZC_Max_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 167
try:
    SAL_App_Signal_StMan_ST_AC_L1_RD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_ST_AC_L1_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 136
try:
    SALIoHwAb_ADC_AC_RLY_TEMP = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_RLY_TEMP')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 574
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_037 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_037')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 232
try:
    SALIoHwAb_PWM_AC_L2_RD = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_PWM_AC_L2_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1261
try:
    SAL_App_Signal_Calib_HWMON_AC_FLY_TEMP_DQ = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_FLY_TEMP_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1025
try:
    SAL_App_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_TMAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_TMAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 627
try:
    SAL_App_TstMan_RelAct_Signal_PWM_AC_N_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_RelAct_Signal_PWM_AC_N_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121
try:
    SALIoHwAb_ADC_AC_DSP_3V3_S1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_DSP_3V3_S1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 565
try:
    SAL_App_Signal_TstMan_Mode_RelAct = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_TstMan_Mode_RelAct')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1253
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_DQ = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 41
try:
    SALIoHwAb_ADC_IF_ADC_B12_SOC3_S2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_IF_ADC_B12_SOC3_S2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\HwCfg_Cfg.h: 3
HWCFG_STMAN_EPWM_INTERRUPT_BASE = INT_EPWM8

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 87
try:
    SAL_App_Signal_Com_MA_V2X_Monitoring_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Com_MA_V2X_Monitoring_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 399
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_060 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_060')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 385
try:
    SAL_App_Signal_GridEval_AC_L3L1_dV_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3L1_dV_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 409
try:
    SAL_App_Signal_GridEval_AC_L3L1_ZC_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3L1_ZC_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1197
try:
    SAL_App_Signal_Calib_HWMON_AC_DSP_3V3_1_MIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_DSP_3V3_1_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 913
try:
    SAL_App_Signal_Calib_GRIDEVAL_PHASECHECK_VOLTAGE_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_PHASECHECK_VOLTAGE_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1363
try:
    SAL_App_Signal_Calib_DERAT_RELAY_TEMP_VALUES = (sint16 * 4).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_DERAT_RELAY_TEMP_VALUES')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 378
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_063 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_063')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 693
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_020 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_020')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 503
try:
    SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LB_IS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LB_IS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1069
try:
    SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_UV_DQ = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_UV_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 211
try:
    SAL_App_Signal_HwCfg_AFE_LA_IS_MaxCurrent = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_HwCfg_AFE_LA_IS_MaxCurrent')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 857
try:
    SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MAX_VALUE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MAX_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 672
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_023 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_023')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 98
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_103 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_103')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 187
try:
    SAL_App_Signal_StMan_ST_AFE_L3_RD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_ST_AFE_L3_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 77
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_106 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_106')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 518
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_045 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_045')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1407
try:
    SALComGetSignal_COMRxSignal_MA_ODD_CNT = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_ODD_CNT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 289
try:
    SAL_App_Signal_GridEval_AC_L3_V_RMS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_V_RMS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 603
try:
    SAL_App_Signal_AFE_TEMP_LB = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_AFE_TEMP_LB')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 462
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_053 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_053')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 125
try:
    SAL_App_Dem_Fault5 = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Dem_Fault5')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1129
try:
    SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1001
try:
    SAL_App_Signal_Calib_RELACT_STATE_DELAY_ENERGIZE_TIME = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_RELACT_STATE_DELAY_ENERGIZE_TIME')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 441
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_056 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_056')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 756
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_011 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_011')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 237
try:
    SAL_App_Signal_GridEval_AC_L1_V_POS_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1_V_POS_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 933
try:
    SAL_App_Signal_Calib_GRIDEVAL_MONITORINGTIMEOUT_THRESHOLD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_MONITORINGTIMEOUT_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 441
try:
    SAL_App_Signal_GridEval_AC_L3L1_PhaseDegree = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3L1_PhaseDegree')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1383
try:
    SAL_App_Signal_Derat_DERAT_STATUS = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Derat_DERAT_STATUS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 735
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_014 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_014')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1325
try:
    SAL_App_Signal_Calib_PCOMP_AFE_DC_VOLTAGE_SENSORGAIN_VALUE = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_PCOMP_AFE_DC_VOLTAGE_SENSORGAIN_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 523
try:
    SAL_App_Signal_PComp_CMPSS1_DACHVAL = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_CMPSS1_DACHVAL')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1089
try:
    SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_VOLTAGEDELTA = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_VOLTAGEDELTA')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 61
try:
    SALIoHwAb_ADC_IF_ADC_B2_SOC5_S2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_IF_ADC_B2_SOC5_S2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 277
try:
    SAL_App_Signal_GridEval_AC_L3_dV_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_dV_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 42
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_111 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_111')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 581
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_036 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_036')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 131
try:
    SALIoHwAb_ADC_AC_DSP_3V3_S3 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_DSP_3V3_S3')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 21
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CRC_10 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CRC_10')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 755
try:
    SAL_App_Flag_Signal_CCP = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Flag_Signal_CCP')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1213
try:
    SAL_App_Signal_Calib_HWMON_AC_L1_FUSE_BLOWN_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L1_FUSE_BLOWN_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 51
try:
    SALIoHwAb_ADC_IF_ADC_C11_SOC3_S2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_IF_ADC_C11_SOC3_S2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 685
try:
    SAL_App_TstMan_PComp_Signal_PFC3PDCLinkVoltMesFactor_Value = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_PFC3PDCLinkVoltMesFactor_Value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 406
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_059 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_059')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 145
try:
    SAL_App_Dem_Fault10 = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Dem_Fault10')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1149
try:
    SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1348
try:
    SAL_App_Signal_Calib_DERAT_MOSFET_LA_WORK_COEF = (uint16 * 4).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_DERAT_MOSFET_LA_WORK_COEF')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1368
try:
    SAL_App_Signal_Calib_DERAT_RELAY_WORK_COEF = (uint16 * 4).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_DERAT_RELAY_WORK_COEF')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 35
try:
    SAL_App_Signal_ComE2E_MA_POWER_Counter_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_ComE2E_MA_POWER_Counter_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 36
try:
    SALIoHwAb_ADC_IF_ADC_B12_SOC0_S1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_IF_ADC_B12_SOC0_S1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 385
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_062 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_062')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\Ccp.h: 6
if hasattr(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'ccpDaq'):
    ccpDaq = _libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'].ccpDaq
    ccpDaq.argtypes = [uint16]
    ccpDaq.restype = None

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 467
try:
    SAL_App_Signal_PComp_PFC3PhaseCurrAMesFactor = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_PFC3PhaseCurrAMesFactor')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 201
try:
    SAL_App_Signal_ClaIf_CM_PLL_STATUS_1PH = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_ClaIf_CM_PLL_STATUS_1PH')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 679
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_022 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_022')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 105
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_102 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_102')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 965
try:
    SAL_App_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMAX_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMAX_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 617
try:
    SAL_App_Signal_RelAct_RelayType = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_RelAct_RelayType')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 84
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_105 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_105')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 525
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_044 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_044')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1053
try:
    SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_OV_DQ = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_OV_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 504
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_047 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_047')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1393
try:
    SALComGetSignal_COMRxSignal_MA_V2X_F = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_V2X_F')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1397
try:
    SAL_App_Signal_Meas_AC_12_VS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Meas_AC_12_VS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 469
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_052 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_052')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 365
try:
    SAL_App_Signal_GridEval_AC_L3L1_V_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3L1_V_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 437
try:
    SAL_App_Signal_GridEval_AC_L1L2_PhaseDegree = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1L2_PhaseDegree')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 448
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_055 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_055')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 885
try:
    SAL_App_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MAX_VALUE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MAX_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 71
try:
    SALIoHwAb_ADC_AFE_LA_IS_S2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AFE_LA_IS_S2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 742
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_013 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_013')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 769
try:
    SAL_App_Signal_Calib_STMAN_V2L_TO_STANDBY_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_V2L_TO_STANDBY_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1277
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MIN = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 707
try:
    SAL_App_TstMan_StMan_Signal_ST_AFE_L3_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_ST_AFE_L3_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 643
try:
    SAL_App_TstMan_RelAct_Signal_PWM_AC_L1L2_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_RelAct_Signal_PWM_AC_L1L2_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 49
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_110 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_110')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 588
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_035 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_035')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 28
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CNT_10 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CNT_10')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 413
try:
    SAL_App_Signal_GridEval_AC_L1L2_ZC_Max_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1L2_ZC_Max_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 567
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_038 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_038')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 168
try:
    Hfl_LogState = (uint16_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_LogState')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 813
try:
    SAL_App_Signal_Calib_STMAN_G2V_CHARGE_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_CHARGE_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1109
try:
    SAL_App_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_QT = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 763
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_010 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_010')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 873
try:
    SAL_App_Signal_Calib_STMAN_G2V_MAX_PRECHARGE_RETRIES = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_MAX_PRECHARGE_RETRIES')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1373
try:
    SAL_App_Signal_Calib_DERAT_MAXIMUM_CUTOFF_TEMP_FLYBACK = (sint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_DERAT_MAXIMUM_CUTOFF_TEMP_FLYBACK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 46
try:
    SALIoHwAb_ADC_IF_ADC_C11_SOC0_S1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_IF_ADC_C11_SOC0_S1')
except:
    pass

SAL_RequestResultType = enum_anon_12
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 413
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_058 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_058')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 392
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_061 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_061')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 686
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_021 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_021')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 305
try:
    SAL_App_Signal_GridEval_AC_L1_FREQ = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1_FREQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 112
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_101 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_101')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 401
try:
    SAL_App_Signal_GridEval_AC_L1L2_ZC_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1L2_ZC_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 789
try:
    SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_FAIL_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_FAIL_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1297
try:
    SAL_App_Signal_Calib_HWMON_AFE_DCLINKVOLTREF_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_DCLINKVOLTREF_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1013
try:
    SAL_App_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_MAX_ERROR = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_MAX_ERROR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 91
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_104 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_104')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 553
try:
    SAL_App_Signal_TstMan_Status = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_TstMan_Status')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 532
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_043 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_043')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 463
try:
    SAL_App_Signal_PComp_PFC3PhaseCurrCMesOffset = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_PFC3PhaseCurrCMesOffset')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 511
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_046 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_046')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1400
try:
    SALComGetSignal_COMRxSignal_MA_ODD_CMD = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_ODD_CMD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1185
try:
    SAL_App_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_VFACTOR = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_VFACTOR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 826
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_001 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_001')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 253
try:
    SAL_App_Signal_GridEval_AC_L2_V_NEG_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2_V_NEG_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 949
try:
    SAL_App_Signal_Calib_GRIDEVAL_3PH_LINETOLINERMSVOLTAGE_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_3PH_LINETOLINERMSVOLTAGE_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 329
try:
    SAL_App_Signal_GridEval_AC_L1_ZC_Max_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1_ZC_Max_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 476
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_051 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_051')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 833
try:
    SAL_App_Signal_Calib_STMAN_SHUTDOWN_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_SHUTDOWN_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 539
try:
    SAL_App_Signal_PComp_CMPSS3_DACHVAL = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_CMPSS3_DACHVAL')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1105
try:
    SAL_App_Signal_Calib_HWMON_BULK_CAPACITORS_UV = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_BULK_CAPACITORS_UV')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 245
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_082 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_082')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1229
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_QT = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 993
try:
    SAL_App_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMIN_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMIN_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 66
try:
    SALIoHwAb_ADC_AFE_LA_IS_S1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AFE_LA_IS_S1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 361
try:
    SAL_App_Signal_GridEval_AC_L2L3_V_NEG_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2L3_V_NEG_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 56
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_109 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_109')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1173
try:
    SAL_App_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_IMIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_IMIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__datagen__\Sal_App_Cfg.c: 11
try:
    ptr_to_0_value = (uint8).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'ptr_to_0_value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 595
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_034 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_034')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1033
try:
    SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_OV_QT = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_OV_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 325
try:
    SAL_App_Signal_GridEval_AC_L3_ZC_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_ZC_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 35
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_112 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_112')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1317
try:
    SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LC_SENSORGAIN_VALUE = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LC_SENSORGAIN_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 573
try:
    SAL_App_Signal_TstMan_Mode_StMan = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_TstMan_Mode_StMan')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 51
try:
    SAL_App_Signal_ComE2E_MA_REQUEST_OP_Counter_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_ComE2E_MA_REQUEST_OP_Counter_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 647
try:
    SAL_App_TstMan_RelAct_Signal_PWM_AC_L3_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_RelAct_Signal_PWM_AC_L3_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 483
try:
    SAL_App_Signal_PComp_PFC3PDCLinkVoltMesFactor = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_PFC3PDCLinkVoltMesFactor')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 269
try:
    SAL_App_Signal_GridEval_AC_L1_dV_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1_dV_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 770
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_009 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_009')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 420
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_057 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_057')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 163
try:
    SAL_App_Signal_StMan_STMAN_SUBSTATE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_STMAN_SUBSTATE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1078
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_3_F = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_3_F')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1372
try:
    SALComGetSignal_COMRxSignal_MA_V2X_MAX_I = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_V2X_MAX_I')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 735
try:
    SAL_App_TstMan_StMan_Signal_AM_OP_MODE_FB = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_AM_OP_MODE_FB')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 119
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_100 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_100')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1249
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_DQ = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__datagen__\Hfl_Cfg.c: 168
try:
    Hfl_DAQCopyVar1 = (real32_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_DAQCopyVar1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 889
try:
    SALComGetSignal_COMTxSignal_AM_PS_T = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_PS_T')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 381
try:
    SAL_App_Signal_GridEval_AC_L2L3_dV_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2L3_dV_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 202
try:
    SALIoHwAb_PWM_AC_L3_RD = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_PWM_AC_L3_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 539
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_042 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_042')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 909
try:
    SAL_App_Signal_Calib_HWCFG_3PH_11_KW_SYS_11KW_IS_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWCFG_3PH_11_KW_SYS_11KW_IS_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 16
try:
    SALIoHwAb_ADC_IF_ADC_A2_SOC0_S1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_IF_ADC_A2_SOC0_S1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 499
try:
    SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LA_IS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LA_IS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1065
try:
    SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_UV_QT = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_UV_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 133
try:
    SAL_App_Dem_Fault7 = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Dem_Fault7')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1137
try:
    SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 901
try:
    SAL_App_Signal_Calib_HWCFG_1PH_3_6_KW_SYS_11KW_IS_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWCFG_1PH_3_6_KW_SYS_11KW_IS_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1338
try:
    SAL_App_Signal_Calib_DERAT_VIN_WORK_COEF = (uint16 * 5).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_DERAT_VIN_WORK_COEF')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 833
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CNT_08 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CNT_08')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 46
class struct_anon_15(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 723
try:
    SAL_App_TstMan_StMan_Signal_ST_AC_L2_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_ST_AC_L2_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 59
try:
    Hfl_OperationMode = (uint32_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_OperationMode')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1022
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_2_RMS_V = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_2_RMS_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1316
try:
    SALComGetSignal_COMRxSignal_MA_REACT_P_PH2 = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_REACT_P_PH2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 429
try:
    SAL_App_Signal_GridEval_AC_L3_ACTIVE_PWR = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_ACTIVE_PWR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 65
try:
    SAL_App_Signal_NM_FAULT_ERROR_PASSIVE = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_NM_FAULT_ERROR_PASSIVE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 661
try:
    SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrBMesOffset_Value = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrBMesOffset_Value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 599
try:
    SAL_App_Signal_AFE_TEMP_LA = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_AFE_TEMP_LA')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 952
try:
    SALComGetSignal_COMTxSignal_AM_PH_1_2_ANGLE = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_PH_1_2_ANGLE')
except:
    pass

SAL_NvM_BlockIdType = uint16
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 86

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 121
try:
    SAL_App_Dem_Fault4 = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Dem_Fault4')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1125
try:
    SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 18
try:
    PFC3PDCLinkVoltMes = (uint16_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'PFC3PDCLinkVoltMes')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 761
try:
    SAL_App_Signal_Calib_STMAN_OFF_TO_RUN_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_OFF_TO_RUN_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1269
try:
    SAL_App_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MIN = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 699
try:
    SAL_App_TstMan_StMan_Signal_PCompSamplingMode = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_PCompSamplingMode')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 252
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_081 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_081')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1141
try:
    SALComGetSignal_COMTxSignal_AM_VERSION_HOUR = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_VERSION_HOUR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1106
try:
    SALComGetSignal_COMTxSignal_AM_DER_STATUS = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DER_STATUS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 777
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_008 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_008')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 749
try:
    SAL_App_TstMan_GridEval_Signal_Operation_Mode = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_GridEval_Signal_Operation_Mode')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1085
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_3_RMS_I = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_3_RMS_I')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1029
try:
    SAL_App_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_IMAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_IMAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 805
try:
    SAL_App_Signal_Calib_STMAN_G2V_PERIPHERAL_INIT_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PERIPHERAL_INIT_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 116
try:
    SALIoHwAb_ADC_AC_L3_VS = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_L3_VS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1379
try:
    SALComGetSignal_COMRxSignal_MA_V2X_MIN_V = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_V2X_MIN_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 91
try:
    SAL_App_Signal_Com_MA_REQUEST_OP_InvalidValue_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Com_MA_REQUEST_OP_InvalidValue_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1201
try:
    SAL_App_Signal_Calib_HWMON_AC_DSP_3V3_1_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_DSP_3V3_1_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 681
try:
    SAL_App_TstMan_PComp_Signal_PFC3PhaseVoltMesFactor_Value = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_PFC3PhaseVoltMesFactor_Value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 336
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_069 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_069')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 896
try:
    SALComGetSignal_COMTxSignal_AM_FET_L3_T = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_FET_L3_T')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1225
try:
    SALComGetSignal_COMTxSignal_AM_ODD_B3 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_ODD_B3')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 849
try:
    SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MAX_VALUE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MAX_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 208
try:
    SALIoHwAb_PWM_AC_N_RD = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_PWM_AC_N_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 215
try:
    SAL_App_Signal_HwCfg_AFE_LB_IS_MaxCurrent = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_HwCfg_AFE_LB_IS_MaxCurrent')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 861
try:
    SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MIN_VALUE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MIN_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 315
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_072 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_072')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1204
try:
    SALComGetSignal_COMTxSignal_AM_ODD_B0 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_ODD_B0')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 297
try:
    SAL_App_Signal_GridEval_AC_L2_IS_RMS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2_IS_RMS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 55
class struct_anon_6(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 781
try:
    SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_TWO_PHASES_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_TWO_PHASES_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1289
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MAX = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1050
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CNT_05 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CNT_05')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 191
try:
    SAL_App_Signal_StMan_PCompDeadTimePassed = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_PCompDeadTimePassed')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 455
try:
    SAL_App_Signal_PComp_PFC3PhaseCurrAMesOffset = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_PFC3PhaseCurrAMesOffset')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1029
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_2_PK_V = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_2_PK_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 389
try:
    SAL_App_Signal_GridEval_AC_L1L2_V_RMS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1L2_V_RMS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 126
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_099 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_099')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1049
try:
    SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_OV_DQ = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_OV_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 449
try:
    SAL_App_Signal_GridEval_PhaseDetection_Check01 = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_PhaseDetection_Check01')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1323
try:
    SALComGetSignal_COMRxSignal_MA_REACT_P_PH1 = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_REACT_P_PH1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 589
try:
    SAL_App_Signal_TstMan_Mode_HwMon = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_TstMan_Mode_HwMon')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 341
try:
    SAL_App_Signal_GridEval_AC_L1L2_V_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1L2_V_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 280
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_077 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_077')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1169
try:
    SALComGetSignal_COMTxSignal_AM_VERSION_MAJOR = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_VERSION_MAJOR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 241
try:
    SAL_App_Signal_GridEval_AC_L1_V_NEG_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1_V_NEG_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 937
try:
    SAL_App_Signal_Calib_GRIDEVAL_PH_PEAKVOLTAGE_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_PH_PEAKVOLTAGE_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1387
try:
    SAL_App_Signal_Derat_AM_DER_MAX_I = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Derat_AM_DER_MAX_I')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 179
try:
    SAL_App_Signal_StMan_ST_AC_L3_RD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_ST_AC_L3_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 161
try:
    SALIoHwAb_ADC_AC_FLY_TEMP = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_FLY_TEMP')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1221
try:
    SAL_App_Signal_Calib_HWMON_AC_L3_FUSE_BLOWN_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L3_FUSE_BLOWN_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 527
try:
    SAL_App_Signal_PComp_CMPSS1_DACLVAL = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_CMPSS1_DACLVAL')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1093
try:
    SAL_App_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_TEMPDELTA = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_TEMPDELTA')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 259
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_080 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_080')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1148
try:
    SALComGetSignal_COMTxSignal_AM_VERSION_RC = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_VERSION_RC')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 881
try:
    SAL_App_Signal_Calib_STMAN_V2L_AC_STABILIZATION_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_V2L_AC_STABILIZATION_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1113
try:
    SALComGetSignal_COMTxSignal_AM_OP_MODE_FB = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_OP_MODE_FB')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1165
try:
    SAL_App_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_IMIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_IMIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 639
try:
    SAL_App_TstMan_RelAct_Signal_PWM_AC_L2_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_RelAct_Signal_PWM_AC_L2_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1092
try:
    SALComGetSignal_COMTxSignal_AM_NO_PHASES = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_NO_PHASES')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__datagen__\Hfl_Cfg.c: 160
try:
    Hfl_DAQCopyVar0 = (real32_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_DAQCopyVar0')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 43
try:
    SAL_App_Signal_ComE2E_MA_V2X_Counter_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_ComE2E_MA_V2X_Counter_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 475
try:
    SAL_App_Signal_PComp_PFC3PhaseCurrCMesFactor = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_PFC3PhaseCurrCMesFactor')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1353
try:
    SAL_App_Signal_Calib_DERAT_MOSFET_LB_WORK_COEF = (uint16 * 4).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_DERAT_MOSFET_LB_WORK_COEF')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1386
try:
    SALComGetSignal_COMRxSignal_MA_V2X_V = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_V2X_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 229
try:
    SAL_App_Signal_GridEval_Operation_Mode = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_Operation_Mode')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 925
try:
    SAL_App_Signal_Calib_GRIDEVAL_TIMERTIMEOUT_THRESHOLD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_TIMERTIMEOUT_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 155
try:
    SAL_App_Signal_StMan_PFCOpState = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_PFCOpState')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 111
try:
    SALIoHwAb_ADC_AC_L2_VS = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_L2_VS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 515
try:
    SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LB_IS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LB_IS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1081
try:
    SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_TEMPDELTA = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_TEMPDELTA')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1153
try:
    SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 17
try:
    PFC3PhaseVoltAMes = (uint16_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'PFC3PhaseVoltAMes')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 31
try:
    SALIoHwAb_ADC_IF_ADC_A2_SOC5_S2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_IF_ADC_A2_SOC5_S2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 343
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_068 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_068')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1232
try:
    SALComGetSignal_COMTxSignal_AM_ODD_B4 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_ODD_B4')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 205
try:
    SAL_App_Signal_ClaIf_CM_PLL_STATUS_3PH = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_ClaIf_CM_PLL_STATUS_3PH')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 214
try:
    SALIoHwAb_PWM_AFE_L3_RD = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_PWM_AFE_L3_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__eut__\hfl_utest\stubbed_Ccp.c: 3
try:
    _p_ccpDaq = (POINTER(CFUNCTYPE(UNCHECKED(None), uint16))).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], '_p_ccpDaq')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 727
try:
    SAL_App_TstMan_StMan_Signal_PFCOpState = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_PFCOpState')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 322
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_071 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_071')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1211
try:
    SALComGetSignal_COMTxSignal_AM_ODD_B1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_ODD_B1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 969
try:
    SAL_App_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMIN_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMIN_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1241
try:
    SAL_App_Signal_Calib_HWMON_AC_FLY_TEMP_QT = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_FLY_TEMP_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1057
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CHK_05 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CHK_05')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 373
try:
    SAL_App_Signal_GridEval_AC_L3L1_V_NEG_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3L1_V_NEG_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 547
try:
    SAL_App_Signal_PComp_IsReady = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_IsReady')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 61
class struct_anon_7(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1036
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_2_F = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_2_F')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 491
try:
    SAL_App_Signal_PComp_ADC_AC_1_65V_VS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_ADC_AC_1_65V_VS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1057
try:
    SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_UV_QT = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_UV_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 101
try:
    SALIoHwAb_ADC_AC_AFE_VOUT_VS_S2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_AFE_VOUT_VS_S2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 715
try:
    SAL_App_TstMan_StMan_Signal_ST_AC_L3_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_ST_AC_L3_RD')
except:
    pass

Std_ReturnType = uint8
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 20

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 637
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_028 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_028')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 287
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_076 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_076')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1176
try:
    SALComGetSignal_COMTxSignal_AM_VERSION_YEAR = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_VERSION_YEAR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 653
try:
    SAL_App_TstMan_PComp_Signal_IsReady = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_IsReady')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 266
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_079 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_079')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1155
try:
    SALComGetSignal_COMTxSignal_AM_VERSION_PATCH = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_VERSION_PATCH')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 821
try:
    SAL_App_Signal_Calib_STMAN_V2L_PREPARE_TO_RUN_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_V2L_PREPARE_TO_RUN_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1120
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CNT_07 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CNT_07')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 113
try:
    SAL_App_Dem_Fault2 = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Dem_Fault2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1117
try:
    SAL_App_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 989
try:
    SAL_App_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMAX_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMAX_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1099
try:
    SALComGetSignal_COMTxSignal_AM_DER_FACT = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DER_FACT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 321
try:
    SAL_App_Signal_GridEval_AC_L2_ZC_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2_ZC_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 877
try:
    SAL_App_Signal_Calib_STMAN_V2L_DCLINK_MARGIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_V2L_DCLINK_MARGIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1377
try:
    SAL_App_Signal_Calib_DERAT_MAXIMUM_OPERATIONAL_TEMP_FLYBACK = (sint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_DERAT_MAXIMUM_OPERATIONAL_TEMP_FLYBACK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 700
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_019 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_019')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 797
try:
    SAL_App_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1305
try:
    SAL_App_Signal_Calib_PCOMP_ADC_LSB_ERROR_THRESHOLD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_PCOMP_ADC_LSB_ERROR_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1021
try:
    SAL_App_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_MAX_ERROR = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_MAX_ERROR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 350
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_067 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_067')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1239
try:
    SALComGetSignal_COMTxSignal_AM_ODD_B5 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_ODD_B5')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 353
try:
    SAL_App_Signal_GridEval_AC_L2L3_V_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2L3_V_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 561
try:
    SAL_App_Signal_TstMan_Disable_WdgM = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_TstMan_Disable_WdgM')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 21
class struct_anon_1(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 26
try:
    SALIoHwAb_ADC_IF_ADC_A2_SOC2_S1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_IF_ADC_A2_SOC2_S1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.c: 136
try:
    Hfl_SmartTrigger_Index = (real32_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_SmartTrigger_Index')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 83
try:
    SAL_App_Signal_Com_MA_V2X_InvalidValue_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Com_MA_V2X_InvalidValue_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 329
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_070 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_070')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1218
try:
    SALComGetSignal_COMTxSignal_AM_ODD_B2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_ODD_B2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 405
try:
    SAL_App_Signal_GridEval_AC_L2L3_ZC_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2L3_ZC_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1193
try:
    SAL_App_Signal_Calib_HWMON_AC_12V_TH_HIGH_QT = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_12V_TH_HIGH_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 673
try:
    SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrBMesFactor_Value = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrBMesFactor_Value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1064
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_3_RMS_V = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_3_RMS_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 841
try:
    SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA2 = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 853
try:
    SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MIN_VALUE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MIN_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 483
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_050 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_050')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1043
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_2_RMS_I = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_2_RMS_I')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 187
try:
    SALIoHwAb_DIO_AFE_LB_DRV_PS_PG = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_DIO_AFE_LB_DRV_PS_PG')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 257
try:
    SAL_App_Signal_GridEval_AC_L3_V_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_V_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 953
try:
    SAL_App_Signal_Calib_GRIDEVAL_3PH_LINERMSVOLTAGE_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_3PH_LINERMSVOLTAGE_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 183
try:
    SAL_App_Signal_StMan_ST_AC_N_RD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_ST_AC_N_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 349
try:
    SAL_App_Signal_GridEval_AC_L1L2_V_NEG_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1L2_V_NEG_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 897
try:
    SAL_App_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_22KW_IS_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_22KW_IS_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 96
try:
    SALIoHwAb_ADC_AC_AFE_VOUT_VS_S1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_AFE_VOUT_VS_S1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 644
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_027 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_027')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1181
try:
    SAL_App_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_IMIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_IMIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 294
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_075 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_075')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1183
try:
    SALComGetSignal_COMTxSignal_AM_VERSION_MONTH = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_VERSION_MONTH')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1041
try:
    SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_OV_QT = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_OV_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 581
try:
    SAL_App_Signal_TstMan_Mode_TempSens = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_TstMan_Mode_TempSens')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 602
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_033 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_033')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 59
try:
    SAL_App_Signal_ComE2E_MA_MCMP_Counter_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_ComE2E_MA_MCMP_Counter_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 273
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_078 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_078')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1162
try:
    SALComGetSignal_COMTxSignal_AM_VERSION_MINOR = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_VERSION_MINOR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.c: 135
try:
    Hfl_StartTs = (uint32_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_StartTs')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1127
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CHK_07 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CHK_07')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 425
try:
    SAL_App_Signal_GridEval_AC_L3_PWR_FACTOR = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_PWR_FACTOR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 233
try:
    SAL_App_Signal_GridEval_AC_L1_V_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1_V_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 929
try:
    SAL_App_Signal_Calib_GRIDEVAL_TIMERVALID_THRESHOLD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_TIMERVALID_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 171
try:
    SAL_App_Signal_StMan_ST_AC_L1L2_RD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_ST_AC_L1L2_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 26
class struct_anon_2(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1321
try:
    SAL_App_Signal_Calib_PCOMP_AFE_AC_VOLTAGE_SENSORGAIN_VALUE = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_PCOMP_AFE_AC_VOLTAGE_SENSORGAIN_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 519
try:
    SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LC_IS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LC_IS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1085
try:
    SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_CURRENTDELTA = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_CURRENTDELTA')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 427
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CRC_01 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CRC_01')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 273
try:
    SAL_App_Signal_GridEval_AC_L2_dV_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2_dV_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1265
try:
    SAL_App_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MAX = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 631
try:
    SAL_App_TstMan_RelAct_Signal_PWM_AFE_L3_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_RelAct_Signal_PWM_AFE_L3_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 707
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_018 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_018')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1257
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_DQ = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 357
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_066 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_066')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1246
try:
    SALComGetSignal_COMTxSignal_AM_ODD_B6 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_ODD_B6')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 917
try:
    SAL_App_Signal_Calib_GRIDEVAL_PHASECHECK_FILTER_SIZE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_PHASECHECK_FILTER_SIZE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.c: 102
try:
    Hfl_Buffer_Index = (uint16_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_Buffer_Index')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 507
try:
    SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LC_IS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LC_IS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1073
try:
    SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_UV_DQ = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_UV_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 141
try:
    SAL_App_Dem_Fault9 = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Dem_Fault9')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1145
try:
    SAL_App_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 546
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_041 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_041')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1071
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_3_PK_V = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_3_PK_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 197
try:
    SALIoHwAb_DIO_AFE_LS_DRV_PS_PG = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_DIO_AFE_LS_DRV_PS_PG')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 34
class struct_anon_13(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 840
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CHK_08 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CHK_08')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 490
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_049 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_049')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 961
try:
    SAL_App_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK02_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK02_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 106
try:
    SALIoHwAb_ADC_AC_L1_VS = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_L1_VS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 293
try:
    SAL_App_Signal_GridEval_AC_L1_IS_RMS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1_IS_RMS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 182
try:
    SALIoHwAb_DIO_AFE_LA_DRV_PS_PG = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_DIO_AFE_LA_DRV_PS_PG')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 669
try:
    SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrAMesFactor_Value = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrAMesFactor_Value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\__build__\hfl_utest\__datagen__\Hfl_Cfg.c: 176
try:
    Hfl_DAQCopyVar2 = (real32_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_DAQCopyVar2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 607
try:
    SAL_App_Signal_AFE_TEMP_LC = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_AFE_TEMP_LC')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 651
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_026 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_026')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1005
try:
    SAL_App_Signal_Calib_RELACT_STATE_DELAY_ZERO_CROSS_TIME = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_RELACT_STATE_DELAY_ZERO_CROSS_TIME')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 630
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_029 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_029')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 301
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_074 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_074')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1190
try:
    SALComGetSignal_COMTxSignal_AM_VERSION_DAY = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_VERSION_DAY')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1393
try:
    SAL_App_Signal_Meas_AC_AFE_VOUT_VS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Meas_AC_AFE_VOUT_VS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 959
try:
    SALComGetSignal_COMTxSignal_AM_CAP_V = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_CAP_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1333
try:
    SAL_App_Signal_Calib_DERAT_VIN_VALUES = (uint16 * 5).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_DERAT_VIN_VALUES')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 609
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_032 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_032')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 784
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_007 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_007')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 703
try:
    SAL_App_TstMan_StMan_Signal_ST_AC_L1L2_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_ST_AC_L1L2_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 434
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CNT_01 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CNT_01')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 146
try:
    SALIoHwAb_ADC_AFE_TEMP_LB = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AFE_TEMP_LB')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1217
try:
    SAL_App_Signal_Calib_HWMON_AC_L2_FUSE_BLOWN_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L2_FUSE_BLOWN_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 981
try:
    SAL_App_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK01_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK01_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 189
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_090 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_090')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 99
try:
    SAL_App_Signal_Com_MA_MCMP_InvalidValue_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Com_MA_MCMP_InvalidValue_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 714
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_017 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_017')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 689
try:
    SAL_App_TstMan_PComp_Signal_AC_DSP_3V3_1_Value = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_AC_DSP_3V3_1_Value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 313
try:
    SAL_App_Signal_GridEval_AC_L3_FREQ = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_FREQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 869
try:
    SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MIN_VALUE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MIN_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 39
try:
    SAL_App_Signal_ComE2E_MA_V2X_Checksum_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_ComE2E_MA_V2X_Checksum_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 903
try:
    SALComGetSignal_COMTxSignal_AM_FET_L2_T = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_FET_L2_T')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 220
try:
    SALIoHwAb_PWM_AC_L1L2_RD = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_PWM_AC_L1L2_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 553
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_040 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_040')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 868
try:
    SALComGetSignal_COMTxSignal_AM_REF_3V3 = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_REF_3V3')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 847
try:
    SALComGetSignal_COMTxSignal_AM_PS_V = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_PS_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 497
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_048 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_048')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 192
try:
    SALIoHwAb_DIO_AFE_LC_DRV_PS_PG = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_DIO_AFE_LC_DRV_PS_PG')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 397
try:
    SAL_App_Signal_GridEval_AC_L3L1_V_RMS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3L1_V_RMS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 785
try:
    SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_THREE_PHASES_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_THREE_PHASES_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1293
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MIN = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 133
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_098 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_098')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 987
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_1_PK_V = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_1_PK_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 658
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_025 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_025')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 543
try:
    SAL_App_Signal_PComp_CMPSS3_DACLVAL = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_CMPSS3_DACLVAL')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 249
try:
    SAL_App_Signal_GridEval_AC_L2_V_POS_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2_V_POS_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 945
try:
    SAL_App_Signal_Calib_GRIDEVAL_V2L_PEAKVOLTAGE_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_V2L_PEAKVOLTAGE_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 966
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CNT_03 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CNT_03')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 337
try:
    SAL_App_Signal_GridEval_AC_L3_ZC_Max_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_ZC_Max_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 829
try:
    SAL_App_Signal_Calib_STMAN_V2L_AC_STABILIZATION_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_V2L_AC_STABILIZATION_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 535
try:
    SAL_App_Signal_PComp_CMPSS2_DACLVAL = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_CMPSS2_DACLVAL')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1101
try:
    SAL_App_Signal_Calib_HWMON_BULK_CAPACITORS_OV = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_BULK_CAPACITORS_OV')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 166
try:
    SALIoHwAb_ADC_AC_12V_VS = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_12V_VS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 63
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_108 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_108')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 889
try:
    SAL_App_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MIN_VALUE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MIN_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 616
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_031 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_031')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 773
try:
    SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_RUN_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_RUN_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1281
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MAX = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 812
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_003 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_003')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 156
try:
    SALIoHwAb_ADC_AC_1_65V_VS = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AC_1_65V_VS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 791
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_006 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_006')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Stub\PFCCtrl.h: 16
try:
    PFC3PhaseVoltCMes = (uint16_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'PFC3PhaseVoltCMes')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 217
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_086 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_086')
except:
    pass

SAL_MemStackRequestType = enum_anon_11
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 103

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1169
try:
    SAL_App_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_VFACTOR = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_VFACTOR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 417
try:
    SAL_App_Signal_GridEval_AC_L2L3_ZC_Max_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2L3_ZC_Max_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 196
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_089 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_089')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 817
try:
    SAL_App_Signal_Calib_STMAN_V2L_PERIPHERAL_INIT_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_V2L_PERIPHERAL_INIT_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 141
try:
    SALIoHwAb_ADC_AFE_TEMP_LA = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AFE_TEMP_LA')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1313
try:
    SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LB_SENSORGAIN_VALUE = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LB_SENSORGAIN_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 569
try:
    SAL_App_Signal_TstMan_Mode_PComp = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_TstMan_Mode_PComp')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 931
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CHK_02 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CHK_02')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 479
try:
    SAL_App_Signal_PComp_PFC3PhaseVoltMesFactor = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_PFC3PhaseVoltMesFactor')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 265
try:
    SAL_App_Signal_GridEval_AC_L3_V_NEG_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_V_NEG_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 910
try:
    SALComGetSignal_COMTxSignal_AM_FET_L1_T = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_FET_L1_T')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 159
try:
    SAL_App_Signal_StMan_STMAN_STATE = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_STMAN_STATE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 226
try:
    SALIoHwAb_PWM_AC_L1_RD = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_PWM_AC_L1_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 977
try:
    SAL_App_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMIN_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMIN_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 560
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_039 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_039')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 875
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CNT_06 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CNT_06')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 309
try:
    SAL_App_Signal_GridEval_AC_L2_FREQ = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2_FREQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 854
try:
    SALComGetSignal_COMTxSignal_AM_HW_VS_V = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_HW_VS_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1017
try:
    SAL_App_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_THRESHOLD = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 28
try:
    ptr_to_0 = (POINTER(uint8)).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'ptr_to_0')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 557
try:
    SAL_App_Signal_TstMan_Disable_SwSec = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_TstMan_Disable_SwSec')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 161
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_094 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_094')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1245
try:
    SAL_App_Signal_Calib_HWMON_AC_RLY_TEMP_DQ = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_RLY_TEMP_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1358
try:
    SAL_App_Signal_Calib_DERAT_MOSFET_LC_WORK_COEF = (uint16 * 4).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_DERAT_MOSFET_LC_WORK_COEF')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 79
try:
    SAL_App_Signal_Com_MA_POWER_Monitoring_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Com_MA_POWER_Monitoring_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 377
try:
    SAL_App_Signal_GridEval_AC_L1L2_dV_PK = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1L2_dV_PK')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 140
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_097 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_097')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1189
try:
    SAL_App_Signal_Calib_HWMON_AC_12V_TH_LOW_QT = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_12V_TH_LOW_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1344
try:
    SALComGetSignal_COMRxSignal_MA_ACT_P_PH1 = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_ACT_P_PH1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 905
try:
    SAL_App_Signal_Calib_HWCFG_3PH_22_KW_SYS_22KW_IS_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWCFG_3PH_22_KW_SYS_22KW_IS_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 994
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_1_F = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_1_F')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 176
try:
    SALIoHwAb_DIO_AFE_DRV_PS_EN = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_DIO_AFE_DRV_PS_EN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 495
try:
    SAL_App_Signal_PComp_AC_DSP_3V3_1 = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_PComp_AC_DSP_3V3_1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1061
try:
    SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_UV_QT = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_UV_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 973
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CHK_03 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CHK_03')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 285
try:
    SAL_App_Signal_GridEval_AC_L2_V_RMS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2_V_RMS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 623
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_030 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_030')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 719
try:
    SAL_App_TstMan_StMan_Signal_ST_AC_L1_RD = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_ST_AC_L1_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1233
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_QT = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_QT')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 819
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_002 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_002')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 997
try:
    SAL_App_Signal_Calib_GRIDEVAL_V2L_LINERMSVOLTAGE_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_V2L_LINERMSVOLTAGE_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 81
try:
    SALIoHwAb_ADC_AFE_LB_IS_S2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AFE_LB_IS_S2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 798
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_005 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_005')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 224
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_085 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_085')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.c: 120
try:
    Hfl_Isr_State = (uint16_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_Isr_State')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 595
try:
    SAL_App_Signal_AC_RLY_TEMP = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_AC_RLY_TEMP')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 151
try:
    SALIoHwAb_ADC_AFE_TEMP_LC = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AFE_TEMP_LC')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 117
try:
    SAL_App_Dem_Fault3 = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Dem_Fault3')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1121
try:
    SAL_App_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 203
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_088 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_088')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 55
try:
    SAL_App_Signal_ComE2E_MA_MCMP_Checksum_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_ComE2E_MA_MCMP_Checksum_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1288
try:
    SALComGetSignal_COMRxSignal_MA_OP_MODE = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_OP_MODE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 938
try:
    SALComGetSignal_COMTxSignal_AM_PH_3_1_ANGLE = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_PH_3_1_ANGLE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1209
try:
    SAL_App_Signal_Calib_HWMON_AC_1_65V_VS_MAX = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_1_65V_VS_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1267
try:
    SALComGetSignal_COMRxSignal_MA_E2E_CNT_02 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_E2E_CNT_02')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 56
try:
    SALIoHwAb_ADC_IF_ADC_B2_SOC2_S1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_IF_ADC_B2_SOC2_S1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 745
try:
    SAL_App_TstMan_GridEval_Signal_GRID_NO_OF_PH = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_GridEval_Signal_GRID_NO_OF_PH')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 917
try:
    SALComGetSignal_COMTxSignal_AM_REL_T = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_REL_T')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 801
try:
    SAL_App_Signal_Calib_STMAN_G2V_PREPARE_TO_RUN_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PREPARE_TO_RUN_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1309
try:
    SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LA_SENSORGAIN_VALUE = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LA_SENSORGAIN_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 882
try:
    SALComGetSignal_COMTxSignal_AM_E2E_CHK_06 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_E2E_CHK_06')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 739
try:
    SAL_App_TstMan_StMan_Signal_NumberOfPhasesConfigured = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_StMan_Signal_NumberOfPhasesConfigured')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 861
try:
    SALComGetSignal_COMTxSignal_AM_REF_1V65 = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_REF_1V65')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 31
try:
    SAL_App_Signal_ComE2E_MA_POWER_Checksum_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_ComE2E_MA_POWER_Checksum_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 621
try:
    SAL_App_Signal_RelAct_RelayStatus = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_RelAct_RelayStatus')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 168
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_093 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_093')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1343
try:
    SAL_App_Signal_Calib_DERAT_MOSFET_TEMP_VALUES = (sint16 * 4).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_DERAT_MOSFET_TEMP_VALUES')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 21
try:
    SALIoHwAb_ADC_IF_ADC_A2_SOC3_S2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_IF_ADC_A2_SOC3_S2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 677
try:
    SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrCMesFactor_Value = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrCMesFactor_Value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 845
try:
    SAL_App_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_THRESHOLD_DELTA = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_THRESHOLD_DELTA')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 147
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_096 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_096')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 137
try:
    SAL_App_Dem_Fault8 = (uint64).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Dem_Fault8')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1141
try:
    SAL_App_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MIN = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1351
try:
    SALComGetSignal_COMRxSignal_MA_E2E_CHK_03 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_E2E_CHK_03')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1001
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_1_RMS_I = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_1_RMS_I')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 21
def SAL_CHECK_IF_FLOATS_ARE_EQUAL(floatsDivided):
    return (floatsDivided < SAL_FLOAT_UPPER_RESOLUTION) and (floatsDivided > SAL_FLOAT_LOWER_RESOLUTION) and TRUE or FALSE or FALSE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 777
try:
    SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_ONE_PHASE_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_ONE_PHASE_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1285
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MIN = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MIN')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1330
try:
    SALComGetSignal_COMRxSignal_MA_ACT_P_PH3 = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_ACT_P_PH3')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 333
try:
    SAL_App_Signal_GridEval_AC_L2_ZC_Max_Counter = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2_ZC_Max_Counter')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 980
try:
    SALComGetSignal_COMTxSignal_AM_AC_PH_1_RMS_V = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_AC_PH_1_RMS_V')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 171
try:
    SALIoHwAb_ADC_AFE_SITE_ID = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AFE_SITE_ID')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 957
try:
    SAL_App_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK01_THRESHOLD = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK01_THRESHOLD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 75
try:
    SAL_App_Signal_Com_MA_POWER_InvalidValue_Fault = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Com_MA_POWER_InvalidValue_Fault')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 91
try:
    SALIoHwAb_ADC_AFE_LC_IS_S2 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AFE_LC_IS_S2')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 433
try:
    SAL_App_Signal_GridEval_AC_L3_REACTIVE_PWR = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L3_REACTIVE_PWR')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 69
try:
    SAL_App_Signal_NM_FAULT_BUSS_OFF = (boolean).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_NM_FAULT_BUSS_OFF')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 665
try:
    SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrCMesOffset_Value = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrCMesOffset_Value')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1045
try:
    SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_OV_DQ = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_OV_DQ')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 445
try:
    SAL_App_Signal_GridEval_AC_L2L3_PhaseDegree = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L2L3_PhaseDegree')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1134
try:
    SALComGetSignal_COMTxSignal_AM_VERSION_MINUTE = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_VERSION_MINUTE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1329
try:
    SAL_App_Signal_Calib_PCOMP_AFE_12V_SENSORGAIN_VALUE = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_PCOMP_AFE_12V_SENSORGAIN_VALUE')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 805
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_004 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_004')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 585
try:
    SAL_App_Signal_TstMan_Mode_GridEval = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_TstMan_Mode_GridEval')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 231
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_084 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_084')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 76
try:
    SALIoHwAb_ADC_AFE_LB_IS_S1 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALIoHwAb_ADC_AFE_LB_IS_S1')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.c: 105
try:
    Hfl_TxRateIdx = (uint16_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_TxRateIdx')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 281
try:
    SAL_App_Signal_GridEval_AC_L1_V_RMS = (float32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_GridEval_AC_L1_V_RMS')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 765
try:
    SAL_App_Signal_Calib_STMAN_G2V_TO_STANDBY_TIMEOUT_TIMER = (uint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_STMAN_G2V_TO_STANDBY_TIMEOUT_TIMER')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1273
try:
    SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MAX = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MAX')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 210
try:
    SALComGetSignal_COMTxSignal_AM_DIAG_087 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMTxSignal_AM_DIAG_087')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.c: 113
try:
    Hfl_SmartTrigger = (uint16_T).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'Hfl_SmartTrigger')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 175
try:
    SAL_App_Signal_StMan_ST_AC_L2_RD = (uint16).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SAL_App_Signal_StMan_ST_AC_L2_RD')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1295
try:
    SALComGetSignal_COMRxSignal_MA_E2E_CHK_01 = (sint32).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'SALComGetSignal_COMRxSignal_MA_E2E_CHK_01')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 942
def SALGetSignal_Signal_Calib_GRIDEVAL_PH_DELTAPEAKVOLTAGE_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_PH_DELTAPEAKVOLTAGE_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1195
SALGetSignalSize_Signal_Calib_HWMON_AC_12V_TH_HIGH_QT = sizeof(SAL_App_Signal_Calib_HWMON_AC_12V_TH_HIGH_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 883
def SALGetSignal_COMTxSignal_AM_E2E_CHK_06():
    return SALComGetSignal_COMTxSignal_AM_E2E_CHK_06

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 334
def SALGetSignal_Signal_GridEval_AC_L2_ZC_Max_Counter():
    return SAL_App_Signal_GridEval_AC_L2_ZC_Max_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 583
SALGetSignalSize_Signal_TstMan_Mode_TempSens = sizeof(SAL_App_Signal_TstMan_Mode_TempSens)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 907
SALGetSignalSize_Signal_Calib_HWCFG_3PH_22_KW_SYS_22KW_IS_MAX = sizeof(SAL_App_Signal_Calib_HWCFG_3PH_22_KW_SYS_22KW_IS_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1162
def SALGetSignal_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MAX():
    return SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 167
def SALGetSignal_Signal_ADC_AC_12V_VS():
    return SALIoHwAb_ADC_AC_12V_VS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 792
def SALGetSignal_COMTxSignal_AM_DIAG_006():
    return SALComGetSignal_COMTxSignal_AM_DIAG_006

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 299
SALGetSignalSize_Signal_GridEval_AC_L2_IS_RMS = sizeof(SAL_App_Signal_GridEval_AC_L2_IS_RMS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 551
SALGetSigGroupRef_TstMan_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 298
def SALGetSignal_Signal_GridEval_AC_L2_IS_RMS():
    return SAL_App_Signal_GridEval_AC_L2_IS_RMS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 850
def SALGetSignal_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MAX_VALUE():
    return SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MAX_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1103
SALGetSignalSize_Signal_Calib_HWMON_BULK_CAPACITORS_OV = sizeof(SAL_App_Signal_Calib_HWMON_BULK_CAPACITORS_OV)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 42
def SALGetSignal_Signal_ADC_AC_L2PF_VS_S2():
    return SALIoHwAb_ADC_IF_ADC_B12_SOC3_S2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 617
def SALGetSignal_COMTxSignal_AM_DIAG_031():
    return SALComGetSignal_COMTxSignal_AM_DIAG_031

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 239
SALGetSignalSize_Signal_GridEval_AC_L1_V_POS_PK = sizeof(SAL_App_Signal_GridEval_AC_L1_V_POS_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 831
SALGetSignalSize_Signal_Calib_STMAN_V2L_AC_STABILIZATION_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_V2L_AC_STABILIZATION_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1086
def SALGetSignal_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_CURRENTDELTA():
    return SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_CURRENTDELTA

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1391
SALGetSigGroupRef_Meas_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 526
def SALGetSignal_COMTxSignal_AM_DIAG_044():
    return SALComGetSignal_COMTxSignal_AM_DIAG_044

struct_anon_2.__slots__ = [
    'member',
]
struct_anon_2._fields_ = [
    ('member', uint8),
]

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 209
SALGetSigGroupRef_HwCfg_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 838
def SALGetSignal_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA1():
    return SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1091
SALGetSignalSize_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_VOLTAGEDELTA = sizeof(SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_VOLTAGEDELTA)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 29
SALGetSigGroupRef_ComE2E_FaultGroup = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 520
def SALGetSignal_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LC_IS():
    return SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LC_IS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 757
SALGetSignalSize_Flag_Signal_CCP = sizeof(SAL_App_Flag_Signal_CCP)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1361
def SALGetSignalArray_Signal_Calib_DERAT_MOSFET_LC_WORK_COEF(index):
    return (SAL_App_Signal_Calib_DERAT_MOSFET_LC_WORK_COEF [index])

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 407
def SALGetSignal_COMTxSignal_AM_DIAG_059():
    return SALComGetSignal_COMTxSignal_AM_DIAG_059

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 185
SALGetSignalSize_Signal_StMan_ST_AC_N_RD = sizeof(SAL_App_Signal_StMan_ST_AC_N_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 803
SALGetSignalSize_Signal_Calib_STMAN_G2V_PREPARE_TO_RUN_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PREPARE_TO_RUN_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1058
def SALGetSignal_Signal_Calib_HWMON_AC_L1_V_RMS_UV_QT():
    return SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_UV_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1387
def SALGetSignal_COMRxSignal_MA_V2X_V():
    return SALComGetSignal_COMRxSignal_MA_V2X_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 501
SALGetSignalSize_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LA_IS = sizeof(SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LA_IS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 743
SALGetSigGroupRef_GridEval_TstMan_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1366
def SALGetSignalArray_Signal_Calib_DERAT_RELAY_TEMP_VALUES(index):
    return (SAL_App_Signal_Calib_DERAT_RELAY_TEMP_VALUES [index])

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 428
def SALGetSignal_COMTxSignal_AM_E2E_CRC_01():
    return SALComGetSignal_COMTxSignal_AM_E2E_CRC_01

SAL_ESyncWriteCbkPtrType = CFUNCTYPE(UNCHECKED(Std_ReturnType), POINTER(None))
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 157

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 199
SALGetSigGroupRef_ClaIf_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1268
def SALGetSignal_COMRxSignal_MA_E2E_CNT_02():
    return SALComGetSignal_COMRxSignal_MA_E2E_CNT_02

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 508
def SALGetSignal_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LC_IS():
    return SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LC_IS

SAL_TEST_ARRAY = struct_anon_2
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 26

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 747
SALGetSignalSize_TstMan_GridEval_Signal_GRID_NO_OF_PH = sizeof(SAL_App_TstMan_GridEval_Signal_GRID_NO_OF_PH)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1351
def SALGetSignalArray_Signal_Calib_DERAT_MOSFET_LA_WORK_COEF(index):
    return (SAL_App_Signal_Calib_DERAT_MOSFET_LA_WORK_COEF [index])

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 365
def SALGetSignal_COMTxSignal_AM_DIAG_065():
    return SALComGetSignal_COMTxSignal_AM_DIAG_065

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1019
SALGetSignalSize_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_THRESHOLD = sizeof(SAL_App_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1274
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MAX():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 173
SALGetSignalSize_Signal_StMan_ST_AC_L1L2_RD = sizeof(SAL_App_Signal_StMan_ST_AC_L1L2_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1177
def SALGetSignal_COMTxSignal_AM_VERSION_YEAR():
    return SALComGetSignal_COMTxSignal_AM_VERSION_YEAR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 473
SALGetSignalSize_Signal_PComp_PFC3PhaseCurrBMesFactor = sizeof(SAL_App_Signal_PComp_PFC3PhaseCurrBMesFactor)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 716
def SALGetSignal_TstMan_StMan_Signal_ST_AC_L3_RD():
    return SAL_App_TstMan_StMan_Signal_ST_AC_L3_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1298
def SALGetSignal_Signal_Calib_HWMON_AFE_DCLINKVOLTREF_THRESHOLD():
    return SAL_App_Signal_Calib_HWMON_AFE_DCLINKVOLTREF_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 162
def SALGetSignal_COMTxSignal_AM_DIAG_094():
    return SALComGetSignal_COMTxSignal_AM_DIAG_094

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1026
def SALGetSignal_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_TMAX():
    return SAL_App_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_TMAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1279
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 142
def SALGetSignal_Dem_Fault9():
    return SAL_App_Dem_Fault9

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1226
def SALGetSignal_COMTxSignal_AM_ODD_B3():
    return SALComGetSignal_COMTxSignal_AM_ODD_B3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 450
def SALGetSignal_Signal_GridEval_PhaseDetection_Check01():
    return SAL_App_Signal_GridEval_PhaseDetection_Check01

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 691
SALGetSignalSize_TstMan_PComp_Signal_AC_DSP_3V3_1_Value = sizeof(SAL_App_TstMan_PComp_Signal_AC_DSP_3V3_1_Value)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1007
SALGetSignalSize_Signal_Calib_RELACT_STATE_DELAY_ZERO_CROSS_TIME = sizeof(SAL_App_Signal_Calib_RELACT_STATE_DELAY_ZERO_CROSS_TIME)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1262
def SALGetSignal_Signal_Calib_HWMON_AC_FLY_TEMP_DQ():
    return SAL_App_Signal_Calib_HWMON_AC_FLY_TEMP_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 85
SALGetSignalSize_Signal_Com_MA_V2X_InvalidValue_Fault = sizeof(SAL_App_Signal_Com_MA_V2X_InvalidValue_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1135
def SALGetSignal_COMTxSignal_AM_VERSION_MINUTE():
    return SALComGetSignal_COMTxSignal_AM_VERSION_MINUTE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 399
SALGetSignalSize_Signal_GridEval_AC_L3L1_V_RMS = sizeof(SAL_App_Signal_GridEval_AC_L3L1_V_RMS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 644
def SALGetSignal_TstMan_RelAct_Signal_PWM_AC_L1L2_RD():
    return SAL_App_TstMan_RelAct_Signal_PWM_AC_L1L2_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 950
def SALGetSignal_Signal_Calib_GRIDEVAL_3PH_LINETOLINERMSVOLTAGE_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_3PH_LINETOLINERMSVOLTAGE_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1203
SALGetSignalSize_Signal_Calib_HWMON_AC_DSP_3V3_1_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AC_DSP_3V3_1_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 70
def SALGetSignal_Signal_NM_FAULT_BUSS_OFF():
    return SAL_App_Signal_NM_FAULT_BUSS_OFF

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1411
for _lib in _libs.values():
    if not hasattr(_lib, 'SAL_NvM_SetDataIndex'):
        continue
    SAL_NvM_SetDataIndex = _lib.SAL_NvM_SetDataIndex
    SAL_NvM_SetDataIndex.argtypes = [SAL_NvM_BlockIdType, uint8]
    SAL_NvM_SetDataIndex.restype = None
    break

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 134
def SALGetSignal_COMTxSignal_AM_DIAG_098():
    return SALComGetSignal_COMTxSignal_AM_DIAG_098

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 374
def SALGetSignal_Signal_GridEval_AC_L3L1_V_NEG_PK():
    return SAL_App_Signal_GridEval_AC_L3L1_V_NEG_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 619
SALGetSignalSize_Signal_RelAct_RelayType = sizeof(SAL_App_Signal_RelAct_RelayType)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1023
def SALGetSignal_COMTxSignal_AM_AC_PH_2_RMS_V():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_2_RMS_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 915
SALGetSignalSize_Signal_Calib_GRIDEVAL_PHASECHECK_VOLTAGE_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_PHASECHECK_VOLTAGE_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1170
def SALGetSignal_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_VFACTOR():
    return SAL_App_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_VFACTOR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 188
def SALGetSignal_Signal_DIO_AFE_LB_DRV_PS_PG():
    return SALIoHwAb_DIO_AFE_LB_DRV_PS_PG

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 820
def SALGetSignal_COMTxSignal_AM_DIAG_002():
    return SALComGetSignal_COMTxSignal_AM_DIAG_002

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 339
SALGetSignalSize_Signal_GridEval_AC_L3_ZC_Max_Counter = sizeof(SAL_App_Signal_GridEval_AC_L3_ZC_Max_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 590
def SALGetSignal_Signal_TstMan_Mode_HwMon():
    return SAL_App_Signal_TstMan_Mode_HwMon

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 890
def SALGetSignal_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MIN_VALUE():
    return SAL_App_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MIN_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1143
SALGetSignalSize_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 142
def SALGetSignal_Signal_ADC_AFE_TEMP_LA():
    return SALIoHwAb_ADC_AFE_TEMP_LA

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 757
def SALGetSignal_COMTxSignal_AM_DIAG_011():
    return SALComGetSignal_COMTxSignal_AM_DIAG_011

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 346
def SALGetSignal_Signal_GridEval_AC_L1L2_V_POS_PK():
    return SAL_App_Signal_GridEval_AC_L1L2_V_POS_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 279
SALGetSignalSize_Signal_GridEval_AC_L3_dV_PK = sizeof(SAL_App_Signal_GridEval_AC_L3_dV_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 903
SALGetSignalSize_Signal_Calib_HWCFG_1PH_3_6_KW_SYS_11KW_IS_MAX = sizeof(SAL_App_Signal_Calib_HWCFG_1PH_3_6_KW_SYS_11KW_IS_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1158
def SALGetSignal_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MIN():
    return SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 157
def SALGetSignal_Signal_ADC_AC_1_65V_VS():
    return SALIoHwAb_ADC_AC_1_65V_VS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 778
def SALGetSignal_COMTxSignal_AM_DIAG_008():
    return SALComGetSignal_COMTxSignal_AM_DIAG_008

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 327
SALGetSignalSize_Signal_GridEval_AC_L3_ZC_Counter = sizeof(SAL_App_Signal_GridEval_AC_L3_ZC_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 578
def SALGetSignal_Signal_TstMan_Mode_Cla():
    return SAL_App_Signal_TstMan_Mode_Cla

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 246
def SALGetSignal_Signal_GridEval_AC_L2_V_PK():
    return SAL_App_Signal_GridEval_AC_L2_V_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 878
def SALGetSignal_Signal_Calib_STMAN_V2L_DCLINK_MARGIN():
    return SAL_App_Signal_Calib_STMAN_V2L_DCLINK_MARGIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1131
SALGetSignalSize_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 72
def SALGetSignal_Signal_ADC_AFE_LA_IS_S2():
    return SALIoHwAb_ADC_AFE_LA_IS_S2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 659
def SALGetSignal_COMTxSignal_AM_DIAG_025():
    return SALComGetSignal_COMTxSignal_AM_DIAG_025

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 251
SALGetSignalSize_Signal_GridEval_AC_L2_V_POS_PK = sizeof(SAL_App_Signal_GridEval_AC_L2_V_POS_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 843
SALGetSignalSize_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA2 = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA2)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1098
def SALGetSignal_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_CURRENTDELTA():
    return SAL_App_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_CURRENTDELTA

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 568
def SALGetSignal_COMTxSignal_AM_DIAG_038():
    return SALComGetSignal_COMTxSignal_AM_DIAG_038

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 234
def SALGetSignal_Signal_GridEval_AC_L1_V_PK():
    return SAL_App_Signal_GridEval_AC_L1_V_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1408
def SALGetSignal_COMRxSignal_MA_ODD_CNT():
    return SALComGetSignal_COMRxSignal_MA_ODD_CNT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 56
def SALGetSignal_Signal_ComE2E_MA_MCMP_Checksum_Fault():
    return SAL_App_Signal_ComE2E_MA_MCMP_Checksum_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 548
def SALGetSignal_Signal_PComp_IsReady():
    return SAL_App_Signal_PComp_IsReady

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 783
SALGetSignalSize_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_TWO_PHASES_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_TWO_PHASES_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1359
def SALGetSignal_Signal_Calib_DERAT_MOSFET_LC_WORK_COEF():
    return SAL_App_Signal_Calib_DERAT_MOSFET_LC_WORK_COEF

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 393
def SALGetSignal_COMTxSignal_AM_DIAG_061():
    return SALComGetSignal_COMTxSignal_AM_DIAG_061

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 181
SALGetSignalSize_Signal_StMan_ST_AC_L3_RD = sizeof(SAL_App_Signal_StMan_ST_AC_L3_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 513
SALGetSignalSize_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LA_IS = sizeof(SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LA_IS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 753
SALGetSigGroupRef_CCP_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1336
def SALGetSignalArray_Signal_Calib_DERAT_VIN_VALUES(index):
    return (SAL_App_Signal_Calib_DERAT_VIN_VALUES [index])

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 302
def SALGetSignal_COMTxSignal_AM_DIAG_074():
    return SALComGetSignal_COMTxSignal_AM_DIAG_074

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 149
SALGetSigGroupRef_StMan_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1366
def SALGetSignal_COMRxSignal_MA_V2X_MAX_P():
    return SALComGetSignal_COMRxSignal_MA_V2X_MAX_P

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 456
def SALGetSignal_Signal_PComp_PFC3PhaseCurrAMesOffset():
    return SAL_App_Signal_PComp_PFC3PhaseCurrAMesOffset

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1303
SALGetSignalSize_Signal_Calib_PCOMP_ZERO_CURRENT_VS_X_NO_OF_SAMPLES = sizeof(SAL_App_Signal_Calib_PCOMP_ZERO_CURRENT_VS_X_NO_OF_SAMPLES)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 183
def SALGetSignal_COMTxSignal_AM_DIAG_091():
    return SALComGetSignal_COMTxSignal_AM_DIAG_091

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1015
SALGetSignalSize_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_MAX_ERROR = sizeof(SAL_App_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_MAX_ERROR)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1270
def SALGetSignal_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MIN():
    return SAL_App_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 123
SALGetSignalSize_Dem_Fault4 = sizeof(SAL_App_Dem_Fault4)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1163
def SALGetSignal_COMTxSignal_AM_VERSION_MINOR():
    return SALComGetSignal_COMTxSignal_AM_VERSION_MINOR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 439
SALGetSignalSize_Signal_GridEval_AC_L1L2_PhaseDegree = sizeof(SAL_App_Signal_GridEval_AC_L1L2_PhaseDegree)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 682
def SALGetSignal_TstMan_PComp_Signal_PFC3PhaseVoltMesFactor_Value():
    return SAL_App_TstMan_PComp_Signal_PFC3PhaseVoltMesFactor_Value

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1310
def SALGetSignal_Signal_Calib_PCOMP_AFE_CURRENT_LA_SENSORGAIN_VALUE():
    return SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LA_SENSORGAIN_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 204
def SALGetSignal_COMTxSignal_AM_DIAG_088():
    return SALComGetSignal_COMTxSignal_AM_DIAG_088

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 990
def SALGetSignal_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMAX_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMAX_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1243
SALGetSignalSize_Signal_Calib_HWMON_AC_FLY_TEMP_QT = sizeof(SAL_App_Signal_Calib_HWMON_AC_FLY_TEMP_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 138
def SALGetSignal_Dem_Fault8():
    return SAL_App_Dem_Fault8

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1044
def SALGetSignal_COMTxSignal_AM_AC_PH_2_RMS_I():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_2_RMS_I

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 446
def SALGetSignal_Signal_GridEval_AC_L2L3_PhaseDegree():
    return SAL_App_Signal_GridEval_AC_L2L3_PhaseDegree

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 687
SALGetSignalSize_TstMan_PComp_Signal_PFC3PDCLinkVoltMesFactor_Value = sizeof(SAL_App_TstMan_PComp_Signal_PFC3PDCLinkVoltMesFactor_Value)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 955
SALGetSignalSize_Signal_Calib_GRIDEVAL_3PH_LINERMSVOLTAGE_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_3PH_LINERMSVOLTAGE_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1210
def SALGetSignal_Signal_Calib_HWMON_AC_1_65V_VS_MAX():
    return SAL_App_Signal_Calib_HWMON_AC_1_65V_VS_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 111
SALGetSignalSize_Dem_Fault1 = sizeof(SAL_App_Dem_Fault1)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 71
def SALGetSignal_COMTxSignal_AM_DIAG_107():
    return SALComGetSignal_COMTxSignal_AM_DIAG_107

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 960
def SALGetSignal_COMTxSignal_AM_CAP_V():
    return SALComGetSignal_COMTxSignal_AM_CAP_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 411
SALGetSignalSize_Signal_GridEval_AC_L3L1_ZC_Counter = sizeof(SAL_App_Signal_GridEval_AC_L3L1_ZC_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 654
def SALGetSignal_TstMan_PComp_Signal_IsReady():
    return SAL_App_TstMan_PComp_Signal_IsReady

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 962
def SALGetSignal_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK02_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK02_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1215
SALGetSignalSize_Signal_Calib_HWMON_AC_L1_FUSE_BLOWN_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AC_L1_FUSE_BLOWN_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 80
def SALGetSignal_Signal_Com_MA_POWER_Monitoring_Fault():
    return SAL_App_Signal_Com_MA_POWER_Monitoring_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 120
def SALGetSignal_COMTxSignal_AM_DIAG_100():
    return SALComGetSignal_COMTxSignal_AM_DIAG_100

SAL_TEST = struct_anon_1
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 21

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 386
def SALGetSignal_Signal_GridEval_AC_L3L1_dV_PK():
    return SAL_App_Signal_GridEval_AC_L3L1_dV_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 629
SALGetSignalSize_TstMan_RelAct_Signal_PWM_AC_N_RD = sizeof(SAL_App_TstMan_RelAct_Signal_PWM_AC_N_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1009
def SALGetSignal_COMTxSignal_AM_E2E_CNT_04():
    return SALComGetSignal_COMTxSignal_AM_E2E_CNT_04

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 943
SALGetSignalSize_Signal_Calib_GRIDEVAL_PH_DELTAPEAKVOLTAGE_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_PH_DELTAPEAKVOLTAGE_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1198
def SALGetSignal_Signal_Calib_HWMON_AC_DSP_3V3_1_MIN():
    return SAL_App_Signal_Calib_HWMON_AC_DSP_3V3_1_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 29
def SALGetSignal_COMTxSignal_AM_E2E_CNT_10():
    return SALComGetSignal_COMTxSignal_AM_E2E_CNT_10

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 918
def SALGetSignal_COMTxSignal_AM_REL_T():
    return SALComGetSignal_COMTxSignal_AM_REL_T

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 335
SALGetSignalSize_Signal_GridEval_AC_L2_ZC_Max_Counter = sizeof(SAL_App_Signal_GridEval_AC_L2_ZC_Max_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 586
def SALGetSignal_Signal_TstMan_Mode_GridEval():
    return SAL_App_Signal_TstMan_Mode_GridEval

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 886
def SALGetSignal_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MAX_VALUE():
    return SAL_App_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MAX_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1139
SALGetSignalSize_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 172
def SALGetSignal_Signal_ADC_AFE_SITE_ID():
    return SALIoHwAb_ADC_AFE_SITE_ID

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 799
def SALGetSignal_COMTxSignal_AM_DIAG_005():
    return SALComGetSignal_COMTxSignal_AM_DIAG_005

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 310
def SALGetSignal_Signal_GridEval_AC_L2_FREQ():
    return SAL_App_Signal_GridEval_AC_L2_FREQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 559
SALGetSignalSize_Signal_TstMan_Disable_SwSec = sizeof(SAL_App_Signal_TstMan_Disable_SwSec)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 291
SALGetSignalSize_Signal_GridEval_AC_L3_V_RMS = sizeof(SAL_App_Signal_GridEval_AC_L3_V_RMS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 851
SALGetSignalSize_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MAX_VALUE = sizeof(SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MAX_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1106
def SALGetSignal_Signal_Calib_HWMON_BULK_CAPACITORS_UV():
    return SAL_App_Signal_Calib_HWMON_BULK_CAPACITORS_UV

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 27
def SALGetSignal_Signal_ADC_AC_L1PF_VS_1PH_S1():
    return SALIoHwAb_ADC_IF_ADC_A2_SOC2_S1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 596
def SALGetSignal_COMTxSignal_AM_DIAG_034():
    return SALComGetSignal_COMTxSignal_AM_DIAG_034

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 242
def SALGetSignal_Signal_GridEval_AC_L1_V_NEG_PK():
    return SAL_App_Signal_GridEval_AC_L1_V_NEG_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 826
def SALGetSignal_Signal_Calib_STMAN_V2L_AC_SOFTSTART_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_V2L_AC_SOFTSTART_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1079
SALGetSignalSize_Signal_Calib_HWMON_AC_L3_V_RMS_UV_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_UV_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 533
def SALGetSignal_COMTxSignal_AM_DIAG_043():
    return SALComGetSignal_COMTxSignal_AM_DIAG_043

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 217
SALGetSignalSize_Signal_HwCfg_AFE_LB_IS_MaxCurrent = sizeof(SAL_App_Signal_HwCfg_AFE_LB_IS_MaxCurrent)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 839
SALGetSignalSize_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA1 = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA1)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1094
def SALGetSignal_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_TEMPDELTA():
    return SAL_App_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_TEMPDELTA

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 521
SALGetSignalSize_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LC_IS = sizeof(SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LC_IS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 759
SALGetSigGroupRef_Calib_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1398
def SALGetSignal_Signal_Meas_AC_12_VS():
    return SAL_App_Signal_Meas_AC_12_VS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 554
def SALGetSignal_COMTxSignal_AM_DIAG_040():
    return SALComGetSignal_COMTxSignal_AM_DIAG_040

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 188
def SALGetSignal_Signal_StMan_ST_AFE_L3_RD():
    return SAL_App_Signal_StMan_ST_AFE_L3_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 814
def SALGetSignal_Signal_Calib_STMAN_G2V_CHARGE_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_CHARGE_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1067
SALGetSignalSize_Signal_Calib_HWMON_AC_L3_V_RMS_UV_QT = sizeof(SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_UV_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1394
def SALGetSignal_COMRxSignal_MA_V2X_F():
    return SALComGetSignal_COMRxSignal_MA_V2X_F

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 496
def SALGetSignal_Signal_PComp_AC_DSP_3V3_1():
    return SAL_App_Signal_PComp_AC_DSP_3V3_1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 737
SALGetSignalSize_TstMan_StMan_Signal_AM_OP_MODE_FB = sizeof(SAL_App_TstMan_StMan_Signal_AM_OP_MODE_FB)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1369
def SALGetSignal_Signal_Calib_DERAT_RELAY_WORK_COEF():
    return SAL_App_Signal_Calib_DERAT_RELAY_WORK_COEF

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 435
def SALGetSignal_COMTxSignal_AM_E2E_CNT_01():
    return SALComGetSignal_COMTxSignal_AM_E2E_CNT_01

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 193
SALGetSignalSize_Signal_StMan_PCompDeadTimePassed = sizeof(SAL_App_Signal_StMan_PCompDeadTimePassed)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1303
def SALGetSignal_COMRxSignal_MA_E2E_CNT_01():
    return SALComGetSignal_COMRxSignal_MA_E2E_CNT_01

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 509
SALGetSignalSize_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LC_IS = sizeof(SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LC_IS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 750
def SALGetSignal_TstMan_GridEval_Signal_Operation_Mode():
    return SAL_App_TstMan_GridEval_Signal_Operation_Mode

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1346
def SALGetSignalArray_Signal_Calib_DERAT_MOSFET_TEMP_VALUES(index):
    return (SAL_App_Signal_Calib_DERAT_MOSFET_TEMP_VALUES [index])

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 344
def SALGetSignal_COMTxSignal_AM_DIAG_068():
    return SALComGetSignal_COMTxSignal_AM_DIAG_068

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 176
def SALGetSignal_Signal_StMan_ST_AC_L2_RD():
    return SAL_App_Signal_StMan_ST_AC_L2_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1184
def SALGetSignal_COMTxSignal_AM_VERSION_MONTH():
    return SALComGetSignal_COMTxSignal_AM_VERSION_MONTH

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 484
def SALGetSignal_Signal_PComp_PFC3PDCLinkVoltMesFactor():
    return SAL_App_Signal_PComp_PFC3PDCLinkVoltMesFactor

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 725
SALGetSignalSize_TstMan_StMan_Signal_ST_AC_L2_RD = sizeof(SAL_App_TstMan_StMan_Signal_ST_AC_L2_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1299
SALGetSignalSize_Signal_Calib_HWMON_AFE_DCLINKVOLTREF_THRESHOLD = sizeof(SAL_App_Signal_Calib_HWMON_AFE_DCLINKVOLTREF_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 169
def SALGetSignal_COMTxSignal_AM_DIAG_093():
    return SALComGetSignal_COMTxSignal_AM_DIAG_093

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1027
SALGetSignalSize_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_TMAX = sizeof(SAL_App_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_TMAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1282
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MAX():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 119
SALGetSignalSize_Dem_Fault3 = sizeof(SAL_App_Dem_Fault3)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1205
def SALGetSignal_COMTxSignal_AM_ODD_B0():
    return SALComGetSignal_COMTxSignal_AM_ODD_B0

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 451
SALGetSignalSize_Signal_GridEval_PhaseDetection_Check01 = sizeof(SAL_App_Signal_GridEval_PhaseDetection_Check01)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 694
def SALGetSignal_TstMan_PComp_Signal_ADC_AC_1_65V_VS_Value():
    return SAL_App_TstMan_PComp_Signal_ADC_AC_1_65V_VS_Value

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1002
def SALGetSignal_Signal_Calib_RELACT_STATE_DELAY_ENERGIZE_TIME():
    return SAL_App_Signal_Calib_RELACT_STATE_DELAY_ENERGIZE_TIME

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1255
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LB_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 88
def SALGetSignal_Signal_Com_MA_V2X_Monitoring_Fault():
    return SAL_App_Signal_Com_MA_V2X_Monitoring_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1142
def SALGetSignal_COMTxSignal_AM_VERSION_HOUR():
    return SALComGetSignal_COMTxSignal_AM_VERSION_HOUR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 394
def SALGetSignal_Signal_GridEval_AC_L2L3_V_RMS():
    return SAL_App_Signal_GridEval_AC_L2L3_V_RMS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 637
SALGetSignalSize_TstMan_RelAct_Signal_PWM_AC_L1_RD = sizeof(SAL_App_TstMan_RelAct_Signal_PWM_AC_L1_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 951
SALGetSignalSize_Signal_Calib_GRIDEVAL_3PH_LINETOLINERMSVOLTAGE_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_3PH_LINETOLINERMSVOLTAGE_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1206
def SALGetSignal_Signal_Calib_HWMON_AC_1_65V_VS_MIN():
    return SAL_App_Signal_Calib_HWMON_AC_1_65V_VS_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 57
def SALGetSignal_COMTxSignal_AM_DIAG_109():
    return SALComGetSignal_COMTxSignal_AM_DIAG_109

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 946
def SALGetSignal_COMTxSignal_AM_PH_2_3_ANGLE():
    return SALComGetSignal_COMTxSignal_AM_PH_2_3_ANGLE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 375
SALGetSignalSize_Signal_GridEval_AC_L3L1_V_NEG_PK = sizeof(SAL_App_Signal_GridEval_AC_L3L1_V_NEG_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 622
def SALGetSignal_Signal_RelAct_RelayStatus():
    return SAL_App_Signal_RelAct_RelayStatus

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 926
def SALGetSignal_Signal_Calib_GRIDEVAL_TIMERTIMEOUT_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_TIMERTIMEOUT_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1179
SALGetSignalSize_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_VFACTOR = sizeof(SAL_App_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_VFACTOR)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 76
def SALGetSignal_Signal_Com_MA_POWER_InvalidValue_Fault():
    return SAL_App_Signal_Com_MA_POWER_InvalidValue_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 193
def SALGetSignal_Signal_DIO_AFE_LC_DRV_PS_PG():
    return SALIoHwAb_DIO_AFE_LC_DRV_PS_PG

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 827
def SALGetSignal_COMTxSignal_AM_DIAG_001():
    return SALComGetSignal_COMTxSignal_AM_DIAG_001

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 382
def SALGetSignal_Signal_GridEval_AC_L2L3_dV_PK():
    return SAL_App_Signal_GridEval_AC_L2L3_dV_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 891
SALGetSignalSize_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MIN_VALUE = sizeof(SAL_App_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MIN_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1146
def SALGetSignal_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MAX():
    return SAL_App_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 127
def SALGetSignal_Signal_ADC_AC_DSP_3V3_S2():
    return SALIoHwAb_ADC_AC_DSP_3V3_S2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 736
def SALGetSignal_COMTxSignal_AM_DIAG_014():
    return SALComGetSignal_COMTxSignal_AM_DIAG_014

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 347
SALGetSignalSize_Signal_GridEval_AC_L1L2_V_POS_PK = sizeof(SAL_App_Signal_GridEval_AC_L1L2_V_POS_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 596
def SALGetSignal_Signal_AC_RLY_TEMP():
    return SAL_App_Signal_AC_RLY_TEMP

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 282
def SALGetSignal_Signal_GridEval_AC_L1_V_RMS():
    return SAL_App_Signal_GridEval_AC_L1_V_RMS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 898
def SALGetSignal_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_22KW_IS_MAX():
    return SAL_App_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_22KW_IS_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1151
SALGetSignalSize_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 162
def SALGetSignal_Signal_ADC_AC_FLY_TEMP():
    return SALIoHwAb_ADC_AC_FLY_TEMP

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 785
def SALGetSignal_COMTxSignal_AM_DIAG_007():
    return SALComGetSignal_COMTxSignal_AM_DIAG_007

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 322
def SALGetSignal_Signal_GridEval_AC_L2_ZC_Counter():
    return SAL_App_Signal_GridEval_AC_L2_ZC_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 571
SALGetSignalSize_Signal_TstMan_Mode_PComp = sizeof(SAL_App_Signal_TstMan_Mode_PComp)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 287
SALGetSignalSize_Signal_GridEval_AC_L2_V_RMS = sizeof(SAL_App_Signal_GridEval_AC_L2_V_RMS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 879
SALGetSignalSize_Signal_Calib_STMAN_V2L_DCLINK_MARGIN = sizeof(SAL_App_Signal_Calib_STMAN_V2L_DCLINK_MARGIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1134
def SALGetSignal_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MIN():
    return SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MIN

SAL_TEST6 = struct_anon_7
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 61

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 97
def SALGetSignal_Signal_ADC_AC_AFE_VOUT_VS_S1():
    return SALIoHwAb_ADC_AC_AFE_VOUT_VS_S1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 694
def SALGetSignal_COMTxSignal_AM_DIAG_020():
    return SALComGetSignal_COMTxSignal_AM_DIAG_020

struct_anon_3.__slots__ = [
    'member3',
    'member2',
    'member1',
]
struct_anon_3._fields_ = [
    ('member3', uint32),
    ('member2', uint8, 6),
    ('member1', uint8, 2),
]

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 254
def SALGetSignal_Signal_GridEval_AC_L2_V_NEG_PK():
    return SAL_App_Signal_GridEval_AC_L2_V_NEG_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 822
def SALGetSignal_Signal_Calib_STMAN_V2L_PREPARE_TO_RUN_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_V2L_PREPARE_TO_RUN_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1075
SALGetSignalSize_Signal_Calib_HWMON_AC_L2_V_RMS_UV_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_UV_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 575
def SALGetSignal_COMTxSignal_AM_DIAG_037():
    return SALComGetSignal_COMTxSignal_AM_DIAG_037

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 227
SALGetSignalSize_Signal_GridEval_GRID_NO_OF_PH = sizeof(SAL_App_Signal_GridEval_GRID_NO_OF_PH)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 787
SALGetSignalSize_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_THREE_PHASES_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_THREE_PHASES_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1042
def SALGetSignal_Signal_Calib_HWMON_AC_L3_V_RMS_OV_QT():
    return SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_OV_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1002
def SALGetSignal_COMTxSignal_AM_AC_PH_1_RMS_I():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_1_RMS_I

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 57
SALGetSignalSize_Signal_ComE2E_MA_MCMP_Checksum_Fault = sizeof(SAL_App_Signal_ComE2E_MA_MCMP_Checksum_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 549
SALGetSignalSize_Signal_PComp_IsReady = sizeof(SAL_App_Signal_PComp_IsReady)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 786
def SALGetSignal_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_THREE_PHASES_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_THREE_PHASES_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1354
def SALGetSignal_Signal_Calib_DERAT_MOSFET_LB_WORK_COEF():
    return SAL_App_Signal_Calib_DERAT_MOSFET_LB_WORK_COEF

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 372
def SALGetSignal_COMTxSignal_AM_DIAG_064():
    return SALComGetSignal_COMTxSignal_AM_DIAG_064

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 184
def SALGetSignal_Signal_StMan_ST_AC_N_RD():
    return SAL_App_Signal_StMan_ST_AC_N_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 636
def SALGetSignal_TstMan_RelAct_Signal_PWM_AC_L1_RD():
    return SAL_App_TstMan_RelAct_Signal_PWM_AC_L1_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 492
def SALGetSignal_Signal_PComp_ADC_AC_1_65V_VS():
    return SAL_App_Signal_PComp_ADC_AC_1_65V_VS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 733
SALGetSignalSize_TstMan_StMan_Signal_STMAN_STATE = sizeof(SAL_App_TstMan_StMan_Signal_STMAN_STATE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1339
def SALGetSignal_Signal_Calib_DERAT_VIN_WORK_COEF():
    return SAL_App_Signal_Calib_DERAT_VIN_WORK_COEF

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 309
def SALGetSignal_COMTxSignal_AM_DIAG_073():
    return SALComGetSignal_COMTxSignal_AM_DIAG_073

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 157
SALGetSignalSize_Signal_StMan_PFCOpState = sizeof(SAL_App_Signal_StMan_PFCOpState)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1345
def SALGetSignal_COMRxSignal_MA_ACT_P_PH1():
    return SALComGetSignal_COMRxSignal_MA_ACT_P_PH1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 457
SALGetSignalSize_Signal_PComp_PFC3PhaseCurrAMesOffset = sizeof(SAL_App_Signal_PComp_PFC3PhaseCurrAMesOffset)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 700
def SALGetSignal_TstMan_StMan_Signal_PCompSamplingMode():
    return SAL_App_TstMan_StMan_Signal_PCompSamplingMode

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1344
def SALGetSignal_Signal_Calib_DERAT_MOSFET_TEMP_VALUES():
    return SAL_App_Signal_Calib_DERAT_MOSFET_TEMP_VALUES

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 330
def SALGetSignal_COMTxSignal_AM_DIAG_070():
    return SALComGetSignal_COMTxSignal_AM_DIAG_070

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1010
def SALGetSignal_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_THRESHOLD():
    return SAL_App_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1263
SALGetSignalSize_Signal_Calib_HWMON_AC_FLY_TEMP_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AC_FLY_TEMP_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 126
def SALGetSignal_Dem_Fault5():
    return SAL_App_Dem_Fault5

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1170
def SALGetSignal_COMTxSignal_AM_VERSION_MAJOR():
    return SALComGetSignal_COMTxSignal_AM_VERSION_MAJOR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 434
def SALGetSignal_Signal_GridEval_AC_L3_REACTIVE_PWR():
    return SAL_App_Signal_GridEval_AC_L3_REACTIVE_PWR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 675
SALGetSignalSize_TstMan_PComp_Signal_PFC3PhaseCurrBMesFactor_Value = sizeof(SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrBMesFactor_Value)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1311
SALGetSignalSize_Signal_Calib_PCOMP_AFE_CURRENT_LA_SENSORGAIN_VALUE = sizeof(SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LA_SENSORGAIN_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 211
def SALGetSignal_COMTxSignal_AM_DIAG_087():
    return SALComGetSignal_COMTxSignal_AM_DIAG_087

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 991
SALGetSignalSize_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMAX_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMAX_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1246
def SALGetSignal_Signal_Calib_HWMON_AC_RLY_TEMP_DQ():
    return SAL_App_Signal_Calib_HWMON_AC_RLY_TEMP_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 131
SALGetSignalSize_Dem_Fault6 = sizeof(SAL_App_Dem_Fault6)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1079
def SALGetSignal_COMTxSignal_AM_AC_PH_3_F():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_3_F

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 447
SALGetSignalSize_Signal_GridEval_AC_L2L3_PhaseDegree = sizeof(SAL_App_Signal_GridEval_AC_L2L3_PhaseDegree)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 690
def SALGetSignal_TstMan_PComp_Signal_AC_DSP_3V3_1_Value():
    return SAL_App_TstMan_PComp_Signal_AC_DSP_3V3_1_Value

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 998
def SALGetSignal_Signal_Calib_GRIDEVAL_V2L_LINERMSVOLTAGE_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_V2L_LINERMSVOLTAGE_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1251
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LA_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 114
def SALGetSignal_Dem_Fault2():
    return SAL_App_Dem_Fault2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 78
def SALGetSignal_COMTxSignal_AM_DIAG_106():
    return SALComGetSignal_COMTxSignal_AM_DIAG_106

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 967
def SALGetSignal_COMTxSignal_AM_E2E_CNT_03():
    return SALComGetSignal_COMTxSignal_AM_E2E_CNT_03

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 422
def SALGetSignal_Signal_GridEval_AC_L3L1_ZC_Max_Counter():
    return SAL_App_Signal_GridEval_AC_L3L1_ZC_Max_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 663
SALGetSignalSize_TstMan_PComp_Signal_PFC3PhaseCurrBMesOffset_Value = sizeof(SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrBMesOffset_Value)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 963
SALGetSignalSize_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK02_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK02_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1218
def SALGetSignal_Signal_Calib_HWMON_AC_L2_FUSE_BLOWN_MAX():
    return SAL_App_Signal_Calib_HWMON_AC_L2_FUSE_BLOWN_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 61
SALGetSignalSize_Signal_ComE2E_MA_MCMP_Counter_Fault = sizeof(SAL_App_Signal_ComE2E_MA_MCMP_Counter_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 99
def SALGetSignal_COMTxSignal_AM_DIAG_103():
    return SALComGetSignal_COMTxSignal_AM_DIAG_103

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 988
def SALGetSignal_COMTxSignal_AM_AC_PH_1_PK_V():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_1_PK_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 387
SALGetSignalSize_Signal_GridEval_AC_L3L1_dV_PK = sizeof(SAL_App_Signal_GridEval_AC_L3L1_dV_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 632
def SALGetSignal_TstMan_RelAct_Signal_PWM_AFE_L3_RD():
    return SAL_App_TstMan_RelAct_Signal_PWM_AFE_L3_RD

struct_anon_1.__slots__ = [
    'member',
]
struct_anon_1._fields_ = [
    ('member', uint8),
]

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 938
def SALGetSignal_Signal_Calib_GRIDEVAL_PH_PEAKVOLTAGE_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_PH_PEAKVOLTAGE_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1191
SALGetSignalSize_Signal_Calib_HWMON_AC_12V_TH_LOW_QT = sizeof(SAL_App_Signal_Calib_HWMON_AC_12V_TH_LOW_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 36
def SALGetSignal_COMTxSignal_AM_DIAG_112():
    return SALComGetSignal_COMTxSignal_AM_DIAG_112

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 925
def SALGetSignal_COMTxSignal_AM_E2E_CNT_02():
    return SALComGetSignal_COMTxSignal_AM_E2E_CNT_02

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 330
def SALGetSignal_Signal_GridEval_AC_L1_ZC_Max_Counter():
    return SAL_App_Signal_GridEval_AC_L1_ZC_Max_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 579
SALGetSignalSize_Signal_TstMan_Mode_Cla = sizeof(SAL_App_Signal_TstMan_Mode_Cla)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 887
SALGetSignalSize_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MAX_VALUE = sizeof(SAL_App_Signal_Calib_STMAN_V2L_AC_PEAK_ONE_PHASE_MAX_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1142
def SALGetSignal_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MIN():
    return SAL_App_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 117
def SALGetSignal_Signal_ADC_AC_L3_VS():
    return SALIoHwAb_ADC_AC_L3_VS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 722
def SALGetSignal_COMTxSignal_AM_DIAG_016():
    return SALComGetSignal_COMTxSignal_AM_DIAG_016

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 311
SALGetSignalSize_Signal_GridEval_AC_L2_FREQ = sizeof(SAL_App_Signal_GridEval_AC_L2_FREQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 562
def SALGetSignal_Signal_TstMan_Disable_WdgM():
    return SAL_App_Signal_TstMan_Disable_WdgM

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 294
def SALGetSignal_Signal_GridEval_AC_L1_IS_RMS():
    return SAL_App_Signal_GridEval_AC_L1_IS_RMS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 862
def SALGetSignal_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MIN_VALUE():
    return SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MIN_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1115
SALGetSignalSize_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_DT = sizeof(SAL_App_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_DT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 32
def SALGetSignal_Signal_ADC_AC_L1PF_VS_1PH_S2():
    return SALIoHwAb_ADC_IF_ADC_A2_SOC5_S2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 603
def SALGetSignal_COMTxSignal_AM_DIAG_033():
    return SALComGetSignal_COMTxSignal_AM_DIAG_033

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 318
def SALGetSignal_Signal_GridEval_AC_L1_ZC_Counter():
    return SAL_App_Signal_GridEval_AC_L1_ZC_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 567
SALGetSignalSize_Signal_TstMan_Mode_RelAct = sizeof(SAL_App_Signal_TstMan_Mode_RelAct)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 235
SALGetSignalSize_Signal_GridEval_AC_L1_V_PK = sizeof(SAL_App_Signal_GridEval_AC_L1_V_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 827
SALGetSignalSize_Signal_Calib_STMAN_V2L_AC_SOFTSTART_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_V2L_AC_SOFTSTART_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1082
def SALGetSignal_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_TEMPDELTA():
    return SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_TEMPDELTA

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1388
def SALGetSignal_Signal_Derat_AM_DER_MAX_I():
    return SAL_App_Signal_Derat_AM_DER_MAX_I

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 512
def SALGetSignal_COMTxSignal_AM_DIAG_046():
    return SALComGetSignal_COMTxSignal_AM_DIAG_046

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 220
def SALGetSignal_Signal_HwCfg_AFE_LC_IS_MaxCurrent():
    return SAL_App_Signal_HwCfg_AFE_LC_IS_MaxCurrent

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 834
def SALGetSignal_Signal_Calib_STMAN_SHUTDOWN_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_SHUTDOWN_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1087
SALGetSignalSize_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_CURRENTDELTA = sizeof(SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_CURRENTDELTA)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 40
def SALGetSignal_Signal_ComE2E_MA_V2X_Checksum_Fault():
    return SAL_App_Signal_ComE2E_MA_V2X_Checksum_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 532
def SALGetSignal_Signal_PComp_CMPSS2_DACHVAL():
    return SAL_App_Signal_PComp_CMPSS2_DACHVAL

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 767
SALGetSignalSize_Signal_Calib_STMAN_G2V_TO_STANDBY_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_TO_STANDBY_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1399
SALGetSignalSize_Signal_Meas_AC_12_VS = sizeof(SAL_App_Signal_Meas_AC_12_VS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 561
def SALGetSignal_COMTxSignal_AM_DIAG_039():
    return SALComGetSignal_COMTxSignal_AM_DIAG_039

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 815
SALGetSignalSize_Signal_Calib_STMAN_G2V_CHARGE_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_CHARGE_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1070
def SALGetSignal_Signal_Calib_HWMON_AC_L1_V_RMS_UV_DQ():
    return SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_UV_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1373
def SALGetSignal_COMRxSignal_MA_V2X_MAX_I():
    return SALComGetSignal_COMRxSignal_MA_V2X_MAX_I

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 497
SALGetSignalSize_Signal_PComp_AC_DSP_3V3_1 = sizeof(SAL_App_Signal_PComp_AC_DSP_3V3_1)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 740
def SALGetSignal_TstMan_StMan_Signal_NumberOfPhasesConfigured():
    return SAL_App_TstMan_StMan_Signal_NumberOfPhasesConfigured

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1378
def SALGetSignal_Signal_Calib_DERAT_MAXIMUM_OPERATIONAL_TEMP_FLYBACK():
    return SAL_App_Signal_Calib_DERAT_MAXIMUM_OPERATIONAL_TEMP_FLYBACK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 470
def SALGetSignal_COMTxSignal_AM_DIAG_052():
    return SALComGetSignal_COMTxSignal_AM_DIAG_052

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 196
def SALGetSignal_Signal_StMan_DriverPowerUpSeq_InProgress():
    return SAL_App_Signal_StMan_DriverPowerUpSeq_InProgress

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1310
def SALGetSignal_COMRxSignal_MA_REACT_P_PH3():
    return SALComGetSignal_COMRxSignal_MA_REACT_P_PH3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 504
def SALGetSignal_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LB_IS():
    return SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LB_IS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1349
def SALGetSignal_Signal_Calib_DERAT_MOSFET_LA_WORK_COEF():
    return SAL_App_Signal_Calib_DERAT_MOSFET_LA_WORK_COEF

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 351
def SALGetSignal_COMTxSignal_AM_DIAG_067():
    return SALComGetSignal_COMTxSignal_AM_DIAG_067

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 169
SALGetSignalSize_Signal_StMan_ST_AC_L1_RD = sizeof(SAL_App_Signal_StMan_ST_AC_L1_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1331
def SALGetSignal_COMRxSignal_MA_ACT_P_PH3():
    return SALComGetSignal_COMRxSignal_MA_ACT_P_PH3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 485
SALGetSignalSize_Signal_PComp_PFC3PDCLinkVoltMesFactor = sizeof(SAL_App_Signal_PComp_PFC3PDCLinkVoltMesFactor)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 728
def SALGetSignal_TstMan_StMan_Signal_PFCOpState():
    return SAL_App_TstMan_StMan_Signal_PFCOpState

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1038
def SALGetSignal_Signal_Calib_HWMON_AC_L2_V_RMS_OV_QT():
    return SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_OV_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1291
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 122
def SALGetSignal_Dem_Fault4():
    return SAL_App_Dem_Fault4

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1212
def SALGetSignal_COMTxSignal_AM_ODD_B1():
    return SALComGetSignal_COMTxSignal_AM_ODD_B1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 430
def SALGetSignal_Signal_GridEval_AC_L3_ACTIVE_PWR():
    return SAL_App_Signal_GridEval_AC_L3_ACTIVE_PWR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 671
SALGetSignalSize_TstMan_PComp_Signal_PFC3PhaseCurrAMesFactor_Value = sizeof(SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrAMesFactor_Value)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1003
SALGetSignalSize_Signal_Calib_RELACT_STATE_DELAY_ENERGIZE_TIME = sizeof(SAL_App_Signal_Calib_RELACT_STATE_DELAY_ENERGIZE_TIME)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1258
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LC_DQ():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 97
SALGetSignalSize_Signal_Com_MA_REQUEST_OP_Monitoring_Fault = sizeof(SAL_App_Signal_Com_MA_REQUEST_OP_Monitoring_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1121
def SALGetSignal_COMTxSignal_AM_E2E_CNT_07():
    return SALComGetSignal_COMTxSignal_AM_E2E_CNT_07

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 395
SALGetSignalSize_Signal_GridEval_AC_L2L3_V_RMS = sizeof(SAL_App_Signal_GridEval_AC_L2L3_V_RMS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 640
def SALGetSignal_TstMan_RelAct_Signal_PWM_AC_L2_RD():
    return SAL_App_TstMan_RelAct_Signal_PWM_AC_L2_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 946
def SALGetSignal_Signal_Calib_GRIDEVAL_V2L_PEAKVOLTAGE_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_V2L_PEAKVOLTAGE_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1199
SALGetSignalSize_Signal_Calib_HWMON_AC_DSP_3V3_1_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AC_DSP_3V3_1_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 66
def SALGetSignal_Signal_NM_FAULT_ERROR_PASSIVE():
    return SAL_App_Signal_NM_FAULT_ERROR_PASSIVE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 64
def SALGetSignal_COMTxSignal_AM_DIAG_108():
    return SALComGetSignal_COMTxSignal_AM_DIAG_108

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 953
def SALGetSignal_COMTxSignal_AM_PH_1_2_ANGLE():
    return SALComGetSignal_COMTxSignal_AM_PH_1_2_ANGLE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 370
def SALGetSignal_Signal_GridEval_AC_L3L1_V_POS_PK():
    return SAL_App_Signal_GridEval_AC_L3L1_V_POS_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 927
SALGetSignalSize_Signal_Calib_GRIDEVAL_TIMERTIMEOUT_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_TIMERTIMEOUT_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1182
def SALGetSignal_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_IMIN():
    return SAL_App_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_IMIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 71
SALGetSignalSize_Signal_NM_FAULT_BUSS_OFF = sizeof(SAL_App_Signal_NM_FAULT_BUSS_OFF)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 221
def SALGetSignal_Signal_PWM_AC_L1L2_RD():
    return SALIoHwAb_PWM_AC_L1L2_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 862
def SALGetSignal_COMTxSignal_AM_REF_1V65():
    return SALComGetSignal_COMTxSignal_AM_REF_1V65

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 383
SALGetSignalSize_Signal_GridEval_AC_L2L3_dV_PK = sizeof(SAL_App_Signal_GridEval_AC_L2L3_dV_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 628
def SALGetSignal_TstMan_RelAct_Signal_PWM_AC_N_RD():
    return SAL_App_TstMan_RelAct_Signal_PWM_AC_N_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 934
def SALGetSignal_Signal_Calib_GRIDEVAL_MONITORINGTIMEOUT_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_MONITORINGTIMEOUT_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1187
SALGetSignalSize_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_VFACTOR = sizeof(SAL_App_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_VFACTOR)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 132
def SALGetSignal_Signal_ADC_AC_DSP_3V3_S3():
    return SALIoHwAb_ADC_AC_DSP_3V3_S3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 743
def SALGetSignal_COMTxSignal_AM_DIAG_013():
    return SALComGetSignal_COMTxSignal_AM_DIAG_013

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 358
def SALGetSignal_Signal_GridEval_AC_L2L3_V_POS_PK():
    return SAL_App_Signal_GridEval_AC_L2L3_V_POS_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 605
SALGetSignalSize_Signal_AFE_TEMP_LB = sizeof(SAL_App_Signal_AFE_TEMP_LB)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 275
SALGetSignalSize_Signal_GridEval_AC_L2_dV_PK = sizeof(SAL_App_Signal_GridEval_AC_L2_dV_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 899
SALGetSignalSize_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_22KW_IS_MAX = sizeof(SAL_App_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_22KW_IS_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1154
def SALGetSignal_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MAX():
    return SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 147
def SALGetSignal_Signal_ADC_AFE_TEMP_LB():
    return SALIoHwAb_ADC_AFE_TEMP_LB

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 764
def SALGetSignal_COMTxSignal_AM_DIAG_010():
    return SALComGetSignal_COMTxSignal_AM_DIAG_010

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 323
SALGetSignalSize_Signal_GridEval_AC_L2_ZC_Counter = sizeof(SAL_App_Signal_GridEval_AC_L2_ZC_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 574
def SALGetSignal_Signal_TstMan_Mode_StMan():
    return SAL_App_Signal_TstMan_Mode_StMan

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 290
def SALGetSignal_Signal_GridEval_AC_L3_V_RMS():
    return SAL_App_Signal_GridEval_AC_L3_V_RMS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 874
def SALGetSignal_Signal_Calib_STMAN_G2V_MAX_PRECHARGE_RETRIES():
    return SAL_App_Signal_Calib_STMAN_G2V_MAX_PRECHARGE_RETRIES

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1127
SALGetSignalSize_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 102
def SALGetSignal_Signal_ADC_AC_AFE_VOUT_VS_S2():
    return SALIoHwAb_ADC_AC_AFE_VOUT_VS_S2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 701
def SALGetSignal_COMTxSignal_AM_DIAG_019():
    return SALComGetSignal_COMTxSignal_AM_DIAG_019

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 263
SALGetSignalSize_Signal_GridEval_AC_L3_V_POS_PK = sizeof(SAL_App_Signal_GridEval_AC_L3_V_POS_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 823
SALGetSignalSize_Signal_Calib_STMAN_V2L_PREPARE_TO_RUN_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_V2L_PREPARE_TO_RUN_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1078
def SALGetSignal_Signal_Calib_HWMON_AC_L3_V_RMS_UV_DQ():
    return SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_UV_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1384
def SALGetSignal_Signal_Derat_DERAT_STATUS():
    return SAL_App_Signal_Derat_DERAT_STATUS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 498
def SALGetSignal_COMTxSignal_AM_DIAG_048():
    return SALComGetSignal_COMTxSignal_AM_DIAG_048

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 230
def SALGetSignal_Signal_GridEval_Operation_Mode():
    return SAL_App_Signal_GridEval_Operation_Mode

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 798
def SALGetSignal_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1051
SALGetSignalSize_Signal_Calib_HWMON_AC_L2_V_RMS_OV_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_OV_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 52
def SALGetSignal_Signal_ComE2E_MA_REQUEST_OP_Counter_Fault():
    return SAL_App_Signal_ComE2E_MA_REQUEST_OP_Counter_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 544
def SALGetSignal_Signal_PComp_CMPSS3_DACLVAL():
    return SAL_App_Signal_PComp_CMPSS3_DACLVAL

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 779
SALGetSignalSize_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_ONE_PHASE_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_ONE_PHASE_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1355
SALGetSignalSize_Signal_Calib_DERAT_MOSFET_LB_WORK_COEF = sizeof(SAL_App_Signal_Calib_DERAT_MOSFET_LB_WORK_COEF)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 379
def SALGetSignal_COMTxSignal_AM_DIAG_063():
    return SALComGetSignal_COMTxSignal_AM_DIAG_063

SAL_AppSingleBlockCbkPtrType = CFUNCTYPE(UNCHECKED(None), SAL_RequestResultType)
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 139

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 177
SALGetSignalSize_Signal_StMan_ST_AC_L2_RD = sizeof(SAL_App_Signal_StMan_ST_AC_L2_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 493
SALGetSignalSize_Signal_PComp_ADC_AC_1_65V_VS = sizeof(SAL_App_Signal_PComp_ADC_AC_1_65V_VS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 736
def SALGetSignal_TstMan_StMan_Signal_AM_OP_MODE_FB():
    return SAL_App_TstMan_StMan_Signal_AM_OP_MODE_FB

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1334
def SALGetSignal_Signal_Calib_DERAT_VIN_VALUES():
    return SAL_App_Signal_Calib_DERAT_VIN_VALUES

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 288
def SALGetSignal_COMTxSignal_AM_DIAG_076():
    return SALComGetSignal_COMTxSignal_AM_DIAG_076

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 160
def SALGetSignal_Signal_StMan_STMAN_STATE():
    return SAL_App_Signal_StMan_STMAN_STATE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1352
def SALGetSignal_COMRxSignal_MA_E2E_CHK_03():
    return SALComGetSignal_COMRxSignal_MA_E2E_CHK_03

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 468
def SALGetSignal_Signal_PComp_PFC3PhaseCurrAMesFactor():
    return SAL_App_Signal_PComp_PFC3PhaseCurrAMesFactor

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 709
SALGetSignalSize_TstMan_StMan_Signal_ST_AFE_L3_RD = sizeof(SAL_App_TstMan_StMan_Signal_ST_AFE_L3_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1345
SALGetSignalSize_Signal_Calib_DERAT_MOSFET_TEMP_VALUES = sizeof(SAL_App_Signal_Calib_DERAT_MOSFET_TEMP_VALUES)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 337
def SALGetSignal_COMTxSignal_AM_DIAG_069():
    return SALComGetSignal_COMTxSignal_AM_DIAG_069

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 53
class union_anon_16(Union):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1011
SALGetSignalSize_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_THRESHOLD = sizeof(SAL_App_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1266
def SALGetSignal_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MAX():
    return SAL_App_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 165
SALGetSignalSize_Signal_StMan_STMAN_SUBSTATE = sizeof(SAL_App_Signal_StMan_STMAN_SUBSTATE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1149
def SALGetSignal_COMTxSignal_AM_VERSION_RC():
    return SALComGetSignal_COMTxSignal_AM_VERSION_RC

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 435
SALGetSignalSize_Signal_GridEval_AC_L3_REACTIVE_PWR = sizeof(SAL_App_Signal_GridEval_AC_L3_REACTIVE_PWR)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 678
def SALGetSignal_TstMan_PComp_Signal_PFC3PhaseCurrCMesFactor_Value():
    return SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrCMesFactor_Value

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1322
def SALGetSignal_Signal_Calib_PCOMP_AFE_AC_VOLTAGE_SENSORGAIN_VALUE():
    return SAL_App_Signal_Calib_PCOMP_AFE_AC_VOLTAGE_SENSORGAIN_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 246
def SALGetSignal_COMTxSignal_AM_DIAG_082():
    return SALComGetSignal_COMTxSignal_AM_DIAG_082

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 986
def SALGetSignal_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK02_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK02_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1239
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LC_QT = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 134
def SALGetSignal_Dem_Fault7():
    return SAL_App_Dem_Fault7

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1086
def SALGetSignal_COMTxSignal_AM_AC_PH_3_RMS_I():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_3_RMS_I

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 442
def SALGetSignal_Signal_GridEval_AC_L3L1_PhaseDegree():
    return SAL_App_Signal_GridEval_AC_L3L1_PhaseDegree

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 683
SALGetSignalSize_TstMan_PComp_Signal_PFC3PhaseVoltMesFactor_Value = sizeof(SAL_App_TstMan_PComp_Signal_PFC3PhaseVoltMesFactor_Value)

struct_anon_6.__slots__ = [
    'member13',
    'member11',
    'member12',
]
struct_anon_6._fields_ = [
    ('member13', uint16 * 2),
    ('member11', uint16),
    ('member12', uint8),
]

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 999
SALGetSignalSize_Signal_Calib_GRIDEVAL_V2L_LINERMSVOLTAGE_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_V2L_LINERMSVOLTAGE_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1254
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LB_DQ():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1107
def SALGetSignal_COMTxSignal_AM_DER_STATUS():
    return SALComGetSignal_COMTxSignal_AM_DER_STATUS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 423
SALGetSignalSize_Signal_GridEval_AC_L3L1_ZC_Max_Counter = sizeof(SAL_App_Signal_GridEval_AC_L3L1_ZC_Max_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 666
def SALGetSignal_TstMan_PComp_Signal_PFC3PhaseCurrCMesOffset_Value():
    return SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrCMesOffset_Value

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 974
def SALGetSignal_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMAX_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMAX_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1227
SALGetSignalSize_Signal_Calib_HWMON_AC_RLY_TEMP_QT = sizeof(SAL_App_Signal_Calib_HWMON_AC_RLY_TEMP_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 63
SALGetSigGroupRef_NM_FaultGroup = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 106
def SALGetSignal_COMTxSignal_AM_DIAG_102():
    return SALComGetSignal_COMTxSignal_AM_DIAG_102

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 995
def SALGetSignal_COMTxSignal_AM_AC_PH_1_F():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_1_F

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 366
def SALGetSignal_Signal_GridEval_AC_L3L1_V_PK():
    return SAL_App_Signal_GridEval_AC_L3L1_V_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 613
SALGetSignalSize_Signal_AC_FLY_TEMP = sizeof(SAL_App_Signal_AC_FLY_TEMP)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 939
SALGetSignalSize_Signal_Calib_GRIDEVAL_PH_PEAKVOLTAGE_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_PH_PEAKVOLTAGE_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1194
def SALGetSignal_Signal_Calib_HWMON_AC_12V_TH_HIGH_QT():
    return SAL_App_Signal_Calib_HWMON_AC_12V_TH_HIGH_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 904
def SALGetSignal_COMTxSignal_AM_FET_L2_T():
    return SALComGetSignal_COMTxSignal_AM_FET_L2_T

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 331
SALGetSignalSize_Signal_GridEval_AC_L1_ZC_Max_Counter = sizeof(SAL_App_Signal_GridEval_AC_L1_ZC_Max_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 582
def SALGetSignal_Signal_TstMan_Mode_TempSens():
    return SAL_App_Signal_TstMan_Mode_TempSens

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 882
def SALGetSignal_Signal_Calib_STMAN_V2L_AC_STABILIZATION_THRESHOLD():
    return SAL_App_Signal_Calib_STMAN_V2L_AC_STABILIZATION_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1135
SALGetSignalSize_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MIN)

SAL_TEST5 = struct_anon_6
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 55

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 122
def SALGetSignal_Signal_ADC_AC_DSP_3V3_S1():
    return SALIoHwAb_ADC_AC_DSP_3V3_S1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 729
def SALGetSignal_COMTxSignal_AM_DIAG_015():
    return SALComGetSignal_COMTxSignal_AM_DIAG_015

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 306
def SALGetSignal_Signal_GridEval_AC_L1_FREQ():
    return SAL_App_Signal_GridEval_AC_L1_FREQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 555
SALGetSignalSize_Signal_TstMan_Status = sizeof(SAL_App_Signal_TstMan_Status)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 271
SALGetSignalSize_Signal_GridEval_AC_L1_dV_PK = sizeof(SAL_App_Signal_GridEval_AC_L1_dV_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 863
SALGetSignalSize_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MIN_VALUE = sizeof(SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MIN_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1118
def SALGetSignal_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MIN():
    return SAL_App_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 57
def SALGetSignal_Signal_ADC_AC_N_VS_S1():
    return SALIoHwAb_ADC_IF_ADC_B2_SOC2_S1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 638
def SALGetSignal_COMTxSignal_AM_DIAG_028():
    return SALComGetSignal_COMTxSignal_AM_DIAG_028

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 319
SALGetSignalSize_Signal_GridEval_AC_L1_ZC_Counter = sizeof(SAL_App_Signal_GridEval_AC_L1_ZC_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 570
def SALGetSignal_Signal_TstMan_Mode_PComp():
    return SAL_App_Signal_TstMan_Mode_PComp

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 238
def SALGetSignal_Signal_GridEval_AC_L1_V_POS_PK():
    return SAL_App_Signal_GridEval_AC_L1_V_POS_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 870
def SALGetSignal_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MIN_VALUE():
    return SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MIN_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1123
SALGetSignalSize_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1389
SALGetSignalSize_Signal_Derat_AM_DER_MAX_I = sizeof(SAL_App_Signal_Derat_AM_DER_MAX_I)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 519
def SALGetSignal_COMTxSignal_AM_DIAG_045():
    return SALComGetSignal_COMTxSignal_AM_DIAG_045

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 213
SALGetSignalSize_Signal_HwCfg_AFE_LA_IS_MaxCurrent = sizeof(SAL_App_Signal_HwCfg_AFE_LA_IS_MaxCurrent)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 835
SALGetSignalSize_Signal_Calib_STMAN_SHUTDOWN_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_SHUTDOWN_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1090
def SALGetSignal_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_VOLTAGEDELTA():
    return SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_VOLTAGEDELTA

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 41
SALGetSignalSize_Signal_ComE2E_MA_V2X_Checksum_Fault = sizeof(SAL_App_Signal_ComE2E_MA_V2X_Checksum_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 533
SALGetSignalSize_Signal_PComp_CMPSS2_DACHVAL = sizeof(SAL_App_Signal_PComp_CMPSS2_DACHVAL)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 770
def SALGetSignal_Signal_Calib_STMAN_V2L_TO_STANDBY_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_V2L_TO_STANDBY_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1394
def SALGetSignal_Signal_Meas_AC_AFE_VOUT_VS():
    return SAL_App_Signal_Meas_AC_AFE_VOUT_VS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 540
def SALGetSignal_COMTxSignal_AM_DIAG_042():
    return SALComGetSignal_COMTxSignal_AM_DIAG_042

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 226
def SALGetSignal_Signal_GridEval_GRID_NO_OF_PH():
    return SAL_App_Signal_GridEval_GRID_NO_OF_PH

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 810
def SALGetSignal_Signal_Calib_STMAN_G2V_PLL_STABILIZATION_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_PLL_STABILIZATION_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1063
SALGetSignalSize_Signal_Calib_HWMON_AC_L2_V_RMS_UV_QT = sizeof(SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_UV_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1380
def SALGetSignal_COMRxSignal_MA_V2X_MIN_V():
    return SALComGetSignal_COMRxSignal_MA_V2X_MIN_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 540
def SALGetSignal_Signal_PComp_CMPSS3_DACHVAL():
    return SAL_App_Signal_PComp_CMPSS3_DACHVAL

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 48
def SALGetSignal_Signal_ComE2E_MA_REQUEST_OP_Checksum_Fault():
    return SAL_App_Signal_ComE2E_MA_REQUEST_OP_Checksum_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 775
SALGetSignalSize_Signal_Calib_STMAN_G2V_PRECHARGE_RUN_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_RUN_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1379
SALGetSignalSize_Signal_Calib_DERAT_MAXIMUM_OPERATIONAL_TEMP_FLYBACK = sizeof(SAL_App_Signal_Calib_DERAT_MAXIMUM_OPERATIONAL_TEMP_FLYBACK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 477
def SALGetSignal_COMTxSignal_AM_DIAG_051():
    return SALComGetSignal_COMTxSignal_AM_DIAG_051

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 203
SALGetSignalSize_Signal_ClaIf_CM_PLL_STATUS_1PH = sizeof(SAL_App_Signal_ClaIf_CM_PLL_STATUS_1PH)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1289
def SALGetSignal_COMRxSignal_MA_OP_MODE():
    return SALComGetSignal_COMRxSignal_MA_OP_MODE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 505
SALGetSignalSize_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LB_IS = sizeof(SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LB_IS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 746
def SALGetSignal_TstMan_GridEval_Signal_GRID_NO_OF_PH():
    return SAL_App_TstMan_GridEval_Signal_GRID_NO_OF_PH

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1330
def SALGetSignal_Signal_Calib_PCOMP_AFE_12V_SENSORGAIN_VALUE():
    return SAL_App_Signal_Calib_PCOMP_AFE_12V_SENSORGAIN_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 274
def SALGetSignal_COMTxSignal_AM_DIAG_078():
    return SALComGetSignal_COMTxSignal_AM_DIAG_078

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 172
def SALGetSignal_Signal_StMan_ST_AC_L1L2_RD():
    return SAL_App_Signal_StMan_ST_AC_L1L2_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1338
def SALGetSignal_COMRxSignal_MA_ACT_P_PH2():
    return SALComGetSignal_COMRxSignal_MA_ACT_P_PH2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 480
def SALGetSignal_Signal_PComp_PFC3PhaseVoltMesFactor():
    return SAL_App_Signal_PComp_PFC3PhaseVoltMesFactor

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 721
SALGetSignalSize_TstMan_StMan_Signal_ST_AC_L1_RD = sizeof(SAL_App_TstMan_StMan_Signal_ST_AC_L1_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1295
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 155
def SALGetSignal_COMTxSignal_AM_DIAG_095():
    return SALComGetSignal_COMTxSignal_AM_DIAG_095

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1039
SALGetSignalSize_Signal_Calib_HWMON_AC_L2_V_RMS_OV_QT = sizeof(SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_OV_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1294
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MIN():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 115
SALGetSignalSize_Dem_Fault2 = sizeof(SAL_App_Dem_Fault2)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1247
def SALGetSignal_COMTxSignal_AM_ODD_B6():
    return SALComGetSignal_COMTxSignal_AM_ODD_B6

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 431
SALGetSignalSize_Signal_GridEval_AC_L3_ACTIVE_PWR = sizeof(SAL_App_Signal_GridEval_AC_L3_ACTIVE_PWR)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 674
def SALGetSignal_TstMan_PComp_Signal_PFC3PhaseCurrBMesFactor_Value():
    return SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrBMesFactor_Value

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 982
def SALGetSignal_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK01_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK01_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1235
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LB_QT = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 100
def SALGetSignal_Signal_Com_MA_MCMP_InvalidValue_Fault():
    return SAL_App_Signal_Com_MA_MCMP_InvalidValue_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1128
def SALGetSignal_COMTxSignal_AM_E2E_CHK_07():
    return SALComGetSignal_COMTxSignal_AM_E2E_CHK_07

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 406
def SALGetSignal_Signal_GridEval_AC_L2L3_ZC_Counter():
    return SAL_App_Signal_GridEval_AC_L2L3_ZC_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 649
SALGetSignalSize_TstMan_RelAct_Signal_PWM_AC_L3_RD = sizeof(SAL_App_TstMan_RelAct_Signal_PWM_AC_L3_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 947
SALGetSignalSize_Signal_Calib_GRIDEVAL_V2L_PEAKVOLTAGE_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_V2L_PEAKVOLTAGE_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1202
def SALGetSignal_Signal_Calib_HWMON_AC_DSP_3V3_1_MAX():
    return SAL_App_Signal_Calib_HWMON_AC_DSP_3V3_1_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 105
SALGetSignalSize_Signal_Com_MA_MCMP_Monitoring_Fault = sizeof(SAL_App_Signal_Com_MA_MCMP_Monitoring_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 43
def SALGetSignal_COMTxSignal_AM_DIAG_111():
    return SALComGetSignal_COMTxSignal_AM_DIAG_111

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 932
def SALGetSignal_COMTxSignal_AM_E2E_CHK_02():
    return SALComGetSignal_COMTxSignal_AM_E2E_CHK_02

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 371
SALGetSignalSize_Signal_GridEval_AC_L3L1_V_POS_PK = sizeof(SAL_App_Signal_GridEval_AC_L3L1_V_POS_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 618
def SALGetSignal_Signal_RelAct_RelayType():
    return SAL_App_Signal_RelAct_RelayType

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 922
def SALGetSignal_Signal_Calib_GRIDEVAL_INIT_DEADTIMEGRIDEVAL_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_INIT_DEADTIMEGRIDEVAL_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1175
SALGetSignalSize_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_IMIN = sizeof(SAL_App_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_IMIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 73
SALGetSigGroupRef_Com_FaultGroup = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 227
def SALGetSignal_Signal_PWM_AC_L1_RD():
    return SALIoHwAb_PWM_AC_L1_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 869
def SALGetSignal_COMTxSignal_AM_REF_3V3():
    return SALComGetSignal_COMTxSignal_AM_REF_3V3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 378
def SALGetSignal_Signal_GridEval_AC_L1L2_dV_PK():
    return SAL_App_Signal_GridEval_AC_L1L2_dV_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 623
SALGetSignalSize_Signal_RelAct_RelayStatus = sizeof(SAL_App_Signal_RelAct_RelayStatus)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 935
SALGetSignalSize_Signal_Calib_GRIDEVAL_MONITORINGTIMEOUT_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_MONITORINGTIMEOUT_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1190
def SALGetSignal_Signal_Calib_HWMON_AC_12V_TH_LOW_QT():
    return SAL_App_Signal_Calib_HWMON_AC_12V_TH_LOW_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 890
def SALGetSignal_COMTxSignal_AM_PS_T():
    return SALComGetSignal_COMTxSignal_AM_PS_T

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 359
SALGetSignalSize_Signal_GridEval_AC_L2L3_V_POS_PK = sizeof(SAL_App_Signal_GridEval_AC_L2L3_V_POS_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 608
def SALGetSignal_Signal_AFE_TEMP_LC():
    return SAL_App_Signal_AFE_TEMP_LC

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 278
def SALGetSignal_Signal_GridEval_AC_L3_dV_PK():
    return SAL_App_Signal_GridEval_AC_L3_dV_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 910
def SALGetSignal_Signal_Calib_HWCFG_3PH_11_KW_SYS_11KW_IS_MAX():
    return SAL_App_Signal_Calib_HWCFG_3PH_11_KW_SYS_11KW_IS_MAX

SAL_SingleBlockCbkPtrType = CFUNCTYPE(UNCHECKED(None), uint8, SAL_RequestResultType)
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 130

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1163
SALGetSignalSize_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 152
def SALGetSignal_Signal_ADC_AFE_TEMP_LC():
    return SALIoHwAb_ADC_AFE_TEMP_LC

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 771
def SALGetSignal_COMTxSignal_AM_DIAG_009():
    return SALComGetSignal_COMTxSignal_AM_DIAG_009

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 302
def SALGetSignal_Signal_GridEval_AC_L3_IS_RMS():
    return SAL_App_Signal_GridEval_AC_L3_IS_RMS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 283
SALGetSignalSize_Signal_GridEval_AC_L1_V_RMS = sizeof(SAL_App_Signal_GridEval_AC_L1_V_RMS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 875
SALGetSignalSize_Signal_Calib_STMAN_G2V_MAX_PRECHARGE_RETRIES = sizeof(SAL_App_Signal_Calib_STMAN_G2V_MAX_PRECHARGE_RETRIES)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1130
def SALGetSignal_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MAX():
    return SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 87
def SALGetSignal_Signal_ADC_AFE_LC_IS_S1():
    return SALIoHwAb_ADC_AFE_LC_IS_S1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 680
def SALGetSignal_COMTxSignal_AM_DIAG_022():
    return SALComGetSignal_COMTxSignal_AM_DIAG_022

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 266
def SALGetSignal_Signal_GridEval_AC_L3_V_NEG_PK():
    return SAL_App_Signal_GridEval_AC_L3_V_NEG_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 818
def SALGetSignal_Signal_Calib_STMAN_V2L_PERIPHERAL_INIT_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_V2L_PERIPHERAL_INIT_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1071
SALGetSignalSize_Signal_Calib_HWMON_AC_L1_V_RMS_UV_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_UV_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1385
SALGetSignalSize_Signal_Derat_DERAT_STATUS = sizeof(SAL_App_Signal_Derat_DERAT_STATUS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 505
def SALGetSignal_COMTxSignal_AM_DIAG_047():
    return SALComGetSignal_COMTxSignal_AM_DIAG_047

SAL_ESyncReadCbkPtrType = CFUNCTYPE(UNCHECKED(Std_ReturnType), POINTER(None))
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 148

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 799
SALGetSignalSize_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1054
def SALGetSignal_Signal_Calib_HWMON_AC_L3_V_RMS_OV_DQ():
    return SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_OV_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 53
SALGetSignalSize_Signal_ComE2E_MA_REQUEST_OP_Counter_Fault = sizeof(SAL_App_Signal_ComE2E_MA_REQUEST_OP_Counter_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 545
SALGetSignalSize_Signal_PComp_CMPSS3_DACLVAL = sizeof(SAL_App_Signal_PComp_CMPSS3_DACLVAL)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 782
def SALGetSignal_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_TWO_PHASES_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_TWO_PHASES_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1364
def SALGetSignal_Signal_Calib_DERAT_RELAY_TEMP_VALUES():
    return SAL_App_Signal_Calib_DERAT_RELAY_TEMP_VALUES

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 414
def SALGetSignal_COMTxSignal_AM_DIAG_058():
    return SALComGetSignal_COMTxSignal_AM_DIAG_058

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 41
class union_anon_14(Union):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 180
def SALGetSignal_Signal_StMan_ST_AC_L3_RD():
    return SAL_App_Signal_StMan_ST_AC_L3_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 806
def SALGetSignal_Signal_Calib_STMAN_G2V_PERIPHERAL_INIT_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_PERIPHERAL_INIT_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1059
SALGetSignalSize_Signal_Calib_HWMON_AC_L1_V_RMS_UV_QT = sizeof(SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_UV_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 488
def SALGetSignal_Signal_Pcomp_AC12VSMesFactor():
    return SAL_App_Signal_Pcomp_AC12VSMesFactor

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 729
SALGetSignalSize_TstMan_StMan_Signal_PFCOpState = sizeof(SAL_App_TstMan_StMan_Signal_PFCOpState)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1335
SALGetSignalSize_Signal_Calib_DERAT_VIN_VALUES = sizeof(SAL_App_Signal_Calib_DERAT_VIN_VALUES)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 295
def SALGetSignal_COMTxSignal_AM_DIAG_075():
    return SALComGetSignal_COMTxSignal_AM_DIAG_075

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 153
SALGetSignalSize_Signal_StMan_PCompSamplingMode = sizeof(SAL_App_Signal_StMan_PCompSamplingMode)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1275
def SALGetSignal_COMRxSignal_MA_CH_V():
    return SALComGetSignal_COMRxSignal_MA_CH_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 469
SALGetSignalSize_Signal_PComp_PFC3PhaseCurrAMesFactor = sizeof(SAL_App_Signal_PComp_PFC3PhaseCurrAMesFactor)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 712
def SALGetSignal_TstMan_StMan_Signal_ST_AC_N_RD():
    return SAL_App_TstMan_StMan_Signal_ST_AC_N_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1340
SALGetSignalSize_Signal_Calib_DERAT_VIN_WORK_COEF = sizeof(SAL_App_Signal_Calib_DERAT_VIN_WORK_COEF)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 316
def SALGetSignal_COMTxSignal_AM_DIAG_072():
    return SALComGetSignal_COMTxSignal_AM_DIAG_072

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1022
def SALGetSignal_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_MAX_ERROR():
    return SAL_App_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_MAX_ERROR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1275
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 168
def SALGetSignal_Signal_StMan_ST_AC_L1_RD():
    return SAL_App_Signal_StMan_ST_AC_L1_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1156
def SALGetSignal_COMTxSignal_AM_VERSION_PATCH():
    return SALComGetSignal_COMTxSignal_AM_VERSION_PATCH

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 476
def SALGetSignal_Signal_PComp_PFC3PhaseCurrCMesFactor():
    return SAL_App_Signal_PComp_PFC3PhaseCurrCMesFactor

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 717
SALGetSignalSize_TstMan_StMan_Signal_ST_AC_L3_RD = sizeof(SAL_App_TstMan_StMan_Signal_ST_AC_L3_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1323
SALGetSignalSize_Signal_Calib_PCOMP_AFE_AC_VOLTAGE_SENSORGAIN_VALUE = sizeof(SAL_App_Signal_Calib_PCOMP_AFE_AC_VOLTAGE_SENSORGAIN_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 253
def SALGetSignal_COMTxSignal_AM_DIAG_081():
    return SALComGetSignal_COMTxSignal_AM_DIAG_081

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 987
SALGetSignalSize_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK02_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK02_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1242
def SALGetSignal_Signal_Calib_HWMON_AC_FLY_TEMP_QT():
    return SAL_App_Signal_Calib_HWMON_AC_FLY_TEMP_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 143
SALGetSignalSize_Dem_Fault9 = sizeof(SAL_App_Dem_Fault9)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1065
def SALGetSignal_COMTxSignal_AM_AC_PH_3_RMS_V():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_3_RMS_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 443
SALGetSignalSize_Signal_GridEval_AC_L3L1_PhaseDegree = sizeof(SAL_App_Signal_GridEval_AC_L3L1_PhaseDegree)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 686
def SALGetSignal_TstMan_PComp_Signal_PFC3PDCLinkVoltMesFactor_Value():
    return SAL_App_TstMan_PComp_Signal_PFC3PDCLinkVoltMesFactor_Value

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 994
def SALGetSignal_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMIN_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMIN_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1247
SALGetSignalSize_Signal_Calib_HWMON_AC_RLY_TEMP_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AC_RLY_TEMP_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 110
def SALGetSignal_Dem_Fault1():
    return SAL_App_Dem_Fault1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1114
def SALGetSignal_COMTxSignal_AM_OP_MODE_FB():
    return SALComGetSignal_COMTxSignal_AM_OP_MODE_FB

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 418
def SALGetSignal_Signal_GridEval_AC_L2L3_ZC_Max_Counter():
    return SAL_App_Signal_GridEval_AC_L2L3_ZC_Max_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 659
SALGetSignalSize_TstMan_PComp_Signal_PFC3PhaseCurrAMesOffset_Value = sizeof(SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrAMesOffset_Value)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 975
SALGetSignalSize_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMAX_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMAX_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1230
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LA_QT():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 141
def SALGetSignal_COMTxSignal_AM_DIAG_097():
    return SALComGetSignal_COMTxSignal_AM_DIAG_097

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1030
def SALGetSignal_COMTxSignal_AM_AC_PH_2_PK_V():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_2_PK_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 367
SALGetSignalSize_Signal_GridEval_AC_L3L1_V_PK = sizeof(SAL_App_Signal_GridEval_AC_L3L1_V_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 615
SALGetSigGroupRef_RelAct_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 918
def SALGetSignal_Signal_Calib_GRIDEVAL_PHASECHECK_FILTER_SIZE():
    return SAL_App_Signal_Calib_GRIDEVAL_PHASECHECK_FILTER_SIZE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1171
SALGetSignalSize_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_VFACTOR = sizeof(SAL_App_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_VFACTOR)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 22
def SALGetSignal_COMTxSignal_AM_E2E_CRC_10():
    return SALComGetSignal_COMTxSignal_AM_E2E_CRC_10

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 911
def SALGetSignal_COMTxSignal_AM_FET_L1_T():
    return SALComGetSignal_COMTxSignal_AM_FET_L1_T

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 342
def SALGetSignal_Signal_GridEval_AC_L1L2_V_PK():
    return SAL_App_Signal_GridEval_AC_L1L2_V_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 591
SALGetSignalSize_Signal_TstMan_Mode_HwMon = sizeof(SAL_App_Signal_TstMan_Mode_HwMon)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 883
SALGetSignalSize_Signal_Calib_STMAN_V2L_AC_STABILIZATION_THRESHOLD = sizeof(SAL_App_Signal_Calib_STMAN_V2L_AC_STABILIZATION_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1138
def SALGetSignal_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MAX():
    return SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_OFFSET_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 107
def SALGetSignal_Signal_ADC_AC_L1_VS():
    return SALIoHwAb_ADC_AC_L1_VS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 708
def SALGetSignal_COMTxSignal_AM_DIAG_018():
    return SALComGetSignal_COMTxSignal_AM_DIAG_018

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 307
SALGetSignalSize_Signal_GridEval_AC_L1_FREQ = sizeof(SAL_App_Signal_GridEval_AC_L1_FREQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 558
def SALGetSignal_Signal_TstMan_Disable_SwSec():
    return SAL_App_Signal_TstMan_Disable_SwSec

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 274
def SALGetSignal_Signal_GridEval_AC_L2_dV_PK():
    return SAL_App_Signal_GridEval_AC_L2_dV_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 858
def SALGetSignal_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MAX_VALUE():
    return SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MAX_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1111
SALGetSignalSize_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_QT = sizeof(SAL_App_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 62
def SALGetSignal_Signal_ADC_AC_N_VS_S2():
    return SALIoHwAb_ADC_IF_ADC_B2_SOC5_S2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 645
def SALGetSignal_COMTxSignal_AM_DIAG_027():
    return SALComGetSignal_COMTxSignal_AM_DIAG_027

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 314
def SALGetSignal_Signal_GridEval_AC_L3_FREQ():
    return SAL_App_Signal_GridEval_AC_L3_FREQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 563
SALGetSignalSize_Signal_TstMan_Disable_WdgM = sizeof(SAL_App_Signal_TstMan_Disable_WdgM)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 247
SALGetSignalSize_Signal_GridEval_AC_L2_V_PK = sizeof(SAL_App_Signal_GridEval_AC_L2_V_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 871
SALGetSignalSize_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MIN_VALUE = sizeof(SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MIN_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1126
def SALGetSignal_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MIN():
    return SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_OFFSET_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 77
def SALGetSignal_Signal_ADC_AFE_LB_IS_S1():
    return SALIoHwAb_ADC_AFE_LB_IS_S1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 666
def SALGetSignal_COMTxSignal_AM_DIAG_024():
    return SALComGetSignal_COMTxSignal_AM_DIAG_024

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 216
def SALGetSignal_Signal_HwCfg_AFE_LB_IS_MaxCurrent():
    return SAL_App_Signal_HwCfg_AFE_LB_IS_MaxCurrent

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 846
def SALGetSignal_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_THRESHOLD_DELTA():
    return SAL_App_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_THRESHOLD_DELTA

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1099
SALGetSignalSize_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_CURRENTDELTA = sizeof(SAL_App_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_CURRENTDELTA)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 36
def SALGetSignal_Signal_ComE2E_MA_POWER_Counter_Fault():
    return SAL_App_Signal_ComE2E_MA_POWER_Counter_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 528
def SALGetSignal_Signal_PComp_CMPSS1_DACLVAL():
    return SAL_App_Signal_PComp_CMPSS1_DACLVAL

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 763
SALGetSignalSize_Signal_Calib_STMAN_OFF_TO_RUN_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_OFF_TO_RUN_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1395
SALGetSignalSize_Signal_Meas_AC_AFE_VOUT_VS = sizeof(SAL_App_Signal_Meas_AC_AFE_VOUT_VS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 547
def SALGetSignal_COMTxSignal_AM_DIAG_041():
    return SALComGetSignal_COMTxSignal_AM_DIAG_041

HFLConfigType = struct_anon_17
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 178

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 221
SALGetSignalSize_Signal_HwCfg_AFE_LC_IS_MaxCurrent = sizeof(SAL_App_Signal_HwCfg_AFE_LC_IS_MaxCurrent)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 811
SALGetSignalSize_Signal_Calib_STMAN_G2V_PLL_STABILIZATION_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PLL_STABILIZATION_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1066
def SALGetSignal_Signal_Calib_HWMON_AC_L3_V_RMS_UV_QT():
    return SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_UV_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 49
SALGetSignalSize_Signal_ComE2E_MA_REQUEST_OP_Checksum_Fault = sizeof(SAL_App_Signal_ComE2E_MA_REQUEST_OP_Checksum_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 541
SALGetSignalSize_Signal_PComp_CMPSS3_DACHVAL = sizeof(SAL_App_Signal_PComp_CMPSS3_DACHVAL)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 778
def SALGetSignal_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_ONE_PHASE_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_INIT_ONE_PHASE_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1374
def SALGetSignal_Signal_Calib_DERAT_MAXIMUM_CUTOFF_TEMP_FLYBACK():
    return SAL_App_Signal_Calib_DERAT_MAXIMUM_CUTOFF_TEMP_FLYBACK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 456
def SALGetSignal_COMTxSignal_AM_DIAG_054():
    return SALComGetSignal_COMTxSignal_AM_DIAG_054

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 206
def SALGetSignal_Signal_ClaIf_CM_PLL_STATUS_3PH():
    return SAL_App_Signal_ClaIf_CM_PLL_STATUS_3PH

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1296
def SALGetSignal_COMRxSignal_MA_E2E_CHK_01():
    return SALComGetSignal_COMRxSignal_MA_E2E_CHK_01

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 516
def SALGetSignal_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LB_IS():
    return SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LB_IS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1331
SALGetSignalSize_Signal_Calib_PCOMP_AFE_12V_SENSORGAIN_VALUE = sizeof(SAL_App_Signal_Calib_PCOMP_AFE_12V_SENSORGAIN_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 281
def SALGetSignal_COMTxSignal_AM_DIAG_077():
    return SALComGetSignal_COMTxSignal_AM_DIAG_077

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1317
def SALGetSignal_COMRxSignal_MA_REACT_P_PH2():
    return SALComGetSignal_COMRxSignal_MA_REACT_P_PH2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 481
SALGetSignalSize_Signal_PComp_PFC3PhaseVoltMesFactor = sizeof(SAL_App_Signal_PComp_PFC3PhaseVoltMesFactor)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 724
def SALGetSignal_TstMan_StMan_Signal_ST_AC_L2_RD():
    return SAL_App_TstMan_StMan_Signal_ST_AC_L2_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1306
def SALGetSignal_Signal_Calib_PCOMP_ADC_LSB_ERROR_THRESHOLD():
    return SAL_App_Signal_Calib_PCOMP_ADC_LSB_ERROR_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 190
def SALGetSignal_COMTxSignal_AM_DIAG_090():
    return SALComGetSignal_COMTxSignal_AM_DIAG_090

struct_anon_15.__slots__ = [
    'CLIENT1',
]
struct_anon_15._fields_ = [
    ('CLIENT1', uint8, 1),
]

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1034
def SALGetSignal_Signal_Calib_HWMON_AC_L1_V_RMS_OV_QT():
    return SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_OV_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1287
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 118
def SALGetSignal_Dem_Fault3():
    return SAL_App_Dem_Fault3

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1254
def SALGetSignal_COMTxSignal_AM_ODD_CNT():
    return SALComGetSignal_COMTxSignal_AM_ODD_CNT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 426
def SALGetSignal_Signal_GridEval_AC_L3_PWR_FACTOR():
    return SAL_App_Signal_GridEval_AC_L3_PWR_FACTOR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 667
SALGetSignalSize_TstMan_PComp_Signal_PFC3PhaseCurrCMesOffset_Value = sizeof(SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrCMesOffset_Value)

struct_anon_13.__slots__ = [
    'CLIENT1',
]
struct_anon_13._fields_ = [
    ('CLIENT1', uint8, 1),
]

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 983
SALGetSignalSize_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK01_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_1PH_ANGLEDEGREECHECK01_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1238
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LC_QT():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 93
SALGetSignalSize_Signal_Com_MA_REQUEST_OP_InvalidValue_Fault = sizeof(SAL_App_Signal_Com_MA_REQUEST_OP_InvalidValue_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1051
def SALGetSignal_COMTxSignal_AM_E2E_CNT_05():
    return SALComGetSignal_COMTxSignal_AM_E2E_CNT_05

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 407
SALGetSignalSize_Signal_GridEval_AC_L2L3_ZC_Counter = sizeof(SAL_App_Signal_GridEval_AC_L2L3_ZC_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 651
SALGetSigGroupRef_PComp_TstMan_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 958
def SALGetSignal_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK01_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK01_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1211
SALGetSignalSize_Signal_Calib_HWMON_AC_1_65V_VS_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AC_1_65V_VS_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 107
SALGetSigGroupRef_Dem_FaultGroup = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 50
def SALGetSignal_COMTxSignal_AM_DIAG_110():
    return SALComGetSignal_COMTxSignal_AM_DIAG_110

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 939
def SALGetSignal_COMTxSignal_AM_PH_3_1_ANGLE():
    return SALComGetSignal_COMTxSignal_AM_PH_3_1_ANGLE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 414
def SALGetSignal_Signal_GridEval_AC_L1L2_ZC_Max_Counter():
    return SAL_App_Signal_GridEval_AC_L1L2_ZC_Max_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 655
SALGetSignalSize_TstMan_PComp_Signal_IsReady = sizeof(SAL_App_TstMan_PComp_Signal_IsReady)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 923
SALGetSignalSize_Signal_Calib_GRIDEVAL_INIT_DEADTIMEGRIDEVAL_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_INIT_DEADTIMEGRIDEVAL_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1178
def SALGetSignal_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_VFACTOR():
    return SAL_App_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_VFACTOR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 81
SALGetSignalSize_Signal_Com_MA_POWER_Monitoring_Fault = sizeof(SAL_App_Signal_Com_MA_POWER_Monitoring_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 209
def SALGetSignal_Signal_PWM_AC_N_RD():
    return SALIoHwAb_PWM_AC_N_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 848
def SALGetSignal_COMTxSignal_AM_PS_V():
    return SALComGetSignal_COMTxSignal_AM_PS_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 379
SALGetSignalSize_Signal_GridEval_AC_L1L2_dV_PK = sizeof(SAL_App_Signal_GridEval_AC_L1L2_dV_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 625
SALGetSigGroupRef_RelAct_TstMan_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 930
def SALGetSignal_Signal_Calib_GRIDEVAL_TIMERVALID_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_TIMERVALID_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1183
SALGetSignalSize_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_IMIN = sizeof(SAL_App_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_IMIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 897
def SALGetSignal_COMTxSignal_AM_FET_L3_T():
    return SALComGetSignal_COMTxSignal_AM_FET_L3_T

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 354
def SALGetSignal_Signal_GridEval_AC_L2L3_V_PK():
    return SAL_App_Signal_GridEval_AC_L2L3_V_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 601
SALGetSignalSize_Signal_AFE_TEMP_LA = sizeof(SAL_App_Signal_AFE_TEMP_LA)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 911
SALGetSignalSize_Signal_Calib_HWCFG_3PH_11_KW_SYS_11KW_IS_MAX = sizeof(SAL_App_Signal_Calib_HWCFG_3PH_11_KW_SYS_11KW_IS_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1166
def SALGetSignal_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_IMIN():
    return SAL_App_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_IMIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 177
def SALGetSignal_Signal_DIO_AFE_DRV_PS_EN():
    return SALIoHwAb_DIO_AFE_DRV_PS_EN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 806
def SALGetSignal_COMTxSignal_AM_DIAG_004():
    return SALComGetSignal_COMTxSignal_AM_DIAG_004

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 303
SALGetSignalSize_Signal_GridEval_AC_L3_IS_RMS = sizeof(SAL_App_Signal_GridEval_AC_L3_IS_RMS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 554
def SALGetSignal_Signal_TstMan_Status():
    return SAL_App_Signal_TstMan_Status

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 286
def SALGetSignal_Signal_GridEval_AC_L2_V_RMS():
    return SAL_App_Signal_GridEval_AC_L2_V_RMS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 854
def SALGetSignal_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MIN_VALUE():
    return SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MIN_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1107
SALGetSignalSize_Signal_Calib_HWMON_BULK_CAPACITORS_UV = sizeof(SAL_App_Signal_Calib_HWMON_BULK_CAPACITORS_UV)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 92
def SALGetSignal_Signal_ADC_AFE_LC_IS_S2():
    return SALIoHwAb_ADC_AFE_LC_IS_S2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 687
def SALGetSignal_COMTxSignal_AM_DIAG_021():
    return SALComGetSignal_COMTxSignal_AM_DIAG_021

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 259
SALGetSignalSize_Signal_GridEval_AC_L3_V_PK = sizeof(SAL_App_Signal_GridEval_AC_L3_V_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 819
SALGetSignalSize_Signal_Calib_STMAN_V2L_PERIPHERAL_INIT_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_V2L_PERIPHERAL_INIT_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1074
def SALGetSignal_Signal_Calib_HWMON_AC_L2_V_RMS_UV_DQ():
    return SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_UV_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1381
SALGetSigGroupRef_Derat_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 484
def SALGetSignal_COMTxSignal_AM_DIAG_050():
    return SALComGetSignal_COMTxSignal_AM_DIAG_050

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 212
def SALGetSignal_Signal_HwCfg_AFE_LA_IS_MaxCurrent():
    return SAL_App_Signal_HwCfg_AFE_LA_IS_MaxCurrent

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 794
def SALGetSignal_Signal_Calib_STMAN_G2V_PRECHARGE_DONE_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_DONE_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1047
SALGetSignalSize_Signal_Calib_HWMON_AC_L1_V_RMS_OV_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_OV_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 32
def SALGetSignal_Signal_ComE2E_MA_POWER_Checksum_Fault():
    return SAL_App_Signal_ComE2E_MA_POWER_Checksum_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 524
def SALGetSignal_Signal_PComp_CMPSS1_DACHVAL():
    return SAL_App_Signal_PComp_CMPSS1_DACHVAL

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1365
SALGetSignalSize_Signal_Calib_DERAT_RELAY_TEMP_VALUES = sizeof(SAL_App_Signal_Calib_DERAT_RELAY_TEMP_VALUES)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 421
def SALGetSignal_COMTxSignal_AM_DIAG_057():
    return SALComGetSignal_COMTxSignal_AM_DIAG_057

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 189
SALGetSignalSize_Signal_StMan_ST_AFE_L3_RD = sizeof(SAL_App_Signal_StMan_ST_AFE_L3_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 807
SALGetSignalSize_Signal_Calib_STMAN_G2V_PERIPHERAL_INIT_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PERIPHERAL_INIT_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1062
def SALGetSignal_Signal_Calib_HWMON_AC_L2_V_RMS_UV_QT():
    return SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_UV_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 489
SALGetSignalSize_Signal_Pcomp_AC12VSMesFactor = sizeof(SAL_App_Signal_Pcomp_AC12VSMesFactor)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 732
def SALGetSignal_TstMan_StMan_Signal_STMAN_STATE():
    return SAL_App_TstMan_StMan_Signal_STMAN_STATE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1370
SALGetSignalSize_Signal_Calib_DERAT_RELAY_WORK_COEF = sizeof(SAL_App_Signal_Calib_DERAT_RELAY_WORK_COEF)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 442
def SALGetSignal_COMTxSignal_AM_DIAG_056():
    return SALComGetSignal_COMTxSignal_AM_DIAG_056

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 156
def SALGetSignal_Signal_StMan_PFCOpState():
    return SAL_App_Signal_StMan_PFCOpState

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1282
def SALGetSignal_COMRxSignal_MA_CH_MAX_I():
    return SALComGetSignal_COMRxSignal_MA_CH_MAX_I

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 464
def SALGetSignal_Signal_PComp_PFC3PhaseCurrCMesOffset():
    return SAL_App_Signal_PComp_PFC3PhaseCurrCMesOffset

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 705
SALGetSignalSize_TstMan_StMan_Signal_ST_AC_L1L2_RD = sizeof(SAL_App_TstMan_StMan_Signal_ST_AC_L1L2_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1341
def SALGetSignalArray_Signal_Calib_DERAT_VIN_WORK_COEF(index):
    return (SAL_App_Signal_Calib_DERAT_VIN_WORK_COEF [index])

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 323
def SALGetSignal_COMTxSignal_AM_DIAG_071():
    return SALComGetSignal_COMTxSignal_AM_DIAG_071

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1023
SALGetSignalSize_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_MAX_ERROR = sizeof(SAL_App_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_MAX_ERROR)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1278
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MIN():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_SENSOR_FAULT_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 161
SALGetSignalSize_Signal_StMan_STMAN_STATE = sizeof(SAL_App_Signal_StMan_STMAN_STATE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1191
def SALGetSignal_COMTxSignal_AM_VERSION_DAY():
    return SALComGetSignal_COMTxSignal_AM_VERSION_DAY

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 477
SALGetSignalSize_Signal_PComp_PFC3PhaseCurrCMesFactor = sizeof(SAL_App_Signal_PComp_PFC3PhaseCurrCMesFactor)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 720
def SALGetSignal_TstMan_StMan_Signal_ST_AC_L1_RD():
    return SAL_App_TstMan_StMan_Signal_ST_AC_L1_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1318
def SALGetSignal_Signal_Calib_PCOMP_AFE_CURRENT_LC_SENSORGAIN_VALUE():
    return SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LC_SENSORGAIN_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 232
def SALGetSignal_COMTxSignal_AM_DIAG_084():
    return SALComGetSignal_COMTxSignal_AM_DIAG_084

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1030
def SALGetSignal_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_IMAX():
    return SAL_App_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_IMAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1283
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 146
def SALGetSignal_Dem_Fault10():
    return SAL_App_Dem_Fault10

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1072
def SALGetSignal_COMTxSignal_AM_AC_PH_3_PK_V():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_3_PK_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 453
SALGetSigGroupRef_PComp_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 695
SALGetSignalSize_TstMan_PComp_Signal_ADC_AC_1_65V_VS_Value = sizeof(SAL_App_TstMan_PComp_Signal_ADC_AC_1_65V_VS_Value)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 995
SALGetSignalSize_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMIN_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_1PH_FREQUENCYMIN_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1250
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LA_DQ():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 89
SALGetSignalSize_Signal_Com_MA_V2X_Monitoring_Fault = sizeof(SAL_App_Signal_Com_MA_V2X_Monitoring_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1093
def SALGetSignal_COMTxSignal_AM_NO_PHASES():
    return SALComGetSignal_COMTxSignal_AM_NO_PHASES

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 419
SALGetSignalSize_Signal_GridEval_AC_L2L3_ZC_Max_Counter = sizeof(SAL_App_Signal_GridEval_AC_L2L3_ZC_Max_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 662
def SALGetSignal_TstMan_PComp_Signal_PFC3PhaseCurrBMesOffset_Value():
    return SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrBMesOffset_Value

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 970
def SALGetSignal_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMIN_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMIN_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1223
SALGetSignalSize_Signal_Calib_HWMON_AC_L3_FUSE_BLOWN_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AC_L3_FUSE_BLOWN_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 60
def SALGetSignal_Signal_ComE2E_MA_MCMP_Counter_Fault():
    return SAL_App_Signal_ComE2E_MA_MCMP_Counter_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 148
def SALGetSignal_COMTxSignal_AM_DIAG_096():
    return SALComGetSignal_COMTxSignal_AM_DIAG_096

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1037
def SALGetSignal_COMTxSignal_AM_AC_PH_2_F():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_2_F

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 362
def SALGetSignal_Signal_GridEval_AC_L2L3_V_NEG_PK():
    return SAL_App_Signal_GridEval_AC_L2L3_V_NEG_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 609
SALGetSignalSize_Signal_AFE_TEMP_LC = sizeof(SAL_App_Signal_AFE_TEMP_LC)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 919
SALGetSignalSize_Signal_Calib_GRIDEVAL_PHASECHECK_FILTER_SIZE = sizeof(SAL_App_Signal_Calib_GRIDEVAL_PHASECHECK_FILTER_SIZE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1174
def SALGetSignal_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_IMIN():
    return SAL_App_Signal_Calib_HWMON_AC_L2_OPEN_CIRCUIT_IMIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 198
def SALGetSignal_Signal_DIO_AFE_LS_DRV_PS_PG():
    return SALIoHwAb_DIO_AFE_LS_DRV_PS_PG

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 834
def SALGetSignal_COMTxSignal_AM_E2E_CNT_08():
    return SALComGetSignal_COMTxSignal_AM_E2E_CNT_08

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 343
SALGetSignalSize_Signal_GridEval_AC_L1L2_V_PK = sizeof(SAL_App_Signal_GridEval_AC_L1L2_V_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 593
SALGetSigGroupRef_TempSens_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 894
def SALGetSignal_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_11KW_IS_MAX():
    return SAL_App_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_11KW_IS_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1147
SALGetSignalSize_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LA_IS_IS_CURR_ACTIVE_OFFSET_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 112
def SALGetSignal_Signal_ADC_AC_L2_VS():
    return SALIoHwAb_ADC_AC_L2_VS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 715
def SALGetSignal_COMTxSignal_AM_DIAG_017():
    return SALComGetSignal_COMTxSignal_AM_DIAG_017

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 350
def SALGetSignal_Signal_GridEval_AC_L1L2_V_NEG_PK():
    return SAL_App_Signal_GridEval_AC_L1L2_V_NEG_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 597
SALGetSignalSize_Signal_AC_RLY_TEMP = sizeof(SAL_App_Signal_AC_RLY_TEMP)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 267
SALGetSignalSize_Signal_GridEval_AC_L3_V_NEG_PK = sizeof(SAL_App_Signal_GridEval_AC_L3_V_NEG_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 859
SALGetSignalSize_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MAX_VALUE = sizeof(SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_TWO_PHASES_MAX_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1114
def SALGetSignal_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_DT():
    return SAL_App_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_DT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 47
def SALGetSignal_Signal_ADC_AC_L3PF_VS_S1():
    return SALIoHwAb_ADC_IF_ADC_C11_SOC0_S1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 624
def SALGetSignal_COMTxSignal_AM_DIAG_030():
    return SALComGetSignal_COMTxSignal_AM_DIAG_030

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 315
SALGetSignalSize_Signal_GridEval_AC_L3_FREQ = sizeof(SAL_App_Signal_GridEval_AC_L3_FREQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 566
def SALGetSignal_Signal_TstMan_Mode_RelAct():
    return SAL_App_Signal_TstMan_Mode_RelAct

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 250
def SALGetSignal_Signal_GridEval_AC_L2_V_POS_PK():
    return SAL_App_Signal_GridEval_AC_L2_V_POS_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 866
def SALGetSignal_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MAX_VALUE():
    return SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MAX_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1119
SALGetSignalSize_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 82
def SALGetSignal_Signal_ADC_AFE_LB_IS_S2():
    return SALIoHwAb_ADC_AFE_LB_IS_S2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 673
def SALGetSignal_COMTxSignal_AM_DIAG_023():
    return SALComGetSignal_COMTxSignal_AM_DIAG_023

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 255
SALGetSignalSize_Signal_GridEval_AC_L2_V_NEG_PK = sizeof(SAL_App_Signal_GridEval_AC_L2_V_NEG_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 847
SALGetSignalSize_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_THRESHOLD_DELTA = sizeof(SAL_App_Signal_Calib_STMAN_G2V_DCLINK_SOFTSTART_THRESHOLD_DELTA)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1102
def SALGetSignal_Signal_Calib_HWMON_BULK_CAPACITORS_OV():
    return SAL_App_Signal_Calib_HWMON_BULK_CAPACITORS_OV

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 37
SALGetSignalSize_Signal_ComE2E_MA_POWER_Counter_Fault = sizeof(SAL_App_Signal_ComE2E_MA_POWER_Counter_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 529
SALGetSignalSize_Signal_PComp_CMPSS1_DACLVAL = sizeof(SAL_App_Signal_PComp_CMPSS1_DACLVAL)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 766
def SALGetSignal_Signal_Calib_STMAN_G2V_TO_STANDBY_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_TO_STANDBY_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 17
def SALGetSignal_Signal_ADC_AC_L1PF_VS_3PH_S1():
    return SALIoHwAb_ADC_IF_ADC_A2_SOC0_S1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 582
def SALGetSignal_COMTxSignal_AM_DIAG_036():
    return SALComGetSignal_COMTxSignal_AM_DIAG_036

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 223
SALGetSigGroupRef_GridEval_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 790
def SALGetSignal_Signal_Calib_STMAN_G2V_PRECHARGE_FAIL_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_FAIL_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1043
SALGetSignalSize_Signal_Calib_HWMON_AC_L3_V_RMS_OV_QT = sizeof(SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_OV_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 44
def SALGetSignal_Signal_ComE2E_MA_V2X_Counter_Fault():
    return SAL_App_Signal_ComE2E_MA_V2X_Counter_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 536
def SALGetSignal_Signal_PComp_CMPSS2_DACLVAL():
    return SAL_App_Signal_PComp_CMPSS2_DACLVAL

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 771
SALGetSignalSize_Signal_Calib_STMAN_V2L_TO_STANDBY_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_V2L_TO_STANDBY_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1375
SALGetSignalSize_Signal_Calib_DERAT_MAXIMUM_CUTOFF_TEMP_FLYBACK = sizeof(SAL_App_Signal_Calib_DERAT_MAXIMUM_CUTOFF_TEMP_FLYBACK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 463
def SALGetSignal_COMTxSignal_AM_DIAG_053():
    return SALComGetSignal_COMTxSignal_AM_DIAG_053

struct_anon_17.__slots__ = [
    'Hfl_CpuDataLogger',
    'Hfl_DaqCopyVar',
    'Hfl_LogAddr',
    'DAQChannel_State',
]
struct_anon_17._fields_ = [
    ('Hfl_CpuDataLogger', real32_T * 650),
    ('Hfl_DaqCopyVar', POINTER(real32_T)),
    ('Hfl_LogAddr', uint32_T),
    ('DAQChannel_State', uint16_T),
]

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 517
SALGetSignalSize_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LB_IS = sizeof(SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LB_IS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 756
def SALGetSignal_Flag_Signal_CCP():
    return SAL_App_Flag_Signal_CCP

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1326
def SALGetSignal_Signal_Calib_PCOMP_AFE_DC_VOLTAGE_SENSORGAIN_VALUE():
    return SAL_App_Signal_Calib_PCOMP_AFE_DC_VOLTAGE_SENSORGAIN_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 260
def SALGetSignal_COMTxSignal_AM_DIAG_080():
    return SALComGetSignal_COMTxSignal_AM_DIAG_080

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 152
def SALGetSignal_Signal_StMan_PCompSamplingMode():
    return SAL_App_Signal_StMan_PCompSamplingMode

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1324
def SALGetSignal_COMRxSignal_MA_REACT_P_PH1():
    return SALComGetSignal_COMRxSignal_MA_REACT_P_PH1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 460
def SALGetSignal_Signal_PComp_PFC3PhaseCurrBMesOffset():
    return SAL_App_Signal_PComp_PFC3PhaseCurrBMesOffset

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 701
SALGetSignalSize_TstMan_StMan_Signal_PCompSamplingMode = sizeof(SAL_App_TstMan_StMan_Signal_PCompSamplingMode)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1307
SALGetSignalSize_Signal_Calib_PCOMP_ADC_LSB_ERROR_THRESHOLD = sizeof(SAL_App_Signal_Calib_PCOMP_ADC_LSB_ERROR_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 197
def SALGetSignal_COMTxSignal_AM_DIAG_089():
    return SALComGetSignal_COMTxSignal_AM_DIAG_089

struct_anon_7.__slots__ = [
    'member14',
    'member15',
]
struct_anon_7._fields_ = [
    ('member14', uint32 * 2),
    ('member15', boolean),
]

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1035
SALGetSignalSize_Signal_Calib_HWMON_AC_L1_V_RMS_OV_QT = sizeof(SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_OV_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1290
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MAX():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_SENSOR_FAULT_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 127
SALGetSignalSize_Dem_Fault5 = sizeof(SAL_App_Dem_Fault5)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1233
def SALGetSignal_COMTxSignal_AM_ODD_B4():
    return SALComGetSignal_COMTxSignal_AM_ODD_B4

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 427
SALGetSignalSize_Signal_GridEval_AC_L3_PWR_FACTOR = sizeof(SAL_App_Signal_GridEval_AC_L3_PWR_FACTOR)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 670
def SALGetSignal_TstMan_PComp_Signal_PFC3PhaseCurrAMesFactor_Value():
    return SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrAMesFactor_Value

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1314
def SALGetSignal_Signal_Calib_PCOMP_AFE_CURRENT_LB_SENSORGAIN_VALUE():
    return SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LB_SENSORGAIN_VALUE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 218
def SALGetSignal_COMTxSignal_AM_DIAG_086():
    return SALComGetSignal_COMTxSignal_AM_DIAG_086

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 978
def SALGetSignal_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMIN_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMIN_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1231
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LA_QT = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LA_QT)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 96
def SALGetSignal_Signal_Com_MA_REQUEST_OP_Monitoring_Fault():
    return SAL_App_Signal_Com_MA_REQUEST_OP_Monitoring_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1058
def SALGetSignal_COMTxSignal_AM_E2E_CHK_05():
    return SALComGetSignal_COMTxSignal_AM_E2E_CHK_05

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 402
def SALGetSignal_Signal_GridEval_AC_L1L2_ZC_Counter():
    return SAL_App_Signal_GridEval_AC_L1L2_ZC_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 645
SALGetSignalSize_TstMan_RelAct_Signal_PWM_AC_L1L2_RD = sizeof(SAL_App_TstMan_RelAct_Signal_PWM_AC_L1L2_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 959
SALGetSignalSize_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK01_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_3PH_ANGLEDEGREECHECK01_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1214
def SALGetSignal_Signal_Calib_HWMON_AC_L1_FUSE_BLOWN_MAX():
    return SAL_App_Signal_Calib_HWMON_AC_L1_FUSE_BLOWN_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 101
SALGetSignalSize_Signal_Com_MA_MCMP_InvalidValue_Fault = sizeof(SAL_App_Signal_Com_MA_MCMP_InvalidValue_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 85
def SALGetSignal_COMTxSignal_AM_DIAG_105():
    return SALComGetSignal_COMTxSignal_AM_DIAG_105

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 974
def SALGetSignal_COMTxSignal_AM_E2E_CHK_03():
    return SALComGetSignal_COMTxSignal_AM_E2E_CHK_03

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 415
SALGetSignalSize_Signal_GridEval_AC_L1L2_ZC_Max_Counter = sizeof(SAL_App_Signal_GridEval_AC_L1L2_ZC_Max_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 658
def SALGetSignal_TstMan_PComp_Signal_PFC3PhaseCurrAMesOffset_Value():
    return SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrAMesOffset_Value

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 966
def SALGetSignal_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMAX_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMAX_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1219
SALGetSignalSize_Signal_Calib_HWMON_AC_L2_FUSE_BLOWN_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AC_L2_FUSE_BLOWN_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 84
def SALGetSignal_Signal_Com_MA_V2X_InvalidValue_Fault():
    return SAL_App_Signal_Com_MA_V2X_InvalidValue_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 215
def SALGetSignal_Signal_PWM_AFE_L3_RD():
    return SALIoHwAb_PWM_AFE_L3_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 855
def SALGetSignal_COMTxSignal_AM_HW_VS_V():
    return SALComGetSignal_COMTxSignal_AM_HW_VS_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 390
def SALGetSignal_Signal_GridEval_AC_L1L2_V_RMS():
    return SAL_App_Signal_GridEval_AC_L1L2_V_RMS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 633
SALGetSignalSize_TstMan_RelAct_Signal_PWM_AFE_L3_RD = sizeof(SAL_App_TstMan_RelAct_Signal_PWM_AFE_L3_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 931
SALGetSignalSize_Signal_Calib_GRIDEVAL_TIMERVALID_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_TIMERVALID_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1186
def SALGetSignal_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_VFACTOR():
    return SAL_App_Signal_Calib_HWMON_AC_L3_OPEN_CIRCUIT_VFACTOR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 233
def SALGetSignal_Signal_PWM_AC_L2_RD():
    return SALIoHwAb_PWM_AC_L2_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 876
def SALGetSignal_COMTxSignal_AM_E2E_CNT_06():
    return SALComGetSignal_COMTxSignal_AM_E2E_CNT_06

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 355
SALGetSignalSize_Signal_GridEval_AC_L2L3_V_PK = sizeof(SAL_App_Signal_GridEval_AC_L2L3_V_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 604
def SALGetSignal_Signal_AFE_TEMP_LB():
    return SAL_App_Signal_AFE_TEMP_LB

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 906
def SALGetSignal_Signal_Calib_HWCFG_3PH_22_KW_SYS_22KW_IS_MAX():
    return SAL_App_Signal_Calib_HWCFG_3PH_22_KW_SYS_22KW_IS_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1159
SALGetSignalSize_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LC_IS_CURR_ACTIVE_OFFSET_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 183
def SALGetSignal_Signal_DIO_AFE_LA_DRV_PS_PG():
    return SALIoHwAb_DIO_AFE_LA_DRV_PS_PG

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 813
def SALGetSignal_COMTxSignal_AM_DIAG_003():
    return SALComGetSignal_COMTxSignal_AM_DIAG_003

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 295
SALGetSignalSize_Signal_GridEval_AC_L1_IS_RMS = sizeof(SAL_App_Signal_GridEval_AC_L1_IS_RMS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 855
SALGetSignalSize_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MIN_VALUE = sizeof(SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_ONE_PHASE_MIN_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1110
def SALGetSignal_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_QT():
    return SAL_App_Signal_Calib_HWMON_DCLINKVOLTAGE_OUT_OF_RANGE_DELTA_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 37
def SALGetSignal_Signal_ADC_AC_L2PF_VS_S1():
    return SALIoHwAb_ADC_IF_ADC_B12_SOC0_S1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 610
def SALGetSignal_COMTxSignal_AM_DIAG_032():
    return SALComGetSignal_COMTxSignal_AM_DIAG_032

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 262
def SALGetSignal_Signal_GridEval_AC_L3_V_POS_PK():
    return SAL_App_Signal_GridEval_AC_L3_V_POS_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 830
def SALGetSignal_Signal_Calib_STMAN_V2L_AC_STABILIZATION_TIMER():
    return SAL_App_Signal_Calib_STMAN_V2L_AC_STABILIZATION_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1083
SALGetSignalSize_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_TEMPDELTA = sizeof(SAL_App_Signal_Calib_HWMON_VOLTAGE_PLAUSIBILITY_TEMPDELTA)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 491
def SALGetSignal_COMTxSignal_AM_DIAG_049():
    return SALComGetSignal_COMTxSignal_AM_DIAG_049

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 207
SALGetSignalSize_Signal_ClaIf_CM_PLL_STATUS_3PH = sizeof(SAL_App_Signal_ClaIf_CM_PLL_STATUS_3PH)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 795
SALGetSignalSize_Signal_Calib_STMAN_G2V_PRECHARGE_DONE_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_DONE_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1050
def SALGetSignal_Signal_Calib_HWMON_AC_L2_V_RMS_OV_DQ():
    return SAL_App_Signal_Calib_HWMON_AC_L2_V_RMS_OV_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 33
SALGetSignalSize_Signal_ComE2E_MA_POWER_Checksum_Fault = sizeof(SAL_App_Signal_ComE2E_MA_POWER_Checksum_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 525
SALGetSignalSize_Signal_PComp_CMPSS1_DACHVAL = sizeof(SAL_App_Signal_PComp_CMPSS1_DACHVAL)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 762
def SALGetSignal_Signal_Calib_STMAN_OFF_TO_RUN_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_OFF_TO_RUN_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1360
SALGetSignalSize_Signal_Calib_DERAT_MOSFET_LC_WORK_COEF = sizeof(SAL_App_Signal_Calib_DERAT_MOSFET_LC_WORK_COEF)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 400
def SALGetSignal_COMTxSignal_AM_DIAG_060():
    return SALComGetSignal_COMTxSignal_AM_DIAG_060

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 192
def SALGetSignal_Signal_StMan_PCompDeadTimePassed():
    return SAL_App_Signal_StMan_PCompDeadTimePassed

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 802
def SALGetSignal_Signal_Calib_STMAN_G2V_PREPARE_TO_RUN_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_PREPARE_TO_RUN_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1055
SALGetSignalSize_Signal_Calib_HWMON_AC_L3_V_RMS_OV_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AC_L3_V_RMS_OV_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 500
def SALGetSignal_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LA_IS():
    return SAL_App_Signal_PComp_ZERO_CURRENT_VS_STANDBY_AFE_LA_IS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 741
SALGetSignalSize_TstMan_StMan_Signal_NumberOfPhasesConfigured = sizeof(SAL_App_TstMan_StMan_Signal_NumberOfPhasesConfigured)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1371
def SALGetSignalArray_Signal_Calib_DERAT_RELAY_WORK_COEF(index):
    return (SAL_App_Signal_Calib_DERAT_RELAY_WORK_COEF [index])

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 449
def SALGetSignal_COMTxSignal_AM_DIAG_055():
    return SALComGetSignal_COMTxSignal_AM_DIAG_055

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 197
SALGetSignalSize_Signal_StMan_DriverPowerUpSeq_InProgress = sizeof(SAL_App_Signal_StMan_DriverPowerUpSeq_InProgress)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1261
def SALGetSignal_COMRxSignal_MA_E2E_CHK_02():
    return SALComGetSignal_COMRxSignal_MA_E2E_CHK_02

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 465
SALGetSignalSize_Signal_PComp_PFC3PhaseCurrCMesOffset = sizeof(SAL_App_Signal_PComp_PFC3PhaseCurrCMesOffset)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 708
def SALGetSignal_TstMan_StMan_Signal_ST_AFE_L3_RD():
    return SAL_App_TstMan_StMan_Signal_ST_AFE_L3_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1350
SALGetSignalSize_Signal_Calib_DERAT_MOSFET_LA_WORK_COEF = sizeof(SAL_App_Signal_Calib_DERAT_MOSFET_LA_WORK_COEF)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 358
def SALGetSignal_COMTxSignal_AM_DIAG_066():
    return SALComGetSignal_COMTxSignal_AM_DIAG_066

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1018
def SALGetSignal_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_THRESHOLD():
    return SAL_App_Signal_Calib_RELACT_STATE_DELAY_CLOSE_RELAY_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1271
SALGetSignalSize_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MIN = sizeof(SAL_App_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 164
def SALGetSignal_Signal_StMan_STMAN_SUBSTATE():
    return SAL_App_Signal_StMan_STMAN_SUBSTATE

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1198
def SALGetSignal_COMTxSignal_AM_NODE_ID():
    return SALComGetSignal_COMTxSignal_AM_NODE_ID

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 472
def SALGetSignal_Signal_PComp_PFC3PhaseCurrBMesFactor():
    return SAL_App_Signal_PComp_PFC3PhaseCurrBMesFactor

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 713
SALGetSignalSize_TstMan_StMan_Signal_ST_AC_N_RD = sizeof(SAL_App_TstMan_StMan_Signal_ST_AC_N_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1319
SALGetSignalSize_Signal_Calib_PCOMP_AFE_CURRENT_LC_SENSORGAIN_VALUE = sizeof(SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LC_SENSORGAIN_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 239
def SALGetSignal_COMTxSignal_AM_DIAG_083():
    return SALComGetSignal_COMTxSignal_AM_DIAG_083

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1031
SALGetSignalSize_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_IMAX = sizeof(SAL_App_Signal_Calib_HWMON_TEMPERATURE_PLAUSIBILITY_IMAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1286
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MIN():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_SENSOR_FAULT_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 139
SALGetSignalSize_Dem_Fault8 = sizeof(SAL_App_Dem_Fault8)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1219
def SALGetSignal_COMTxSignal_AM_ODD_B2():
    return SALComGetSignal_COMTxSignal_AM_ODD_B2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 697
SALGetSigGroupRef_StMan_TstMan_Group = pointer(ptr_to_0)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1006
def SALGetSignal_Signal_Calib_RELACT_STATE_DELAY_ZERO_CROSS_TIME():
    return SAL_App_Signal_Calib_RELACT_STATE_DELAY_ZERO_CROSS_TIME

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1259
SALGetSignalSize_Signal_Calib_HWMON_AFE_TEMP_LC_DQ = sizeof(SAL_App_Signal_Calib_HWMON_AFE_TEMP_LC_DQ)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 92
def SALGetSignal_Signal_Com_MA_REQUEST_OP_InvalidValue_Fault():
    return SAL_App_Signal_Com_MA_REQUEST_OP_InvalidValue_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1100
def SALGetSignal_COMTxSignal_AM_DER_FACT():
    return SALComGetSignal_COMTxSignal_AM_DER_FACT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 398
def SALGetSignal_Signal_GridEval_AC_L3L1_V_RMS():
    return SAL_App_Signal_GridEval_AC_L3L1_V_RMS

SAL_TEST2 = struct_anon_3
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 33

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 641
SALGetSignalSize_TstMan_RelAct_Signal_PWM_AC_L2_RD = sizeof(SAL_App_TstMan_RelAct_Signal_PWM_AC_L2_RD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 971
SALGetSignalSize_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMIN_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMIN_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1226
def SALGetSignal_Signal_Calib_HWMON_AC_RLY_TEMP_QT():
    return SAL_App_Signal_Calib_HWMON_AC_RLY_TEMP_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 67
SALGetSignalSize_Signal_NM_FAULT_ERROR_PASSIVE = sizeof(SAL_App_Signal_NM_FAULT_ERROR_PASSIVE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 127
def SALGetSignal_COMTxSignal_AM_DIAG_099():
    return SALComGetSignal_COMTxSignal_AM_DIAG_099

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1016
def SALGetSignal_COMTxSignal_AM_E2E_CHK_04():
    return SALComGetSignal_COMTxSignal_AM_E2E_CHK_04

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 363
SALGetSignalSize_Signal_GridEval_AC_L2L3_V_NEG_PK = sizeof(SAL_App_Signal_GridEval_AC_L2L3_V_NEG_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 612
def SALGetSignal_Signal_AC_FLY_TEMP():
    return SAL_App_Signal_AC_FLY_TEMP

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 914
def SALGetSignal_Signal_Calib_GRIDEVAL_PHASECHECK_VOLTAGE_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_PHASECHECK_VOLTAGE_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1167
SALGetSignalSize_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_IMIN = sizeof(SAL_App_Signal_Calib_HWMON_AC_L1_OPEN_CIRCUIT_IMIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 203
def SALGetSignal_Signal_PWM_AC_L3_RD():
    return SALIoHwAb_PWM_AC_L3_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 841
def SALGetSignal_COMTxSignal_AM_E2E_CHK_08():
    return SALComGetSignal_COMTxSignal_AM_E2E_CHK_08

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 338
def SALGetSignal_Signal_GridEval_AC_L3_ZC_Max_Counter():
    return SAL_App_Signal_GridEval_AC_L3_ZC_Max_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 587
SALGetSignalSize_Signal_TstMan_Mode_GridEval = sizeof(SAL_App_Signal_TstMan_Mode_GridEval)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 895
SALGetSignalSize_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_11KW_IS_MAX = sizeof(SAL_App_Signal_Calib_HWCFG_1PH_7_4_KW_SYS_11KW_IS_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1150
def SALGetSignal_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MIN():
    return SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MIN

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 137
def SALGetSignal_Signal_ADC_AC_RLY_TEMP():
    return SALIoHwAb_ADC_AC_RLY_TEMP

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 750
def SALGetSignal_COMTxSignal_AM_DIAG_012():
    return SALComGetSignal_COMTxSignal_AM_DIAG_012

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 351
SALGetSignalSize_Signal_GridEval_AC_L1L2_V_NEG_PK = sizeof(SAL_App_Signal_GridEval_AC_L1L2_V_NEG_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 600
def SALGetSignal_Signal_AFE_TEMP_LA():
    return SAL_App_Signal_AFE_TEMP_LA

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 270
def SALGetSignal_Signal_GridEval_AC_L1_dV_PK():
    return SAL_App_Signal_GridEval_AC_L1_dV_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 902
def SALGetSignal_Signal_Calib_HWCFG_1PH_3_6_KW_SYS_11KW_IS_MAX():
    return SAL_App_Signal_Calib_HWCFG_1PH_3_6_KW_SYS_11KW_IS_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1155
SALGetSignalSize_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MAX = sizeof(SAL_App_Signal_Calib_HWMON_AFE_LB_IS_CURR_ACTIVE_OFFSET_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 52
def SALGetSignal_Signal_ADC_AC_L3PF_VS_S2():
    return SALIoHwAb_ADC_IF_ADC_C11_SOC3_S2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 631
def SALGetSignal_COMTxSignal_AM_DIAG_029():
    return SALComGetSignal_COMTxSignal_AM_DIAG_029

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 326
def SALGetSignal_Signal_GridEval_AC_L3_ZC_Counter():
    return SAL_App_Signal_GridEval_AC_L3_ZC_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 575
SALGetSignalSize_Signal_TstMan_Mode_StMan = sizeof(SAL_App_Signal_TstMan_Mode_StMan)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 243
SALGetSignalSize_Signal_GridEval_AC_L1_V_NEG_PK = sizeof(SAL_App_Signal_GridEval_AC_L1_V_NEG_PK)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 867
SALGetSignalSize_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MAX_VALUE = sizeof(SAL_App_Signal_Calib_STMAN_G2V_AC_PEAK_THREE_PHASES_MAX_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1122
def SALGetSignal_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MAX():
    return SAL_App_Signal_Calib_HWMON_AFE_LA_IS_CURR_OFFSET_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 67
def SALGetSignal_Signal_ADC_AFE_LA_IS_S1():
    return SALIoHwAb_ADC_AFE_LA_IS_S1

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 652
def SALGetSignal_COMTxSignal_AM_DIAG_026():
    return SALComGetSignal_COMTxSignal_AM_DIAG_026

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 258
def SALGetSignal_Signal_GridEval_AC_L3_V_PK():
    return SAL_App_Signal_GridEval_AC_L3_V_PK

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 842
def SALGetSignal_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA2():
    return SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_THRESHOLD_DELTA2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1095
SALGetSignalSize_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_TEMPDELTA = sizeof(SAL_App_Signal_Calib_HWMON_CURRENT_PLAUSIBILITY_TEMPDELTA)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 22
def SALGetSignal_Signal_ADC_AC_L1PF_VS_3PH_S2():
    return SALIoHwAb_ADC_IF_ADC_A2_SOC3_S2

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 589
def SALGetSignal_COMTxSignal_AM_DIAG_035():
    return SALComGetSignal_COMTxSignal_AM_DIAG_035

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 231
SALGetSignalSize_Signal_GridEval_Operation_Mode = sizeof(SAL_App_Signal_GridEval_Operation_Mode)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 791
SALGetSignalSize_Signal_Calib_STMAN_G2V_PRECHARGE_FAIL_TIMEOUT_TIMER = sizeof(SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_FAIL_TIMEOUT_TIMER)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1046
def SALGetSignal_Signal_Calib_HWMON_AC_L1_V_RMS_OV_DQ():
    return SAL_App_Signal_Calib_HWMON_AC_L1_V_RMS_OV_DQ

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1401
def SALGetSignal_COMRxSignal_MA_ODD_CMD():
    return SALComGetSignal_COMRxSignal_MA_ODD_CMD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 45
SALGetSignalSize_Signal_ComE2E_MA_V2X_Counter_Fault = sizeof(SAL_App_Signal_ComE2E_MA_V2X_Counter_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 537
SALGetSignalSize_Signal_PComp_CMPSS2_DACLVAL = sizeof(SAL_App_Signal_PComp_CMPSS2_DACLVAL)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 774
def SALGetSignal_Signal_Calib_STMAN_G2V_PRECHARGE_RUN_TIMEOUT_TIMER():
    return SAL_App_Signal_Calib_STMAN_G2V_PRECHARGE_RUN_TIMEOUT_TIMER

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1356
def SALGetSignalArray_Signal_Calib_DERAT_MOSFET_LB_WORK_COEF(index):
    return (SAL_App_Signal_Calib_DERAT_MOSFET_LB_WORK_COEF [index])

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 386
def SALGetSignal_COMTxSignal_AM_DIAG_062():
    return SALComGetSignal_COMTxSignal_AM_DIAG_062

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 202
def SALGetSignal_Signal_ClaIf_CM_PLL_STATUS_1PH():
    return SAL_App_Signal_ClaIf_CM_PLL_STATUS_1PH

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 512
def SALGetSignal_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LA_IS():
    return SAL_App_Signal_PComp_ZERO_CURRENT_VS_ACTIVE_AFE_LA_IS

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 751
SALGetSignalSize_TstMan_GridEval_Signal_Operation_Mode = sizeof(SAL_App_TstMan_GridEval_Signal_Operation_Mode)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1327
SALGetSignalSize_Signal_Calib_PCOMP_AFE_DC_VOLTAGE_SENSORGAIN_VALUE = sizeof(SAL_App_Signal_Calib_PCOMP_AFE_DC_VOLTAGE_SENSORGAIN_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 267
def SALGetSignal_COMTxSignal_AM_DIAG_079():
    return SALComGetSignal_COMTxSignal_AM_DIAG_079

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 147
SALGetSignalSize_Dem_Fault10 = sizeof(SAL_App_Dem_Fault10)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1359
def SALGetSignal_COMRxSignal_MA_E2E_CNT_03():
    return SALComGetSignal_COMRxSignal_MA_E2E_CNT_03

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 461
SALGetSignalSize_Signal_PComp_PFC3PhaseCurrBMesOffset = sizeof(SAL_App_Signal_PComp_PFC3PhaseCurrBMesOffset)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 704
def SALGetSignal_TstMan_StMan_Signal_ST_AC_L1L2_RD():
    return SAL_App_TstMan_StMan_Signal_ST_AC_L1L2_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1302
def SALGetSignal_Signal_Calib_PCOMP_ZERO_CURRENT_VS_X_NO_OF_SAMPLES():
    return SAL_App_Signal_Calib_PCOMP_ZERO_CURRENT_VS_X_NO_OF_SAMPLES

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 176
def SALGetSignal_COMTxSignal_AM_DIAG_092():
    return SALComGetSignal_COMTxSignal_AM_DIAG_092

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1014
def SALGetSignal_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_MAX_ERROR():
    return SAL_App_Signal_Calib_RELACT_STATE_DELAY_OPEN_RELAY_MAX_ERROR

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1267
SALGetSignalSize_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MAX = sizeof(SAL_App_Signal_Calib_HWMON_HV1_PRI_TEMP_SENSOR_FAULT_MAX)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 130
def SALGetSignal_Dem_Fault6():
    return SAL_App_Dem_Fault6

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1240
def SALGetSignal_COMTxSignal_AM_ODD_B5():
    return SALComGetSignal_COMTxSignal_AM_ODD_B5

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 438
def SALGetSignal_Signal_GridEval_AC_L1L2_PhaseDegree():
    return SAL_App_Signal_GridEval_AC_L1L2_PhaseDegree

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 679
SALGetSignalSize_TstMan_PComp_Signal_PFC3PhaseCurrCMesFactor_Value = sizeof(SAL_App_TstMan_PComp_Signal_PFC3PhaseCurrCMesFactor_Value)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1315
SALGetSignalSize_Signal_Calib_PCOMP_AFE_CURRENT_LB_SENSORGAIN_VALUE = sizeof(SAL_App_Signal_Calib_PCOMP_AFE_CURRENT_LB_SENSORGAIN_VALUE)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 225
def SALGetSignal_COMTxSignal_AM_DIAG_085():
    return SALComGetSignal_COMTxSignal_AM_DIAG_085

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 979
SALGetSignalSize_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMIN_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_1PH_LINERMSVOLTAGEMIN_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1234
def SALGetSignal_Signal_Calib_HWMON_AFE_TEMP_LB_QT():
    return SAL_App_Signal_Calib_HWMON_AFE_TEMP_LB_QT

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 135
SALGetSignalSize_Dem_Fault7 = sizeof(SAL_App_Dem_Fault7)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 403
SALGetSignalSize_Signal_GridEval_AC_L1L2_ZC_Counter = sizeof(SAL_App_Signal_GridEval_AC_L1L2_ZC_Counter)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 648
def SALGetSignal_TstMan_RelAct_Signal_PWM_AC_L3_RD():
    return SAL_App_TstMan_RelAct_Signal_PWM_AC_L3_RD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 954
def SALGetSignal_Signal_Calib_GRIDEVAL_3PH_LINERMSVOLTAGE_THRESHOLD():
    return SAL_App_Signal_Calib_GRIDEVAL_3PH_LINERMSVOLTAGE_THRESHOLD

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1207
SALGetSignalSize_Signal_Calib_HWMON_AC_1_65V_VS_MIN = sizeof(SAL_App_Signal_Calib_HWMON_AC_1_65V_VS_MIN)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 104
def SALGetSignal_Signal_Com_MA_MCMP_Monitoring_Fault():
    return SAL_App_Signal_Com_MA_MCMP_Monitoring_Fault

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 92
def SALGetSignal_COMTxSignal_AM_DIAG_104():
    return SALComGetSignal_COMTxSignal_AM_DIAG_104

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 981
def SALGetSignal_COMTxSignal_AM_AC_PH_1_RMS_V():
    return SALComGetSignal_COMTxSignal_AM_AC_PH_1_RMS_V

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 410
def SALGetSignal_Signal_GridEval_AC_L3L1_ZC_Counter():
    return SAL_App_Signal_GridEval_AC_L3L1_ZC_Counter

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 967
SALGetSignalSize_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMAX_THRESHOLD = sizeof(SAL_App_Signal_Calib_GRIDEVAL_3PH_FREQUENCYMAX_THRESHOLD)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1222
def SALGetSignal_Signal_Calib_HWMON_AC_L3_FUSE_BLOWN_MAX():
    return SAL_App_Signal_Calib_HWMON_AC_L3_FUSE_BLOWN_MAX

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 77
SALGetSignalSize_Signal_Com_MA_POWER_InvalidValue_Fault = sizeof(SAL_App_Signal_Com_MA_POWER_InvalidValue_Fault)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 113
def SALGetSignal_COMTxSignal_AM_DIAG_101():
    return SALComGetSignal_COMTxSignal_AM_DIAG_101

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 391
SALGetSignalSize_Signal_GridEval_AC_L1L2_V_RMS = sizeof(SAL_App_Signal_GridEval_AC_L1L2_V_RMS)

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 41
class struct_anon_4(Structure):
    pass

union_anon_14.__slots__ = [
    'Client',
    'Clients',
]
union_anon_14._fields_ = [
    ('Client', struct_anon_13),
    ('Clients', uint8),
]

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\HFL\Src\Hfl.h: 179
try:
    HflConfig = (HFLConfigType * 3).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'HflConfig')
except:
    pass

union_anon_16.__slots__ = [
    'Client',
    'Clients',
]
union_anon_16._fields_ = [
    ('Client', struct_anon_15),
    ('Clients', uint8),
]

SalEvt_EvtOnUp_Activated_Stop_Type = union_anon_16
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 53

SalEvt_EvtOnCh_Activated_Stop_Type = union_anon_14
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 41

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 73
class struct_anon_9(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 1416
for _lib in _libs.values():
    if not hasattr(_lib, 'SAL_NvM_RequestHandling'):
        continue
    SAL_NvM_RequestHandling = _lib.SAL_NvM_RequestHandling
    SAL_NvM_RequestHandling.argtypes = [SAL_NvM_BlockIdType, SAL_MemStackRequestType, SAL_AppSingleBlockCbkPtrType]
    SAL_NvM_RequestHandling.restype = None
    break

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 48
class struct_anon_5(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 217
try:
    EvtOnCh_Activated_Stop = (SalEvt_EvtOnCh_Activated_Stop_Type).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'EvtOnCh_Activated_Stop')
except:
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 219
try:
    EvtOnUp_Activated_Stop = (SalEvt_EvtOnUp_Activated_Stop_Type).in_dll(_libs['C:/Projects/ygr_oem_ei_00128_stla_obc_sw/05_Units/PFC/__build__/hfl_utest/hfl_utest.dll'], 'EvtOnUp_Activated_Stop')
except:
    pass

struct_anon_9.__slots__ = [
    'member19',
]
struct_anon_9._fields_ = [
    ('member19', SAL_TEST5),
]

struct_anon_5.__slots__ = [
    'member8',
    'member9',
    'member10',
]
struct_anon_5._fields_ = [
    ('member8', SAL_TEST2 * 4),
    ('member9', uint32),
    ('member10', SAL_TEST),
]

SAL_TEST4 = struct_anon_5
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 48

SAL_TEST8 = struct_anon_9
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 73

struct_anon_4.__slots__ = [
    'member5',
    'member7',
    'member4',
    'member6',
]
struct_anon_4._fields_ = [
    ('member5', SAL_TEST2),
    ('member7', uint16),
    ('member4', SAL_TEST),
    ('member6', boolean),
]

SAL_TEST3 = struct_anon_4
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 41

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 79
class struct_anon_10(Structure):
    pass

# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 68
class struct_anon_8(Structure):
    pass

SAL_TEST9 = struct_anon_10
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 79

struct_anon_10.__slots__ = [
    'member23',
    'member22',
]
struct_anon_10._fields_ = [
    ('member23', SAL_TEST3),
    ('member22', uint32),
]

SAL_TEST7 = struct_anon_8
# C:\Projects\ygr_oem_ei_00128_stla_obc_sw\05_Units\PFC\SAL\Src\Sal.h: 68

struct_anon_8.__slots__ = [
    'member16',
    'member17',
    'member18',
]
struct_anon_8._fields_ = [
    ('member16', SAL_TEST4),
    ('member17', uint32, 29),
    ('member18', uint32, 3),
]

def EUT_GetCVariable(name, type_):
    return (type_).in_dll(_libs[list(_libs.keys())[0]], name)

def EUT_GetCFunction(name, argtypes=[], restype=None):
    if hasattr(_libs[list(_libs.keys())[0]], name):
        fct = getattr(_libs[list(_libs.keys())[0]], name)
        fct.argtypes = argtypes
        fct.restype = restype
    else:
        raise Exception('Function %s does not exist!' % name)
    return fct

# No inserted files

