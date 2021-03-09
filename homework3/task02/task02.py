import hashlib
import struct

cacher = dict()


def slow_calculate(value):
    """Some weird voodoo magic calculations"""

    # time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    # print(len(data), data, "<-len(data)")
    ans = sum(struct.unpack("<" + "B" * len(data), data))
    if ans in cacher:
        print(value, cacher[ans], "<-")
        print(hashlib.md5(str(value).encode()).digest(), hashlib.md5(str(cacher[ans]).encode()).digest())

    cacher[ans] = value
    return ans


for i in range(500):
    slow_calculate(i)
