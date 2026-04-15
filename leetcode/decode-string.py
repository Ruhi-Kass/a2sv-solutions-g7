class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_string = ""
        
        for char in s:
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            elif char == '[':
                stack.append((cur_string, cur_num))
                cur_string = ""
                cur_num = 0
            elif char == ']':
                prev_string, num = stack.pop()
                cur_string = prev_string + cur_string * num
            else:
                cur_string += char
        
        return cur_string
