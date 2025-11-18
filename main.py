#!/usr/bin/env python3
# Educational Purpose Only

import os
import time
import sys

# Colors for terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def clear_screen():
    os.system('clear')

def banner():
    clear_screen()
    print(f"""{Colors.GREEN}
    ╔══════════════════════════════════╗
    ║      @TGINWPBANER - TOOL         ║
    ║    FOR EDUCATIONAL PURPOSE       ║
    ║          ONLY FOR LEARNING       ║
    ╚══════════════════════════════════╗
    {Colors.END}""")

def main_menu():
    banner()
    print(f"\n{Colors.YELLOW}[MAIN MENU]{Colors.END}")
    print(f"{Colors.BLUE}1. Telegram Channel Info")
    print("2. Instagram Account Info")
    print("3. WhatsApp Number Info")
    print("4. Telegram Account Info")
    print("5. About This Tool")
    print("6. Exit{Colors.END}")
    
    choice = input(f"\n{Colors.GREEN}Select option: {Colors.END}")
    return choice
  
