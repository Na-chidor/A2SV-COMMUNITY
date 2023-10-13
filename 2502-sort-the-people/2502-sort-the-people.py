class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mylist=list(zip(names,heights))
        sortedlist=sorted(mylist, key=lambda x:x[1], reverse=True)
        return [x[0] for x in sortedlist]
