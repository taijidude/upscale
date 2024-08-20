
from rembg import remove
import typer
from pathlib import Path

def main(file_to_process: Path):
    if not file_to_process.exists():
        raise Exception("Der Pfad: "+str(file_to_process)+" existiert nicht!")
    
    output_path = Path('.').joinpath('background-removed').joinpath(file_to_process)

    with open(file_to_process, 'rb') as i:
        with open(output_path, 'xb') as o:
            input = i.read()
            output = remove(file_to_process)
            o.write(output_path)


if __name__ == "__main__":
    print("Remove Background started...")
    typer.run(main)
