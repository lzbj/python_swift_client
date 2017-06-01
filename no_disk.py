import zipfile
import requests
import StringIO

u = requests.get("http://www.pythonchallenge.com/pc/def/channel.zip")
f = StringIO.StringIO()
f.len
f.read
f.write(u.content)

def extract_zip(input_zip):
    input_zip = zipfile.ZipFile(input_zip)
    return {i: input_zip.read(i) for i in input_zip.namelist()}
extracted = extract_zip(f)

print extracted