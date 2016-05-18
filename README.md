Goals for this lab
==================

This lab provides practice in writing functions on Python lists to:

-   count the number of items in a list that meet certain criteria
-   return a new list with some change applied to each item in the list

This exercise also provides practice with writing functions that use Boolean logic, and with using functions you've already defined to make new functions.

What you'll be doing: a heuristic for syllable counting
=======================================================

Many word processing programs (e.g. Microsoft Word) have tools built in that determine the "reading level" of a piece of text. This is important for choosing reading assignments in K-12 education, and for things like determining whether a ballot initiative can be understood by the average California voter.

One factor in determining reading level is the average number of syllables per word. Because English is such a complex language, the only way to be 100% sure of the number of syllables in each word is to look up each word in a dictionary. However, even if we don't have a dictionary, we can still use a technique called a "heuristic" to get a good approximation of the number of syllables in a word.

A "heuristic" is an approach to solving a problem that might not produce an answer that is 100% correct, but it is an answer that is often "good enough". In Computer Science, when problems are difficult to solve with 100% certainty, we often take the approach of coming up with a heuristic, and then trying to improve on that heuristic.

For syllables, here's a first heuristic:

-   The number of vowels in a word is a pretty good indication of the number of syllables in that word.

Taking just the words in the preceding sentence, and treating y as a vowel (in addition to a,e,i,o, and u) we see that this heuristic works for every word in that sentence, except for the words "good" and "indication", which is a 90% success rate for that sentence.

However, we can improve the heuristic if we remove "consecutive vowels" before we count—that is, if we have two or more vowels, in a row, we remove the extra ones. Thus "good" becomes "god", and "indication" becomes "indicatin" before we count the vowels. If we do that, then our heuristic of counting vowels is 100% effective on that sentence!

However, this heuristic is still not perfect. For example, if fails on words such as "like", "there", and "looked".

Thus we introduce two more heuristics: ones to try to remove silent e from words such as "like", "there", "plane", etc., and the "ed" that doesn't contribute an extra syllable to words such as "looked", "jumped", "kissed", and "frowned".

The comments in the sample code discuss these heuristics. Be sure to read the comments carefully. They are there to help you make sense of the functions, and how the heuristics were developed.

As you'll see the addition of the silent e and -ed removal heuristics improve our syllable counting, but there are still words on which these techniques fail. (The word "techniques" is one example). If we had more time in the quarter, we'd extend this exercise to challenge you to come up with additional heuristics to make our syllable counting technique even more accurate.

As it is, there are still some challenges for you—applying the techniques of writing recursive functions for lists to this syllable counting problem. So, for this exercise, stick to the heuristics given.

If you want to experiment with additional heuristics, just for fun as a challenge to yourself, then finish the exercise as given first in a file called `lab08.py`. Then make a separate copy called `lab08_v2.py`, in which you experiment with your additional heuristics. You can then include both when you submit.

Note that working on additional heuristics for the spelling problem, while not required for this exercise, is an excellent way to study for the exam. Just like with swimming or playing the guitar, the more you do it, the better you will get at it. What we are learning in this class is not primarily a collect of facts, but a new way of thinking, and you need to practice that way of thinking to improve.

Step by Step Instructions
=========================

Step 0: Getting Started
-----------------------

First, create a *~/cs20/lab08* directory in the usual manner.

@@@@@@@@@@@@@@@@ links @@@@@@@@@@@@@@@@
You'll then need to copy all of the files from this web page into your directory:

-   <http://www.cs.ucsb.edu/~pconrad/cs8/14S/labs/lab08/code>

If you are working on CSIL, you can copy both into your current directory with the following Unix command. Note the . at the end of the command, which is separated from the filename by a space—the command will not work without this dot, which stands for "current directory".

`cp -r /cs/faculty/pconrad/public_html/cs8/14S/labs/lab08/code/* .`

If you are working on your own computer, you can use an secure copy client to copy these. On Mac and Linux it can be done at the command line:

`scp -r yourusername@csil.cs.ucsb.edu:/cs/faculty/pconrad/public_html/cs8/14S/labs/lab08/code/* .`

Or, on Windows, use a program such as WinSCP.

If all else fails, you can visit this web page and download them one at a time using "Save As", though that will be tedious.

-   <http://www.cs.ucsb.edu/~pconrad/cs8/14S/labs/lab08/code>
    -   Note that if you use the one file at a time method, you also will need a subdirectory called "tests", and it will need to have all of the files shown in tests in it. So this method is not recommended.

The starting point code is in the file lab08Funcs.py.

The file lab08Tests.py runs our tests, but this week the actual tests are in .txt files stored in the subdirectory called tests.

This week, there are so many tests that to make them easier to read, we wrote them in "docstring" style, and separated them out into separate files, one for each function. We then have a file call allTests.txt that contains all of the tests for all eight functions. You'll see the code at the end of the lab08Tests.py code that loads the tests from a file.

Step 1: Read through the comments, code and test cases in the ENTIRE file first
-------------------------------------------------------------------------------

Before you jump in, just read through the ENTIRE file from start to finish. Read all of the comments, all of the code, and all of the test cases. Having a sense of the entire file will really help you as you proceed.

You can read through the code by loading it into IDLE, or just look at it on the web here:

-   <http://www.cs.ucsb.edu/~pconrad/cs8/14S/labs/lab08/code/lab08Funcs.py>
-   <http://www.cs.ucsb.edu/~pconrad/cs8/14S/labs/lab08/code/lab08Tests.py>

Look through the tests too. It may help to look at the tests along with each function from lab08Funcs.py

-   <http://www.cs.ucsb.edu/~pconrad/cs8/14S/labs/lab08/code/tests>

Find the stubs. These are the places where you'll be adding code in Step 2. But don't just jump in and start coding yet.

As you find things you don't understand, ask the TA or the instructor, or make a note to do so during class or office hours.

Only after you've read the entire file through—and you understand the big picture—proceed to step 2.

Step 2: Starting from the top, replace the stubs with correct function bodies
-----------------------------------------------------------------------------

Your task is to replace the stubs (things like return -1 and return "stub") with correct function bodies, so that all the tests pass.

It is best to start at the top, and do the functions in the order they appear in the file.

What NOT do to...

There can be a temptation to make your test cases pass by changing them to the answer your function returns, even if it is wrong, but that is not permitted—in fact, it is a kind of academic dishonesty.

So, don't change any of the test cases, unless you have permission of the TA/Instructor. (This should only be done if we determine that there is an error in the test cases provided.) When all the test cases pass...

When your file contains all the functions and test cases from the original lab08StartingPoint.py, and all the tests pass, you are finished!

Step 3: Submitting via turnin
-----------------------------

Before submitting:

-   Change the header comment in lab08Funcs.py in the normal way (e.g. put in your name and your pair partner's name)
-   Remove all comment lines with @@@ in them (those are just instructions to help you complete the exercise)
-   Review the grading rubric below

Evaluation and Grading (300 points)
===================================

Grading Rubric:

| Function                   | Item                                                                          | Points   |
|----------------------------|-------------------------------------------------------------------------------|----------|
| all                        | Naming and submitting your file correctly, and submitting on time.            | (30 pts) |
| all                        | Fixing the header comment in the lab08Funcs.py file                           | (10 pts) |
| all                        | Code style overall(variable names, comments, etc, removing all the @@@ lines) | (20 pts) |
| noConsecDups()             | correctness of code                                                           | (30 pts) |
| isVowel()                  | correctness of code                                                           | (30 pts) |
| countVowels()              | correctness of code                                                           | (30 pts) |
| allVowelsA()               | correctness of code                                                           | (30 pts) |
| syllableHelper()           | correctness of code                                                           | (30 pts) |
| removeSilentE()            | correctness of code                                                           | (30 pts) |
| removeEdWhenNotASyllable() | correctness of code                                                           | (30 pts) |
| countSyllables()           | correctness of code                                                           | (30 pts) |


