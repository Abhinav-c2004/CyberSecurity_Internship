import os
import shutil
from datetime import datetime


class SmartFileOrganizer:

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = []

        self.categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
            "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
            "Audio": [".mp3", ".wav", ".aac", ".flac"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Programs": [".exe", ".msi", ".apk", ".py", ".c", ".cpp", ".java"]
        }

        self.stats = {
            "Images": 0,
            "Documents": 0,
            "Videos": 0,
            "Audio": 0,
            "Archives": 0,
            "Programs": 0,
            "Others": 0
        }

    # -------------------------------
    # Module 1
    # -------------------------------

    def validate_directory(self):
        try:
            if not os.path.exists(self.folder_path):
                print("Folder does not exist.")
                return False

            if not os.path.isdir(self.folder_path):
                print("Invalid directory.")
                return False

            return True

        except PermissionError:
            print("Permission denied.")
            return False

    # -------------------------------
    # Module 2
    # -------------------------------

    def scan_files(self):

        self.files.clear()

        try:
            for file in os.listdir(self.folder_path):

                full_path = os.path.join(self.folder_path, file)

                if os.path.isfile(full_path):
                    self.files.append(file)

            print("\nFound", len(self.files), "files\n")

            for file in self.files:
                name, ext = os.path.splitext(file)
                print(file, "->", ext)

        except Exception as e:
            print("Error:", e)

    # -------------------------------
    # Helper Function
    # -------------------------------

    def get_category(self, extension):

        extension = extension.lower()

        for category in self.categories:

            if extension in self.categories[category]:
                return category

        return "Others"

    # -------------------------------
    # Module 3
    # -------------------------------

    def organize_files(self):

        for key in self.stats:
            self.stats[key] = 0

        try:

            folders = list(self.categories.keys())
            folders.append("Others")

            for folder in folders:
                os.makedirs(os.path.join(self.folder_path, folder), exist_ok=True)

            for file in self.files:

                source = os.path.join(self.folder_path, file)

                if not os.path.exists(source):
                    continue

                name, ext = os.path.splitext(file)

                category = self.get_category(ext)

                destination = os.path.join(
                    self.folder_path,
                    category,
                    file
                )

                try:
                    shutil.move(source, destination)
                    self.stats[category] += 1

                except shutil.Error:
                    print(file, "already exists in", category)

            print("\nFiles organized successfully.")

        except PermissionError:
            print("Permission denied.")

        except Exception as e:
            print("Error:", e)

    # -------------------------------
    # Module 4
    # -------------------------------

    def show_statistics(self):

        total = 0

        print("\n==============================")
        print("      FILE STATISTICS")
        print("==============================")

        for category in self.stats:
            print("{:<15}{}".format(category, self.stats[category]))
            total += self.stats[category]

        print("------------------------------")
        print("{:<15}{}".format("Total Files", total))
        print("==============================")

    # -------------------------------
    # Module 5
    # -------------------------------

    def search_by_name(self):

        keyword = input("Enter file name: ").lower()

        found = False

        print()

        for root, dirs, files in os.walk(self.folder_path):

            for file in files:

                if keyword in file.lower():
                    print(os.path.join(root, file))
                    found = True

        if not found:
            print("No matching files found.")

    def search_by_extension(self):

        extension = input("Enter extension (Example: .pdf): ").lower()

        found = False

        print()

        for root, dirs, files in os.walk(self.folder_path):

            for file in files:

                if file.lower().endswith(extension):
                    print(os.path.join(root, file))
                    found = True

        if not found:
            print("No matching files found.")

    def search_files(self):

        print("\n1. Search by Name")
        print("2. Search by Extension")

        choice = input("Enter choice: ")

        if choice == "1":
            self.search_by_name()

        elif choice == "2":
            self.search_by_extension()

        else:
            print("Invalid choice.")

    # -------------------------------
    # Module 6
    # -------------------------------

    def find_duplicates(self):

        names = {}
        duplicates = []

        for root, dirs, files in os.walk(self.folder_path):

            for file in files:

                if file in names:
                    duplicates.append(file)
                else:
                    names[file] = 1

        if duplicates:

            print("\nDuplicate Files Found:\n")

            for file in duplicates:
                print(file)

        else:

            print("\nNo Duplicate Files Found.")

# -------------------------------
# Module 7
# -------------------------------

    def generate_report(self):

        report_path = os.path.join(self.folder_path, "file_report.txt")

        try:

            report = open(report_path, "w")

            report.write("SMART FILE ORGANIZER REPORT\n")
            report.write("=" * 40 + "\n\n")

            report.write("Date : ")
            report.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
            report.write("\n")

            report.write("Folder : ")
            report.write(self.folder_path)
            report.write("\n\n")

            total = sum(self.stats.values())

            report.write("Total Files : ")
            report.write(str(total))
            report.write("\n\n")

            report.write("Category-wise Count\n")
            report.write("-" * 25 + "\n")

            for category in self.stats:
                report.write("{:<15}{}\n".format(category, self.stats[category]))

            report.write("\n")

            report.write("Duplicate Files\n")
            report.write("-" * 25 + "\n")

            names = {}
            duplicate_found = False

            for root, dirs, files in os.walk(self.folder_path):

                for file in files:

                    if file == "file_report.txt":
                        continue

                    if file in names:
                        report.write(file + "\n")
                        duplicate_found = True
                    else:
                        names[file] = 1

            if not duplicate_found:
                report.write("No Duplicate Files Found\n")

            report.write("\n")

            report.write("Folder Structure\n")
            report.write("-" * 25 + "\n")

            for folder in os.listdir(self.folder_path):

                full = os.path.join(self.folder_path, folder)

                if os.path.isdir(full):
                    report.write(folder + "\n")

            report.close()

            print("\nReport generated successfully.")
            print("Saved as:", report_path)

        except Exception as e:
            print("Error generating report:", e)


# -------------------------------
# Main Program
# -------------------------------

def main():

    print("=" * 45)
    print("        SMART FILE ORGANIZER")
    print("=" * 45)

    path = input("Enter Folder Path: ")

    organizer = SmartFileOrganizer(path)

    if not organizer.validate_directory():
        return

    while True:

        print("\n========== MENU ==========")
        print("1. Scan Files")
        print("2. Organize Files")
        print("3. Show Statistics")
        print("4. Search Files")
        print("5. Find Duplicates")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":
                organizer.scan_files()

            elif choice == "2":

                if len(organizer.files) == 0:
                    organizer.scan_files()

                organizer.organize_files()

            elif choice == "3":
                organizer.show_statistics()

            elif choice == "4":
                organizer.search_files()

            elif choice == "5":
                organizer.find_duplicates()

            elif choice == "6":
                organizer.generate_report()

            elif choice == "7":
                print("Thank you for using Smart File Organizer.")
                break

            else:
                print("Invalid choice.")

        except FileNotFoundError:
            print("Folder not found.")

        except PermissionError:
            print("Permission denied.")

        except shutil.Error:
            print("File already exists.")

        except Exception as e:
            print("Unexpected Error:", e)


if __name__ == "__main__":
    main()