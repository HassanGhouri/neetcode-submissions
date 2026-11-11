class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends or target in deadends:
            return -1

        lock = "0000"
        seen = set()
        seen.add(target)
        queue = [(target, 0)]

        head = 0
        while head < len(queue):
            og_combination, turns = queue[head]
            head += 1
            if og_combination == lock:
                return turns
            
            else:
                seen.add(og_combination)
                for i in range(4):
                    combination = list(og_combination)
                    combination[i] = str((int(combination[i]) + 1) % 10)
                    combination = "".join(combination)

                    if combination not in seen:
                        if combination not in deadends:
                            queue.append((combination, turns + 1))
                            seen.add(combination)

                    combination = list(combination)
                    combination[i] = str((int(combination[i]) - 2) % 10)
                    combination = "".join(combination)

                    if combination not in seen:
                        if combination not in deadends:
                            queue.append((combination, turns + 1))
                            seen.add(combination)

        return -1



