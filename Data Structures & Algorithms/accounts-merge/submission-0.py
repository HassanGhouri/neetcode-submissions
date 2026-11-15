class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = {}
        self.parents = [i for i in range(len(accounts))]

        for i in range(len(accounts)):
            account = accounts[i]

            for email in account[1:]:
                if email not in emails:
                    emails[email] = i
                else:
                    root_a = self.find(i)
                    root_b = self.find(emails[email])

                    if root_a != root_b:
                        self.parents[root_a] = root_b

        for email in emails:
            emails[email] = self.find(emails[email])

        index_to_emails = {}

        for email in emails:
            if emails[email] in index_to_emails:
                index_to_emails[emails[email]].append(email)
            else:
                index_to_emails[emails[email]] = [email]

        ans = []

        for index in index_to_emails:
            ans.append(
                [accounts[index][0]] + sorted(index_to_emails[index])
            )

        return ans

    def find(self, x):
        while x != self.parents[x]:
            x = self.parents[x]
        return x
                