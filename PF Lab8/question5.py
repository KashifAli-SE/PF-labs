# a part 
message="The secret of this message is that it is secret."
print(message)

# b part 
length= len(message)
print('length of message= ', len(message))

# c part 
count= message.count('secret')
print("secret word count= ", count)

# d part 
censored = message.replace('secret', 'xxxxxx') 
print('censored = ',censored)
