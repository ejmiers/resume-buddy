from flask_server import app
from sys import argv, exit

def checkDebug():
    debugTrue = "debug=true"
    debugFalse = "debug=false"

    if len(argv) != 2:
        printUsage()

    arg = argv[1]
    if arg.lower() == debugTrue:
        return True
    elif arg.lower() == debugFalse:
        return False
    else:
        printUsage()

def printUsage():
    print("Error: first argument must contain 'debug=true' or 'debug=false'")
    exit()


if __name__ == '__main__':
    debug = checkDebug()
    app.run(debug=debug)
