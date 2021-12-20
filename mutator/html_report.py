# to open/create a new html file in the write mode
import os
import sys
from configparser import ConfigParser
from mutant_dictionary import all_mutants
from mutant_dictionary import all_mutant_keys
import filediff
import containsmutant
import read_xml

if not os.path.exists('./config.ini'):  # Config parser - From Drew's and Luke's Code
    print("Error: Config File does not exist")
    with open('config.ini', 'w', encoding="utf-8") as f:
        f.write('testing')
        sys.exit()
else:
    file = 'config.ini'
    config = ConfigParser()
    config.read(file)
    mutants = config.options('Mutants')
    filename = "../CMakeLists.txt"
    mutant_list = []
    active_mutants = []
    created_mutants = []

    for x in mutants:  # Parses config for mutants that are marked active
        if config.get('Mutants', x) == '1':
            mutant_list.append(x)  # Creates list of active mutants from config file

    for x in all_mutant_keys:
        if x.lower() in mutant_list:
            active_mutants.append(all_mutants[x])

    for x in active_mutants:
        if containsmutant.containsMutant("../src/example.cpp", x.get_regex()):
            with open("diff" + "_" + x.get_name() + ".html", "w+") as diff_file:
                diff_file.write("""
<head><meta http-equiv="Content-Type"
 content="text/html; charset=utf-8" />
 <title></title>
 <style type="text/css">
 table.diff {font-family:Courier; border:medium;}
 diff_header {background-color:#e0e0e0}
 td.diff_header {text-align:right}
 .diff_next {background-color:#c0c0c0}
 .diff_add {background-color:#aaffaa}
 .diff_chg {background-color:#ffff77}
 .diff_sub {background-color:#ffaaaa}</style></head><body>""")
                killed = read_xml.getMutantKilledInfo(x.get_name())
                print("MUTANT :" + x.get_name() + " KILLED BY:")
                print(killed)
                if killed:
                    diff_file.write("<h1>" + x.get_name() + ": Killed by ")
                    diff_file.write(", ".join(killed))
                    diff_file.write("</h1>")
                else:
                    diff_file.write("<h1>" + x.get_name() + ": Survived")
                diffs = filediff.generateHTMLDiff("example.cpp", x.get_name())
                diff_file.write(diffs)
                diff_file.write("</body>")
            created_mutants.append(x)

f = open('MutationTesting.html', 'w')

html_out = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>C++ Mutation Testing</h2>

<p>Read Me File:<a href="../../PorcupinesMutator/README.md">README</a></p>
<p>Mutants Used:<a href="config.ini">Mutants</a></p>
<p> Mutation Test(s):</p>"""
for x in created_mutants:
    killed = read_xml.getMutantKilledInfo(x.get_name())
    if killed:
        html_out += '<a href="diff_' + x.get_name() + '.html">KILLED: ' + x.get_name() + '</a><br>'
    else:
        html_out += '<a href="diff_' + x.get_name() + '.html">SURVIVED: ' + x.get_name() + '</a><br>'

html_out += """

</body>
</html>
"""
#writing the code into the file
f.write(html_out)

# close the file
f.close()
