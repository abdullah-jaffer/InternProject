from helper import repeating_to_single_string_converter
from helper import remove_first_occurence_of_character


def main():
    input_file = open("input", "r")
    open('output', 'w').close()
    output_file = open("output", "a+")

    first_occurence_removal_result = ""
    input_file_list = input_file.readlines()
    output_file.write("Function 1:\n")

    for given_word in input_file_list:

        output_file_output = repeating_to_single_string_converter(given_word)
        output_file.write(output_file_output)
        first_occurence_removal_result = first_occurence_removal_result + remove_first_occurence_of_character(given_word)

    output_file.write("\nFunction 2:\n")
    output_file.write(first_occurence_removal_result)


if __name__ == "__main__":
    main()


