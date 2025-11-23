import base64
import zipfile

z = zipfile.ZipFile("zip_99.zip")
pa = base64.b64decode(open("password_99.txt", "rb").read())
pass_list = [pa]

while True:
    zi = None
    pa_ = None
    if len(z.filelist) != 2:
        break

    for f in z.filelist:
        if f.filename.endswith(".txt"):
            pa_ = z.extract(f.filename, pwd=pa)
        elif f.filename.endswith(".zip"):
            f = z.extract(f.filename, pwd=pa)
            zi = zipfile.ZipFile(f)

    pa = base64.b64decode(open(pa_, "rb").read())
    print(pa_, pa, z, zi)
    z = zi
    pass_list.append(pa)
    pass
open("pw.bin", "wb").write(b''.join(pass_list[::-1]))
