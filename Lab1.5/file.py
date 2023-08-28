import glob

files = glob.glob("c:\\TEMP\\*.log")
L=[]
ip_addr = set()

for current_file in files :
    with open(current_file) as f:
        for line in f:
            if "ip address" in line:
               ip_addr.add(line.replace("ip address", "").strip())


for i in ip_addr:
    sorted(ip_addr)
    print(i)