def main():
    # Prompt the user for a time
    time = input("Enter a time in 24-hour format (HH:MM): ")

    # Convert the time to the corresponding number of hours
    total_hours = convert(time)

    # Check if it's breakfast time
    if 7 <= total_hours <= 8:
        print("breakfast time")

    # Check if it's lunch time
    if 12 <= total_hours <= 13:
        print("lunch time")

    # Check if it's dinner time
    if 18 <= total_hours <= 19:
        print("dinner time")

def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time.split(':'))

    # Calculate the total hours as a float
    total_hours = hours + minutes / 60

    return total_hours

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()