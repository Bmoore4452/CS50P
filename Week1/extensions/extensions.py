x = input("File name: ").strip().casefold()

if x.endswith(".gif") == True:
    print("image/gif")
elif x.endswith(".jpg") == True or x.endswith(".jpeg") == True:
    print("image/jpeg")
elif x.endswith(".png") == True:
    print("image/png")
elif x.endswith(".pdf") == True:
    print("application/pdf")
elif x.endswith(".zip") == True:
    print("application/zip")
elif x.endswith(".txt") == True:
    print("text/plain")
else:
    print("application/octet-stream")
