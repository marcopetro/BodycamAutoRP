#!/usr/bin/env python3
"""
Automated Bodycam RP farming loop:

TAB -> SPACE -> E -> E -> DOWN -> DOWN -> CLICK (pos1) -> CLICK ->
WAIT 38s -> TAB -> CLICK (pos2) -> CLICK (pos3) -> SPACE -> REPEAT
"""

import pydirectinput
import time
import sys

# ==================== CONFIGURATION ====================

pos_versus = (1476, 819)       # Position 1
pos_settings = (2437, 105)     # Position 2
pos_leave_btn = (2110, 447)    # Position 3

# Safety / timing settings
START_DELAY = 5                # Seconds before starting
CYCLE_DELAY = 10               # Seconds between cycles
MATCH_WAIT = 38                # Seconds to wait in the match
NUM_CYCLES = None              # None = infinite

# ==================== END CONFIGURATION ====================


def print_header():
    """Print startup information."""
    print("\n" + "=" * 50)
    print("Bodycam RP Farm")
    print("=" * 50)
    print(f"[+] Start delay: {START_DELAY}s")
    print(f"[+] Match wait:  {MATCH_WAIT}s")
    print(f"[+] Cycle delay: {CYCLE_DELAY}s")
    print(f"[+] Cycles:      {'Infinite' if NUM_CYCLES is None else NUM_CYCLES}")
    print("=" * 50)


def run_cycle(cycle_number: int):
    """Run one complete automation cycle."""

    print(f"\n[+] Cycle #{cycle_number} started")

    try:
        # Open menu / navigate
        pydirectinput.press('tab')
        time.sleep(0.5)

        pydirectinput.press('space')
        time.sleep(0.5)

        pydirectinput.press('e')
        time.sleep(0.5)

        pydirectinput.press('e')
        time.sleep(0.5)

        pydirectinput.press('down')
        time.sleep(0.5)

        pydirectinput.press('down')
        time.sleep(0.5)

        # Select versus mode
        pydirectinput.click(*pos_versus)
        time.sleep(0.5)

        pydirectinput.click()
        time.sleep(0.5)

        # Wait for the match
        print(f"[+] Waiting {MATCH_WAIT}s...")
        time.sleep(MATCH_WAIT)

        # Open menu
        pydirectinput.press('tab')
        time.sleep(0.5)

        # Settings / leave match
        pydirectinput.click(*pos_settings)
        time.sleep(0.5)

        pydirectinput.click(*pos_leave_btn)
        time.sleep(0.5)

        pydirectinput.press('space')
        time.sleep(0.5)

        print(f"[+] Cycle #{cycle_number} completed")

    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        raise

    except Exception as error:
        print(f"[!] Error: {error}")
        raise


def main():
    """Main program loop."""

    print_header()

    print(f"[+] Starting in {START_DELAY}s...")
    time.sleep(START_DELAY)

    cycle_number = 1

    try:
        while NUM_CYCLES is None or cycle_number <= NUM_CYCLES:
            run_cycle(cycle_number)

            cycle_number += 1

            if NUM_CYCLES is None or cycle_number <= NUM_CYCLES:
                print(f"[+] Next cycle in {CYCLE_DELAY}s...")
                time.sleep(CYCLE_DELAY)

    except KeyboardInterrupt:
        completed_cycles = cycle_number - 1
        rp_earned = completed_cycles * 400

        print("\n" + "=" * 50)
        print(f"[!] Stopped after {completed_cycles} cycles")
        print(f"[+] RP earned: {rp_earned}")
        print("=" * 50)

        sys.exit(0)

    except Exception as error:
        print("\n" + "=" * 50)
        print(f"[!] Fatal error: {error}")
        print("=" * 50)

        sys.exit(1)


if __name__ == "__main__":
    main()
