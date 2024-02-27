# users to create, update, and track their to-do lists
import sqlite3

conn = sqlite3.connect('todos_data.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS todos (
               id INTEGER PRIMARY KEY,
               title TEXT NOT NULL,
               text TEXT NOT NULL
    )
''')


def view_todo():
    cursor.execute("SELECT * FROM todos")
    for row in cursor.fetchall():
        print(row)

def create_todo(title, para):
    cursor.execute("INSERT INTO todos (title, text) VALUES (?, ?)", (title, para))
    conn.commit()

def update_todo(todo_id, new_title, new_para):
    cursor.execute("UPDATE todos SET title = ?, text= ? WHERE id =?",(new_title, new_para, todo_id))
    conn.commit()

def delete_todo(todo_id):
    cursor.execute("DELETE FROM todos where id = ?", (todo_id,))
    conn.commit()



def main():
    while True:
        print("\n TO-DO LIST | CODSOFT PROJECT ")
        print("1.View the to-do list ")
        print("2.Create a to-do list ")
        print("3. Update to-do ")
        print("4. Delete a to-do ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        

        if choice == '1':
            view_todo()
        elif choice == '2':
            title = input("Enter the to-do title: ")
            para = input("Enter the to-do text: ")
            create_todo(title, para)
        elif choice == '3':
            todo_id = input("Enter to-do ID to update: ")
            title = input("Enter the to-do title: ")
            para = input("Enter the to-do text: ")
            update_todo(todo_id, title, para)
        elif choice == '4':
            todo_id = input("Enter to-do ID to delete: ")
            delete_todo(todo_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ")

    conn.close()    

if __name__ ==  "__main__":
    main() 