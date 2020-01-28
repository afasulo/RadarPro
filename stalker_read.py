import serial
import csv
import xlsxwriter
from collections import deque

ser = serial.Serial(
        port='/dev/cu.usbserial',
        baudrate=9600,
        timeout=None, 
        xonxoff=False
        )

stop = False
rep_count = 0
reps = 0
p_count = 0
tbl = []

print('\n----------Stalker Velo Logger--------------\n')
print("\n-----Please make sure athletes stay in order and don't deviate from training plan------\n\n")

wbname = input("Workbook name (ex: V_tool_09_2019.xlsx):")
wb = xlsxwriter.Workbook(wbname)

while not stop:

    name = input("\n\tAthlete's Name:")
    reps = int(input("Reps to log (leave blank to log infinitely for athlete until the shift + Q key is pressed):"))
    print("\n\n\n{} reps will be logged for {}".format(reps, name))

    tbl.insert(p_count, name)

    athlete_worksheet = wb.add_worksheet(name)
    mph = []
    mph.clear()

    while rep_count <= reps:
        print('rep count {}'.format(rep_count))
        ser_bytes = ser.read(5)
        decoded_bytes = ser_bytes.decode("ascii").strip()
        mph.insert(rep_count, decoded_bytes)
        #tbl[p_count][rep_count].extend(ser.readline().strip().decode('ascii'))


        with open("test_data.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            #writer.writerow([mph[rep_count]])
            rep_count = rep_count + 1


    else:
        rep_count = 0
        tbl[p_count] = tbl.append(mph)
        print(tbl)
        p_count += 1
        break






