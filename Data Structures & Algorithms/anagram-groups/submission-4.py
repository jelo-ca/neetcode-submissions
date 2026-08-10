class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        seen = dict()
        for word in strs:
            key = "".join(sorted(word))

            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]

        for key in seen:
            ans.append(seen[key])
        return ans
