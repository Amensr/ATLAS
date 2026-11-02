import platform
import sys


def system_info():

    print("\n===== ATLAS SYSTEM DIAGNOSTICS =====")

    print(f"Operating System : {platform.system()}")
    print(f"Platform         : {platform.platform()}")
    print(f"Python Version   : {sys.version.split()[0]}")
    print(f"Python Executable: {sys.executable}")

    print("===================================\n")
