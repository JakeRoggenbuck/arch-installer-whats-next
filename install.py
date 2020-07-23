import subprocess

def runner(line):
    line = line.strip("\n")
    runline = input(f"Run: {line} [Y/n] ")
    if runline.upper() == "Y":
        try:
            subprocess.run([line], shell=True)
        except subprocess.CalledProcessError as e:
            print(e.output)
    elif runline.upper() == "E":
        subprocess.run([f"echo \"{line}\" > /tmp/runline"], shell=True)
        subprocess.run(["vim /tmp/runline"], shell=True)
        y = subprocess.check_output(["cat /tmp/runline"], shell=True).decode("UTF-8")
        runner(y)

lines = [
    "ls /sys/firmware/efi/efivars",
    "ping 8.8.8.8",
    "ip link",
    "timedatectl set-ntp true",
    "date",
    "lsblk",
    "cfdisk /dev/sda",
    "lsblk",
    "mkfs.fat -F32 /dev/sda1",
    "mkfs.ext4 /dev/sda2",
    "mkfs.ext4 /dev/sda3",
    "mount /dev/sda2 /mnt",
    "mkdir /mnt/home",
    "mount /dev/sda3 /mnt/home",
    "lsblk",
    "pacstrap /mnt base linux linux-firmware"
    "genfstab -U /mnt >> /mnt/etc/fstab",
    "cat /mnt/etc/fstab",
    "arch-chroot /mnt /bin/bash"
]

dolist = input("print list? [Y/n] ")
if dolist.upper() == "Y":
    for x,line in enumerate(lines):
        print(f"{x} : {line}")

start = input("Select the starting point: ")

print("For each command, type 'E' for edit, or [Y/n] for running it")
for line in lines[int(start):]:
    runner(line)
