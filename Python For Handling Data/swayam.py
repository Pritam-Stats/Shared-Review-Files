import pandas as pd

# URL for CSV export
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQRfIO7X-GvUiGo3EmWdWSILJyqjeTNfY5WsuC48n6s--tDGYHizlsqjXNfO0qY7yZqONcSEoYBCTkN/pub?output=csv"

# Load data, skipping the first 3 rows
df = pd.read_csv(sheet_url, skiprows=10)

# View the DataFrame
# print(df.head())

# Filter rows where the "Type of Course" is "New"
new_courses = df[df["Type of course"] == "New"]

# Filter courses where the "Type of course" is "New" and the "Discipline" is "Computer Science and Engineering"
cs_courses = df[
    df["Discipline"].isin([
        "Computer Science and Engineering", 
        "Mathematics and Computing", 
        "Mathematics", 
        "Statistics", 
        "Data Science", 
        "Artificial Intelligence", 
        "Machine Learning", 
        "Deep Learning",
        "Math and Sciences",
        'Mathematics / Statistics / Economics',
        'Computer Science',
        'Mathematics & Statistics',
        'Science and Engineering',
        'Applied Statistics/Finance','Mathematical Sciences', 'Management & Entrepreneurship', 'Computer Science and Engineering, Mathematics',
        "Business Administration"
    ])
]
# # Display the filtered DataFrame or specific columns
# print(cs_courses[["Course Name", "Course ID", "Institute"]])
print(cs_courses[cs_courses["Institute"] == "IIT Madras"])
