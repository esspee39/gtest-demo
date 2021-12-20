# to open/create a new html file in the write mode
import os
import sys
from configparser import ConfigParser
from mutant_dictionary import all_mutants
from mutant_dictionary import all_mutant_keys
import filediff
import containsmutant
import getfilename

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
            filediff.generateHTMLDiff("example.cpp", x.get_name())
            created_mutants.append(x)

f = open('MutationTesting.html', 'w')

# the html code which will go in the file GFG.html
html_template = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>C++ Mutation Testing</h2>

<p>Read Me File:<a href="../../PorcupinesMutator/README.md">README</a></p>
<p>Mutants Used:<a href="config.ini">Mutants</a></p>
<p> Mutation Test(s):</p>"""
for x in created_mutants:
      html_template +='<a href="diff_' + x.get_name() + '.html">' + x.get_name() + '</a><br>'

html_template += """

</body>
</html>
"""
#writing the code into the file
f.write(html_template)

# close the file
f.close()
