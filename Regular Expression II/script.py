class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        # s_i = 0
        # p_i = 0
        # star_p_i = None
        # star_s_i = None
        
        # res = True
        
        # while s_i < len(s) or p_i < len(p):
        #     if p_i+1 < len(p) and p[p_i+1] == "*":
        #         p_i+=2
        #         star_p_i, star_s_i = p_i, s_i
        #     else:
        #         if s_i < len(s) and p_i < len(p) and (s[s_i] == p[p_i] or p[p_i] == "."):
        #             s_i+=1
        #             p_i+=1
        #         else:
        #             if star_p_i != None \
        #                 and star_s_i < len(s) and (p[star_p_i-2] == "." or s[star_s_i] == p[star_p_i-2]):
        #                 star_s_i+=1
        #                 s_i, p_i = star_s_i, star_p_i
        #             else:
        #                 res = False
        #                 break
                
        # return res
        # s_i = 0
        # p_i = 0
        # st = []
        
        # res = True
        
        # while s_i < len(s) or p_i < len(p):
        #     if p_i+1 < len(p) and p[p_i+1] == "*":
        #         p_i+=2
        #         st.append([p_i, s_i])
        #     else:
        #         if s_i < len(s) and p_i < len(p) and (s[s_i] == p[p_i] or p[p_i] == "."):
        #             s_i+=1
        #             p_i+=1
        #         else:
        #             if st \
        #                 and st[-1][0] < len(s) and (p[st[-1][0]-2] == "." or s[st[-1][1]] == p[st[-1][0]-2]):
        #                 st[-1][1]+=1
        #                 p_i = s[-1]
        #             else:
        #                 res = False
        #                 break
                
        # return res
        s_i = 0
        p_i = 0
        st = []

        res = True
        
        while s_i < len(s) or p_i < len(p):
            if p_i+1 < len(p) and p[p_i+1] == "*":
                p_i+=2
                st.append([p_i, s_i])
            else:
                if s_i < len(s) and p_i < len(p) and (s[s_i] == p[p_i] or p[p_i] == "."):
                    s_i+=1
                    p_i+=1
                else:
                    while st and (st[-1][1] >= len(s) or p[st[-1][0]-2] != "." and s[st[-1][1]] != p[st[-1][0]-2]):
                        # print st[-1][1], s[st[-1][1]], p[st[-1][0]-2]
                        # print "Popped"
                        st.pop()
                    
                    if st and st[-1][1] < len(s) and (p[st[-1][0]-2] == "." or s[st[-1][1]] == p[st[-1][0]-2]):
                        st[-1][1]+=1
                        p_i, s_i = st[-1]
                    else:
                        res = False
                        break
                
        return res
            

if __name__=="__main__":
    print Solution().isMatch("abbbc", "ab*c")