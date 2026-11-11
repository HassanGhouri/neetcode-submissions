class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        relations = {}
        trusts_someone = set()

        for a,b in trust:
            trusts_someone.add(a)

            if b in relations:
                relations[b].append(a)
            
            else:
                relations[b] = [a]

        print(relations)
        
        for key in relations.keys():
            if len(relations[key]) == n - 1 and key not in trusts_someone:
                print(len(relations[key]), key)
                return key
        
        return -1