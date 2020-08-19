"""
Написать класс, который позволит сохранить список дел, отмечать сделанное и показывать то, что нужно сделать.
Хранить список дел в json файле
При запуске программы должна появится меню с вариантами действий: добавить в список, вывести весь список, вывести
список не сделанных дел, отметить как сделаное
"""
import json, datetime


class Item:
    def __init__(self, done, info, last_updated):
        self.done = done
        self.info = info
        self.last_updated = last_updated

    # необходим для записи аргументов
    def as_dict(self):
        return {
            'done': self.done,
            'info': self.info,
            'last_updated': str(self.last_updated),
        }

    # def __str__(self):
    #     return self.info
    #
    # def __repr__(self):
    #     return self.info


class TodoList:
    def __init__(self, name, owner, dead_line):
        self.name = name
        self.owner = owner
        self.dead_line = dead_line
        # self.file_name = 'tasks.json'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(f'{self.name}__#{self.owner}.json', 'r') as file:
                data = json.load(file)
                tasks = []
                for item in data:
                    tasks.append(Item(item.get('done'), item.get('info'), item.get('last_updated')))
                return tasks
        except FileNotFoundError:
            return []

    @property
    def tasks_list(self):
        tasks = ''
        for index, item in enumerate(self.tasks):
            tasks += f'\n {index}\t {item.done}\t {item.info}\t {item.last_updated}'
        return tasks

    @property
    def not_ready_tasks(self):
        tasks = ''
        for item in self.tasks:
            if not item.done:
                tasks += f'\n {item.done}\t {item.info}\t {item.last_updated}'
        return tasks

    def done_task(self, index):
        self.tasks[index].done = True
        self.tasks[index].last_updated = ''

    def undone_task(self, index, last_updated):
        self.tasks[index].done = False
        self.tasks[index].last_updated = last_updated

    def add_task(self, task):
        self.tasks.append(task)

    def get_task_index(self, task):
        return self.tasks.index(task)

    def to_json(self):
        with open(f'{self.name}__#{self.owner}.json', 'w') as file:
            tasks = []
            for task in self.tasks:
                tasks.append(task.as_dict())
            json.dump(tasks, file, indent=4)


def init_todo_list(time=None):
    list_name = input('list_name: _')
    owner = input('owner: _')
    return TodoList(list_name, owner, time)


def main():
    def numeral_verify(text):
        input_num = input(text)
        while not input_num.isdigit():
            input_num = input('Not correct. Retry:\n>')
        return int(input_num)

    def commands():
        if input_func[0] == 'add' and input_func[1] is not None:
            done = input('The task is done or no:\n>')
            while done not in ['yes', 'no', 'y', 'n', 'Yes', 'No', 'Y', 'N']:
                done = input('Unknown command. Retry:\n>')
            if done in ['yes', 'y', 'Yes', 'Y']:
                done = True
            else:
                done = False
            info = ' '.join(input_func[1:])
            if done == False:
                dead_line = numeral_verify('Deadline (days):\n>')
            else:
                dead_line = None
            todo_list.add_task(Item(done, info, (f'{dead_line} day(-s)' if done == False else '')))
            return f'The {info} added'

        elif input_func[0].isdigit() and input_func[1] == 'ok':
            indexed = int(input_func[0])
            todo_list.done_task(indexed)
            return 'The task is Done'

        elif input_func[0].isdigit() and input_func[1] == 'not':
            indexed = int(input_func[0])
            dead_line = numeral_verify('Deadline (days):\n>')
            dead_line = f'{dead_line} day(-s)'
            todo_list.undone_task(indexed, dead_line)
            return 'The task is Undone'

        elif input_func[0] == 'tasklist':
            return todo_list.tasks_list

        elif input_func[0] == 'undonelist':
            return todo_list.not_ready_tasks

        elif input_func[0] == 'exit':
            todo_list.to_json()
            exit(0)

        else:
            return 'Unknown command'

    todo_list = init_todo_list()
    print('''╔══════════════════════════════════════╗
║  You can:                            ║
║    \033[1m\033[31madd\033[30m #task\033[0m - to add new task       ║
║    \033[1m#INDEXtask \033[32mok\033[0m - to done task      ║
║    \033[1m#INDEXtask \033[34mnot\033[0m - to undone task   ║
║    \033[1m\033[35mtasklist\033[0m - to show done-list      ║
║    \033[1m\033[35mundonelist\033[0m - to show undone-list  ║
║    \033[1mexit\033[0m - to exit                    ║
╚══════════════════════════════════════╝''')
    while True:
        input_func = input('>').split()
        try:
            print(commands())
        except IndexError:
            print('Unknown command')
            todo_list.to_json()
            continue
        todo_list.to_json()


if __name__ == '__main__':
    main()
    # TODO: есть задумка о том, как вычислять дату для каждой созданной задачи, но ее реализация очень большая можно
    #  записать при первой записи в json-файл дату его создания, а после исходить от вычисления дат задач и даты
    #  изменения файла
    #  datetime = datetime.datetime.now() - datetime.timedelta(days=14)
    #  print(datetime.strftime('%d-%m-%Y'))