[README (6).md](https://github.com/user-attachments/files/30935695/README.6.md)
# 📓 Personal Journal Manager

A simple, menu-driven Python application that allows users to create and manage personal journal entries using **file handling**.

## 📌 Project Information

**Project Name:** Personal Journal Manager

**Programming Language:** Python

**Main Concept:** File Handling in Python

The project uses:

* `os` module
* `datetime` module
* Classes and objects
* File handling
* Exception handling
* Menu-driven programming
* String operations
* `if-elif-else`
* `while` loop

The program stores journal entries in a file named `journal.txt`.

## ✨ Features

1. **Add a New Entry**
   * Allows the user to enter a journal entry.
   * Prevents empty entries.
   * Automatically adds the current date and time.
   * Saves the entry into `journal.txt`.

2. **View All Entries**
   * Reads and displays all saved journal entries.
   * Shows a suitable message if no entries exist.

3. **Search for an Entry**
   * Allows the user to search using a keyword or date.
   * The search is case-insensitive.
   * Displays matching journal entries.
   * Shows a message if no matching entry is found.

4. **Delete All Entries**
   * Allows the user to delete all journal entries.
   * Asks for confirmation before deleting.
   * Uses `os.remove()` to remove the journal file.

5. **File Handling Modes**
   * `r` – Read
   * `w` – Write
   * `a` – Append
   * `x` – Create

6. **Exit**
   * Safely exits the program with a thank-you message.

## 🧠 Technical Concepts Used

This project demonstrates the following Python concepts:

* Importing modules
* Class and object
* Constructor `__init__()`
* Functions/methods
* `input()` and `print()`
* File opening and closing
* `with open()`
* File modes
* Reading and writing files
* Appending data
* Creating files
* Deleting files
* `os.path.exists()`
* `os.remove()`
* `try-except`
* `FileNotFoundError`
* `PermissionError`
* `OSError`
* `datetime.now()`
* String methods such as `.strip()`, `.lower()`, and `.split()`
* `while` loop
* Conditional statements

## ⚙️ How the Program Works

1. Program starts.
2. A `JournalManager` object is created.
3. A welcome message is displayed.
4. A menu is displayed repeatedly.
5. The user selects an option.
6. The corresponding method is executed.
7. Journal data is stored in or read from `journal.txt`.
8. The program continues until the user selects Exit.

## 📋 Menu

```text
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. File Handling Modes
6. Exit
```

## 📁 File Structure

```text
Personal-Journal-Manager/
│
├── PR.6 FILE OPERATOR.py
├── journal.txt
└── README.md
```

`journal.txt` is created and used automatically by the program to store all journal entries. It gets created the first time you add a new entry.

## ▶️ How to Run

1. Install Python.
2. Save the Python program.
3. Open the folder in VS Code or IDLE.
4. Open the terminal.
5. Run the program using:

```bash
python "PR.6 FILE OPERATOR.py"
```

Note: The exact command may depend on how you have named the Python file.

## 🖥️ Sample Program Output

Below is an actual run of the program, showing every menu option in action.

```text
==========================================
 WELCOME TO PERSONAL JOURNAL MANAGER
==========================================

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. File Handling Modes
6. Exit

Enter your choice: 1

Enter your journal entry: Today was a good day . I have learned raise keyword.

Entry added successfully!

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. File Handling Modes
6. Exit

Enter your choice: 2

Your Journal Entries:
----------------------------------------
[2026-08-11 17:47:35]
Today was a good day . I have learned raise keyword.

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. File Handling Modes
6. Exit

Enter your choice: 3

Enter a keyword or date to search: good

Matching Entries:
----------------------------------------
[2026-08-11 17:47:35]
Today was a good day . I have learned raise keyword.

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. File Handling Modes
6. Exit

Enter your choice: 4

Are you sure you want to delete all entries? (yes/no): yes

All journal entries have been deleted.

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. File Handling Modes
6. Exit

Enter your choice: 2

Error: The journal file does not exist.
Please add a new entry first.

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. File Handling Modes
6. Exit

Enter your choice: 5

File Handling Modes:
----------------------------------------
r  - Read the contents of a file
w  - Write to a file and replace old contents
a  - Add new content at the end of a file
x  - Create a new file
----------------------------------------

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. File Handling Modes
6. Exit

Enter your choice: 6

Thank you for using Personal Journal Manager.
Goodbye!
```

This run demonstrates all six menu options: adding an entry, viewing it, searching by keyword, deleting all entries, seeing the "file not found" message after deletion, and viewing the file handling modes before exiting.

## 🛡️ Exception Handling

The program handles common file-related errors such as:

* File not found
* Permission denied
* General operating system errors
* Empty input

Exception handling is useful in this project because it prevents the program from crashing unexpectedly. Instead of showing a confusing error message, the program shows a simple, easy-to-understand message and lets the user continue using the menu.

## 🎯 Learning Objectives

Through this project, a student can learn:

* Understanding file handling in Python
* Learning different file modes
* Storing data permanently in a text file
* Reading and searching file contents
* Handling errors using exceptions
* Using classes and methods
* Creating a menu-driven application

## ✅ Advantages

* Easy to use
* Simple menu-driven interface
* Automatically records date and time
* Data is stored in a file
* Search functionality is available
* Demonstrates important Python file-handling concepts

## ⚠️ Limitations

* Data is stored in a simple text file.
* There is no password protection.
* All entries are deleted together when the delete option is used.
* It is a console-based application.
* It does not have a graphical user interface.

## 🚀 Future Improvements

* Delete individual journal entries
* Edit existing entries
* Add password protection
* Add a GUI using Tkinter
* Store entries in a database
* Add categories or moods
* Export journal entries to PDF

## 📝 Conclusion

The Personal Journal Manager is a simple Python project created to demonstrate file handling and basic Python programming concepts through a practical real-life application. It shows how a text file can be used to permanently store, read, search, and delete data using core Python features like classes, loops, and exception handling.

## 📄 License

This project is open-source and free to use for learning purposes (MIT License).

## 👤 Author Section

**Created by:** Student
**Language:** Python
**Project Type:** Python Practical / College Project
**Year:** 2026

## 🙏 Acknowledgements

* Built using Python's built-in `os` and `datetime` modules — no external libraries required.
* Created as part of a college Python file-handling practical assignment.

## 📬 Feedback

Suggestions and improvements are always welcome. Since this is a practical/learning project, feel free to modify it further and add your own features as you keep learning Python.
