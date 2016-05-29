Goals for this lab


This lab provides practice in writing functions on Python lists to:

-   count the number of items in a list that meet certain criteria
-   return a new list with some change applied to each item in the list

This exercise also provides practice with writing functions that use Boolean logic, and with using functions you've already defined to make new functions.

What you'll be doing: a heuristic for syllable counting


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


Step 0: Getting Started
-----------------------

Step 0a: Create Private Repo
-----------------------


First, create a private repo called CS20-S16-lab08.

* Specify that you want a README.md
* Specify that you want a .gitignore for Python
* Don't worry about a LICENSE---its ok to have, or not have one.
 
You can create this either on github.com or github.ucsb.edu

Step 0b: Add Collaborators
-----------------------


Then, add `pconrad` and `sarahmzhong` as collaborators.

Step 0c: Clone repo 
-----------------------


Then, clone the repo on either CSIL or your own machine (either way is fine.)

Step 0d: Add remote for starter code and pull 
-----------------------

Now we want to add some starter code from https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab08. We'll use the HTTPS remote URL, but you could use the SSH remote URL if you like. Remember, these are the same URLs we use to clone a repo.

To add a remote for the starter code, do this:

`git remote add starter https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab08.git`

Then, do a `git pull starter master`

You may have a merge conflict in the README.md file.

To deal with those:

* edit the `README.md`  with a text editor (Notepad, TextEdit, nano, etc.) to remove the `<<<< HEAD`, `=====` and `>>>>> hex-number here ` lines, and fix up the file to something reasonable.
* `git add README.md`  
* `git commit -m 'fix merge conflict on README.md'`
* `git push origin master`

You should then have a clean repo with a `code` subdirectory containing:

* lab08Funcs.py (stubs)
* lab08DocTests.py (the file that controls testing)
* tests subdirectory, containing your tests

For this lab, there are so many tests that to make them easier to read, we wrote them in "docstring" style, and separated them out into separate files, one for each function. We then have a file call `allTests.txt` that contains all of the tests for all eight functions. You'll see the code at the end of the `lab08DocTests.py` code that loads the tests from a file.

This is a different style of testing.  We'll discuss this in lecture.

Step 1: Read through the comments, code and test cases in the ENTIRE file first
-------------------------------------------------------------------------------

Before you jump in, just read through the ENTIRE file from start to finish. Read all of the comments, all of the code, and all of the test cases. Having a sense of the entire file will really help you as you proceed.

You can read through the code by loading it into IDLE, or just look at it on the web here:


https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab08/tree/master/code

Look through the tests too. It may help to look at the tests along with each function from `lab08Funcs.py`.

Find the stubs. These are the places where you'll be adding code in Step 2. But don't just jump in and start coding yet.

As you find things you don't understand, ask the instrcutor about them, or make a note to do so during class or office hours.

Only after you've read the entire file through—and you understand the big picture—proceed to step 2.

Step 2: Starting from the top, replace the stubs with correct function bodies
-----------------------------------------------------------------------------

Your task is to replace the stubs (things like return -1 and return "stub") with correct function bodies, so that all the tests pass.

It is best to start at the top, and do the functions in the order they appear in the file.

What NOT do to...

There can be a temptation to make your test cases pass by changing them to the answer your function returns, even if it is wrong, but that is not permitted—in fact, it is a kind of academic dishonesty.

So, don't change any of the test cases, unless you have permission of the Instructor. (This should only be done if we determine that there is an error in the test cases provided.) When all the test cases pass...

When your file contains all the functions and test cases from the original lab08 starting point, and all the tests pass, you are finished!

Step 3: Submitting via submit
-----------------------------

You'll see two submission opportunities here.  

* [lab08](https://submit.cs.ucsb.edu/form/project/493/submission) runs ALL the tests all at once.
* [lab08a](https://submit.cs.ucsb.edu/form/project/494/submission) runs the tests in individual groups, so you can get partial credit

You may submit to either or both.  If you get a clean green output on either, you are done!


