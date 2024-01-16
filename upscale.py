import cv2
import sys 
import os
from pathlib import Path

print("Upscale wird gestartet...")

imageName = os.getenv('file_to_convert')

fileToWorkWith=Path(imageName)
if not fileToWorkWith.is_file():
    print("Die Datei "+str(fileToWorkWith)+" existiert nicht!")
    sys.exit(1)

print('Datei gefunden...')


fileToWorkWith = str(fileToWorkWith)

print('SR object erzeugen')
sr = cv2.dnn_superres.DnnSuperResImpl.create()

print('Bild einlesen')  
image = cv2.imread(fileToWorkWith)
print(image.shape)



print('Read the desired model')
path = "LapSRN_x2.pb"
sr.readModel(path)

print('Set the desired model and scale to get correct pre- and post-processing') 
sr.setModel("lapsrn", 2)

print('Upscale the image')
result = sr.upsample(image)  
print(result.shape)
print('Save the image')
cv2.imwrite('./out/upscaled-'+imageName, result)