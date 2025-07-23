import math

def batt_to_motor(current_mA: float) -> float:
    """
    Converts battery-side current (in mA) to motor-side current (in A).
    Formula: motor_current = 0.925 * ln(batt_current) - 4.324
    """
    if current_mA <= 0:
        raise ValueError("Battery current must be positive")
    return 0.925 * math.log(current_mA) - 4.324

def motor_to_batt(current_A: float) -> float:
    """
    Converts motor-side current (in A) to battery-side current (in mA).
    Formula: batt_current = exp((motor_current + 4.324) / 0.925)
    """
    return math.exp((current_A + 4.324) / 0.925)



# Constants
MAX_BATTERY_CURRENT = 12800  # in mA
FIXED_CURRENT = 2.5          # Amps
NUM_FIXED = 4
NUM_FLEXIBLE = 9

# Step 1: Calculate total battery current used by fixed motors
reserved_batt = NUM_FIXED * motor_to_batt(FIXED_CURRENT)

# Step 2: Compute remaining battery current for flexible motors
remaining_batt = MAX_BATTERY_CURRENT - reserved_batt
per_flexible_batt = remaining_batt / NUM_FLEXIBLE

# Step 3: Convert back to motor current for flexible motors
flexible_current = batt_to_motor(per_flexible_batt)

# Cap to max allowed per motor
flexible_current = min(flexible_current, FIXED_CURRENT)

# Output
print(f"Total reserved battery current (fixed motors): {reserved_batt:.2f} mA")
print(f"Remaining battery current (for flexible motors): {remaining_batt:.2f} mA")
print(f"Battery current per flexible motor: {per_flexible_batt:.2f} mA")
print(f"Calculated motor-side current per flexible motor: {flexible_current:.3f} A")