import eep1
import eep0

instruction_list = []

continue_running = True
continue_running_eep0 = True
continue_running_eep1 = True

print("Welcome to this EEP0/EEP1 assembler!")
print("Please note that for Imm8 and Imm5 the number should be entered in decimals! "
      "The conversion into hex has been inbuilt into this assembler")
user_input = input("What would you like to do? EEP0[0]/EEP1[1]/Exit[E]: ").lower()

if user_input == "e":
    continue_running = False

while continue_running:
    if user_input == "0":
        while continue_running_eep0:
            instruction = eep0.input_instruction()
            eep0.operate_eep0(instruction)
            instruction_list += [eep0.output_of_eep0(instruction)]
            run_again = input("continue running? Y/N: ").lower()
            if run_again == "n":
                continue_running_eep0 = False
    else:
        while continue_running_eep1:
            instruction = eep1.input_instruction()
            eep1.operate_eep1(instruction)
            instruction_list += [eep1.output_of_eep1(instruction)]
            run_again = input("continue running? Y/N: ").lower()
            if run_again == "n":
                continue_running_eep1 = False
    user_input = input("What would you like to do? EEP0[0]/EEP1[1]/Exit[E]: ").lower()
    if user_input == "e":
        continue_running = False

index = 0

while index < len(instruction_list):
    print(instruction_list[index])
    index += 1

print("thanks for using this assembler! :)")








