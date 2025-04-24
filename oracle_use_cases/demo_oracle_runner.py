import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from oracle_use_cases.crm_ticket_cleaning import crm_demo
from oracle_use_cases.survey_feedback_cleaning import survey_demo
from oracle_use_cases.model_input_preprocessing import model_demo

def run_all_demos():
    print("\n🔧 Running All Oracle Use Case Demos:\n")
    print("────────────────────────────────────────────\n")
    crm_demo()
    print("────────────────────────────────────────────\n")
    survey_demo()
    print("────────────────────────────────────────────\n")
    model_demo()
    print("────────────────────────────────────────────\n")

if __name__ == "__main__":
    run_all_demos()
