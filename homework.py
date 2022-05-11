# 1 Istifadəçinin girdiyi mətnlərdəki hərfləri əlifba sırsanıda özünən sonra gələn hərflə dəyişdirən program yazın.

# text = input('Bir cumle yazin: ')
# 
# final = []
# 
# letters = ''

# for i in text:
#     if ord(i) >= 65:
#         new_i = chr(ord(i)+1)
#         letters += new_i
#     else:
#         final.append(letters)
#         letters = ''
# else:
#     final.append(letters)        
# 
# print(final)   

# 2 İstifadəçinin girdiyi mətn daxilindəki hərflərin ingilis əlifbasındakı sırasına qarşılıq gələn ədədlərlə dəyişdirilmiş şəkildə göstərin.


# text = input('Bir cumle yazin: ')
# 
# final = []
# 
# for i in text:
#     if ord(i) >= 65:
#         new_i = ord(i)
#         final.append(new_i)
# 
# print(*final)      
#   

################################## SON TAPSIRIQLAR ###################################

# 1 Istifadəçinin girdiyi stringi binary şəklində göstərin.

# from ntpath import join
# 
# 
# things = input('Bir cumle yazin: ')
# 
# con_binary = ' '.join(format(ord(c), 'b')for c in things)  
# 
# print(con_binary)

# 2 Istifadəçi input olaraq color: rgb(127, 255, 12) şəklində CSS rəngi girəcək. Siz istifadəçinin girdiyi rəngi 16-lıq sistemdəki qarşılığına çevirin.

# def rgb_to_hex(r, g, b):
#   return ('{:X}{:X}{:X}').format(r, g, b)
# 
# print(rgb_to_hex(127, 255, 12))
