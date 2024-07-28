# Meme Generator Script Documentation

## Overview

This script allows users to generate meme images using the [Memegen API](https://api.memegen.link/). By choosing from a list of popular meme templates and providing custom text, users can create and save memes to their local machine.

## Features

- Select from a list of popular meme templates.
- Add custom top and bottom text to the meme.
- Choose the desired image format (PNG, JPEG, GIF, WebP).
- Automatically fetch and save the generated meme image.

## Prerequisites

- Python 3.x installed on your system.
- Internet connection to access the Memegen API.
- Python's `requests` library for making HTTP requests.

## Installation

1. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

2. Install the `requests` library if it's not already installed:

   ```bash
   pip install requests
   ```

## Script Usage

### Step-by-Step Instructions

1. **Run the Script**: Execute the script in a Python environment. 

   ```bash
   python meme_generator.py
   ```

2. **Select a Meme Template**: The script will display a list of available meme templates. Choose one by typing its name exactly as shown in the list.

3. **Enter Top Text**: Provide the text you want to display at the top of the meme. Spaces will be replaced with underscores for URL compatibility.

4. **Enter Bottom Text**: Provide the text you want at the bottom of the meme. Again, spaces will be replaced with underscores.

5. **Choose Image Format**: Enter the desired file extension for the image (e.g., png, jpg, gif, webp).

6. **Fetch and Save**: The script will generate the meme, save it locally, and print the file name and URL used to generate it.

### Example Run

```plaintext
 - Buzz Lightyear
 - Drake Hotline Bling
 - Distracted Boyfriend
 - Oprah You Get a Car
 - I Don't Always
 - Grumpy Cat
 - Success Kid
 - One Does Not Simply
 - Brace Yourselves
 - Y U NO
 - Ancient Aliens
 - Two Buttons

Enter Your Template: Buzz Lightyear
Enter your top text: Memes
Enter your bottom text: Everywhere
Enter your extension (png, gif, jpg, webp): png

Meme saved as: buzz.png
URL: https://api.memegen.link/images/buzz/Memes/Everywhere.png
```

## Code Explanation

Below is a detailed breakdown of how the script works:

```python
import requests

# Base URL for the memegen API
url = "https://api.memegen.link/images/"

# Dictionary mapping meme template names to their API identifiers
interface = {
    "Buzz Lightyear": "buzz",
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
    "Two Buttons": "twobuttons",
}

# Display available meme templates to the user
for i in interface.keys():
    print(f" - {i}")

# Prompt the user to select a template and enter text and format
template = input("Enter Your Template: ")
top_txt = input("Enter your top text: ").replace(" ", "_")
bottom_txt = input("Enter your bottom text: ").replace(" ", "_")
extension = input("Enter your extension (png, gif, jpg, webp): ")

# Construct the URL for the requested meme
url_formation = f"{url}{interface[template]}/{top_txt}/{bottom_txt}.{extension}"

# Make a request to the API
make_request = requests.get(url_formation)

# Save the meme image to a file
file_name = f"{interface[template]}.{extension}"
with open(file_name, "wb") as f:
    f.write(make_request.content)

# Output the saved file name and URL
print(f"Meme saved as: {file_name}")
print(f"URL: {url_formation}")
```

### Code Components

1. **Imports**:
   - `requests`: Used for making HTTP requests to the Memegen API.

2. **Variables**:
   - `url`: The base URL for the Memegen API.
   - `interface`: A dictionary mapping user-friendly meme names to their respective template IDs used by the API.

3. **Template Selection**:
   - The script displays available meme templates for user selection.

4. **User Input**:
   - `template`: The user inputs the desired meme template.
   - `top_txt` and `bottom_txt`: User inputs for the top and bottom text of the meme, with spaces replaced by underscores for URL compatibility.
   - `extension`: The image format the user wishes to save the meme in.

5. **URL Construction**:
   - The URL is constructed by combining the base URL, template ID, top and bottom texts, and the chosen image extension.

6. **HTTP Request**:
   - The script makes a GET request to the constructed URL to fetch the meme.

7. **File Saving**:
   - The response content (image) is saved to a file named according to the template and chosen extension.

8. **Output**:
   - The script prints the filename and URL of the generated meme.

## Troubleshooting

- **Invalid Template**: Ensure you type the template name exactly as listed.
- **Unsupported Extension**: Use only supported image formats (`png`, `jpg`, `gif`, `webp`).
- **Network Issues**: Make sure you have an active internet connection when running the script.

## Conclusion

This script offers a simple way to create and download memes using the Memegen API. By following the steps outlined, users can customize meme templates with their own text and save them in various formats.

For any issues or contributions, feel free to contact the author.


