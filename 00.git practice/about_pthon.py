# Election between BJP and Congress

print("Welcome to the Election Result Program")

bjp_votes = int(input("Enter BJP votes: "))
congress_votes = int(input("Enter Congress votes: "))

if bjp_votes > congress_votes:
    print("BJP wins the election!")
elif congress_votes > bjp_votes:
    print("Congress wins the election!")
else:
    print("Election is tied between BJP and Congress!")

print(f"Total votes: {bjp_votes + congress_votes}")
