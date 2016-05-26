# lab08Tests.py    Syllable Counting, for CS8, Spring 2014
# P. Conrad, UCSB CS Department.
# tests come from files in a subdirectory called "tests"

if __name__ == "__main__":
   import doctest
   from lab08Funcs import *

   # @@@ UNCOMMENT THESE ONE AT A TIME TO GET THE TESTS TO PASS.
   # @@@ WHEN YOU ARE FINISHED, LEAVE ONLY THE "allTests.txt" line uncommented.

   doctest.testfile("tests/noConsecDupsTests.txt", verbose=True)
   #doctest.testfile("tests/isVowelTests.txt", verbose=True)
   #doctest.testfile("tests/countVowelsTests.txt", verbose=True)
   #doctest.testfile("tests/allVowelsATests.txt", verbose=True)
   #doctest.testfile("tests/syllableHelperTests.txt", verbose=True)
   #doctest.testfile("tests/removeSilentETests.txt", verbose=True)
   #doctest.testfile("tests/removeEdWhenNotASyllableTests.txt", verbose=True)
   #doctest.testfile("tests/countSyllablesTests.txt", verbose=True)
   #doctest.testfile("tests/allTests.txt", verbose=True)
