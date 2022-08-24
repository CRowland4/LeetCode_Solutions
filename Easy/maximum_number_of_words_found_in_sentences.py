"""A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.



Example 1:

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation:
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
Example 2:

Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3
Explanation: It is possible that multiple sentences contain the same number of words.
In this example, the second and third sentences (underlined) have the same number of words.


Constraints:

1 <= sentences.length <= 100
1 <= sentences[i].length <= 100
sentences[i] consists only of lowercase English letters and ' ' only.
sentences[i] does not have leading or trailing spaces.
All the words in sentences[i] are separated by a single space."""
import performance_test

"""First solution is a fun one-liner. We use list comprehension to create a list of the word counts of all of the
sentences, and return the max of that list."""


def use_split_method(sentences):
    return max([len(sentence.split()) for sentence in sentences])


"""This is the exact same idea with list comprehension, but instead of using sentence.split(), which creates a new 
list for every element in sentences, we only count the number of spaces of each element in sentences, since the space 
is the default delimiter of .split() anyway, and return that max count + 1 (there is always one more thing than the 
number of things used to divide them). We'll use the performance test to see which one's faster."""


def count_the_spaces(sentences):
    return max([sentence.count(' ') for sentence in sentences]) + 1


"""Based on the performance test, the second method of just counting the spaces is faster every time."""

# After looking
"""Didn't find any significantly bette solutions."""
