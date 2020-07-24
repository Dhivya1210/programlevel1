def chat():
    l=[]
    #until quit chat continuous
    while True:
        #chat of the person1
        print("person 1")
        s1=input()
        #check user input 
        if(s1=="quit"):
            l.append("quit")
            break
        l.append(s1)
        #chat of the person2
        print("person 2")
        s2=input()
        if s2=="quit":
            l.append("quit")
            break
        l.append(s2)
    return l
def rep_word(l,k):
    d={}
    c=0
    for i in range(k):
        for j in range(i+1,k):
            if l[i]==l[j]:
                c+=1
    print("Number of repeated words in chat:"+str(c))
def len_conv(l):
    c=0
    for i in l:
        c+=1
    return c
def rep_char(m):
    l={}
    c=0
    s=""
    for i in m:
        s+=i
    for i in s:
        if i in l:
            l[i]+=1
        else:
            l[i]=1
    print("Number of characters repeated in the chat")
    for i,j in l.items():
        if l[i]>0:
            print(i,l[i])
#Get the user interest        
print("enter chat or quit")
n=input()
word_collections=[]
if n=="chat":
    print("chat here")
    #collect the words from the chat
    word_collections=chat()
    #check whether the chat is ended
    if word_collections[len(word_collections)-1]=="quit":
        if len(word_collections)>0:
            #get the length of the chat
            k=len_conv(word_collections)
            word_collections.pop()
            #call repeted word fuction to find repeated words in the chat
            rep_word(word_collections,k-1)
            #call repeted character fuction to find repeated character in the chat
            rep_char(word_collections)
            #displaying the length of the chat
            print("length of the chat:"+str(len_conv(word_collections)))
else:
    print("No chats here")
    
