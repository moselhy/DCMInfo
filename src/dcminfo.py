import dicom, os, sys
from tempfile import NamedTemporaryFile

filename = sys.argv[1]
ds = dicom.read_file(filename)
f = NamedTemporaryFile(suffix='.TMP.txt', delete=False)
f.write(str(ds))
f.close()
os.system(f.name)