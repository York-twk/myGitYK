import LOG

def gcdOfStrings(self, str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """

    ''' 自己想的
    str_leg1 = len(str1)
    str_leg2 = len(str2)
    short_leg = str_leg1 if str_leg1 < str_leg2 else str_leg2

    if(str_leg1 > str_leg2):
        long_str = str1
        short_str = str2
    else:
        long_str = str2
        short_str = str1

    ans_str = ''
    for i in range(short_leg+1, 2, -1):
        s_head = short_str[0:i] #全部字串從起始位置開始縮短
        s_tail = short_str[-i:] #全部字串從末端位置開始縮短
        #print(s_head)
        #print(s_tail)
        if s_head in long_str:
            ans_str = s_head
        if s_tail in long_str:
            ans_str = s_tail

    # 若答案為空 直接回傳答案
    if(ans_str == ''):
        return ans_str
    
    # 若有答案 檢查是否為遞回字串
    for i in range(2, len(ans_str), 1):
        #從最短字串開始擴增至全字串
        for j in range(0, len(ans_str)-i+1, 1):
            #從起始開始以最短字串尋找
            s_search = ans_str[j:j+i]
            print(s_search)
    '''
    
    # 最大公因字串 正向相加應等於反向相加
    print(str1 + str2)
    print(str2 + str1)

    if str1 + str2 != str2 + str1:
        return ""
    
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x%y)
    return str1[:gcd(len(str1), len(str2))]


            
print("ans={}".format(gcdOfStrings("", "ABC", "ABCDEABCDE")))



