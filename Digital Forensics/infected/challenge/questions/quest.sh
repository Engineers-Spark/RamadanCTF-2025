#!/bin/bash

# Define colors using ANSI escape codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
MAGENTA='\033[0;35m'
WHITE='\033[0;37m'
BOLD='\033[1m'
RESET='\033[0m'

# Define a list of questions, expected answers, and responses
questions=(
    "Enter the name of the function that is holding the name of the file intrenat.exe that orange.exe drops as your answer"
)

answers=(
    "sub_40A7A3"
)

# Function to ask a question and verify the answer
ask_question() {
    local question="$1"
    local correct_answer="$2"
    local user_answer

    while true; do
        echo -e "${MAGENTA}${question}${WHITE}${RESET}"
        echo -e "${WHITE}> \c"
        read user_answer

        if [ "$user_answer" == "$correct_answer" ]; then
            echo -e "${GREEN}[+] Correct!${RESET}\n"
            break
        else
            echo -e "${RED}[-] Wrong Answer.${RESET}\n"
        fi
    done
}

# Main function
main() {
    echo -e "\n${YELLOW}+----------------------+--------------------------------------------------------------------------+"
    echo -e "|        Title         |                         Description                                      |"
    echo -e "+----------------------+--------------------------------------------------------------------------+"
    echo -e "|They destroy my life 2|          My system got hacked by malware! Can you help me?               |"
    echo -e "+----------------------+--------------------------------------------------------------------------+\n${RESET}"

    # Loop through each question and answer it
    for i in "${!questions[@]}"; do
        ask_question "${questions[$i]}" "${answers[$i]}"
    done

    # Once all questions are answered correctly, display the flag
    echo -e "${BLUE}${BOLD}[+] Here is the flag: Spark{Y0U_5AV3_MY_L1F3}${RESET}"
}

# Call the main function
main
