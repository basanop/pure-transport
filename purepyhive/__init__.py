__version__ = '0.1.0'
__version_info__ = (0, 0, 2)

try:
    from .factory import transport_factory
except ImportError:
    pass
