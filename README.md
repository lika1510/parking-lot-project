Smart Parking Lot Management
Overview
This project implements a Smart Parking Lot Management system using Python. It simulates the real-time management of a parking lot by tracking car entries and exits, dynamically allocating parking slots, and efficiently handling situations when the lot is full through a waitlist system. The core data structure used is a linked list to keep track of active parked cars, demonstrating practical use of dynamic memory management concepts.

Features
Dynamic tracking of parked cars using linked lists.

Real-time allocation and release of parking slots.

Queue-based waitlist for cars when the parking lot is full.

Interactive command-line interface for ease of use.

Displays currently parked cars and the waitlist.

Calculates and displays parking duration when a car exits.

How to Run
Make sure Python 3 is installed on your system.

Clone or download this repository.

Open a terminal and navigate to the project directory.

Run the program using the command:

bash
python3 smart_parking_lot.py
Follow the on-screen menu options to park cars, retrieve cars, view parked cars, or view the waitlist.

Example Output
text
Enter total number of parking slots: 2

--- Parking Lot Menu ---
1. Park a car
2. Retrieve a car
3. Show parked cars
4. Show waitlist
5. Exit
Enter choice (1-5): 1
Enter car plate number: ABC123
Car ABC123 parked in slot 2.

--- Parking Lot Menu ---
1. Park a car
2. Retrieve a car
3. Show parked cars
4. Show waitlist
5. Exit
Enter choice (1-5): 1
Enter car plate number: XYZ789
Car XYZ789 parked in slot 1.

--- Parking Lot Menu ---
1. Park a car
2. Retrieve a car
3. Show parked cars
4. Show waitlist
5. Exit
Enter choice (1-5): 1
Enter car plate number: LMN555
Parking lot is full! Car LMN555 added to waitlist.

--- Parking Lot Menu ---
1. Park a car
2. Retrieve a car
3. Show parked cars
4. Show waitlist
5. Exit
Enter choice (1-5): 3
Parked Cars:
  Plate: XYZ789, Slot: 1, Parked since: Wed Aug 20 15:02:40 2025
  Plate: ABC123, Slot: 2, Parked since: Wed Aug 20 15:02:30 2025

--- Parking Lot Menu ---
1. Park a car
2. Retrieve a car
3. Show parked cars
4. Show waitlist
5. Exit
Enter choice (1-5): 2
Enter car plate number to retrieve: ABC123
Car ABC123 leaving slot 2. Time parked: 10.12 seconds.
Allocating slot to waitlisted car LMN555.
Car LMN555 parked in slot 2.
