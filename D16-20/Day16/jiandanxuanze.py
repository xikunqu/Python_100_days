#简单排序算法，依次对比
def selection_sort(arr):
    for i in range(len(arr)-1):
        print(i)
        minIndex=i
        for j in range(i+1,len(arr)):
            print("j",j)
            if arr[j]<=arr[minIndex]:
                minIndex=j
        if i==minIndex:
            pass
        else:
            arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr


if __name__ == '__main__':
    testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
    print(selection_sort(testlist))