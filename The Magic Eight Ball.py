import random


# get the information out of the file, and send it to main for use
def get_info():
    # get fortunes for the eight ball from the file
    infile = open('magic_eight_ball.txt', 'r')

    # create a list to read the data into
    meb = []

    # create a temporary variable to hold each line
    temp = " "

    # prime meb with the first fortune
    temp = infile.readline()
    # don't forget to strip the \n from the end of the line!
    temp = temp.rstrip('\n')

    # use a for loop to get the rest of the file
    while temp != "":
        # append temp to meb
        meb.append(temp)
        # read the next line
        temp = infile.readline()
        # rstrip the \n
        temp = temp.rstrip('\n')

    # don't forget to close the file
    infile.close()
    # return meb to main so we can use it
    return meb


def main():
    # start by creating a list to hold the data from get_info()
    eight_ball = get_info()

    # get a random number for the eight ball's answer
    temp = random.randint(1, 100)
    # print(temp)

    # holding variable for the question
    holding = input("Ask the Magic Eight Ball a question: ")

    # print the magic eight ball's response
    # remember that the list starts at 0, so positive answers will be between 0 and 5, unsure answers between 6 and 10
    # and negative answers between 11 and 15
    x = temp % 15
    # print(x)
    print('The Magic Eight Ball says:', eight_ball[x])

main()
