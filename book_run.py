import os
import re
import pandas as pd

from config import Config as cf


class PhoneBook:
    def __init__(self):
        self.df = None
        self.answer = pd.DataFrame(columns=['ФИО', 'личный телефон',
                                            'рабочий телефон',
                                            'Организация'])
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_colwidth', None)

    def init_empty_frame(self) -> None:
        """
        initilize dataframe with columns
        :return:
         """

        self.df = pd.DataFrame(
            columns=['ФИО', 'личный телефон',
                     'рабочий телефон',
                     'Организация']
        )

    def _ask_line(self) -> None:
        """Ask new line to dataframe
        :return:
       """
        ins = []
        ins.append(input(cf.ins_fio))
        ins.append(input(cf.ins_phone))
        ins.append(input(cf.ins_work_phone))
        ins.append(input(cf.ins_name_org))
        return ins

    def dump_to_pickle(self) -> None:
        """Save dataframe to pickle file.
        path into config
        :return:
        """

        self.df.to_pickle(cf.path_to_pickle)
        print(cf.save_successfull)

    def read_from_dump(self) -> None:
        """
        :return:
        """
        try:
            self.df = pd.read_pickle(cf.path_to_pickle)
            print(cf.successfull_load)
        except FileNotFoundError:
            self.init_empty_frame()
            print(cf.file_err)

    def list_book(self, length=None) -> None:
        """print actual dataframe
        :param length:
        :return:
        """
        if not length:
            length = len(self.df.index)
        print(self.df[:length])

    def print_statistic(self) -> None:
        """print how many rows and memory used
        :return:
        """
        try:
            print(cf.count_lines.format(len(self.df.index)))
            statistic = os.stat(cf.path_to_pickle)
            print(cf.memory_used.format(statistic.st_size / 1000000))
        except FileNotFoundError:
            print(cf.file_err)

    def search_by_fio(self, word) -> None:
        """Search all rows with have word in fio.
        Case ignored
        :param word:
        :return:
        """
        resposne = self.df.ФИО.str.contains(word,
                                            flags=re.IGNORECASE)
        count = 0
        for i, j in enumerate(resposne):
            if j:
                self.answer.loc[
                    len(self.answer.index)] = self.df.loc[i]
                count += 1
        if not count:
            print(cf.empty_serch)
        else:
            print(self.answer)
            print(cf.lenght_of_ans.format(count))

    def edit_line(self, num) -> None:
        """change line with index = num
        :param num:
        :return:
        """
        if num not in self.df.index:
            print(cf.index_err)
        ins = self._answer_line()
        self.df.loc[num] = ins

    def delete_line(self) -> None:
        """
        Ask index and delete row with equale index
        :return:
        """
        num = input(cf.ask_row)
        try:
            self.df.drop(labels=[int(num)], axis=0, inplace=True)
        except KeyError:
            print(cf.index_err)

    def insert_data(self) -> None:
        """just ask and insert new row to df
        :return:
        """

        ins = self._answer_line()
        self.df.loc[len(self.df.index)] = ins

    def main(self):
        """just for test
        :return:
        """
        self.read_from_dump()
        self.list_book()
        self.print_statistic()
        self.search_by_fio('Петр')

        print(self.df)


if __name__ == '__main__':
    book = PhoneBook()
    book.main()
