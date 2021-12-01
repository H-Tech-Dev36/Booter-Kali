import os 
iso = raw_input("iso cible :>>> ")
print(iso)
sdX = raw_input("Nom [sdb]:>>>  ")
print(sdX)
os.system("sudo dd if="+ iso +" of=/dev/"+sdX +" bs=4M status=progress conv=fdatasync ")
print("FINISH ;) thanks you :")
print("GitHub : https://github.com/H-Tech-Dev36")
print("don't froget the Star pleas ;) ")
exit 