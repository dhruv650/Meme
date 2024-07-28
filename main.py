import requests


url = "https://api.memegen.link/images/"

interface = {"Buzz Lightyear": "buzz",
  "Drake Hotline Bling": "drake",
  "Distracted Boyfriend": "disastergirl",
  "Oprah You Get a Car": "oprah",
  "I Don't Always": "aag",
  "Grumpy Cat": "grumpycat",
  "Success Kid": "success",
  "One Does Not Simply": "onedoesnot",
  "Brace Yourselves": "brace",
  "Y U NO": "yuno",
  "Ancient Aliens": "aliens",
  "Two Buttons": "twobuttons",}

for i in interface.keys():
        print(f" - {i}")

templete = input("Enter Your Templete: ")
top_txt = input("Enter you top text: ").replace(" ",>
bottom_txt = input("Enter your bootom text: ").repla>
extension = input("Enter your extension(png, gif, je>


url_formation = f"{url}{interface[templete]}{top_txt>

make_request = requests.get(url_formation)

file_name = f"{interface[templete]}.{extension}"
with open(file_name, "wb") as f:
    f.write(make_request.content)
print(f"Meme saved as: {file_name}")
print(f"url: {url_formation}")