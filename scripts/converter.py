import os
import img2pdf

SESSIONS_DIR = '../sessions'
EXPORT_DIR = '../pdf'
SESSIONS = os.listdir(SESSIONS_DIR)

def extract_num(image) -> int:
    dgt = 0
    for ch in image:
        if ch.isdigit():
            dgt = 10*dgt + int(ch)
    return dgt

def extract_pdf(session, export_path):
    path = f"{SESSIONS_DIR}/{session}"
    images = os.listdir(path)
    srted_by_num = {}
    for pos in range(len(images)):
        srted_by_num[pos] = extract_num(images[pos])
    sorted(srted_by_num.items(), key=lambda item: item[1])
    srtImage = [0]*len(images)
    for key in srted_by_num:
        srtImage[key] = f'{path}/{images[key]}'
    with open(f'{export_path}/{session}.pdf', 'wb') as f:
        f.write(img2pdf.convert(srtImage))

if __name__ == '__main__':
    for session in SESSIONS:
        extract_pdf(session, EXPORT_DIR)
    print("SUCCESS")
