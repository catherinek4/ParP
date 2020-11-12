import time
from concurrent.futures import ThreadPoolExecutor as tpe
from concurrent.futures import ProcessPoolExecutor as ppe
from multiprocessing import Process, Pool


# запис рядку до файлу
def write_files(file_path, string):
    with open(file_path, "w") as file:
        file.write(string)


# запис рядку у певну кількість файлів
def create_input_files(file_count):
    string = 'a' * 40000
    path = 'given_files\\'
    for k in range(file_count):
        write_files(path + str(k) + '.txt', string)


# читаємо з файлу
def get_file_content(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        return content


create_input_files(1000)


# створюємо нові файли в папці rewritten_files
def rewrite_files(n):
    for k in range(n):
        write_files('rewritten_files\\' + str(k) + '.txt',
                    get_file_content('given_files\\' + str(k) + '.txt'))


# запис до одного файлу
def write_one_file(k):
    write_files('rewritten_files\\' + str(k) + '.txt',
                get_file_content('given_files\\' + str(k) + '.txt'))


if __name__ == '__main__':

    start = time.time()
    with tpe(8) as executor:
        executor.map(write_one_file, range(1000))

    print('Час виконання ф-ції паралельно за допомогою потоків ThreadPoolExecutor: ',
          time.time() - start, 'c.')

    start = time.time()
    with ppe(8) as executor:
        executor.map(write_one_file, range(1000))

    print('Час виконання ф-ції паралельно за допомогою процесів ProcessPoolExecutor: ',
          time.time() - start, 'c.')

    start = time.time()
    rewrite_files(1000)
    print('Час виконання ф-ції послідовно: ', time.time() - start, 'c.')
