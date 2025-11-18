from main import *
from telegram_module import telegram_channel_menu
from instagram_module import instagram_info
from whatsapp_module import whatsapp_info

def telegram_account_info():
    print(f"\n{Colors.YELLOW}[TELEGRAM ACCOUNT INFO]{Colors.END}")
    username = input(f"{Colors.BLUE}Enter username: {Colors.END}")
    print(f"{Colors.GREEN}Learning about account safety...{Colors.END}")
    time.sleep(2)

def about_tool():
    banner()
    print(f"""
{Colors.YELLOW}ABOUT THIS EDUCATIONAL TOOL{Colors.END}

{Colors.BLUE}Purpose: 
• Learn about platform reporting systems
• Understand digital safety measures
• Educational demonstration only

{Colors.GREEN}Important:
• This doesn't actually report anything
• For learning programming concepts
• Always use official channels for real issues

{Colors.RED}Disclaimer:
This tool is created for educational purposes only.
Misuse of this knowledge is strictly prohibited.
{Colors.END}
    """)
    input(f"\n{Colors.BLUE}Press Enter to continue...{Colors.END}")

def main():
    while True:
        choice = main_menu()
        
        if choice == '1':
            telegram_channel_menu()
        elif choice == '2':
            instagram_info()
        elif choice == '3':
            whatsapp_info()
        elif choice == '4':
            telegram_account_info()
        elif choice == '5':
            about_tool()
        elif choice == '6':
            print(f"{Colors.GREEN}Thanks for learning!{Colors.END}")
            break
        else:
            print(f"{Colors.RED}Invalid choice!{Colors.END}")
            time.sleep(1)

if __name__ == "__main__":
    main()
