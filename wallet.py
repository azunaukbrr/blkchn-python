import subprocess
import json
from pprint import pprint

command = "php hd-wallet-derive/hd-wallet-derive.php -g --mnemonic=\"toss sing pride history initial afford oval liar only lamp unveil educate\" --cols=path,address,privkey --format=json"

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p.wait()
keys = json.loads(output)
pprint(keys)