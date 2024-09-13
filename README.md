## URL Shortener Script
This script allows you to shorten URLs using the Bitly service via the pyshorteners library. You can input a long URL, and the script will return a shortened version.

## Prerequisites
Before running the script, ensure you have the following installed:

1.	Python: Ensure Python is installed on your system.
2.	pyshorteners: Install this library using the following command:
            pip install pyshorteners
3.	Bitly Access Token: You'll need to generate an API access token from Bitly. Get your access token here.

## Usage
1.	Clone or download this repository.
2.	Install the required dependencies:
            pip install pyshorteners
3.	Open the script and replace the placeholder for the ACCESS_TOKEN with your Bitly API key.
            ACCESS_TOKEN = "Your Bitly Access Token"
4.	Run the script:
            python script.py
5.	Enter the long URL when prompted. The script will return a shortened URL using the Bitly service.

## Example
Input a long URL: https://www.example.com/very-long-url-that-needs-shortening
Short URL is : https://bit.ly/abc123

## Troubleshooting
•	Ensure you have a valid Bitly access token.
•	Make sure your internet connection is stable while running the script, as it relies on an external API.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



