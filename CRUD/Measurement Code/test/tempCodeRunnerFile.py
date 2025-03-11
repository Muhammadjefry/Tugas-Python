# Komunikasi Serial From Arduino

# import serial.tools.list_ports

# ports = list(serial.tools.list_ports.comports())
# for p in ports:
#     print(p)

# #exit()

# ser = serial.Serial('COM6', 9600)
# data = ''
# old_data = ''
# while True:
#     if ser.in_waiting > 0:
#         try:
#             data = ser.readline().decode('ascii').strip()
#             if data != old_data:
#                 print(f'Data dari arduino: {data}')
#                 old_data = data
                
#         except:
#             pass