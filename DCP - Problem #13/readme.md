### Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

### For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

` solution -:`

- Use Sliding window approach
1. maintain two pointer `start` and `end` and a `dictionary` to hold `k` distinct characters.
2. traverse the string from starting
3. increment the frequency of current character in dictionary i.e, `d[s[end]]+=1`
4. now inside while loop, check if len(d) i.e, distinct keys in dictionary is more than k is yes than do `d[s[start]]-=1`
5. if d[s[start]]=0, then delete that key from dictionary
6. now `start` will point to starting index of the desired substring and `end` will be on last index of substring.
7. update ans=max(ans,end-start+1)
8. at the end `ans` will hold desired result.
