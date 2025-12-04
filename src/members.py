class Members:
    def __init__(self):
        self.members = []

    def add_member(self, member_id, name):
        self.members.append({
            "member_id": member_id,
            "name": name
        })
        return f"Member '{name}' registered."
