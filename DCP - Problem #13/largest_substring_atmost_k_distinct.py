def largestSubstring_atmost_k_distinct(s,k):
    if not s:
        return 0
    
    d={}
    start=0
    ans=0
    for end in range(len(s)):
        
        d[s[end]]=d.get(s[end],0)+1
        
        while len(d)>k:
            
            d[s[start]]-=1
            
            if d[s[start]]==0:
                del d[s[start]]
            
            start+=1
        
        if len(d)==k or end==len(s)-1:
            ans=max(ans,end-start+1)
    return ans

print(largestSubstring_atmost_k_distinct("abcdef",1))
