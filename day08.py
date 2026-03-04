#counting frequency of elements in an array
def count_freq(arr):
    freq={}
    for item in arr:
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
    return freq
def print_freq(freq):
    for key, value in freq.items():
        print(f"{key}: {value}")
def main():
    arr=[1,2,2,3,3,3,4,4,4,4]
    freq=count_freq(arr)
    print_freq(freq)
main()