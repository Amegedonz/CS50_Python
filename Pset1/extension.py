extensions = {".gif" : "image/GIF",
              ".jpg" : "image/jpg",
              ".jpeg" : "image/jpeg",
              ".png" : "image/png",
              ".pdf" : "document/pdf",
              ".txt" : "text/txt",
              ".zip" : "compressed file/zip"
              }

def main():
    count = 0
    fileName = input("Enter File Name here: ")
    for ending in extensions:
        if fileName.endswith(ending):
            count += 1
            print(extensions[ending])
        
    if count == 0:
        print("application/octet-stream")
    

    


main()