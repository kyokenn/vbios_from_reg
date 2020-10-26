import winreg
import sys


def main():
    root_hkey = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\Class')

    i = 0
    class_hkey = None
    while True:
        try:
            name = winreg.EnumKey(root_hkey, i)
            i += 1
            class_hkey = winreg.OpenKey(root_hkey, name)
            value, rtype = winreg.QueryValueEx(class_hkey, 'Class')
            if value == 'Display':
                print('Found display class')
                break
        except OSError:
            print('Display class not found')
            sys.exit(1)

    i = 0
    device_hkey = None
    while True:
        try:
            name = winreg.EnumKey(class_hkey, i)
            i += 1
            device_hkey = winreg.OpenKey(class_hkey, name)
            value, rtype = winreg.QueryValueEx(device_hkey, 'DriverDesc')
            if 'NVIDIA' in value.upper():
                print('Found NVIDIA display adaptor')
                break
        except OSError:
            print('NVIDIA display adaptor not found')
            sys.exit(1)

    sesson_hkey = winreg.OpenKey(device_hkey, 'Session')
    vbios, rtype = winreg.QueryValueEx(sesson_hkey, 'vbios')
    filename = 'vbios.rom'
    with open(filename, 'wb') as f:
        f.write(vbios)

    print('VBIOS saved to file "{}"'.format(filename))


if __name__ == '__main__':
    main()
