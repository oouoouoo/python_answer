def check(lineData):
    ans = []
    for line in lineData:
        stack = []
        ans_list = list(line)
        output = [' '] * len(line)
        for i, c in enumerate(line):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    output[i] = '?'
        while stack:
            op = stack.pop()
            output[op] = 'x'
        ans.append(''.join(ans_list))
        ans.append(''.join(output))
    return ans


input_lines = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

output_lines = check(input_lines)

for line in output_lines:
    print(line)
