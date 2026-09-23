from pathlib import Path


#preparing path to dir with project
path = Path.cwd() / "test"


#creating path to dir
path.mkdir(exist_ok = True)

file = path / "test1.txt"

#preparing info for file

info = ["First test",
        "second test",
        "third test"]




with file.open("a") as f:
    for line in info:
        f.write(line + "\n")