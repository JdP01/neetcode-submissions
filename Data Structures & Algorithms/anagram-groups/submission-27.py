class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = defaultdict(list)

        for word in strs: 

            fp = [0]*26

            for i in word: 
                index = ord(i) - ord('a') #create an index for any letter
                fp[index] +=1 #increment index of any given letter by one where found

            output[tuple(fp)].append(word)

        #print(output)

        return list(output.values())
