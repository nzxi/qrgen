import qrcode
import os
import sys


TITLE = r"""
   ____  _____   _____ ______ _   _ 
  / __ \|  __ \ / ____|  ____| \ | |
 | |  | | |__) | |  __| |__  |  \| |
 | |  | |  _  /| | |_ |  __| | . ` |
 | |__| | | \ \| |__| | |____| |\  |
  \___\_\_|  \_\\_____|______|_| \_|

  By nzxi@github
"""

def export(image):
    file_name = ""
    while not file_name:
        file_name = input("Save file as: ").strip()
    if not file_name.lower().endswith(".png"):
        file_name += ".png"
    image.save(file_name)
    print(f"QR code saved as {file_name}")

def default_qr(qr_data=None):
        while not qr_data:
            qr_data = input("Enter url/text: ")
        qr = qrcode.make(qr_data)
        export(qr)

def mail_qr(qr_data=None):
        while not qr_data:
            qr_data = input("Enter the email address: ")
        qr = qrcode.make(f"mailto:{qr_data}")
        export(qr)
    
def phone_qr(qr_data=None):
    while not qr_data:
        qr_data = input("Enter a phone number: ")
    qr = qrcode.make(f"tel:{qr_data}")
    export(qr)
    
def clear_screen():
    if not sys.stdout.isatty():
        return
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def kill():
    sys.exit(0)

def main():
    while True:
        clear_screen()
        print(TITLE + '\n')
        print("1. Default QR(URL)")
        print("2. Mail QR")
        print("3. Phone number QR")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            default_qr()
            input("Press Enter to continue...")
        elif choice == '2':
            mail_qr()
            input("Press Enter to continue...")
        elif choice == '3':
            phone_qr()
            input("Press Enter to continue...")
        elif choice == '4':
            kill()
        else:
            print("Invalid choice")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
