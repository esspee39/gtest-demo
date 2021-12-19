import re

def containsMutant(file, mutant):
    reg = re.compile(mutant)
    with open(file, "r") as f:
        if re.search(reg, f.read()):
            return True
        else:
            return False
    close()
