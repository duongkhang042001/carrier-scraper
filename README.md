# Carrier Scraper

A Python web scraping application to collect detailed information about mobile carriers from [IMEI.info](https://www.imei.info/carriers/).

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Carrier Scraper is a Python application that scrapes information about mobile carriers from the IMEI.info website. It collects both basic and detailed information for each carrier and stores it in a structured JSON file. The application uses `requests` for making HTTP requests and `BeautifulSoup` for parsing HTML.

## Features
- Scrape basic information about carriers (Code, Operator, Country).
- Navigate to detailed carrier pages and scrape comprehensive details.
- Save the collected data in a structured JSON file.

## Installation
### Prerequisites
- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using `pip`:
```bash
pip install requests beautifulsoup4

