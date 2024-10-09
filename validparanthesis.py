def is_valid(s:str) -> bool:
    brack_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []  
    for char in s:
        if char in brack_map:
            if char in brack_map:
                top_elem = stack.pop() if stack else "#"
                if brack_map[char] != top_elem:
                    return False
            else:
                stack.append(char)
    return not stack
    
s = "()"

print(is_valid(s))