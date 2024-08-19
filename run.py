
from removebackground import remove
import typer
from pathlib import Path

def main(file_to_process: Path):
    if not file_to_process.exists():
        raise Exception("Der Pfad: "+file_to_process+" existiert nicht!")
    
    output_path = './background-removed/'+file_to_process.name

    with open(file_to_process, 'rb') as i:
        with open(output, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)


if __name__ == "__main__":
    print("Remove Background started...")
    typer.run(main)
