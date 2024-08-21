# Dice sum probability calculator
# Författare: Norton Haglind Hilbers
# Datum: 2024-08-21
from collections import Counter
all_sum = []
def main():
    user_input = input().split(" ")#user_input[0]=första tal user_input[1]=andra tal
    for i in range(int(user_input[0])+1):
        for x in range(int(user_input[1])+1):
            summ = x + i
            all_sum.append(summ)
    most_common = Counter(all_sum).most_common(5)
    print(most_common[0])

if __name__ == "__main__":
    main()
    