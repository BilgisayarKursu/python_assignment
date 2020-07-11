age = input("Are you a cigarette addict older than 75 years old? Please answer YES or NO ").strip().lower() == "yes"
chronic = input("Do you have a severe chronic disease? Please answer YES or NO ").strip().lower() == "yes"
immune = input("Is your immune system too weak? Please answer YES or NO ").strip().lower() == "yes"

death_risk = age or (chronic or immune)
if death_risk:
    print("You are in risky group")
else:
    print("You are not in risky group")
