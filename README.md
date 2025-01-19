Unfollow Instagram Bot

This bot is designed to remove followers who do not follow you back on Instagram. The application leverages Python and Selenium to interact with Instagram's web interface.

How to Use the App

Clone the repository to your local machine.

git clone https://github.com/sergiozimmermann/unfollow-instagram-bot.git
<br/>cd unfollow-instagram-bot

Install the required dependencies:

pip install -r requirements.txt

Create a .env file in the root directory of the project with the following parameters:

username_instagram="YOUR_INSTAGRAM_USERNAME"
<br/>password_instagram="YOUR_INSTAGRAM_PASSWORD"

Replace YOUR_INSTAGRAM_USERNAME and YOUR_INSTAGRAM_PASSWORD with your actual Instagram login credentials.

Run the application:

python main.py

After the login process is completed, you may be prompted to press "Enter" in the terminal. This step is necessary for accounts with two-factor authentication enabled.

The bot will then proceed to analyze your "Following" list and remove any users who are not following you back.

Notes

Ensure that you have Google Chrome installed, and the correct version of the ChromeDriver compatible with your browser version. You can download ChromeDriver here.

The bot simulates browser actions, so do not use your account for spamming or violating Instagram's terms of service to avoid being banned.

If you encounter issues, verify that the .env file is correctly configured and that the XPath selectors in the script match Instagram's current DOM structure.

Disclaimer

Use this tool responsibly. The developer is not responsible for any account restrictions or bans resulting from misuse of this application.

Feel free to contribute to this project by submitting issues or pull requests on the GitHub repository!
