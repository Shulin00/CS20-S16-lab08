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

    # return -1 stub

    if (type(theList) not in [str,list]):
        return theList    
    elif (len(theList)==0):
       return theList    # not [], because then it doesn't work on tuples or strings
    elif len(theList)==1:
       return theList
    # Now we know that the list has a least two elements.

    # @@@ FINISH THIS FUNCTION THEN REMOVE THE return "stub" comment
    # @@@ and these @@@ comments 
    # @@@ HINT: Initialize a variable called
    # @@@ result with list[0:1].   That will be a string or list
    # @@@ depending on which one was passed in.
    # @@@
    # @@@ Then use a for loop that uses an index i that goes from 1 to
    # @@@ the end of the list.  Accumulate the result by appending only
    # @@@ elements that don't match the last value added to  result (i.e.
    # @@@ the "last" element in the result list accumulated so far.
    # @@@ When you select out element i to accumulate, 
    # @@@     instead of:  result = result + [theList[i]], use
    # @@@     use:         result = result + theList[i:i+1]
    # @@@  Reason: that works for both lists and strings.

    return "stub"

def isVowel(letter):
   """
   isVowel checks whether a given letter is a vowel.  For purposes of this
   function, treat y as always a vowel, w never as a vowel.
   letter should be a string containing a single letter
   return "error" if the value of the parameter is not a single letter string,
   return True, if the letter is a vowel, otherwise False
   """
              
   return "stub"  # this is a stub for testing the test cases

   # @@@ REPLACE THE STUB WITH A CORRECT FUNCTION SO THAT THE TEST CASES PASS
   # @@@ HINTS:
   # @@@  You need to check both the type and the length 


def countVowels(word):
   """
   parameter words should be a string
   produces:   an integer
   return boolean value False if the input is not a string,
   otherwise return number of vowels in word
   Note: the empty string is legal, and should produce the answer 0
   """
              
   return "stub"  # a stub for testing the tests

   # @@@ REPLACE THE STUB WITH A CORRECT FUNCTION SO THAT THE TEST CASES PASS
   # @@@ HINTS:
   # @@@  (1) You can use the accumulator pattern to count the vowels
   # @@@  (2) This is example of counting items in a list, so look back
   # @@@      at functions like countOdd() or countEven() for hints.




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
    return -1 # stub value

   # @@@ FINISH THIS FUNCTION!
   # @@@ This can be done with a for loop that accumulates the result



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
    return -1 # stub value




# @@@ FINISH THIS FUNCTION!
# @@@ Hint: consider reusing the functions you've already written.
# @@@ This can be a one line function if you see the trick.
# @@@ You may need to pass the result of one function into another function.

# removeSilentE is an example of a "heuristic".  A heuristic is an approach to
#   a problem that is not perfect, not guaranteed to succeed, but is still
#   useful.
# We want to remove silent e from the ends of words in English.  We'll use this approach:
#    (1) Let "howMany" be the number of 'a's in the word after it has been
#        processed by the syllableHelper function.
#    (2) If the original word now ends in 'e', and howMany is >= 2,
#        then, return the original word without the 'e' in place.
#    (3) Otherwise, return the word unchanged.
# These rules work for many words, such as "rule", "take", and "defenestrate"--we'll remove the silent
#  'e' from these words.  The rule also works for 'be', 'we', 'the', where the final e should
#  NOT be removed.  Some words where this rule fails are  "castle", "chronicle", "muscle"
#  The idea of a heuristic is that exceptions like these
#  are rare, so the rule is still pretty good.    Problem solving is often a matter of
#  starting with a "pretty good heuristic", and sucessively refining it.  (Can you think of an
#  improved rule that handles the words "castle", "chronicle" and "muscle" as well?)
                
            
def removeSilentE(word):
    """
    parameter "word" should be a string---otherwise return boolean value False
    returns word, but with silent e removed, according to the heuristic rules
      in the comment above.
    Note: the empty string is legal, and should produce the answer '' (empty string)
    """
                 
    return -1  # a stub for testing the tests


  
# removeEdWhenNotASyllable is another example of a "heuristic".
# In order to be able to count syllables, we want to 
# remove ed from the ends of words in English such as "owned","phoned",
#   "rehearsed" and "goverened" when it doesn't add an extra syllable.
# We don't want to remove it from
#   words like "wed","cred", "bed", "tried"
# We'll use a similar approach to removeSilentE:
#    (1) Let "howMany" be the number of 'a's in the word after it has been
#        processed by the syllableHelper function.
#    (2) If the original word now ends in 'ed', and howMany is >= 2,
#        then, return the original word without the 'ed' in place.
#    (3) Otherwise, return the word unchanged.
# Words where this heuristic fails are "busted", "instituted", "embed"
# Can you think of an improvement to the heurisitc that handles those cases?

            
def removeEdWhenNotASyllable(word):
    """
    word should be a string---otherwise return boolean value False
    if word is a string, return the same string, but with silent ed removed,
       according to the heuristic rules in the comment above.
    Note: the empty string is legal, and should produce the answer '' (empty string)
    """
                 
    return -1  # a stub for testing the tests


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
     """
     word should be a string---otherwise, return False
     as long a word is a string, return an integer,
       our best guess at the number of syllables in word, using the heuristic above
     Note: the empty string is legal, and should produce the answer 0
     """
                 
     return "stub"  # a stub for testing the tests


