
from rembg import remove
import typer
from pathlib import Path
from PIL import Image

def main(file_to_process: Path):
    if not file_to_process.exists():
        raise Exception("Der Pfad: "+str(file_to_process)+" existiert nicht!")
    
    output_path = Path('.').joinpath('background-removed') #  
    output_path.mkdir(exist_ok=True, parents=True)

    output_path = output_path.joinpath(file_to_process.name)

    input = Image.open(str(file_to_process))
    output = remove(input)
    output.save(str(output_path))



  #  with open(file_to_process, 'rb') as i:
      #  with open(output_path, 'x') as o:
          #  input = i.read()
          #  output = remove(str(file_to_process))
         #   o.write(str(output_path))

if __name__ == "__main__":
    print("Remove Background started...")
    typer.run(main)
