import cv2
import sys 
import os
import typer
from pathlib import Path


def main(upscale: Path):
    if not upscale.exists():
        raise Exception("Der Pfad: "+upscale+" existiert nicht!")
    
    print('Create an SR object...')
    sr = cv2.dnn_superres.DnnSuperResImpl.create()

    print('Read image')  
    image = cv2.imread(upscale.name)
    print("Image Size - Before:")
    print(image.shape)

    print('Read the desired model')
    sr.readModel("LapSRN_x2.pb")

    print('Set the desired model and scale to get correct pre- and post-processing') 
    sr.setModel("lapsrn", 2)

    print('Upscale the image')
    result = sr.upsample(image)
    print("Image Size - Before:")
    print(result.shape)
    print('Save the image')
    cv2.imwrite('./upscaled-'+upscale.name, result)

if __name__ == "__main__":
    print("Upscale started...")
    typer.run(main)
