import numpy as np
import PIL.Image
import face_recognition.api as face_recognition
from threading import Lock

DEFAULT_TOLERANCE = 0.69 # nice

try:
    import dlib.cuda
    try:
        dlib.cuda.get_num_devices()
        has_cuda = True
    except RuntimeError:
        has_cuda = False
    del dlib.cuda
except ImportError:
    has_cuda = False

DEFAULT_MODEL = 'cnn' if has_cuda else 'hog'

# face_recognition.api is not thread safe
_model_lock = Lock()

def load_faces(f):
    return list(np.load(f)['supersenya'])

def cmp_face(v1, v2):
    if isinstance(v2, list) and len(v2) > 1:
        raise Exception('v2 cant be list')
    if isinstance(v1, list) and len(v1) > 1:
        return np.mean([np.linalg.norm(x - v2) for x in v1])
    return np.linalg.norm(v1 - v2)

def same_face(v1, v2, tol=DEFAULT_TOLERANCE):
    return cmp_face(v1, v2) <= tol

def extract_faces(im, mode='RGB', model=DEFAULT_MODEL, upsample=0):
    if not isinstance(im, PIL.Image.Image):
        im = PIL.Image.open(im)
    im = np.array(im.convert(mode))

    with _model_lock:
        loc = face_recognition.face_locations(im, number_of_times_to_upsample=upsample, model=model)
        if len(loc) == 0:
            return []

        enc = face_recognition.face_encodings(im, known_face_locations=loc)
        return enc

def any_same_face(target, faces, tol=DEFAULT_TOLERANCE):
    return any(same_face(target, f, tol) for f in faces)
