import difflib as dl

def generateHTMLDiff(srcname, mutantname):
    with open("../src/" + srcname) as f:
        original_file = f.read()

    with open("../mutants/" + mutantname + "/src/" + srcname.replace(".cpp", "_" + mutantname + ".cpp")) as f:
        mutated_file = f.read()

    hd = dl.HtmlDiff()

    diffs = hd.make_table(original_file.split("\n"), mutated_file.split("\n"), fromdesc='Source', todesc=mutantname, context=False, numlines=0)
    return diffs
    #with open("diff" + "_" + mutantname + ".html","w+") as diff_file:
    #    diff_file.write(diffs)

