from PIL import Image
import piexif
import os
from datetime import datetime, timedelta

location = "/media/dwegmull/HOLGA/DCIM/100MEDIA/"

files = os.listdir(location)

# Exif time codes will be dated today and each file will be separated from the next by one second.
numberOfFiles = len(files)
a = datetime.now()
d = timedelta(seconds=-numberOfFiles)
a = a  + d
d = timedelta(seconds=1)

for file in files:
    img = Image.open(location + file)
    exif_dict = piexif.load(img.info["exif"])
    exifList = exif_dict["Exif"]
    exifList[36867] = str(a.year)+":"+str(a.month)+":"+str(a.day)+" "+str(a.hour)+":"+str(a.minute)+":"+str(a.second)
    a = a + d
    print a
    img.save(location + file, exif=piexif.dump(exif_dict))
    
