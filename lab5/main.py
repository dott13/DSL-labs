from toChomsky import ChomskyConverter
from grammar import Grammar


class Main:

    @staticmethod
    def run():
        my_grammar = Grammar(VN={'S', 'A', 'B', 'C', 'E'},
                             VT={'a', 'b'},
                             P={
                                 'S': {'bAC', 'B'},
                                 'A': {'a', 'aS', 'bCaCb'},
                                 'B': {'AC', 'bS', 'aAa'},
                                 'C': {'', 'AB'},
                                 'E': {'BA'}
                             })
        print(my_grammar)

        convertor = ChomskyConverter(my_grammar.VN, my_grammar.VT, my_grammar.P)
        upd_grammar = convertor.convert()

        print(upd_grammar)


if __name__ == '__main__':
    Main.run()
    