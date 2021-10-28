from pprint import pprint
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
def people_output(documents):
    number = input('number:')
    for x in documents:
        if number == x['number']:
            pprint(x['name'])
            return x['name']
    for x in documents:
        if number != x['number']:
            pprint('Введен некорректный номер документа!')
            return

def shelf_output(directories):
    number = input('Введите номер документа:')
    for x in directories.values():
        if number in x:
            print(list(directories.keys())[list(directories.values()).index(x)])
            return
    for x in documents:
        if number not in x:
            print('Введен некорректный номер документа!')
            return

def list_output(documents):
    list_1 = []
    for x in documents:
        list_1.append(' '.join(list(x.values())))
    print(list_1)

def add_document(documents, directories):
    number = input('number:')
    type_1 = input('type:')
    name = input('name:')
    shelf = input('shelf:')
    documents.append({'type': type_1, 'number': number, 'name': name})
    for x in directories:
        if shelf == x:
            directories[x].append(number)
            pprint(documents)
            pprint(directories)
            return (documents[-1]['number'], documents[-1]['type'], documents[-1]['name'], directories[shelf][-1])
    for x in directories:
        if shelf != x:
            return pprint('Введен некорректный номер полки!')

def delete_document(documents, directories):
    number = input('number:')
    for x in documents:
        if number == x['number']:
            documents.remove(x)
            flag = True
            for key, value in dict(directories).items():
                if number in value:
                    value.remove(number)
    pprint(documents)
    return flag

def move_document(directories):
    number = input('Введите номер документа:')
    documents_list = []
    for x in directories.values():
        documents_list.extend(x)
    if number not in documents_list:
        print('Введен несуществующий номер документа!')
        return
    shelf = input('Введите номер полки:')
    shelfs_list = []
    for x in directories:
        shelfs_list.append(x)
    if shelf not in shelfs_list:
        print('Введен несуществующий номер полки!')
        return
    for key, value in dict(directories).items():
        if number in value:
            value.remove(number)
            directories[shelf].append(number)
            print(directories)
            return

def add_shelf(directories):
    new_shelf = input('Введите номер новой полки:')
    for x in directories:
        if new_shelf == x:
            print('Полка с данным номером уже существует!')
            return
    for x in directories:
        if new_shelf != x:
            directories[new_shelf] = []
            print(directories)
            return

# while True:
#     command = input('Введите команду:')
#     if command == 'p':
#         people_output(documents)
#     elif command == 's':
#         shelf_output(directories)
#     elif command == 'l':
#         list_output(documents)
#     elif command == 'a':
#         add_document(documents, directories)
#     elif command == 'd':
#         delete_document(documents, directories)
#     elif command == 'm':
#         move_document(directories)
#     elif command == 'as':
#         add_shelf(directories)
#     elif command == 'exit':
#         print('Работа окончена, до свидания!')
#         break
#     else:
#         print('Введена некорректная команда!')

