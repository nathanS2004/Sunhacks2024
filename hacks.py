# Define the file path
file_path = 'data.txt'
initialBuyIn = 16.66
plusDays = 0 
restDays = 0
results = []

# Open the file and read line by line
with open(file_path, 'r') as file:
    # Skip the first line (header)
    next(file)
    
    for line in file:
        # Split the line by spaces
        parts = line.split()
        
        # Check if there are at least three parts
        if len(parts) > 2:
            # Join everything after the second space and strip whitespace
            result = ' '.join(parts[2:]).strip()  
            
            # Only process if result is not 'Change'
            if result != 'Change':
                # Check if result ends with '%' and remove it
                if result.endswith('%'):
                    removePercent = float(result[:-1])  # Convert to float
                    results.append(removePercent)  # Append the numeric value

                else:
                    print(f"Skipping non-percentage value: {result}")
            else:
                print('Skipping Change')
        else:
            print('Not enough parts in the line.')

# Print the final list of results
total=initialBuyIn
restDayLoopCounter=0
plusDayLoopCounter=0
yeet=len(results)
for k in range(yeet):
    if plusDayLoopCounter<=plusDays:
        if results[k]>=0.0: 
            plusDayLoopCounter+=1     
        total+=total*(results[k]/100)
        restDayLoopCounter=0
        print(total)
    elif results[k]<0.0 and restDayLoopCounter<=restDays:
        plusDayLoopCounter=0
        #total+=total*results[k]
        restDayLoopCounter+=1
print(total)

            




