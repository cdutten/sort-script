import argparse

class InsertionSort:

    def __init__(self):
        self.get_arguments()
        self.sort()
        print(self.li)


    def get_arguments(self):
        parser = argparse.ArgumentParser(description='Sort with Insertion sort algorithm')
        parser.add_argument('integers', metavar='integers', nargs='+', type=int,
                            help='Integers to sort')
        parser.add_argument('-v','--verbose',
                           help='Whether or not print all comparison\'s')
        args = parser.parse_args()
        self.li = args.integers
        self.verbose = args.verbose

    def sort(self):
        '''
        Sorts the list with insertion algorithm
        :return:
        '''
        j = 0
        for i in range(1, len(self.li)):
            self.print_state(i, j)

            if self.li[i] >= self.li[i - 1]:
               # TODO: this form of print state is too much coupled
               #    Needs a better approach
                if (self.verbose):
                    print('i don\'t do anything')
                    continue
            while (i != 0) and self.li[i] < self.li[i - 1]:
                self.switch_with_before_element(self.li, i)
                i = i - 1
                j = j + 1
                self.print_state(i, j)

    def switch_with_before_element(self, li, i):
        keep = li[i - 1]
        li[i - 1] = li[i]
        li[i] = keep
        return li

    def print_state(self, i, j):
        '''
        prints the state of the sorting

        TODO: this form of print state is too much coupled
            Needs a better approach

        :param i:
        :param j:
        :return:
        '''
        if (self.verbose):
            print('elements: ' + str(self.li))
            print('element: ' + str(self.li[i]))
            print('index: ' + str(i))
            print('moves: ' + str(j))
            print('')

InsertionSort()
