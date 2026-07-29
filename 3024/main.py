"""SurprisingVote"""

S = float(input())
M = float(input())

if M <= 2:
    print("Not surprising")
elif S <= 2 * M:
    print("Surprising")
elif S < 3 * M - 2:
    print("Surprising")
else:
    print("Not surprising")
