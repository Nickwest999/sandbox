"""
Nicholas West
27/8/2020
Broken Scores
"""


def main():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    print(status_results(score))


def status_results(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()