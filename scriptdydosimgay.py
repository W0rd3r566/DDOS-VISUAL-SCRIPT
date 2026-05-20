import sys
import time
import random
import os

# Пытаемся импортировать colorama для цвета, если нет - работаем без неё
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    GREEN = Fore.GREEN
    RED = Fore.RED
    CYAN = Fore.CYAN
    YELLOW = Fore.YELLOW
    MAGENTA = Fore.MAGENTA
    RESET = Style.RESET_ALL
except ImportError:
    GREEN = RED = CYAN = YELLOW = MAGENTA = RESET = ""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dramatic_print(text, delay=0.03, color=GREEN):
    """Печатает текст по одной букве, создавая драматический эффект."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_progress(task, duration):
    """Имитирует прогресс-бар."""
    sys.stdout.write(CYAN + f"[*] {task}... " + RESET)
    for i in range(101):
        time.sleep(duration / 100)
        sys.stdout.write(f"\r{CYAN}[*] {task}... {i}%{RESET}")
        sys.stdout.flush()
    print()

def main():
    clear_screen()
    
    # --- БАННЕР ---
    print(MAGENTA + """
    ╔══════════════════════════════════════╗
    ║     ░█▀▄░█▀▀░█▀▀░▀█▀░█▀▀░█░█░▄▀▀    ║
    ║     ░█░░░█▀▀░▀▀▄░░█░░█▀▀░█░█░▀▄▄    ║
    ║     ░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀░    ║
    ║  ███▓▒░░TERMINAL EXPLOIT v4.2░░▒▓███ ║
    ╚══════════════════════════════════════╝
    """ + RESET)

    target = input(RED + "\n[@] ENTER TARGET IP / USERNAME: " + GREEN).strip()
    
    if not target:
        print(RED + "[!] NO TARGET PROVIDED. CONNECTION TERMINATED." + RESET)
        sys.exit(1)

    clear_screen()
    dramatic_print(f"\n>>> INITIATING SECURE CONNECTION TO {target}...", 0.02, CYAN)
    time.sleep(1)

    # Фейковые этапы взлома
    steps = [
        ("SCANNING OPEN PORTS", 1.5),
        ("BYPASSING FIREWALL (ADVANCED EVASION TECHNIQUE)", 2.5),
        ("INJECTING PAYLOAD INTO TCP/443", 2.0),
        ("ESCALATING PRIVILEGES TO ROOT", 2.0),
        ("DUMPING DATABASE CREDENTIALS", 2.5),
        ("DECRYPTING HASHES (AES-256)", 3.0),
        ("EXFILTRATING SENSITIVE DATA", 2.0),
        ("COVERING TRACKS (PURGING LOGS)", 1.5),
    ]

    for step, duration in steps:
        fake_progress(step, duration)
        time.sleep(0.2)
    
    print("\n" + YELLOW + "[!] " + RESET + YELLOW + "ACCESS GRANTED. ROOT SHELL ESTABLISHED." + RESET)
    time.sleep(0.5)
    
    # Генерация фейковых данных
    fake_db = [
        f"admin:{random.randint(100000, 999999)}",
        f"user_{random.randint(1, 99)}:password{random.randint(100, 999)}",
        f"{target}_backup:root{random.randint(1000, 9999)}"
    ]
    
    fake_files = [
        "/root/secret_project_alpha.pdf",
        "/etc/shadow",
        "/var/www/html/config.php",
        "/home/user/bitcoin_wallet.dat"
    ]
    
    dramatic_print("\n--- CREDENTIALS DUMP ---", 0.01, MAGENTA)
    for cred in fake_db:
        dramatic_print(f"[+] {cred}", 0.02, GREEN)
    
    dramatic_print("\n--- FOUND SENSITIVE FILES ---", 0.01, MAGENTA)
    for file in fake_files:
        dramatic_print(f"[>] {file}", 0.02, CYAN)

    print("\n" + RED + "[!] " + RESET + RED + "TRACE ROUTE INITIATED. TARGET LOCATION: " + RESET, end="")
    cities = ["Moscow, RU", "Berlin, DE", "New York, US", "Tokyo, JP", "Amsterdam, NL"]
    dramatic_print(random.choice(cities), 0.03, YELLOW)
    
    print("\n" + GREEN + "[√] OPERATION 'SHADOW FALL' COMPLETED SUCCESSFULLY." + RESET)
    print(RED + "[WARNING] DISCONNECT IN 5 SECONDS TO AVOID TRACE..." + RESET)
    
    for i in range(5, 0, -1):
        sys.stdout.write(f"\r{RED}EXITING IN {i}...{RESET}")
        sys.stdout.flush()
        time.sleep(1)
    
    clear_screen()
    print(GREEN + "SECURE CHANNEL CLOSED." + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(RED + "\n[!] ABORT MISSION! COVER YOUR TRACKS!" + RESET)
        sys.exit(0)