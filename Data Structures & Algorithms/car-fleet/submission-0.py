class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        cars = sorted(zip(position, speed), reverse=True)

        for position, speed in cars:
            arrival_t = (target - position) / speed
            
            if len(stack) == 0:
                stack.append(arrival_t)
            
            else:
                if arrival_t > stack[-1]:
                    stack.append(arrival_t)
        
        return len(stack)



              

               
        