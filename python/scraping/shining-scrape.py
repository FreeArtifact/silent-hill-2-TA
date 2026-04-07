from bs4 import BeautifulSoup
import requests
import os
archive_url='https://imsdb.com/scripts/Shining,-The.html'
def get_linkContents():
    r = requests.get(archive_url)
    print(f"{r=}")
    soup = BeautifulSoup(r.content, 'html.parser')


    linkText = []
    for item in soup.findAll(['pre', 'b']):
        print(f"{item.text}")

        linkText.append(item.text)
    print(linkText)
    download_toFile(linkText)
    return
def download_toFile(linkText):

    file_name = "shinning-dialogue.txt"
    print("Downloading file: " + file_name)
    working_dir = os.getcwd()
    file_deposit = os.path.join(working_dir, file_name)
    print(file_deposit)
 
    with open(file_deposit, 'w') as f:
   
        for item in linkText:
            f.write(item + '\n')

            print("Downloaded " + item)

    return
if __name__ == "__main__":
    get_links = get_linkContents()