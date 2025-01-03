# Read and clean the text file
with open("jupyter_files/swayam_course_details.txt", "r", encoding="utf-8", errors="replace") as txt_file:
    lines = txt_file.readlines()

# Write the cleaned content back to a new file
with open("cleaned_swayam_course_details.txt", "w", encoding="utf-8") as cleaned_file:
    for line in lines:
        cleaned_file.write(line)

print("File cleaned. Now converting to CSV.")

# Parse cleaned file to CSV
import csv
with open("cleaned_swayam_course_details.txt", "r", encoding="utf-8") as txt_file:
    lines = txt_file.readlines()

with open("course_data.csv", "w", newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    for line in lines:
        writer.writerow(line.split())

print("Space-separated text file converted to CSV.")
