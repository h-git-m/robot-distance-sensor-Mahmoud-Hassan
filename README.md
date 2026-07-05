# robot-distance-sensor-Mahmoud-Hassan
This script simulates a simple robot obstacle-avoidance system.
# Robot Distance Sensor Processor

## What does this program do?
It simulates a robot's obstacle-avoidance system. Given a list of distance
sensor readings, it decides whether the robot should stop, slow down, or
move fast, while tracking battery drain and handling invalid sensor data.

## How does the class work?
The class `robot_distance_sensor_processor` is constructed with a robot's
name, starting battery level, and a list of distance readings (in meters).
It stores these as instance attributes and exposes a single method to
process the readings and print a status report for each one.

## What does each method do?
- **`__init__(self, robot_name, battery_level, distance_readings)`**
  Constructor. Stores the robot's name, battery level, and sensor readings.

- **`process_readings(self)`**
  Loops through each distance reading and:
  - Stops the loop immediately if battery is at 0% (low battery shutdown).
  - Uses a `try/except` block to catch invalid readings (non-numeric →
    `TypeError`, negative → `ValueError`), printing an error and skipping them.
  - Chooses an action based on distance: `EMERGENCY STOP` (0), `STOP`
    (<0.5 m), `SLOW` (0.5–1 m), or `MOVE FAST` (>1 m).
  - Prints a status message and reduces battery by 5% per valid reading.

## How do I run the code?
1. Make sure Python 3 is installed.
2. Run the script from the terminal:
   ```
   python3 robot_distance_sensor_processor.py
   ```
3. The script automatically runs 5 built-in test cases and prints the results.

## What did you learn from AI?
I can give feedback directly on specific generated lines and have the AI
regenerate the code around that feedback, instead of rewriting everything
from scratch myself.
