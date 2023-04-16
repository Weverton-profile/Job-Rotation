dic = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "outros": 19849.53}
total = 0
for chave in dic.keys():
  total = total + dic[chave]
for chave in dic.keys():
  print(f'{chave} representa {round(dic[chave] * 100 / total, 2)}%')