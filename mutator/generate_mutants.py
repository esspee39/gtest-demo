import os
import sys
from configparser import ConfigParser
from mutant_dictionary import all_mutants
from mutant_dictionary import all_mutant_keys
import getfilename
import containsmutant

class GenerateMutants():

    if not os.path.exists('./config.ini'): #Config parser - From Drew's and Luke's Code
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

        if os.path.exists('../mutants'):
            os.system("rm -r ../mutants/")

        for x in mutants: #Pareses config for mutants that are marked active
            if config.get('Mutants', x) == '1':
                mutant_list.append(x) #Creates list of active mutants from config file

        for x in all_mutant_keys:
            if x.lower() in mutant_list:
                active_mutants.append(all_mutants[x])

        for x in active_mutants:
            if containsmutant.containsMutant("../src/example.cpp", x.get_regex()):
                created_mutants.append(x)
            else:
                print("File does not contain " + x.get_name())

        if not os.path.exists('../mutants'):
            os.mkdir('../mutants')

        for i in created_mutants:  #Creates folders for all active mutants
            build_dir = '../mutants/' + i.get_name()
            if not os.path.exists(build_dir):
                os.mkdir(build_dir) #Creates folder
                os.mkdir(build_dir + "/src/")
                os.mkdir(build_dir + "/test/")

            with open(build_dir + "/CMakeLists.txt", "w+") as f: #Writes CMakeLists file for mutant
                f.write("add_subdirectory(src)\n")
                f.write("enable_testing()\n")
                f.write("add_subdirectory(test)\n")

            with open(build_dir + "/src/CMakeLists.txt", "w+") as f:
                f.write("add_library(example_" + i.get_name() + ")\n")
                f.write("target_sources(example_" + i.get_name() + "\n")
                f.write("  PRIVATE\n")
                srcfiles = getfilename.getFilenamesFromCMakeLists("../src/CMakeLists.txt")
                for srcfile in srcfiles:
                    f.write("    " + srcfile.replace(".cpp", "_" + i.get_name() + ".cpp\n"))
                f.write("  PUBLIC\n")
                headers = getfilename.getHeaderFilenamesFromCMakeLists("../src/CMakeLists.txt")
                for srcfile in headers:
                    f.write("    " + srcfile.replace(".h", "_" + i.get_name() + ".h\n"))
                f.write("  )\n")
                f.write("\n")
                f.write("target_include_directories(example_" + i.get_name() + "\n")
                f.write("  PUBLIC\n")
                f.write("    ${CMAKE_CURRENT_LIST_DIR}\n")
                f.write("  )")
                f.write("\n")

            with open(build_dir + "/test/CMakeLists.txt", "w+") as f:
                f.write("add_executable(\n")
                f.write("    unit_tests_" + i.get_name() + "\n")
                for testfile in getfilename.getFilenamesFromCMakeLists("../test/CMakeLists.txt"):
                    f.write("    " + testfile.replace(".cpp", "_" + i.get_name() + ".cpp\n"))
                f.write("    )\n")
                f.write("\n")
                f.write("target_link_libraries(unit_tests_" + i.get_name() + "\n")
                f.write("  PRIVATE\n")
                f.write("  example_" + i.get_name() + "\n")
                f.write("    gtest_main\n")
                f.write("  )\n")
                f.write("\n")
                f.write("# automatic discovery of unit tests\n")
                f.write("include(GoogleTest)\n")
                f.write("gtest_discover_tests(unit_tests_" + i.get_name() + "\n")
                f.write("  PROPERTIES\n")
                f.write("    LABELS \"unit\"\n")
                f.write("  DISCOVERY_TIMEOUT  # how long to wait (in seconds) before crashing\n")
                f.write("    240\n")
                f.write("  )\n")

            with open('../mutants/CMakeLists.txt', "a+") as f:
                f.write("add_subdirectory(" + i.get_name() + ")\n")

            mutation_targets = getfilename.getFilenamesFromCMakeLists("../src/CMakeLists.txt")
            mutation_headers = getfilename.getHeaderFilenamesFromCMakeLists("../src/CMakeLists.txt")
            test_targets = getfilename.getFilenamesFromCMakeLists("../test/CMakeLists.txt")

            for target in mutation_targets:
                with open("../src/" + target, "r") as input:
                    newfilename = target.replace(".cpp", "_" + i.get_name() + ".cpp")
                    with open(build_dir + "/src/" + newfilename, "w+") as output:
                        for line in input:
                            mutated_line = i.mutate(line)
                            for hdr in mutation_headers:
                                newheader = hdr.replace(".h", "_" + i.get_name() + ".h")
                                final_line = mutated_line.replace(hdr, newheader)
                            output.write(final_line)

            for hdr in mutation_headers:
                with open("../src/" + hdr, "r") as input:
                    newname = build_dir + "/src/" + hdr.replace(".h", "_" + i.get_name() + ".h")
                    with open(newname, "w+") as output:
                        for line in input:
                            output.write(line)

            for test in test_targets:
                with open("../test/" + test, "r") as input:
                    newnm = build_dir + "/test/" + test.replace(".cpp", "_" + i.get_name() + ".cpp")
                    with open(newnm, "w+") as output:
                        for line in input:
                            for target in mutation_targets:
                                newnm = target.replace(".cpp", "_" + i.get_name())
                                modified_line = line.replace(target.replace(".cpp", ""), newnm)
                                for hdr in mutation_headers:
                                    newhdr = hdr.replace(".h", "_" + i.get_name() + ".h")
                                    output.write(modified_line.replace(hdr, newhdr))

        sys.exit()
