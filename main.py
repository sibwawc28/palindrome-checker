def palcheck(word):
    reverse="".join(reversed(word))
    #if you do word.reverse(), reversed 'word' will be stored in word
    if(word==reverse):
        return 1
    else:
        return 0
    
user=input("Enter a word to check if it's palindrome or not ")
ans=palcheck(user)

if(ans==1):
    print(f"yes, {user} is a palindrome ")
else:
    print(f"{user} is not a palindrome")