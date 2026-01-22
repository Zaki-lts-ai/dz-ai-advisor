print("--- Advanced Financial Report ---")
total = 0
count = 0  # To count how many entries

try:
    with open("expenses.txt", "r") as file:
        lines = file.readlines()
        
        for line in lines:
            data = line.strip().split(": ")
            if len(data) == 2:
                item = data[0]
                amount = float(data[1])
                total += amount
                count += 1  # Increment counter for each line
                print(f"[{count}] Item: {item} | Amount: {amount}")

    print("-" * 30)
    print(f"Total Items Processed: {count}")
    print(f"Total Budget: {total}")
    
    # Calculate Average
    if count > 0:
        average = total / count
        print(f"Average Expense: {average:.2f}")

except FileNotFoundError:
    print("Error: File not found.")
