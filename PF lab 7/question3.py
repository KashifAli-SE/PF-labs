#Question a
word1='anachronistically'
word2="counterintuitive."
if(len(word1)-len(word2)==1):
    print("The number of characters in the word 'anachronistically' is 1 more")
else:
    print("The number of characters in the word 'anachronistically' is not 1 more")
#Question b
word1="misinterpretation"
word2="misrepresentation"
lis=[word1,word2]
lis.sort()
if (lis[0]==word1):
    print(f"The word {word1} appears earlier in the dictionary than the word {word2}")
else:
    print(f"The word {word1} does not appear earlier in the dictionary than the word")
# c part
if 'e' in "ﬂoccinaucinihilipiliﬁcation.":
    print('letter e appears in word "ﬂoccinaucinihilipiliﬁcation." ')
else:
    print('letter e does not appears in word "ﬂoccinaucinihilipiliﬁcation."')    
# d part
word= "counterrevolution"
word1= "counter"
word2= "resolution"
if len(word)==len(word1)+len(word2):
    print('YES')
else:
    print('NO')

