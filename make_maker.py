# import argparse
# from functools import reduce

# def build_run_string(in_arg_list):
#     run_string = "run:  "
#     dot_o_files = ""

#     for arg in in_arg_list:
#         dot_o_files.append("{0}.o".format(arg))

#     print(dot_o_files)

# def build_make_file(in_arg_list):
#     # f = open("makefile", "x")

#     print("CC =g++ # CC is a variable containing the complier we are using.")
#     print(
#         "\n\nCFLAGS = -g -c -Wall # -c means compile and -wall is a necessary warning, -g is debug data."
#     )
#     print("all:" + "\t" + "run")

#     dot_o = list(map(lambda a: a + ".o", in_arg_list))
#     dot_o = " ".join(dot_o)
#     print("\t" + dot_o + " #dependencies")

# def main():
#     try:
#         parser = argparse.ArgumentParser()
#         parser.add_argument("text",
#                             nargs="+",
#                             action="store",
#                             help="Input names of cpp files for make file.")
#         args = parser.parse_args()
#     except:
#         pass

#     build_make_file(args.text)


def main():
    list_of_files = list()
    list_of_dependencies = list()
    file = open("makefile", "w")

    while True:

        print("C++ Makefile Maker\n" + "-----------------------------\n" +
              "1. Enter File and Dependencies\n" +
              "2. Proceed to makefile Creation\n" + "3. Exit Program")
        choice = input("What would you like to do: ")

        if choice == "1":
            print("If file has no dependencies enter self in dependencies")

            file_name = input("Input file name, exclude file extension: ")

            dependency = input(
                "Input dependencies seperated by spaces, including file extensions: "
            )

            if dependency.lower() == "self":
                dependency = "{0}.h {0}.cpp".format(file_name)
            else:
                dependency += " {0}.cpp".format(file_name)

            list_of_files.append(file_name)
            list_of_dependencies.append(dependency.split())

        elif choice == "2":
            file_dictionary = dict(zip(list_of_files, list_of_dependencies))
            file.write(
                "CC = g++ #CC is a variable containing the compiler we are using\n"
            )
            file.write(
                "CFlAGS = -g -c -Wall # -c means compile, -Wall is a necessary warning, -g is debug data\n"
            )
            file.write("all:" + "\t" + "run\n")
            file_o = [file + ".o" for file in list_of_files]
            file_o = " ".join(file_o)
            file.write("run:" + "\t" + file_o)
            file.write("\t" + "$(CC) -o " + file_o + "\n")

            post_run = ""

            for key, value in file_dictionary.items():
                post_run += "{0}.o:".format(key) + "\t" + "{1}".format(
                    key, " ".join(value)) + "\n"
                post_run += "\t" + "$(CC) $(CFLAGS) {0}.cpp".format(key) + "\n"

            file.write(post_run)

            file.write("clean:\n")
            file.write("\t" + "rm *.o run")

            file.close()
        elif choice == "3":
            break


if __name__ == "__main__":
    main()
