from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, mask_start=0, mask_end=32):
        IPv4Network.__init__(self,
                             (random.randint(0x0B000000, 0xDF000000),
                              random.randint(mask_start, mask_end)),
                             strict=False
                             )

    def regular(self):
        return self.is_global and not (self.is_multicast or self.is_link_local or self.is_loopback or self.is_private or self.is_reserved or self.is_unspecified)
    def key_value(self):
        return int(self.network_address) + (int(self.netmask) << 32)

def sortfunc(x):
    return x.key_value()

random.seed()

network_list = []

while len(network_list) < 50:
    random_network = IPv4RandomNetwork(8, 24)
    if random_network.regular() and random_network not in network_list:
        network_list.append(random_network)

for n in sorted(network_list, key=sortfunc):
    print(n)
