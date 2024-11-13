from datetime import datetime
import pytz

def convert_time(source_timezone, target_timezone):
    try:
        # Define the timezones
        source_tz = pytz.timezone(source_timezone)
        target_tz = pytz.timezone(target_timezone)

        # Get the current time in the source timezone
        source_time = datetime.now(source_tz)
        print(f"\nCurrent time in {source_timezone}: {source_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Convert the time to the target timezone
        target_time = source_time.astimezone(target_tz)
        print(f"Converted time in {target_timezone}: {target_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    except Exception as e:
        print(f"Error: {e}\n")

if __name__ == "__main__":
    while True:  # Start an infinite loop
        print("Welcome to the Timezone Converter!")

        # Ask for timezones
        source_timezone = input("Enter the source timezone (e.g., Europe/London): ")
        target_timezone = input("Enter the target timezone (e.g., America/New_York): ")

        # Perform the conversion
        convert_time(source_timezone, target_timezone)

        # Ask if the user wants to continue
        continue_choice = input("Do you want to convert another timezone? (yes/no): ").strip().lower()

        # Exit if the user says "no"
        if continue_choice == 'no':
            print("Thank you for using the Timezone Converter. Goodbye!")
            break  # Exit the loop
        elif continue_choice != 'yes':
            print("Invalid input, exiting the program.")
            break  # Exit if the input is not "yes"
