import h5py
# import os
# print(os.path.exists('.\\weight\\pmfinal.h5'))  # True หมายถึงไฟล์มีอยู่
try:
    with h5py.File('.\\weight\\pmfinal.h5', 'r') as f:
        print("File loaded successfully.")
except Exception as e:
    print(f"Error: {e}")
