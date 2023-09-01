# def strcounter(string): # Сложность O(n ** 2)
#     for symbol in string:
#         counter = 0
#         for sub_stmbol in string:
#             if symbol == sub_stmbol:
#                 counter+=1
#         print(symbol, counter)
#
# strcounter('abcdcdab')


# def strcounter(string): # Сложность O(n * m)
#     for symbol in set(string):
#         counter = 0
#         for sub_stmbol in string:
#             if symbol == sub_stmbol:
#                 counter+=1
#         print(symbol, counter)
#
# strcounter('abcdcdab')


# def strcounter(string):
#     syms_counter = {}
#     for symbol in string:
#         syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
#     print(syms_counter)

# strcounter('aaabbccdee')
