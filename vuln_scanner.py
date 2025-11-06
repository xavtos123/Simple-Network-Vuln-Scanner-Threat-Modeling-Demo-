# Simple Network Vuln Scanner - Like a treasure hunt for weak spots in a spy network!
# Imagine a secret spy base with doors (ports) and walls (firewalls). This tool checks if doors are unlocked or walls are thin.
# I use a pretend list of 'devices' (like computers in space) and Qs like "Is the door open?" to find risks.
# Output: List of 'bad spots' and how to fix, based on cybersecurity threat modeling work.

import random  # Like rolling dice to pick a pretend network spot.

def scan_network(devices):
    # devices = list of pretend spy base computers, e.g., ['satellite1', 'ground_control']
    risks = []  # List to collect 'bad spots' like a shopping list of problems.
    for device in devices:
        # Pretend check: Is the 'door' (port 80) open? 30% chance, like a random draw.
        if random.choice([True, False, False, False, False, False, False]):  # 1/7 chance it's open (bad!).
            risk = f"{device}: Open door (port 80)! Bad guys could sneak in. Fix: Lock it with firewall (NIST tip)."
            risks.append(risk)
        # Pretend check: Is the 'wall' (TLS) weak? 20% chance.
        if random.choice([True, False, False, False, False]):  # 1/5 chance weak (vulg!).
            risk = f"{device}: Weak wall (TLS not hardened). Messages could be read. Fix: Add zero-trust lock."
            risks.append(risk)
    return risks

# Pretend spy base (like a space network with satellites).
spy_base = ['satellite1', 'satellite2', 'ground_station', 'orbital_relay']

# Run the hunt!
found_risks = scan_network(spy_base)
print("Hunt Results - Weak Spots Found:")
if found_risks:
    for risk in found_risks:
        print(risk)
else:
    print("All spots secure! Great job hardening the network.")
# Tip: can ran this many times to see different 'risks' – like real threat modeling.
