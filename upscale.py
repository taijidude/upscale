import cv2
import sys

imageName = sys.argv[1]

print('Create an SR object') 
sr = cv2.dnn_superres.DnnSuperResImpl.create()

print('Read image')  
image = cv2.imread('./'+imageName)
  
print('Read the desired model') 
path = "LapSRN_x2.pb"
sr.readModel(path)

print('Set the desired model and scale to get correct pre- and post-processing') 
sr.setModel("lapsrn", 2)

print('Upscale the image')
result = sr.upsample(image)  
print('Save the image')
cv2.imwrite('./out/upscaled-'+imageName, result)