from helper import remove_character_first_occurance
from helper import repeating_to_single_string_converter


def main():
    global input_file, output_file
    try:
        input_file = open("input", "r")
        open('output', 'w').close()
        output_file = open("output", "a+")
    except IOError:
        print("Could not open file")
    else:
        first_occurrence_removal_result = ""
        input_file_list = input_file.readlines()
        output_file.write("Function 1:\n")

        for given_word in input_file_list:
            output_file_output = \
                repeating_to_single_string_converter(given_word)
            output_file.write(output_file_output)
            first_occurrence_removal_result = \
                first_occurrence_removal_result + \
                remove_character_first_occurance(given_word)

        output_file.write("\nFunction 2:\n")
        output_file.write(first_occurrence_removal_result)
    finally:
        input_file.close()
        output_file.close()


if __name__ == "__main__":
    main()
