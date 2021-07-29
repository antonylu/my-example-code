#
# generate a 99 multiplication table for Kahoot questions
#
# The output looks like below, delimited by tab:
#   Question a1 a2 a3 a4 time correct_answer
#
#   example:
#   1 x 2 = ?	1	2	3	4	60	2
#
# Output: 99_table.txt
#
# Copy & Paste content of 99_table.txt to KahootQuizTemplate.xlsx
# Import to kahoot.com
#


import random

class Kahoot():
    def table9x9(self,m, shuffle=False):
        """
        two layers for loop,
            generate questions & answers
        """
        result = []
        for i in m:
            for j in range(1,10):
                if i == 1:
                    answers = [i+j, i*j, j*10+i, i*10+j]
                else:
                    answers = [i+j, i*j, i*(j+1), i*10+j]
                random.shuffle(answers)
                #print("{} x {} = ?\t{}\t{}\t{}\t{}\t60\t{}\t{}".format(i,j, *answers, answers.index(i*j)+1,'*' if len(set(answers)) != len(answers) else ""))
                result.append("{} x {} = ?\t{}\t{}\t{}\t{}\t60\t{}".format(i,j, *answers, answers.index(i*j)+1))

        if shuffle: random.shuffle(result)
        return result


if __name__ == "__main__":
    q = [1,2,3,4,5,6,7,8,9]
    q = [3,4,6]
    q = [4,8]
    q = [3,6]
    q = [7,9]
    #result = Kahoot().table9x9(q,shuffle=True)
    result = Kahoot().table9x9(q, True)

    f = open("99_table.txt", "w")
    for s in result:
        print(s)
        f.write(s)
        f.write('\n')

    f.close()
