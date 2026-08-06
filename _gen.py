import base64,sys
s=base64.b64decode(sys.argv[1]).decode()
open(sys.argv[2],"w").write(s)
