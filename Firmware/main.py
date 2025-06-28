import time
from machine import Pin # Import the Pin class for GPIO control

# --- Configuration based on your Schematic ---
# Define the GPIO pins connected to the Rows and Columns of your matrix.
# These correspond to the pins on the "ReguLar" (ESP32) component in your schematic.
# We will use the Pico W's GPIO numbers directly.

# Based on connections to "ReguLar" (ESP32) in the schematic:
# Rows connected to: IO10, IO11, IO12, IO13
# In MicroPython on Pico, these are just GPIO10, GPIO11, etc.
ROW_PINS_GPIO = [10, 11, 12, 13] 

# Columns connected to: IO34, IO35, IO36, IO37, IO38, IO39, IO40, IO41, IO42, IO43, IO44, IO45, IO46
# Note: Schematic shows COL0-COL12. Assuming they map sequentially to these IO pins.
# These are valid GPIO numbers on the Pico W.
COLUMN_PINS_GPIO = [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]

# Key map: A simple representation of what character each key represents.
# This assumes a standard keyboard layout for a 4x13 matrix.
KEY_MAP = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'], # ROW0
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'Enter', ' '], # ROW1 (Space placeholder)
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift', 'Up', ' '], # ROW2 (Up Arrow placeholder)
    ['Ctrl', 'Win', 'Alt', 'Space', ' ', ' ', ' ', ' ', ' ', ' ', 'Left', 'Down', 'Right'] # ROW3 (Space, arrows placeholders)
]

# For the Rotary Encoder Switch (SW70 in your schematic)
# This is typically just another switch in the matrix or a separate GPIO.
# If SW70 is wired as a normal matrix switch (e.g., COL11, ROW2 as implied in the top part of your schematic logic),
# it's handled by the matrix scan.
# If it's on a dedicated pin (e.g., IO47 for the 'ENC' signal shown), we'd read that directly.
# Assuming 'ENC' (IO47) is a separate input for the switch press.
ENCODER_SWITCH_PIN_GPIO = 47 # Assuming this maps to the 'ENC' signal on the ESP32

# --- Rotary Encoder Rotation Pins (New for Volume Knob) ---
# Assuming these are connected to available GPIOs on your Pico W.
ENCODER_A_PIN_GPIO = 26 # Connect encoder CLK/A pin here
ENCODER_B_PIN_GPIO = 27 # Connect encoder DT/B pin here

# --- Pin Objects Initialization ---
# Create Pin objects for rows and columns.
row_pins = [Pin(gpio, Pin.OUT) for gpio in ROW_PINS_GPIO]
column_pins = [Pin(gpio, Pin.IN, Pin.PULL_UP) for gpio in COLUMN_PINS_GPIO]
encoder_switch_pin = Pin(ENCODER_SWITCH_PIN_GPIO, Pin.IN, Pin.PULL_UP)

# Rotary Encoder Pin Objects
# These usually need pull-ups as well if your encoder module doesn't have them
encoder_a_pin = Pin(ENCODER_A_PIN_GPIO, Pin.IN, Pin.PULL_UP)
encoder_b_pin = Pin(ENCODER_B_PIN_GPIO, Pin.IN, Pin.PULL_UP)

# Global variables to track encoder state for rotation detection
last_encoder_a_state = None
# A small dictionary to store the last state of the encoder for each instance if multiple
# are needed, or simply global variables if only one encoder.

# --- MicroPython-Specific Functions ---

def scan_keyboard_matrix_pico():
    """
    Scans the keyboard matrix to detect pressed keys on Raspberry Pi Pico W.
    Uses MicroPython's machine.Pin objects.
    """
    pressed_keys = []
    
    # Ensure all row pins are high (inactive) initially
    for pin_obj in row_pins:
        pin_obj.value(1) # Set high (inactive)
    
    # Column pins are already configured as inputs with pull-ups during initialization.

    for r_idx, row_pin_obj in enumerate(row_pins):
        # Drive the current row low
        row_pin_obj.value(0) # Activate row
        time.sleep(0.005) # Small debounce delay for signal stabilization

        # Read the state of each column
        for c_idx, col_pin_obj in enumerate(column_pins):
            if col_pin_obj.value() == 0: # If column reads LOW, key is pressed
                try:
                    key = KEY_MAP[r_idx][c_idx]
                    pressed_keys.append(key)
                except IndexError:
                    # Fallback if KEY_MAP doesn't cover all matrix positions
                    pressed_keys.append(f"Key at ({r_idx}, {c_idx}) (No map)")
        
        # Deactivate the current row by setting it high again
        row_pin_obj.value(1) # Deactivate row

    return pressed_keys

def check_encoder_switch_pico():
    """
    Checks the state of the rotary encoder's push-button switch on Raspberry Pi Pico W.
    """
    # The encoder_switch_pin is already initialized with a pull-up.
    if encoder_switch_pin.value() == 0: # If button pulls pin LOW
        return "Encoder Button Pressed"
    else:
        return "Encoder Button Not Pressed"

def check_rotary_encoder_pico():
    """
    Detects rotary encoder rotation and direction (for volume knob).
    This is a basic polling method. For more robust detection (especially fast turns),
    interrupts are often preferred.
    """
    global last_encoder_a_state

    # Read current states of A and B pins
    current_a_state = encoder_a_pin.value()
    current_b_state = encoder_b_pin.value()

    # Initialize last_encoder_a_state on first run
    if last_encoder_a_state is None:
        last_encoder_a_state = current_a_state
        return None # No rotation detected yet

    # Only process if A state has changed
    if current_a_state != last_encoder_a_state:
        # Debounce: wait a tiny bit to ensure the signal is stable
        time.sleep_us(500) # Microseconds delay
        current_a_state = encoder_a_pin.value() # Re-read after debounce
        current_b_state = encoder_b_pin.value() # Re-read after debounce

        if current_a_state != last_encoder_a_state: # Confirm state change after debounce
            if current_b_state != current_a_state:
                # If B is different from A when A changes, it's one direction
                rotation_direction = "Clockwise (Volume Up)"
            else:
                # If B is the same as A when A changes, it's the other direction
                rotation_direction = "Counter-Clockwise (Volume Down)"
            last_encoder_a_state = current_a_state # Update last state
            return rotation_direction
    
    return None # No significant rotation detected

# --- Main Loop (Example for Pico W) ---
if __name__ == "__main__":
    # This block won't run directly on a desktop Python interpreter
    # because 'machine' module is for MicroPython.
    # To run this, upload it to your Raspberry Pi Pico W.

    print("Running Keyboard Matrix Scan & Rotary Encoder on Raspberry Pi Pico W (MicroPython)")
    print("----------------------------------------------------------------------------------")
    print("Connect to Pico's serial console to see output.")

    # Main loop to continuously scan for key presses and encoder rotations
    while True:
        current_pressed_keys = scan_keyboard_matrix_pico()
        current_encoder_button_state = check_encoder_switch_pico()
        rotation_event = check_rotary_encoder_pico()

        if current_pressed_keys:
            print(f"Keys Pressed: {current_pressed_keys}")
        
        if "Pressed" in current_encoder_button_state:
            print(f"Encoder Switch: {current_encoder_button_state}")
            
        if rotation_event:
            print(f"Encoder Rotated: {rotation_event}")
            
        time.sleep(0.05) # Scan every 50ms (adjust as needed for responsiveness vs. CPU usage)
