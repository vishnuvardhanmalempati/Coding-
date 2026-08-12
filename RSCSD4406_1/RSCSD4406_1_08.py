#Convert seconds into hours, minutes and seconds 
total_seconds = int(input("Enter total seconds: "))
hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60
print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)
