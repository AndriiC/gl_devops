import psutil

metrics = input("Enter metrics type 'cpu' or 'mem' = ")
if metrics=="cpu":
        print(psutil.cpu_times())
elif metrics=="mem":
        print(psutil.virtual_memory())
else:
        print("Please specify correct metrics")