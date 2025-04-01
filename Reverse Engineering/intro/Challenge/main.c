#include <stdio.h>

int check_conditions(char input[]);
unsigned char xor_keys[] = {0x78, 0x77, 0x12, 0xB7, 0xCD, 0x1E, 0xE9, 0xD4, 0x0E, 0xE3, 0x60, 0xBB, 0xE2, 0x27, 0x8E, 0x9A, 0xEB, 0x1B, 0x41, 0x4A, 0xB7, 0x53};
unsigned char expected_values[] = {0x2B, 0x07, 0x73, 0xC5, 0xA6, 0x65, 0x91, 0xE4, 0x7C, 0xBC, 0x09, 0x8E, 0xBD, 0x49, 0xBE, 0xEE, 0xB4, 0x48, 0x75, 0x2C, 0x84, 0x2E};

int main() {
    printf("\n\n");
    printf("   ██╗   ██████╗  ██╗  ██╗  █████╗    ████╗ ████╗\n");
    printf(" ████║   ██╔══██╗ ██║  ██║ ██╔══██╗   ██╔████╔██║\n");
    printf("██ ██║   ██║  ██║ ███████║ ██║  ██║   ██║╚██╔╝██║\n");
    printf("   ██║   ██║  ██║ ██╔══██║ █████████║ ██║ ╚═╝ ██║\n");
    printf("   ██║   ██████╔╝ ██║  ██║      ██║   ██║     ██║\n");
    printf(" ██████  ╚═════╝  ╚═╝ ╚═╝       ╚═╝   ╚═╝     ╚═╝\n");
    printf("\n");
    printf("[*] H0ll0 H4CK3R Welc0me T0 Spark Ramdhan-CTF\n");
    printf("[*] Can you try to guess the Flag ?\n[*]>> ");
    
    char input[25]; 
    scanf("%22s", input); 
    
    if (check_conditions(input)) {
        printf("[*] G00d j0b H4CK3R!\n");
    } else {
        printf("[!] Wrong Flag. Try Again!\n");
    }
    
    return 0;
}

int check_conditions(char input[]) {
    for (int i = 0; i < 22; i++) {
        
        if ((input[i] ^ xor_keys[i]) != expected_values[i]) {
            return 0;  
        }
    }
    return 1;  
}
