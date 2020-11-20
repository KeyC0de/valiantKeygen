import random
import sys
import os

if ( len( sys.argv ) < 2 ):
    foundValueThroughDbg = 783
else:
    foundValueThroughDbg = sys.argv[0]

def checkKey( key ):
    keysum = 0
    for c in key:
        keysum += ord( c )
    
    return keysum

key = ""
foundKeys = 0
while True:
    key += random.choice( "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" )
    keysum = checkKey( key )
    
    if keysum > foundValueThroughDbg:
        key = ""    # start over
    elif keysum == foundValueThroughDbg:
        print( "Found key: {0}".format( key ) )
        foundKeys += 1
    else:
        continue
    
    if foundKeys == 100:    # acquire 100 keys for now
        break