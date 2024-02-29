filename = input("File name : ")
filename_lower = filename.lower()

if filename_lower.endswith('.gif'):
    print("image/gif")
elif filename_lower.endswith('.jpg') or filename_lower.endswith('.jpeg'):
    print("image/jpeg")
elif filename_lower.endswith('.png'):
    print("image/png")
elif filename_lower.endswith('.pdf'):
    print("application/pdf")
elif filename_lower.endswith('.txt'):
    print("text/plain")
elif filename_lower.endswith('.zip'):
    print("application/zip")
else:
    print("Unknown file type")
