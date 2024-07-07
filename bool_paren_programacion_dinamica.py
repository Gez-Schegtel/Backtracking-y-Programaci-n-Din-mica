from enum import Enum
from typing import List, Tuple

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

def booleanTrueParenthesization(operands: List[bool], operators: List[BOOLEAN_OPERATOR]) -> Tuple[int, List[str], List[List[int]], List[List[int]]]:
    n = len(operands)
    T = [[0] * n for _ in range(n)]
    F = [[0] * n for _ in range(n)]
    T_expr = [[[] for _ in range(n)] for _ in range(n)]
    F_expr = [[[] for _ in range(n)] for _ in range(n)]

    # Initialize base cases (i.e. single-operand subexpressions)
    for i in range(n):
        if operands[i]:
            T[i][i] = 1
            T_expr[i][i] = [str(operands[i])]
        else:
            F[i][i] = 1
            F_expr[i][i] = [str(operands[i])]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            for k in range(i, j):  # Break points for subexpressions
                op = operators[k]
                if op == BOOLEAN_OPERATOR.AND:
                    T[i][j] += T[i][k] * T[k + 1][j]
                    F[i][j] += (T[i][k] + F[i][k]) * (T[k + 1][j] + F[k + 1][j]) - (T[i][k] * T[k + 1][j])

                    for left in T_expr[i][k]:
                        for right in T_expr[k + 1][j]:
                            T_expr[i][j].append(f'({left} AND {right})')
                    for left in T_expr[i][k] + F_expr[i][k]:
                        for right in T_expr[k + 1][j] + F_expr[k + 1][j]:
                            if not (left in T_expr[i][k] and right in T_expr[k + 1][j]):
                                F_expr[i][j].append(f'({left} AND {right})')

                elif op == BOOLEAN_OPERATOR.OR:
                    T[i][j] += (T[i][k] + F[i][k]) * (T[k + 1][j] + F[k + 1][j]) - (F[i][k] * F[k + 1][j])
                    F[i][j] += F[i][k] * F[k + 1][j]

                    for left in T_expr[i][k] + F_expr[i][k]:
                        for right in T_expr[k + 1][j] + F_expr[k + 1][j]:
                            T_expr[i][j].append(f'({left} OR {right})')
                    for left in F_expr[i][k]:
                        for right in F_expr[k + 1][j]:
                            F_expr[i][j].append(f'({left} OR {right})')

                elif op == BOOLEAN_OPERATOR.XOR:
                    T[i][j] += (T[i][k] * F[k + 1][j]) + (F[i][k] * T[k + 1][j])
                    F[i][j] += (T[i][k] * T[k + 1][j]) + (F[i][k] * F[k + 1][j])

                    for left in T_expr[i][k]:
                        for right in F_expr[k + 1][j]:
                            T_expr[i][j].append(f'({left} XOR {right})')
                    for left in F_expr[i][k]:
                        for right in T_expr[k + 1][j]:
                            T_expr[i][j].append(f'({left} XOR {right})')
                    for left in T_expr[i][k]:
                        for right in T_expr[k + 1][j]:
                            F_expr[i][j].append(f'({left} XOR {right})')
                    for left in F_expr[i][k]:
                        for right in F_expr[k + 1][j]:
                            F_expr[i][j].append(f'({left} XOR {right})')

    return T[0][n - 1], T_expr[0][n - 1], T, F

def print_matrix(matrix: List[List[int]], name: str):
    print(f"Matrix {name}:")
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

def main():
    # Los valores de "operands" y "operators" deben ser modificados conjuntamente para que el programa admita más o menos valores de verdad.
    operands = [True, False, True, False, False]
    operators = [BOOLEAN_OPERATOR.AND, BOOLEAN_OPERATOR.OR, BOOLEAN_OPERATOR.XOR, BOOLEAN_OPERATOR.XOR]

    # Convert the boolean list to strings for display
    operands_str = ['True' if op else 'False' for op in operands]
    operators_str = [operator_to_str(op) for op in operators]

    expression = " ".join(f"{operands_str[i]} {operators_str[i]}" for i in range(len(operators))) + f" {operands_str[-1]}"
    print(f"\nInput Expression: {expression} \n")

    count, expressions, T_matrix, F_matrix = booleanTrueParenthesization(operands, operators)
    print(f"Number of ways to parenthesize to get True: {count} \n")

    for expr in expressions:
        print(expr)

    print("\n")
    print_matrix(T_matrix, "T (True counts)")
    print_matrix(F_matrix, "F (False counts)")

if __name__ == "__main__":
    main()
