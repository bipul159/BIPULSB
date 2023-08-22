#<\>!python3.11
#<\>coded by RMX
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://www.facebook.com/mdbipul.khan.1420354?mibextid=ZbWKwL )
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf BIPULSB.so')
except:
    pass
os.system('rm -rf BIPULSB.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('BIPULSB.so'):
        os.system('curl -L https://github.com/bipul159/executables/blob/main/BIPULSB.cpython-311.so?raw=true -o BIPULSB.so') 
        import RMXXD
        #RMXXD.RM()
    else:
        import RMXXD
        #RMXXD.RM()
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    
