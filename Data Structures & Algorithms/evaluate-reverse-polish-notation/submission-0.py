class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []

        for ch in tokens:

            if ch == '+':
                b = st.pop()
                a = st.pop()
                st.append(a + b)

            elif ch == '-':
                b = st.pop()
                a = st.pop()
                st.append(a - b)

            elif ch == '*':
                b = st.pop()
                a = st.pop()
                st.append(a * b)

            elif ch == '/':
                b = st.pop()
                a = st.pop()
                st.append(int(a / b))

            else:
                st.append(int(ch))

        return st[-1]