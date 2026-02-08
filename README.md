# Multi-Page Book Scraper using Selenium

# Why I did this project

I wanted to understand how web scraping works when a website has multiple pages and requires browser interaction.
Instead of manually copying data page by page, I built a script that automates this process using Selenium.

This project helped me understand how browser automation works in practice and how to extract structured data from websites.



# What this project does

The script:
- Opens a website using a real browser, i used chrome
- Extracts book information from each page
- Automatically navigates through all pages
- Stores the collected data in a CSV file

The data collected includes:
- Book title
- Price
- Rating



# How Selenium interacts with the website

When a webpage loads in a browser, it is internally represented as a structured tree of elements.
This structure is called the Document Object Model (DOM).

Selenium interacts with this DOM structure rather than the visual page.
By identifying the correct elements in the DOM, Selenium can extract information reliably.

In this project, each book is contained inside a specific container element.
The script first locates this container and then extracts relevant details from inside it.

# How the script works. 

1. Open the website in Chrome
2. Wait for book elements to load
3. Extract details for each book on the page
4. Click the "Next" button to move to the next page
5. Repeat until no more pages are left
6. Save all collected data into a CSV file


# Challenges I faced

- Identifying the correct HTML elements for book titles
- Handling the pagination button properly
- Ensuring the page was fully loaded before scraping
- Fixing issues when elements were not interactable

Working through these issues helped me understand Selenium better.



# Output

The script generates a file called:

`books_dataset.csv`

This file contains all scraped book data in a structured format.


# Technologies used

- Python
- Selenium
- Pandas

# How to run the project

1. Install dependencies:
