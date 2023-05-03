# # # def find(char, string) :
# # #     """Return the first i such that string[i] == 'char'
# # #
# # #     Parameters:
# # #         char (string): The character being searched for.
# # #         string (string): The string being searched.
# # #
# # #     Return:
# # #         int: Index position of 'char' in 'string',
# # #              or -1 if 'char' does not occur in 'string'.
# # #     """
# # #     i = 0
# # #     length = len(string)
# # #     while i < length :
# # #         if char == string[i] :
# # #             return i
# # #         i += 1
# # #     return -1
# # #
# # #
# # # # Example of use
# # # print(find('m', 'spam'))
# # # print(find('s', 'spam'))
# # # print(find('x', 'spam'))
# from a2 import *
# from a2_support import *
# command = "describe Bash"
# card_dic = {
#     "Strike": Strike,
#     "Defend": Defend,
#     "Bash": Bash,
#     "Neutralize": Neutralize,
#     "Survivor": Survivor,
#     "Eruption": Eruption,
#     "Vigilance": Vigilance
# }
#
# command = command.split(" ")
# if command[1] in card_dic:
#     name = command[1]
#     print(name)
#     print(card_dic[name].get_description(Card))
#     # print(card_dic[name].get_description())
#     print(Strike.get_description(Card))



