# Program: Trust and Reputation System for Service Providers
# Question 29 – AI & Expert System (MLA0102)

class ServiceProvider:
    def __init__(self, name):
        self.name = name
        self.feedback = []          # Store feedback as +1 (positive) or -1 (negative)

    def add_feedback(self, rating):
        self.feedback.append(rating)

    def trust_score(self):
        return sum(self.feedback) / len(self.feedback) if self.feedback else 0


class ReputationSystem:
    def __init__(self):
        self.providers = {}

    def add_provider(self, name):
        self.providers[name] = ServiceProvider(name)

    def give_feedback(self, provider_name, positive=True):
        if positive:
            self.providers[provider_name].add_feedback(1)
        else:
            self.providers[provider_name].add_feedback(-1)

    def compute_reputation(self):
        print("\n--- Provider Trust & Reputation Scores ---")
        for name, provider in self.providers.items():
            print(f"{name}: Trust Score = {provider.trust_score():.2f}")

    def best_provider(self):
        best = max(self.providers.values(), key=lambda p: p.trust_score())
        print(f"\n✅ Best provider based on reputation: {best.name}")


# -------- Main Program -------- #
system = ReputationSystem()

# Add service providers
system.add_provider("Provider A")
system.add_provider("Provider B")
system.add_provider("Provider C")

# Clients give feedback (positive or negative)
system.give_feedback("Provider A", positive=True)
system.give_feedback("Provider A", positive=False)
system.give_feedback("Provider B", positive=True)
system.give_feedback("Provider B", positive=True)
system.give_feedback("Provider C", positive=False)

# Compute trust scores & reputation
system.compute_reputation()

# Select the best provider
system.best_provider()
