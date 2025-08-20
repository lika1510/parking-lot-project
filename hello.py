import time
from collections import deque

class CarNode:
    def __init__(self, plate, slot, entry_time):
        self.plate = plate
        self.slot = slot
        self.entry_time = entry_time
        self.next = None

class ParkingLot:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.active_cars_head = None  # Linked list head
        self.available_slots = set(range(1, total_slots + 1))
        self.waitlist = deque()
    
    def park_car(self, plate):
        if not self.available_slots:
            print(f"Parking lot is full! Car {plate} added to waitlist.")
            self.waitlist.append(plate)
            return False
        slot = self.available_slots.pop()
        entry_time = time.time()
        new_car = CarNode(plate, slot, entry_time)
        new_car.next = self.active_cars_head
        self.active_cars_head = new_car
        print(f"Car {plate} parked in slot {slot}.")
        return True

    def retrieve_car(self, plate):
        prev = None
        curr = self.active_cars_head
        while curr:
            if curr.plate == plate:
                self.available_slots.add(curr.slot)
                duration = time.time() - curr.entry_time
                print(f"Car {plate} leaving slot {curr.slot}. Time parked: {duration:.2f} seconds.")
                # Remove from linked list
                if prev:
                    prev.next = curr.next
                else:
                    self.active_cars_head = curr.next
                del curr
                # Handle waitlist
                if self.waitlist:
                    next_plate = self.waitlist.popleft()
                    print(f"Allocating slot to waitlisted car {next_plate}.")
                    self.park_car(next_plate)
                return True
            prev = curr
            curr = curr.next
        print("Car not found in the parking lot.")
        return False

    def display_parked_cars(self):
        curr = self.active_cars_head
        cars = []
        while curr:
            cars.append((curr.plate, curr.slot, time.ctime(curr.entry_time)))
            curr = curr.next
        if not cars:
            print("No cars currently parked.")
        else:
            print("Parked Cars:")
            for c in cars:
                print(f"  Plate: {c[0]}, Slot: {c[1]}, Parked since: {c}")

    def display_waitlist(self):
        if not self.waitlist:
            print("Waitlist is empty.")
        else:
            print("Cars in Waitlist (order):")
            for i, plate in enumerate(self.waitlist, 1):
                print(f"  {i}. {plate}")

def main():
    total_slots = int(input("Enter total number of parking slots: "))
    lot = ParkingLot(total_slots=total_slots)

    while True:
        print("\n--- Parking Lot Menu ---")
        print("1. Park a car")
        print("2. Retrieve a car")
        print("3. Show parked cars")
        print("4. Show waitlist")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            plate = input("Enter car plate number: ").strip()
            lot.park_car(plate)
        elif choice == '2':
            plate = input("Enter car plate number to retrieve: ").strip()
            lot.retrieve_car(plate)
        elif choice == '3':
            lot.display_parked_cars()
        elif choice == '4':
            lot.display_waitlist()
        elif choice == '5':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
