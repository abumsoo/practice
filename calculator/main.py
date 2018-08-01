#!/usr/bin/env python

import re

# Simple equation parser

# TODO
# [ ] Handle just the addition
# [ ] 
# [ ] Deal with order of operations
# [ ] Handle conversion from input string to numbers

# Need to separate the input into individual units
# i.e. summand, operator, summand, maybe another operator, etc.
# Go through the input string and determine what's a number and what's
# an operator.

# ex. 2+9-3
# [2,9,3]
# [+,-]

def lexer(cmd):
    cmd = cmd.replace(" ", "")
    # Need to also think about order of operations
    operands = re.split("[-\+\*/]", cmd)
    # operators = re.split("[^\^][0-9]+", cmd)
    operators = []
    for char in cmd:
        if "-" in char or "+" in char or "*" in char or "/" in char:
            operators.append(char)
    return operands, operators

def parser(operands):
    ops_len = len(operands)
    for i in range(ops_len):
        if operands[i].isdigit():
            operands[i] = int(operands[i])
    return operands

def execute(operands, operators):
    if len(operands) == 1:
        return operands[0]
    if not operators:
        return operands[0]
    if operators[0] == "+":
        tot = operands[0] + operands[1]
        del operands[0]
        operands[0] = tot
        del operators[0]
        return execute(operands, operators)
    elif operators[0] == "-":
        tot = operands[0] - operands[1]
        del operands[0]
        operands[0] = tot
        del operators[0]
        return execute(operands, operators)
    elif operators[0] == "*":
        pass
    elif operators[0] == "/":
        pass
       

def main():
    cmd = input("> ")
    while cmd != "quit":
        operands, operators = lexer(cmd)
        operands = parser(operands)
        total = execute(operands, operators)
        print(total)
        cmd = input("> ")

if __name__ == "__main__":
        main()
