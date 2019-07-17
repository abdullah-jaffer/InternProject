def repeating_to_single_string_converter(multi_occurring_string):
    string_after_single_occurrence = ""

    for index_for_multi_occurrence in multi_occurring_string:
        if index_for_multi_occurrence.lower() not in string_after_single_occurrence.lower():
            string_after_single_occurrence = string_after_single_occurrence + index_for_multi_occurrence

    return string_after_single_occurrence


def is_repeating(repeating_character_string, key_character):
    counter = 0
    for index_for_repeating_character in repeating_character_string:
        counter = counter + 1 if index_for_repeating_character.lower() == key_character.lower() else counter

    is_true = True if counter > 1 else False
    return is_true


def remove_given_character(input_string, key_character):
    index_for_character_removal = input_string.find(key_character)

    if index_for_character_removal == 0:
        input_string = input_string[1:]
    elif index_for_character_removal == len(input_string) - 1:
        input_string = input_string[0: len(input_string) - 1]
    else:
        input_string = input_string[0:index_for_character_removal] + input_string[
                                                                     index_for_character_removal + 1: len(input_string)]

    return input_string


def remove_first_occurrence_of_character(removing_string):
    """How 'remove_first_occurrence_of_character(arg)' works.

       this function first finds repeating characters and then uses
       removes it's first occurrence
    """
    string_after_removal = ""
    # the below variable keeps tabs of which characters have had the first occurrence removed so it is not removed again
    removed_list = []

    for index_of_removing_string in removing_string:
        if is_repeating(removing_string, index_of_removing_string) and \
                index_of_removing_string.lower() not in removed_list:
            string_after_removal = remove_given_character(removing_string, index_of_removing_string)
            removed_list.append(index_of_removing_string.lower())
            removing_string = string_after_removal

    return string_after_removal
