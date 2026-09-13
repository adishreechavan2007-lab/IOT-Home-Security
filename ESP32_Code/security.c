// IoT Home Security System in C Language
// Made by Adishree Chavan - 1st Year
// For ESP32

#include <stdio.h>
#include <stdbool.h>

// Assume these are sensor pins
#define PIR_PIN 13
#define DOOR_PIN 12
#define BUZZER_PIN 14

// Simple function to check sensors
void checkSecurity(int motion, int door) {
    printf("\n--- Checking Home ---\n");
    
    if(motion == 1) {
        printf("ALERT: Motion Detected!\n");
        printf("Buzzer ON\n");
    }
    
    if(door == 0) {
        printf("ALERT: Door is Open!\n");
        printf("Buzzer ON\n");
    }
    
    if(motion == 0 && door == 1) {
        printf("Status: SAFE - All good\n");
        printf("Buzzer OFF\n");
    }
}

// Main function
int main() {
    printf("IoT Home Security System\n");
    printf("Made by Adishree Chavan\n");
    printf("System Started...\n");

    // Test cases like a student would test
    int test1_motion = 0, test1_door = 1; // safe
    int test2_motion = 1, test2_door = 1; // motion alert
    int test3_motion = 0, test3_door = 0; // door alert

    printf("\nTest 1: No motion, Door closed");
    checkSecurity(test1_motion, test1_door);

    printf("\nTest 2: Motion detected!");
    checkSecurity(test2_motion, test2_door);

    printf("\nTest 3: Door opened!");
    checkSecurity(test3_motion, test3_door);

    printf("\nProgram Finished\n");
    return 0;
}
