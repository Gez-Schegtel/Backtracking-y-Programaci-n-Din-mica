from enum import Enum
from typing import List, Tuple, Dict

class BOOLEAN_OPERATOR(Enum):
    AND = 1
    OR = 2
    XOR = 3

def operator_to_str(op: BOOLEAN_OPERATOR) -> str:
    if op == BOOLEAN_OPERATOR.AND:
        return 'AND'
    elif op == BOOLEAN_OPERATOR.OR:
        return 'OR'
    elif op == BOOLEAN_OPERATOR.XOR:
        return 'XOR'

def evaluate(op1: bool, operator: BOOLEAN_OPERATOR, op2: bool) -> bool:
    if operator == BOOLEAN_OPERATOR.AND:
        return op1 and op2
    elif operator == BOOLEAN_OPERATOR.OR:
        return op1 or op2
    elif operator == BOOLEAN_OPERATOR.XOR:
        return op1 != op2

def count_ways(operands: List[bool], operators: List[BOOLEAN_OPERATOR], start: int, end: int, is_true: bool, memo: Dict[Tuple[int, int, bool], Tuple[int, List[str]]]) -> Tuple[int, List[str]]:
    if start == end:
        expr = "True" if operands[start] else "False"
        if is_true:
            return (1, [expr]) if operands[start] else (0, [])
        else:
            return (1, [expr]) if not operands[start] else (0, [])

    if (start, end, is_true) in memo:
        return memo[(start, end, is_true)]

    ways = 0
    expressions = []

    for i in range(start, end):
        operator = operators[i]
        operator_str = operator_to_str(operator)

        left_true, left_true_exprs = count_ways(operands, operators, start, i, True, memo)
        left_false, left_false_exprs = count_ways(operands, operators, start, i, False, memo)
        right_true, right_true_exprs = count_ways(operands, operators, i + 1, end, True, memo)
        right_false, right_false_exprs = count_ways(operands, operators, i + 1, end, False, memo)

        if operator == BOOLEAN_OPERATOR.AND:
            if is_true:
                ways += left_true * right_true
                for l in left_true_exprs:
                    for r in right_true_exprs:
                        expressions.append(f"({l} AND {r})")
            else:
                ways += left_false * right_true + left_true * right_false + left_false * right_false
                for l in left_false_exprs:
                    for r in right_true_exprs:
                        expressions.append(f"({l} AND {r})")
                for l in left_true_exprs:
                    for r in right_false_exprs:
                        expressions.append(f"({l} AND {r})")
                for l in left_false_exprs:
                    for r in right_false_exprs:
                        expressions.append(f"({l} AND {r})")
        elif operator == BOOLEAN_OPERATOR.OR:
            if is_true:
                ways += left_true * right_true + left_true * right_false + left_false * right_true
                for l in left_true_exprs:
                    for r in right_true_exprs:
                        expressions.append(f"({l} OR {r})")
                for l in left_true_exprs:
                    for r in right_false_exprs:
                        expressions.append(f"({l} OR {r})")
                for l in left_false_exprs:
                    for r in right_true_exprs:
                        expressions.append(f"({l} OR {r})")
            else:
                ways += left_false * right_false
                for l in left_false_exprs:
                    for r in right_false_exprs:
                        expressions.append(f"({l} OR {r})")
        elif operator == BOOLEAN_OPERATOR.XOR:
            if is_true:
                ways += left_true * right_false + left_false * right_true
                for l in left_true_exprs:
                    for r in right_false_exprs:
                        expressions.append(f"({l} XOR {r})")
                for l in left_false_exprs:
                    for r in right_true_exprs:
                        expressions.append(f"({l} XOR {r})")
            else:
                ways += left_true * right_true + left_false * right_false
                for l in left_true_exprs:
                    for r in right_true_exprs:
                        expressions.append(f"({l} XOR {r})")
                for l in left_false_exprs:
                    for r in right_false_exprs:
                        expressions.append(f"({l} XOR {r})")

    memo[(start, end, is_true)] = (ways, expressions)
    return ways, expressions

def main():
    # Los valores de "operands" y "operators" deben ser modificados conjuntamente para que el programa admita más o menos valores de verdad.
    operands = [True, False, True, False, False]
    operators = [BOOLEAN_OPERATOR.AND, BOOLEAN_OPERATOR.OR, BOOLEAN_OPERATOR.XOR, BOOLEAN_OPERATOR.XOR]

    memo = {}
    count, parenthesizations = count_ways(operands, operators, 0, len(operands) - 1, True, memo)
    print(f"\nNumber of ways to parenthesize to get True: {count}\n")
    for expr in parenthesizations:
        print(expr)

if __name__ == "__main__":
    main()
