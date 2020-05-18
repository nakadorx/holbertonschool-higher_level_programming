#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as err:
        import sys
        print("Exception:", err, file=sys.stderr)
        return False
    return True
