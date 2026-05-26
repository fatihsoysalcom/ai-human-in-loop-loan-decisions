import random

def simulate_ai_loan_prediction(applicant_id):
    """Simulates an AI predicting the probability of loan default."""
    # In a real scenario, this would be a complex ML model.
    # For this example, we'll use a random probability.
    probability_of_default = random.uniform(0.1, 0.8)
    print(f"AI for Applicant {applicant_id}: Predicted default probability = {probability_of_default:.2f}")
    return probability_of_default

def human_review_decision(applicant_id, ai_suggestion):
    """Simulates a human reviewing a high-risk AI decision."""
    print(f"\n--- Human Review Required for Applicant {applicant_id} ---")
    print(f"AI's initial suggestion: {ai_suggestion}")
    while True:
        human_input = input("Human reviewer: Do you (A)pprove, (R)eject, or (M)odify? [A/R/M]: ").strip().upper()
        if human_input in ['A', 'R', 'M']:
            if human_input == 'M':
                new_decision = input("Enter new decision (e.g., 'Approved with conditions', 'Rejected due to insufficient data'): ").strip()
                return new_decision
            return "Approved" if human_input == 'A' else "Rejected"
        else:
            print("Invalid input. Please enter A, R, or M.")

def process_loan_application(applicant_id):
    """Processes a loan application using a Human-in-the-Loop approach."""
    print(f"\nProcessing loan application for Applicant {applicant_id}...")
    default_prob = simulate_ai_loan_prediction(applicant_id)

    # Define thresholds for risk levels
    AUTO_APPROVE_THRESHOLD = 0.3
    HUMAN_REVIEW_THRESHOLD = 0.6 # If prob > this, it's auto-reject, otherwise human review if > AUTO_APPROVE_THRESHOLD

    final_decision = ""
    ai_suggestion = ""

    if default_prob < AUTO_APPROVE_THRESHOLD:
        ai_suggestion = "Approved (Low Risk)"
        final_decision = ai_suggestion
        print(f"AI automatically approves loan for Applicant {applicant_id}.")
    elif default_prob >= HUMAN_REVIEW_THRESHOLD:
        ai_suggestion = "Rejected (High Risk)"
        final_decision = ai_suggestion
        print(f"AI automatically rejects loan for Applicant {applicant_id}.")
    else:
        # This is the "Human-in-the-Loop" part: AI flags for human intervention
        ai_suggestion = "Requires Human Review (Medium Risk)"
        print(f"AI suggests human review for Applicant {applicant_id}.")
        final_decision = human_review_decision(applicant_id, ai_suggestion)
        print(f"Human reviewer's final decision for Applicant {applicant_id}: {final_decision}")

    print(f"Final outcome for Applicant {applicant_id}: {final_decision}")
    return final_decision

if __name__ == "__main__":
    print("--- Human-in-the-Loop Loan Application System ---")
    # Simulate processing a few applications
    for i in range(1, 4):
        process_loan_application(f"APP-{i:03d}")
    print("\n--- System finished ---")
