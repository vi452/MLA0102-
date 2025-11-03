
import random

TOTAL_RESOURCE = 100     #
# discount factor (0 < δ ≤ 1)
discount_A = 0.9     # Agent A values delay less
discount_B = 0.85    # Agent B values delay even less

max_rounds = 10      # stop if no agreement within these rounds


def utility(share, discount, round_no):
    return share * (discount ** round_no)


# Negotiation Process
def negotiate():
    round_no = 0

    while round_no < max_rounds:
        print(f"\n--- Round {round_no + 1} ---")

        # Agent A makes an offer
        offer_A = random.randint(40, 70)        # A proposes how much they want
        A_share = offer_A
        B_share = TOTAL_RESOURCE - offer_A

        print(f"Agent A proposes: A = {A_share}, B = {B_share}")

        # Compute utility for Agent B to decide accept/reject
        if utility(B_share, discount_B, round_no) >= utility(0, discount_B, round_no):
            print("Agent B ACCEPTS ✅")
            return A_share, B_share

        print("Agent B rejects ❌")

        round_no += 1

        # Agent B makes counteroffer
        offer_B = random.randint(30, 60)
        B_share = offer_B
        A_share = TOTAL_RESOURCE - offer_B

        print(f"Agent B proposes: A = {A_share}, B = {B_share}")

        # Agent A decision
        if utility(A_share, discount_A, round_no) >= utility(0, discount_A, round_no):
            print("Agent A ACCEPTS ✅")
            return A_share, B_share

        print("Agent A rejects ❌")

        round_no += 1

    print("\n❌ No agreement reached.")
    return None


# ---- Main Program ----
agreement = negotiate()

if agreement:
    print("\nFinal Agreement Reached:")
    print(f"Agent A gets: {agreement[0]} units")
    print(f"Agent B gets: {agreement[1]} units")
else:
    print("\nNegotiation Failed.")

output
