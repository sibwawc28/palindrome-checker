def palcheck(word):

    reverse="".join(reversed(word))
    ans=1

    for i in range(len(word)):
        if(reverse[i]!=word[i]):
            ans=0
            break

    return ans
    

user=input("Enter a word to check if it's palindrome or not ")
ans=palcheck(user)


if(ans==1):
    print(f"yes, {user} is a palindrome ")
else:
    print(f"{user} is not a palindrome")


    