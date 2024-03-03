import sys
# check for errors
if len(sys.argv) < 2 :
    sys.exit (print('very less arguments'))
for arg in sys.argv[1:-1]:#slicing
    print('hellos ',arg)