"""
Robot Distance Sensor Processor
--------------------------------
This script simulates a simple robot obstacle-avoidance system.

What the code does:
1. Defines a class `robot_distance_sensor_processor` that stores a robot's
   name, battery level, and a list of distance sensor readings (in meters).
2. Provides a method `process_readings()` that loops through each distance
   reading and decides an action based on these rules:
       - distance == 0        -> "EMERGENCY STOP" (sensor detects contact / zero distance)
       - 0 < distance < 0.5    -> "STOP" (obstacle too close)
       - 0.5 <= distance <= 1  -> "SLOW" (obstacle nearby)
       - distance > 1          -> "MOVE FAST" (path is clear)
3. Each time a reading is processed, the battery level decreases by 5%.
   If the battery drops to 0% (or below), the robot prints a low battery
   warning, forces a "STOP" action, and the loop BREAKS immediately -
   no further readings are processed for that robot.
4. Includes error handling using try/except blocks for invalid readings:
       - Negative distance values raise a ValueError (caught, logged, skipped).
       - Non-numeric values raise a TypeError (caught, logged, skipped).
5. Prints a clear status message for every reading using f-strings, e.g.:
       Robot R2D2 | Battery: 85% | Distance: 0.3 m | Action: STOP
6. Runs 5 test cases with different robot names, battery levels, and
   different lists of sensor readings (including edge cases like 0,
   negative numbers, and invalid/non-numeric values).
"""


class robot_distance_sensor_processor:
    """Processes a robot's distance sensor readings and decides actions."""

    def __init__(self, robot_name, battery_level, distance_readings):
        """
        Constructor.

        Parameters:
            robot_name (str): Name/ID of the robot.
            battery_level (float/int): Starting battery percentage (0-100).
            distance_readings (list): List of distance sensor readings (meters).
                                       May contain invalid values (negative,
                                       non-numeric) to test error handling.
        """
        self.robot_name = robot_name
        self.battery_level = battery_level
        self.distance_readings = distance_readings

    def process_readings(self):
        """
        Loops through each distance reading, decides an action, decreases
        battery by 5% per reading, and prints a status message for each one.
        """
        print(f"\n--- Starting sensor processing for Robot: {self.robot_name} ---")

        for index, distance in enumerate(self.distance_readings, start=1):

            # --- Battery check BEFORE processing: if depleted, STOP entirely ---
            if self.battery_level <= 0:
                print(f"Robot {self.robot_name} | Battery: {self.battery_level}% | "
                      f"Action: STOP | WARNING: Low battery! Robot has completely stopped all actions.")
                break  # Battery depleted: exit the loop, no further readings are processed

            # --- try/except block: handles invalid / non-numeric and negative readings ---
            try:
                # Reject non-numeric values (also reject bool, since bool is a subclass of int)
                if not isinstance(distance, (int, float)) or isinstance(distance, bool):
                    raise TypeError(f"Invalid distance value '{distance}' (not a number).")

                # Reject negative distances
                if distance < 0:
                    raise ValueError(f"Negative distance value ({distance} m) is invalid.")

                # --- Decide action based on distance ---
                if distance == 0:
                    action = "EMERGENCY STOP"
                elif distance < 0.5:
                    action = "STOP"
                elif 0.5 <= distance <= 1:
                    action = "SLOW"
                else:  # distance > 1
                    action = "MOVE FAST"

                # --- Print clear status message ---
                print(f"Robot {self.robot_name} | Battery: {self.battery_level}% | "
                      f"Distance: {distance} m | Action: {action}")

                # --- Decrease battery by 5% after successfully processing this reading ---
                self.battery_level -= 5
                if self.battery_level <= 0:
                    self.battery_level = 0
                    print(f"Robot {self.robot_name} | Battery: {self.battery_level}% | "
                          f"WARNING: Battery critically low! Robot will STOP for remaining readings.")

            except (TypeError, ValueError) as error:
                print(f"Robot {self.robot_name} | Reading #{index} | "
                      f"Error: {error} Skipping.")
                continue

        print(f"--- Finished processing for Robot: {self.robot_name} "
              f"(Final Battery: {self.battery_level}%) ---\n")


# ---------------------------------------------------------------------------
# TEST CASES
# ---------------------------------------------------------------------------
if __name__ == "__main__":

    # Test Case 1: Normal readings, healthy battery
    robot1 = robot_distance_sensor_processor(
        robot_name="R2D2",
        battery_level=100,
        distance_readings=[1.5, 0.8, 0.3, 2.0, 0.6]
    )
    robot1.process_readings()

    # Test Case 2: Includes a zero reading (emergency stop) and negative value (error)
    robot2 = robot_distance_sensor_processor(
        robot_name="WALL-E",
        battery_level=50,
        distance_readings=[0, -1.2, 0.9, 1.1, 0.4]
    )
    robot2.process_readings()

    # Test Case 3: Low starting battery to trigger low-battery stop mid-way (loop breaks)
    robot3 = robot_distance_sensor_processor(
        robot_name="BB8",
        battery_level=15,
        distance_readings=[2.0, 1.5, 0.9, 0.4, 3.0]
    )
    robot3.process_readings()

    # Test Case 4: Includes invalid non-numeric values (error handling test)
    robot4 = robot_distance_sensor_processor(
        robot_name="OptimusPrime",
        battery_level=80,
        distance_readings=[1.2, "far", None, 0.45, 0.7]
    )
    robot4.process_readings()

    # Test Case 5: Battery already depleted at start
    robot5 = robot_distance_sensor_processor(
        robot_name="Terminator",
        battery_level=0,
        distance_readings=[3.0, 0.2, 0.9]
    )
    robot5.process_readings()
