import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from dataset.data_generator import KNOWLEDGE_BASE

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "all_qa_list.txt")

CATEGORY_LABELS = {
    "General":      "GENERAL SCHOOL COMMUNICATION",
    "Fees":         "FEES & PAYMENTS",
    "Admissions":   "ADMISSIONS & ENROLLMENT",
    "Academic":     "ACADEMICS & EXAMS",
    "Facilities":   "FACILITIES & SERVICES",
    "Staff":        "STAFF & CONTACT",
    "Policies":     "POLICIES & RULES",
    "HR":           "HR & PAYROLL (STAFF)",
    "Health":       "HEALTH & MEDICAL",
    "Events":       "EVENTS & COMPETITIONS",
    "ParentPortal": "PARENT PORTAL & DIGITAL SERVICES",
    "Counseling":   "COUNSELING & CLUBS",
    "Safety":       "SAFETY & INFRASTRUCTURE",
}

INTROS = [
    "", "Can you tell me, ", "I want to know: ", "Please explain: ",
    "Question: ", "Query: ", "Sir/Madam, ", "Hello, ", "Hi, "
]

OUTROS = [
    "", " Thank you.", " Please be specific.", " Thanks!",
    " Kindly advise.", " Please help.", " Urgent please."
]

total_pairs = 0

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for category, items in KNOWLEDGE_BASE.items():
        label = CATEGORY_LABELS.get(category, category.upper())

        # ── Category header ──────────────────────────────────
        f.write(f"\n{'─' * 70}\n")
        f.write(f"  {label}\n")
        f.write(f"{'─' * 70}\n\n")

        for base_q, base_a, variations in items:
            all_questions = [base_q] + list(variations)

            for q in all_questions:
                for intro in INTROS:
                    for outro in OUTROS:
                        final_q = (intro + q + outro).strip()
                        f.write(f"Q: {final_q}\n")
                        f.write(f"A: {base_a}\n\n")
                        total_pairs += 1

            f.write(f"{'- ' * 35}\n\n")  # separator between facts

print(f"Done! Exported {total_pairs:,} Q&A pairs (all combos, categorized) to:\n  {OUTPUT_FILE}")
