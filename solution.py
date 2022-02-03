
# ### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    #1
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "mtls"
    #2
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    #3
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    #4
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    #5
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    #6
    elif question == "What is the MD5 hashing value to the following message: \'NYU Computer Networking\' - " \
                     "Use MD5 hash generator and use the answer in your code":
        answer = "42b76fe51778764973077a5a94056724"
    #7
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    #8
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - " \
                     "The answer should be a numeric number":
        answer = 5
    #9
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - " \
                     "The answer should be a numeric number":
        answer = 4
    return(answer)
# Complete all the questions.

if __name__ == "__main__":
    #use this space to debug and verify that the program works
    #1
    debug_question = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    print(welcome_assignment_answers(debug_question))
    #2
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    #3
    debug_question = "Is it possible to decrypt a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    #4
    debug_question = "Is it possible to decode a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    #5
    debug_question = "Is a hashed message supposed to be un-hashed? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    #6
    debug_question = "What is the MD5 hashing value to the following message: \'NYU Computer Networking\' - " \
                     "Use MD5 hash generator and use the answer in your code"
    print(welcome_assignment_answers(debug_question))
    #7
    debug_question = "Is MD5 a secured hashing algorithm? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    #8
    debug_question = "What layer from the TCP/IP model the protocol DHCP belongs to? - " \
                     "The answer should be a numeric number"
    print(welcome_assignment_answers(debug_question))
   # 9
    debug_question = "What layer of the TCP/IP model the protocol TCP belongs to? - " \
                 "The answer should be a numeric number"
    print(welcome_assignment_answers(debug_question))