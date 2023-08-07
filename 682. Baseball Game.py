class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for ops in operations:
            if ops == "C":
                record.pop()
            elif ops == "D":
                double = record[-1] * 2
                record.append(double)
            elif ops == "+": 
                if record[-2]:
                    new_score = record[-1] + record[-2]
                record.append(new_score)
            else:
                record.append(int(ops))
# record = [5, -2, -4, 9, 5, 14]
        return sum(record)
