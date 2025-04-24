import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.cleaner import clean_text

def crm_demo():
    print("🧾 Oracle CRM Ticket Cleaning Demo\n")

    raw_tickets = [
        "Can't log in to my account — keeps saying password is wrong.",
        "I can’t login, says my credentials are invalid!",
        "Login doesn’t work, tried resetting too.",
        "Password reset link not working. I can’t get in!"
    ]

    for i, ticket in enumerate(raw_tickets, 1):
        cleaned = clean_text(ticket)
        print(f"[Ticket {i}]\nOriginal: {ticket}\nCleaned:  {cleaned}\n")

if __name__ == "__main__":
    crm_demo()
