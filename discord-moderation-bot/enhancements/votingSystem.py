# votingSystem.py (Python)

"""
This file contains the implementation of the voting system for users to participate in decision-making processes within the server.
"""

class VotingSystem:
    def __init__(self):
        self.votes = {}

    def start_vote(self, vote_id, question, options):
        if vote_id in self.votes:
            return "Vote ID already exists"
        self.votes[vote_id] = {"question": question, "options": {option: 0 for option in options}}
        return "Vote started successfully"

    def get_question(self, vote_id):
        if vote_id in self.votes:
            return self.votes[vote_id]["question"]
        return "Vote ID not found"

    def get_options(self, vote_id):
        if vote_id in self.votes:
            return self.votes[vote_id]["options"]
        return "Vote ID not found"

    def vote(self, vote_id, option):
        if vote_id in self.votes:
            if option in self.votes[vote_id]["options"]:
                self.votes[vote_id]["options"][option] += 1
                return "Vote cast successfully"
            return "Option not found"
        return "Vote ID not found"

    def end_vote(self, vote_id):
        if vote_id in self.votes:
            results = self.votes[vote_id]["options"]
            del self.votes[vote_id]
            return results
        return "Vote ID not found"

# End of votingSystem.py