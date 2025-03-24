def get_run_times():
    total_seconds = 0
    print("Please input your time for each 5k practice run.")
    for i in range(1, 6):
        minutes = int(input(f"Enter the minutes for run {i}: "))
        seconds = int(input(f"Enter the seconds for run {i}: "))
        total_seconds += (minutes * 60 + seconds)

    avg_seconds = total_seconds // 5
    avg_minutes = avg_seconds // 60
    avg_remaining_seconds = avg_seconds % 60

    print("\nCalculating your average running time...")
    print(f"Your average running time is {avg_minutes} minutes and {avg_remaining_seconds} seconds.")

get_run_times()

