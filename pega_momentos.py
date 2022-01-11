def lines_that_equal(line_to_match,fp):
    return [line for line in fp if line == line_to_match

with open('freq.log', 'r') as fp:
    for line in lines_that_equal("Ground",fp):
        print(line)




#try:
#    file_read = open('freq.log','r')
#    text = str(Ground)
#    lines = file_read.readlines()
#    moments = []
#    idx = 0
#    for line in lines:
#        if text in line:
#            moments.insert(idx),line
#            idx += 1
#    file_read.close
#    if len(moments) == 0:
#        print("deu ruim")
#    else:
#        lineLen = len(moments)
#        for i in range(lineLen):
#            print(end=new_list[i])
#        print()
#except:
#    print("fudeu tudo")


