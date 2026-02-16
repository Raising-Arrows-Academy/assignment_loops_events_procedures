"""
Main module for Python assignment.
This assignment demonstrates use of Variables and Conditional Statements.
"""


def main():
    print("=" * 75)

    # store the member's name (string)
    member_name = "John Smith"

    # store the books that are checked out (number)
    books_checked_out = 3

    # store whether the library account is active (boolean)
    account_is_active = True

    print("Member Name:", member_name)
    print("Books Checked Out:", books_checked_out)
    print("Account Active:", account_is_active)

    # conditional statement to check the library rules
    if not account_is_active:
        print("You must have an active account in order to check out any books.")
    elif books_checked_out >= 5:
        print("You cannot check out anymore books, 5 is the limit.")
    else:
        print("You can check out more books.")

    print("=" * 75)


if __name__ == "__main__":
    main()
