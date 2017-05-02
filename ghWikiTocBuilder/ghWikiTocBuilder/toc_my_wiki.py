import constants
import toc_applier
import input_validator


input_path = ""

input_valid = False
while not input_valid:
    print(constants.path_prompt_msg)
    input_path = input()
    input_valid = input_validator.validate_input(input_path)
    if not input_valid:
        print(constants.valid_path_request_msg)


print(constants.processing_msg)
toc_str = toc_applier.apply_toc(input_path)
print()
print(constants.complete_msg)
print()
print(constants.view_toc_or_quit_msg)
toc_or_quit_input = input()
print()


if toc_or_quit_input == "toc":
    print(toc_str)
    print()
    print(constants.quit_msg)    
    input()

print(constants.closing_msg)
