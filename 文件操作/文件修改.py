with open('./修改前.txt', encoding="utf-8") as f, open('./修改后.bak', 'w', encoding="utf-8") as f1:
  for line in f:
    if '李小勇' in line:
      line = line.replace('李小勇','李雨hong')
      print(line)
    f1.write(line)

import os
os.remove('修改前.txt')
os.rename('修改后.bak', '修改前.txt')
