from collections import Counter

while True:
    seq_uinput= input("Please enter your sequence of numbers: ")

    if not seq_uinput.strip():
        print("Please provide an input. Retrying...\n")
        continue
    try:
        nums = sorted(list(map(int, seq_uinput.replace(',',' ').split())))
        break
    except Exception:
        print("Invalid input. Retrying...\n")
print(f"Your sequence: {nums}")
print("Do you want to find: ")
print("1. Mean")
print("2. Median")
print("3. Mode")
while True:
    try:
        uinput=(int(input("Please enter the number corresponding to the option: ")))
        if uinput in [1,2,3]:
            break
        else:
            print("Please input one of the given options. Retrying...\n")
    except Exception:
        print("Please input one of the given options. Retrying...\n")

if (uinput==1):
    sumnum=sum(nums)
    avg = sumnum/len(nums)
    if avg % 1 == 0:
        print(f"The mean(average) of your sequence is: {int(avg)}")
    else:
        print(f"The mean(average) of your sequence is: {avg}")
        print(f"The mean(average) up to 2 decimal places is: {avg:.2f}")
    print("Goodbye!")
if(uinput==2):
    sorted_nums= sorted(nums)
    listofnums=len(nums)
    if (listofnums%2==0):
        pos1 = sorted_nums[(listofnums//2)-1]
        pos2 = sorted_nums[(listofnums//2)]
        median = (pos1+pos2)/2
        if median % 1 == 0:
            print(f"The median of your sequence is: {int(median)}")
        else:
            print(f"The median of your sequence is: {median}")
            print(f"The median up to 2 decimal places is: {median:.2f}")
        print("Goodbye!")
    else:
        median  = sorted_nums[listofnums//2]
        print(f"The median of your sequence is: {int(median)}")
        print("Goodbye!")
if(uinput==3):
    sorted_nums= sorted(nums)
    counts = Counter(nums)
    max_count = counts.most_common(1)[0][1]
    modes = [num for num, count in counts.items() if count == max_count]
    indices = [index+1 for index, value in enumerate(nums) if value in modes]
    print(f"The mode(s) of your sequence: {modes}, present at {indices} position(s).")
    print(f"Each/This mode was observed {max_count} time(s).")
    print("Goodbye!")
