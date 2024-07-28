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
top_txt = input("Enter you top text: ").replace(" ","_")
bottom_txt = input("Enter your bootom text: ").replace('','_')
extension = input("Enter your extension(png, gif, jpeg, webp): ")


url_formation = f"{url}{interface[templete]}/{top_txt}/{bottom_txt}.{extension}"
make_request = requests.get(url_formation)
file_name = f"{interface[templete]}.{extension}"
with open(file_name, "wb") as f:
    f.write(make_request.content)

if make_request.status_code == 200:
  print("Image Generated Successfully")
print(f"Meme saved as: {file_name}")
print(f"url: {url_formation}")