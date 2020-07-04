'''
最小的k个数
'''
def getLeastNumbers(arr,k):
    arr.sort()
    return arr[:k]

'''
前K个高频元素
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def shift(i,k):#维护最小堆
            while True:
                t=2*i+1
                if t >= k :
                    return
                if t+1<k and hashlist[t][1]>hashlist[t+1][1]:
                    t=t+1
                if hashlist[t][1]<hashlist[i][1]:
                    hashlist[t],hashlist[i]=hashlist[i],hashlist[t]
                    i=t
                else:
                    return


        #建立哈希表
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        #print(hashmap)
        #将哈希表转为二维列表
        hashlist=[ [key,v] for key, v in hashmap.items() ]
        #print(hashlist)
        #建立K个元素的最小堆
        for i in range(k/2,-1,-1):
            shift(i,k)
        #剩余依次和堆顶比较
        for i in range(k,len(hashlist)):
            if hashlist[i][1]>=hashlist[0][1]:
                hashlist[0]=hashlist[i]
                shift(0,k)
        return [hashlist[i][0] for i in range(k)]

