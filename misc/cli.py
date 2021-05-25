import sys
from senya import load_faces, extract_faces, any_same_face

if __name__ == '__main__':
    supersenya = load_faces(sys.argv[1])
    for fn in sys.argv[2:]:
        print(fn, end=': ')
        faces = extract_faces(fn)

        if any_same_face(supersenya, faces):
            print("О, Сеня!")
        else:
            print(f'нашел {len(faces)} ебла, но где Сеня...')
