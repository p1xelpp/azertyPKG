import os

# using nuitka --onefile here, i dunno if i want a 2gb installer >M<
os.system("""
chmod +x ./cp2bin
sudo ./cp2bin cp2bin
sudo cp2bin rmbin
sudo cp2bin bin2home
sudo cp2bin vpkg-install
sudo cp2bin vpkg
""")

choice = input("do you want the build tool for a .vpkg? (y/n) >>> ").strip().lower()

if choice == "y":
    os.system("sudo cp2bin vellpkg-build")
else:
    print("alrighty, if you change ur mind, just use sudo cp2bin vellpkg-build")

