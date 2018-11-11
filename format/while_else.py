count = 0
while count <=5:
    count += 1
    if count == 3:
        break
        # pass
    print('loop', count)
else:
    print('循环正常执行')
# 如果while循环被break打断，后面的else不会走，如果没有被break打断，else里面的语句会正常执行
