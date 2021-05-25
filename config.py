import sys as _sys
import os as _os

__all__ = [
    'MODEL_PATH',
    'TOLERANCE',

    'ALLOWED_MIMETYPES',
    'ALLOWED_PIL_FORMATS',
]

_PREFIX = 'SENYA'
def _die(m):
    print(m, file=_sys.stderr)
    _sys.exit(1)

ALLOWED_MIMETYPES = {
    'image/jpeg',
    'image/png',

    'application/octet-stream',
}

ALLOWED_PIL_FORMATS = (
    'JPEG',
    'PNG',
)

_model_path = _os.getenv(f'{_PREFIX}_MODEL_PATH')
if not _model_path:
    _die(f'ERROR: env var {_PREFIX}_MODEL_PATH is required')
MODEL_PATH = _model_path

TOLERANCE = None
_tolerance = _os.getenv(f'{_PREFIX}_TOLERANCE')
if _tolerance:
    try:
        _tolerance = float(_tolerance)
        if not (0 <= _tolerance <= 1):
            raise ValueError('out of range')
        TOLERANCE = _tolerance
    except ValueError:
        _die(f'invalid value for {_PREFIX}_TOLERANCE – must be float in [0, 1] range')
