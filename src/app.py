from books import Books
from members import Members
from issue_return import IssueReturn

def main():
    print("===== Library Management System =====")

    books = Books()
    members = Members()
    issue_return = IssueReturn()

    print("Sample operations running...")

    # Add sample book
    print(books.add_book("B101", "Python Programming", "James"))

    # Add sample member
    print(members.add_member("M001", "Ananya"))

    # Issue sample book
    print(issue_return.issue_book("M001", "B101"))

if __name__ == "__main__":
    main()
