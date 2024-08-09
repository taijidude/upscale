import typer
from pathlib import Path
from PIL import Image


def main(check: Path):
    if not check.exists():
        raise Exception("Der Pfad: "+str(check)+" existiert nicht!")
    image = Image.open(str(check))
    print(str(check) +' - '+ str(image.size))

if __name__ == "__main__":
    typer.run(main)