# Utility functions for the calculator

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Add more utility functions as needed
