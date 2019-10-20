'''Program to read from a file 'PlainText.txt' Created by Prateek Mahajan, Get a key and produce a cypher text using ceasor cypher
#0 Write the Plaintext in the plainText.txt file
#1 Input key which is an integer from 0 to 26
#2 The program converts letters to numbers from 0-25 seperately for capital and small and adds the key(and mods) to produce a new letter
#3 Output is stored into the cipherText File(will be created if not present)'''

try:
    file=open("plainText.txt","r")#Read text from the file plainText
    plainText=file.read()#Read contents of file in string format
    file.close
except:
    print("The file plainText.txt is created please type plain text in it")
    file=open("plainText.txt","w+")
    file.close()

print("The plain text is '"+plainText+'\'') # '\'' <- is used for printing '

key=int(input('Enter the key: '))

cipherText=""

for i in plainText: #ignore special characters and produce cipherText
    #for small letters
    if(ord(i)>=96 and ord(i)<=122):
        cipherText+=chr(((ord(i)-97)+key)%26+97)

        #here ord(i) gives ascii value of ith character
        #subtracting 97 will give numbers from 0-25
        #add key
        #take mod26 so that the number does not go out of range(0,26)
        #then add 97 to get the new ascii characters
        #This is done so that key can be negative also

    #for capital letters
    elif(ord(i)>=65 and ord(i)<=90):
        cipherText+=chr(((ord(i)-65)+key)%26+65)
print("The cipher text is "+cipherText)
file=open("cipherText.txt","w+")
file.write(cipherText)
file.close()
