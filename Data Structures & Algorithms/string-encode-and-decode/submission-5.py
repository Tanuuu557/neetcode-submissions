from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = [] 
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start_str = j + 1
            end_str = start_str + length
            decoded.append(s[start_str:end_str])

            i = end_str
        return decoded


