# lab08Funcs.py    Syllable Counting, for CS8, Spring 2014
# P. Conrad, UCSB CS Department.

def noConsecDups(theList):
    """
    noConsecDups is a function that takes a list of items, or
    a string and
    returns a copy of that string list with no consecutive duplicates

    produces: the same list with any consecutive duplicates remove
    example: noConsecDups([2,3,3,3,4,4,5,6,6,2,2,1,5,3,3,2]
    produces: [2,3,4,5,6,2,1,5,3,2]

    if theList is not a string or list then return theList back unchanged
    """

    

    if (type(theList) not in [str,list]):
        return theList    
    elif (len(theList)==0):
       return theList    # not [], because then it doesn't work on tuples or strings
    elif len(theList)==1:
       return theList
    # Now we know that the list has a least two elements.


    else:
        result=theList[0:1]
        i = 1
        le=len(theList)

        for i in range(1,le-1):
            if theList[i-1]!=theList[i]:
                result=result+theList[i:i+1]
                    
            else:
                i = i+1
        if theList[le-2]!=theList[le-1]:
             result += theList[len(theList)-1:len(theList)]
    word=result
    return word
def isVowel(letter):
   """
   isVowel checks whether a given letter is a vowel.  For purposes of this
   function, treat y as always a vowel, w never as a vowel.
   letter should be a string containing a single letter
   return "error" if the value of the parameter is not a single letter string,
   return True, if the letter is a vowel, otherwise False
   """
              
   if type(letter)!=str or len(letter)!=1:
       return 'error'
   
   List=['a','e','i','o','u','y','A','E','I','O','U','Y']
   L=len(List)
   i=0
   if letter==List[i]:
       return True
   for i in range(0,L-1):
   
       if letter!=List[i]:
           i=i+1
           while letter==List[i]:
               
               return True
   else:
       return False

    


def countVowels(word):
   """
   parameter words should be a string
   produces:   an integer
   return boolean value False if the input is not a string,
   otherwise return number of vowels in word
   Note: the empty string is legal, and should produce the answer 0
   """
   if type(word)!=str:
       return False
   List=['a','e','i','o','u','y','A','E','I','O','U','Y']
   I=len(word)
   i=0
   num=''
   J=len(List)
   j=0
   for i in range(0,I):
       for j in range(0,J-1):
           if word[i]==List[j]:
               num+=word[i]
           else:
               j=j+1
   return len(num)
       





def allVowelsA(word):
    """
     allVowelsA is a function that changes all vowels to A.
       This function is a building block for a function that will count
       syllables by counting vowels.  For that purpose, all vowels are equivalent.
       But, we want to remove consecutive duplicate vowels.  Converting all
       vowels to the same vowel is a first step.
     word should be a string---otherwise return boolean value False
     when word is a string, return word with all vowels changed to the letter a
     examples:
       allVowelsA("by") produces "ba"
       allVowelsA("alien") produces "alaan"
       allVowelsA("boot") produces "baat"
       allVowelsA("fruition") produces "fraataan"
     Note: empty string is legal, and should return empty string
    """              
    if type(word)!=str:
       return False
    List=['a','e','i','o','u','y','A','E','I','O','U','Y']
    I=len(word)
    J=len(List)
    j=0
    i=0
    lista=list(word)
    
    
    for i in range(0,I):
        for j in range(0,J-1):
        
            if word[i]==List[j]:
                lista[i]='a'

                word=''.join(lista)
                
            else:
                j=j+1
        
    return word
 
    


def syllableHelper(word):
    """
    # syllableHelper is a function that is a building block for a function
    # that counts syllables.  It transforms a word by doing two things:
    #   (1) changing all vowels to the letter a
    #   (2) removing all consecutive duplicates
    # parameter word should be a string--if not return boolean value False
    # otherwise, return another string, with all vowels changed to the letter a,
    #     and consecutive duplicates removed
    # examples:
    #   syllableHelper("by") produces "ba"
    #   syllableHelper("alien") produces "alan"
    #   syllableHelper("boot") produces "bat"
    #   syllableHelper("fruition") produces "fratan"
    # Note: empty string is legal, and should return empty string
    """
    if type(word)!=str:
       return False
    if word=='':
        return ''
    List=['a','e','i','o','u','y','A','E','I','O','U','Y']
    I=len(word)
    J=len(List)
    j=0
    i=0
    lista=list(word)
    result=''
    
    for i in range(0,I):
        for j in range(0,J-1):
        
            if word[i]==List[j]:
                lista[i]='a'

                word=''.join(lista)
                
            else:
                j=j+1
    for k in range(0,I):
        if word[k-1]!=word[k]:
            result+=word[k]
    if word[0]=='a' and result[0]!='a':
        result=word[0]+result
                  
    return result
    




def removeSilentE(word):
    """
    parameter "word" should be a string---otherwise return boolean value False
    returns word, but with silent e removed, according to the heuristic rules
      in the comment above.
    Note: the empty string is legal, and should produce the answer '' (empty string)
    """
    if type(word)!=str:
        return False
    result=syllableHelper(word)
    I=len(result)
    num=''
    for i in range(0,I):
        if result[i]=='a':
            num+=result[i]
    howmany=len(num)
    J=len(word)
    if howmany>=2 and word[J-1]=='e':
        word=word[0:J-1]
    
                 
    return word


       
def removeEdWhenNotASyllable(word):
    """
    word should be a string---otherwise return boolean value False
    if word is a string, return the same string, but with silent ed removed,
       according to the heuristic rules in the comment above.
    Note: the empty string is legal, and should produce the answer '' (empty string)
    """
                 
    if type(word)!=str:
        return False
    result=syllableHelper(word)
    
    I=len(result)
    num=''
    for i in range(0,I):
        if result[i]=='a':
            num+=result[i]
    howmany=len(num)
    J=len(word)
    if howmany>=2 and word[J-2:J]=='ed':
        word=word[0:J-2]
    
                 
    return word
# countSyllables is a final example of a heuristic
# The theory is that the number of vowels in a word is a good indicator of the number of syllables
# in the word, if we (a) remove silent e, (b) remove final ed when it doesn't create a new syllable
# and (c) remove duplicate consecutive vowels in words like "boat", "patient", "pursuit" and "gaucho"
#
# This works for most words.   Convince yourself by trying it in your head on all the words in
# this sentence.  Then, try it on the first paragraph or two of the declaration of independence,
# found here: 
#
# This heuristic does fail for some words.  Here are some examples:
#   "alien", "likely", "States".
#
# Here's our approach:   Write the code to do this.
#    (1) removeSilentE, removeEdWhenNotASyllable, and then all consecutive duplicate letters
#    (2) count the remaining vowels in the word that you get as a result of step 1 and return that.
#                 
#  Note that this approach also removes duplicate consonants, but we don't care, since we are only
#  counting vowels.  (If we changed our heuristic, that might change also).                 
                
                 
def countSyllables(word):
    if type(word)!=str:
        return False
    eword=removeSilentE(word)
    edword=removeEdWhenNotASyllable(eword)
    single=syllableHelper(edword)
    
    List=['a','e','i','o','u','y','A','E','I','O','U','Y']
    I=len(single)
    J=len(List)
    j=0
    i=0
    num=''
    for i in range(0,I):
        for j in range(0,J-1):
            if single[i]==List[j]:
                num+=single[i]
            else:j=j+1
    
    return len(num)

                 
     


