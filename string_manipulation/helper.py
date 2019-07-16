

def remove_multy_occurence(multy_occuring_string):
    string_after_single_occurence = ""

    for index_for_multy_occurence in multy_occuring_string:
        if index_for_multy_occurence.lower() not in string_after_single_occurence.lower():
            string_after_single_occurence = string_after_single_occurence + index_for_multy_occurence

    return string_after_single_occurence


def repeats(repeating_character_string, key_character):
    counter = 0
    for index_for_repeating_character in repeating_character_string:
        if index_for_repeating_character.lower() == key_character.lower():
            counter = counter + 1

    if counter>1:
        return True
    else:
        return False


def remove_given_character(removing_string, key_character):

    index_for_character_removal = removing_string.find(key_character)

    if index_for_character_removal == 0:
        removing_string = removing_string[1:]
    elif index_for_character_removal == len(removing_string) - 1:
        removing_string = removing_string[0: len(removing_string) - 1]
    else:
        removing_string = removing_string[0:index_for_character_removal] + removing_string[index_for_character_removal + 1: len(removing_string)]

    return removing_string

# this function first uses 'repeat()' to find repeating characters and then uses
# 'remove_given_character(,)' to remove it's first occurrence
# 'remove_list' keeps tabs of which characters have had there first occurrence removed so it is not removed again


def remove_first_occurence_of_character(removing_string):
    resulting_string_after_function = ""
    removed_list = []
    for index_of_removing_string in removing_string:
        if repeats(removing_string, index_of_removing_string) == True\
                and index_of_removing_string.lower() not in removed_list:
            resulting_string_after_function = remove_given_character(removing_string, index_of_removing_string)
            removed_list.append(index_of_removing_string.lower())
            removing_string = resulting_string_after_function

    return resulting_string_after_function
