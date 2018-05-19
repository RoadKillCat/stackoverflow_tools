import json
import matplotlib.pyplot as plt
import numpy as np

#get stack data json from "Edit Profile & Settings" section

p = 32
w = 0.4
d = json.loads(open('../Downloads/stack_data.json').read())

k = list(d['Data']['InterestingTags']['stackoverflow.com'].keys())[:p]
v = list(d['Data']['InterestingTags']['stackoverflow.com'].values())[:p]

f = plt.figure()
i = np.arange(len(k))
plt.bar(i, v, width=w)
plt.xticks(i, k)
plt.yticks(np.arange(0, 1.05, 0.05))
plt.grid(linestyle=':')
f.autofmt_xdate()
f.set_size_inches(10, 5)
#plt.show()
plt.savefig('data.pdf')
