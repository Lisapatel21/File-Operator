# ==========================================
# PERSONAL JOURNAL MANAGER
# File Operator Project
# ==========================================

import os
from datetime import datetime


class JournalManager:
    def __init__(self):
        self.file_name = "journal.txt"

    # ------------------------------------------
    # Add a new journal entry
    # ------------------------------------------
    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry: ")

            if entry.strip() == "":
                print("Journal entry cannot be empty.")
                return

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            journal_entry = f"[{current_time}]\n{entry}\n\n"

            # x mode creates a new file
            # if the file does not already exist.
            if not os.path.exists(self.file_name):
                try:
                    with open(self.file_name, "x") as file:
                        file.write(journal_entry)
                except FileExistsError:
                    with open(self.file_name, "a") as file:
                        file.write(journal_entry)
            else:
                # a mode adds the new entry at the end
                with open(self.file_name, "a") as file:
                    file.write(journal_entry)

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied. Cannot write to the file.")
        except OSError as error:
            print("Error while saving the entry:", error)

    # ------------------------------------------
    # View all journal entries
    # ------------------------------------------
    def view_entries(self):
        try:
            with open(self.file_name, "r") as file:
                content = file.read()

            if content.strip() == "":
                print("\nNo journal entries found.")
                return

            print("\nYour Journal Entries:")
            print("----------------------------------------")
            print(content)

        except FileNotFoundError:
            print("\nError: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")

    # ------------------------------------------
    # Search for a journal entry
    # ------------------------------------------
    def search_entry(self):
        try:
            keyword = input("\nEnter a keyword or date to search: ")

            if keyword.strip() == "":
                print("Search value cannot be empty.")
                return

            with open(self.file_name, "r") as file:
                content = file.read()

            # Split the file into individual entries
            entries = content.strip().split("\n\n")

            found = False

            print("\nMatching Entries:")
            print("----------------------------------------")

            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry)
                    print()
                    found = True

            if not found:
                print("No entries were found for the keyword:", keyword)

        except FileNotFoundError:
            print("\nError: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")

    # ------------------------------------------
    # Delete all journal entries
    # ------------------------------------------
    def delete_entries(self):
        try:
            if not os.path.exists(self.file_name):
                print("\nNo journal entries to delete.")
                return

            choice = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            )

            if choice.lower() == "yes":
                os.remove(self.file_name)
                print("\nAll journal entries have been deleted.")

            elif choice.lower() == "no":
                print("\nDelete operation cancelled.")

            else:
                print("\nPlease enter yes or no.")

        except PermissionError:
            print("Error: Permission denied. Cannot delete the file.")

        except OSError as error:
            print("Error while deleting the file:", error)

    # ------------------------------------------
    # Explain file modes
    # ------------------------------------------
    def show_file_modes(self):
        print("\nFile Handling Modes:")
        print("----------------------------------------")
        print("r  - Read the contents of a file")
        print("w  - Write to a file and replace old contents")
        print("a  - Add new content at the end of a file")
        print("x  - Create a new file")
        print("----------------------------------------")


# ==========================================
# Main Program
# ==========================================

journal = JournalManager()

print("\n========================================")
print("     WELCOME TO PERSONAL JOURNAL")
print("            MANAGER")
print("========================================")

while True:

    print("\nPlease select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. File Handling Modes")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        journal.add_entry()

    elif choice == "2":
        journal.view_entries()

    elif choice == "3":
        journal.search_entry()

    elif choice == "4":
        journal.delete_entries()

    elif choice == "5":
        journal.show_file_modes()

    elif choice == "6":
        print("\nThank you for using Personal Journal Manager.")
        print("Goodbye!")
        break

    else:
        print("\nInvalid option.")
        print("Please select a valid option from the menu.")