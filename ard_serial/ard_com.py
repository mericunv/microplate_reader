import serial 
import time
import re
ser = serial.Serial('COM5', baudrate=9600, timeout=1)

def get_valid_columns():
    while True:
        user_input = input("Enter columns to process (1-12, separated by commas/spaces): ").strip()
        if not user_input:
            print("Please enter at least one column.")
            continue
        
        # Split input into parts (handling commas, spaces, or mixed delimiters)
        parts = re.split(r'[, \s]+', user_input)
        
        try:
            # Convert to integers, remove duplicates, and validate
            columns = list(set(map(int, parts)))
            if not columns:
                print("No valid columns entered.")
                continue
            
            # Check all columns are within 1-12
            invalid = [col for col in columns if col < 1 or col > 12]
            if invalid:
                print(f"Invalid columns: {invalid}. Columns must be 1-12.")
                continue
            
            return columns  # Validated columns (e.g., [1, 5])
        
        except ValueError:
            print("Invalid input. Please enter numbers only.")


booleans_dict = {}
for letter in 'ABCDEFGH':
    for number in range(1, 13):
        key = f"{letter}{number}"
        booleans_dict[key] = False

columns = get_valid_columns() # get valid columns from user

selected_keys = [f"{letter}{col}" for col in columns for letter in 'ABCDEFGH'] # Convert to column names (e.g., [1, 5] -> ['A1', 'A2', ...])

for key in selected_keys:
    booleans_dict[key] = True
    
print("Updated values in selected columns:")

for key in selected_keys[:1]:  # Print first 5 keys as a sample
    print(f"{key}: {booleans_dict,[key]}\n")	

def send_to_arduino():
    for key in selected_keys: 
        print(f"Sending {key} to Arduino")
        ser.write(key.encode())
        time.sleep(0.2)
        data = ser.readline().decode('utf-8').strip()
        if data:
            print(f"Received from Arduino: {data}")
        else:
            print("No response from Arduino.")
        time.sleep(0.2)


send_to_arduino()

