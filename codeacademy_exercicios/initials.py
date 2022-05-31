# This program takes 2 given initials and display them as ASCII art
# By first is created a dictionary with the alphabet, and thus we can 
# print your initials :D

# alphabet here:
alpha = {}
alpha['A'] = "  A     A A   A   A  AAAAA  A   A  A   A  A   A  "
alpha['B'] = "BBBB   B   B  B   B  BBBB   B   B  B   B  BBBB   "
alpha['C'] = " CCC   C   C  C      C      C      C   C   CCC   "
alpha['D'] = "DDDD   D   D  D   D  D   D  D   D  D   D  DDDD   "
alpha['E'] = "EEEEE  E      E      EEE    E      E      EEEEE  "
alpha['F'] = "FFFFF  F      F      FFF    F      F      F      "
alpha['G'] = " GGG   G   G  G      GGGGG  G   G  G   G   GGG   "
alpha['H'] = "H   H  H   H  H   H  HHHHH  H   H  H   H  H   H  "
alpha['I'] = "IIIII    I      I      I      I      I    IIIII  "
alpha['J'] = "JJJJJ    J      J      J    J J    J J     JJ    "
alpha['K'] = "K   K  K  K   K K    KK     K K    K  K   K   K  "
alpha['L'] = "L      L      L      L      L      L      LLLLL  "
alpha['M'] = "M   M  MM MM  MM MM  M M M  M   M  M   M  M   M  "
alpha['N'] = "N   N  NN  N  N N N  N  NN  N   N  N   N  N   N  "
alpha['O'] = " OOO   O   O  O   O  O   O  O   O  O   O   OOO   "
alpha['P'] = "PPPP   P   P  P   P  PPPP   P      P      P      "
alpha['Q'] = " QQQ   Q   Q  Q   Q  Q   Q  Q   Q  Q  Q    QQ Q  "
alpha['R'] = "RRRR   R   R  R   R  RRRR   R R    R  R   R   R  "
alpha['S'] = " SSS   S   S  S       SSS       S  S   S   SSS   "
alpha['T'] = "TTTTT    T      T      T      T      T      T    "
alpha['U'] = "U   U  U   U  U   U  U   U  U   U  U   U   UUU   "
alpha['V'] = "V   V  V   V  V   V  V   V  V   V   V V     V    "
alpha['W'] = "W   W  W   W  W   W  W W W  WW WW  WW WW  W   W  "
alpha['X'] = "X   X  X   X   X X     X     X X   X   X  X   X  "
alpha['Y'] = "Y   Y   Y Y     Y      Y      Y      Y      Y    "
alpha['Z'] = "ZZZZZ      Z     Z     Z     Z     Z      ZZZZZ  "

# taking your inits:
name_surname = "Patrícia Barbosa"
name = (name_surname.split(" "))[0]
surname = (name_surname.split(" "))[1]
init1 = name[0]
init2 = surname[0]

# and now printing:
for i in range(7):
  print (alpha[init1][i*7:i*7+7], alpha[init2][i*7:i*7+7])







