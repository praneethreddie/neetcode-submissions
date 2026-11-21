class Solution:
    def groupAnagrams(self, strs: List[str]):
     hashMap = {}
     for string in strs:
             sorteds  = "".join(sorted(string))
             if sorteds in hashMap:
                hashMap[sorteds].append(string)
             else:
                hashMap[sorteds]=[string]
     return list(hashMap.values())


    

        