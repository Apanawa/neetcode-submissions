class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        ans = []
        for s in range(len(strs)):

            aux = strs[s] 
            temp = "".join(sorted(strs[s]))
            print(temp)
            if temp in my_dict:
                my_dict[temp].append(aux)
            else:
                my_dict[temp] = [aux]
        print(my_dict)
        for val in my_dict.values():
            ans.append(val)
        return ans