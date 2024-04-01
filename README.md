![GitHub License](https://img.shields.io/github/license/mehdirexon/Nobitex-Crypto-Price-Extractor)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/mehdirexon/Nobitex-Crypto-Price-Extractor)
![Static Badge](https://img.shields.io/badge/Website-mehdirexon.ir-purple?link=https://mehdirexon.ir)
![GitHub last commit](https://img.shields.io/github/last-commit/mehdirexon/Nobitex-Crypto-Price-Extractor)


# Nobitex Online Cryto Prices💰📈

A python script 🐍 working with selenium library to scrape the prices of cryptos in real time 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Future Features and Goals](#future-features-and-goals)
- [Contributing](#contributing)
- [License](#license)

## Introduction 🚀

Nobitex Online Crypto Prices: Fetches real-time cryptocurrency data from Nobitex. Automate price tracking with ease.
## Features ✨

- OOP structure 🏗️
- Easy to use 🤖
- Flexible for Django 💪
- Export to excel 📊

## Installation 💻

1. Download the project.
2. Run this code below the class 
```python
    if __name__ == "__main__":
        scraper = NobitexBot()
        scraper.getPrices(delay=3,
        infinityRequest=True,
        optionalDelay=0.5,
        link="https://nobitex.ir/en/prices/",
        element="element",
        exportInExcel=True,
        excelPath="./"
        )
```
3. Have a watch at outputs where you defined ```excelPath```.

## Future Features and Goals 🚀

Here are some features and goals I plan to implement in future versions:

- **Webserver:** Exports and updates the outputs in real-time using websockets.
- **Analyzer:** Uses AI and database for Analyzing changes.


## Contributing 🤝

1. You can have contact with me in [telegram](https://t.me/mehdirexon).
2. Have a PR on my repo.

## Contributers
<a href="https://github.com/mehdirexon/Nobitex-Crypto-Price-Extractor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mehdirexon/Nobitex-Crypto-Price-Extractor" />
</a>

## License 📄

This project is licensed under the [MIT License](LICENSE).
