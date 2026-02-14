import os
import time
import csv

basepath = "/home/ansh/Biometric_EVM"
votepath = "/home/ansh/Biometric_EVM/votes"
os.makedirs(votepath, exist_ok=True)

while True:
    line = ser.readline().decode().strip()

    if line:
        print(line)

        try:
            constituency, party = line.split("_", 1)
            imagepath = f"{basepath}/{line}.png"
            command = f"sudo fbi -T 1 -d /dev/fb0 --noverbose {imagepath}"
            os.system(command)
            time.sleep(3)
            os.system("sudo pkill fbi")
            csv_file = f"{votepath}/{constituency}.csv"
            votes = {}
            if os.path.exists(csv_file):
                with open(csv_file, mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if len(row) == 2:
                            votes[row[0]] = int(row[1])
            if party in votes:
                votes[party] += 1
            else:
                votes[party] = 1
            with open(csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                for p, count in votes.items():
                    writer.writerow([p, count])

        except Exception as e:
            print("Error:", e)
            vote = "black"
            imagepath = f"{basepath}/{vote}.png"
            command = f"sudo fbi -T 1 -d /dev/fb0 --noverbose {imagepath}"
            os.system(command)

    else:
        vote = "black"
        imagepath = f"{basepath}/{vote}.png"
        command = f"sudo fbi -T 1 -d /dev/fb0 --noverbose {imagepath}"
        os.system(command)
