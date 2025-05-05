# your_app/import_data.py
import pandas as pd
from two.models import Student

def import_data():
    # Path to your existing Excel file
    excel_file_path = './student.xlsx'

    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(excel_file_path)
    except FileNotFoundError:
        print("file ot found")
        df = pd.DataFrame(columns=['Name', 'Marks'])

    # Save DataFrame records to the database
    for index, row in df.iterrows():
        name = row['Name']
        marks = row['Marks']

        # Check if the student already exists in the database
        if not Student.objects.filter(name=name).exists():
            student = Student(name=name, marks=marks)
            student.save()

if __name__ == '__main__':
    import_data()
