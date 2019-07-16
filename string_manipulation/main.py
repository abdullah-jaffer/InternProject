from helper import remove_multy_occurence
from helper import remove_first_occurence_of_character


def main():

    input_file = open("input", "r")
    open('output', 'w').close()
    output_file = open("output", "a+")

    list_for_first_occurence_removal = []
    input_file_list = input_file.readlines()
    output_file.write("Function 1:\n")

    for given_word in input_file_list:

        str = remove_multy_occurence(given_word)
        output_file.write(str)
        list_for_first_occurence_removal.append(remove_first_occurence_of_character(given_word))

    output_file.write("\nFunction 2:\n")

    for given_word in list_for_first_occurence_removal:
        output_file.write(given_word)

    output_file.write("\n")


if __name__ == "__main__":
    main()
