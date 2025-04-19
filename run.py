import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x bazyab')
    os.system('./bazyab')
elif bit == '32bit':
    os.system('chmod +x bazyab32')
    os.system('./bazyab32')
else:
    print('device not supported')
