# News Scraper and Email Scheduler

## Overview
This project scrapes news articles from The Guardian's international news section and sends them via email at a scheduled time daily. It uses Python for web scraping, email automation, and task scheduling.

## Features
- Scrapes news articles from `https://www.theguardian.com/international`.
- Extracts article title, category, summary, publish time, and link to the article.
- Filters out articles with incomplete data.
- Sends formatted news articles via email using Gmail's SMTP server.
- Schedules email delivery at a specified time daily (default: 08:00, this can be changed).
- Uses environment variables for secure email credentials.
- Configurable URL via `config.ini`.

## Requirements
- Python 3.x
- Required Python packages (install via `pip`):
  ```bash
  pip install beautifulsoup4 requests python-dotenv schedule
  ```
- Gmail account with an App Password for SMTP access.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project root:
   ```plaintext
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASS=your-app-password
   ```
   - Replace `your-email@gmail.com` with your Gmail address.
   - Replace `your-app-password` with a Gmail App Password (see "Setting Up Email for Automation" below).

4. **Configure `config.ini`**:
   - Ensure the URL is set to `https://www.theguardian.com/international`:
     ```ini
     [Settings]
     url = https://www.theguardian.com/international
     ```

5. **Run the script**:
   ```bash
    cd news_summarizer
    python main.py
   ```
   - The script will scrape news articles and schedule an email to be sent daily at 08:00 to `the set email address`.

## Setting Up Email for Automation
To enable email automation with Gmail, follow these steps to configure your email account and generate an App Password:

1. **Enable 2-Step Verification**:
   - Go to your [Google Account](https://myaccount.google.com/security).
   - Under "Security," select **2-Step Verification** and follow the prompts to enable it (e.g., using your phone number for verification).

2. **Generate an App Password**:
   - After enabling 2-Step Verification, go to [App Passwords](https://myaccount.google.com/security#signin) in the Security section.
   - Click **Generate**, select **Other (Custom name)**, and enter a name (e.g., "News Scraper").
   - Copy the 16-character App Password generated (e.g., `xxxx xxxx xxxx xxxx`).

3. **Add Credentials to `.env`**:
   - In the project root, create or edit the `.env` file.
   - Add your Gmail address and the App Password:
     ```plaintext
     EMAIL_USER=your-email@gmail.com
     EMAIL_PASS=your-app-password
     ```
   - Replace `your-email@gmail.com` with your Gmail address and `your-app-password` with the generated App Password.

4. **Secure the `.env` File**:
   - Add `.env` to your `.gitignore` file to prevent it from being uploaded to version control.
   - Ensure the file has restricted permissions (e.g., readable only by the owner).

5. **Test Email Sending**:
   - Run the script to verify that emails are sent successfully.
   - If you encounter authentication errors, double-check the `EMAIL_USER` and `EMAIL_PASS` values in `.env`.

**Note**: Do not use your regular Gmail password in the `.env` file, as Gmail requires an App Password for third-party apps like this script.

## File Structure
- `main.py`: Entry point; orchestrates news scraping and email scheduling.
- `scraper.py`: Handles web scraping and news compilation logic.
- `utils.py`: Contains utility functions for error handling and configuration.
- `scheduler.py`: Manages scheduling of tasks using the `schedule` library.
- `config.ini`: Configuration file for the news website URL.
- `.env`: Stores sensitive email credentials (not tracked in version control).
- `README.md`: Project documentation.

## Usage
- The script runs continuously, checking for scheduled tasks every second.
- News articles are scraped when the script starts and compiled into an email.
- The email is sent daily at 15:54 (configurable in `main.py`).
- If no articles are found, a console message is printed instead of sending an email.

## Notes
- The scraper is designed specifically for `https://www.theguardian.com/international` due to its HTML structure. Other websites may not work without modifying the scraping logic in the `scraper.py`.
- Ensure your Gmail account has 2-Step Verification enabled to generate an App Password.
- Add `.env` to `.gitignore` to prevent exposing credentials in version control.
- The recipient email is configurable in `main.py`).

## Troubleshooting
- **SMTP Authentication Error**: Verify `EMAIL_USER` and `EMAIL_PASS` in `.env` are correct and that the App Password is valid.
- **No Articles Found**: Check `config.ini` URL and ensure the website's HTML structure hasn’t changed.
- **Scheduling Issues**: Confirm the system time matches the scheduled time in `main.py`.


## Keynotes
- Built using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping.
- Email automation powered by [smtplib](https://docs.python.org/3/library/smtplib.html).
- Scheduling handled by [schedule](
