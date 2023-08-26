from config import Config as cf
from book_run import PhoneBook

book = None

while True:
    inpt = input(cf.ask_mode_file)
    if inpt == '1':
        book = PhoneBook()
        book.read_from_dump()
        break
    elif inpt == '2':
        book = PhoneBook()
        book.init_empty_frame()
        break
    print(cf.mode_err)

user_inpt = ''
while user_inpt != 'ext':
    print(cf.menu)
    user_inpt = input()
    if user_inpt == 'list':
        ln = input(cf.ask_count_rows)
        if ln == '0':
            book.list_book()
        else:
            book.list_book(int(ln))

    elif user_inpt == 'fio':
        fio = input(cf.ask_fio)
        book.search_by_fio(fio)


    elif user_inpt == 'ins':

        book.insert_data()

    elif user_inpt == 'edit':
        nm = input(cf.ask_row)
        book.edit_line(int(nm))
    elif user_inpt == 'st':
        book.print_statistic()
    elif user_inpt == 'sv':
        book.dump_to_pickle()
    elif user_inpt == 'dl':
        book.delete_line()

while True:
    inpt = input(cf.ask_to_save)
    if inpt == 'yes':
        book.dump_to_pickle()
        print(cf.goodbye)
        break
    elif inpt == 'no':
        print(cf.goodbye)

        break
