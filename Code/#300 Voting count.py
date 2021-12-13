"""
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.

Write a program that reads this file as a stream and returns the top 3 candidates at any given time.
If you find a voter voting more than once, report this as fraud.
"""
from chrono import chrono

def mostPopularCandidates(file, numCandidates = 3):
    candidateVotes = {}
    alreadyVoted = set([])
    mostPopularCandidates = []
    with open(file) as f:
        while True:
            lastLine = f.readline()
            while not lastLine:
                lastLine = f.readline()

            voter, candidate = line #TODO

            if voter in alreadyVoted:
                continue #This vote is not valid
            alreadyVoted.add(voter)

            if candidate not in candidateVotes:
                candidateVotes[candidate] = 0
            candidateVotes[candidate] += 1

            #TODO

if __name__ == "__main__":
    pass
