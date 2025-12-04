class IssueReturn:
    def __init__(self):
        self.issues = []

    def issue_book(self, member_id, book_id):
        self.issues.append({
            "member_id": member_id,
            "book_id": book_id
        })
        return f"Book {book_id} issued to member {member_id}."
