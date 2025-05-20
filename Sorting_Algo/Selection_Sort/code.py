def selection_sort(ar):
    n=len(ar)
    for i in range(n-1):
        m_index = i
        for j in range(i+1,n):
            if ar[j] < ar[m_index]:
                m_index = j

        ar[i], ar[m_index] = ar[m_index], ar[i]

    return ar

def main():
    ar = list(map(int,input().split()))
    print(selection_sort(ar))

if __name__ == "__main__":
    main() 