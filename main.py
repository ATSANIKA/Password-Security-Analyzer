"""
Project Name : Password Security Analyzer

Developer : Sanika Patil

Description :
This module performs password security analysis,
calculates password score, entropy,
estimated crack time and suggestions.
"""

from analyzer import analyze_password, generate_strong_password

print("=" * 50)
print(" PASSWORD SECURITY ANALYZER ".center(50))
print("=" * 50)

password = input("Enter your password: ")

results = analyze_password(password)

print("\nAnalysis Result")
print("-" * 40)

checks = [
    ("Length", "length"),
    ("Uppercase", "uppercase"),
    ("Lowercase", "lowercase"),
    ("Number", "number"),
    ("Special Character", "special"),
    ("Common Password", "common")
]

for title, key in checks:
    status, message = results[key]
    print(f"{title}: {message}")

print("\n" + "=" * 40)
print(f"Overall Score      : {results['score']}/100")
print(f"Password Entropy : {results['entropy']} bits")
print(f"Estimated Crack Time : {results['crack_time']}")
print(f"Password Strength  : {results['strength']}")
print("=" * 40)
print("\nSuggestions")
print("-" * 40)

for suggestion in results["suggestions"]:
    print(f"• {suggestion}")

print("=" * 40)

print("\nSuggested Strong Password")
print("-" * 40)
print(generate_strong_password())
print("=" * 40)
