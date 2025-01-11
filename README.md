# Crypto News Sentiment Analyzer

This project is a **Crypto News Sentiment Analyzer** that fetches recent news and trading ideas for a selected cryptocurrency symbol and uses a language model to analyze the sentiment. The output is a table summarizing the news and a sentiment-based conclusion.

## Features

- Fetches the latest trading ideas and news articles for popular cryptocurrencies (e.g., BTC, ADA, ETH).
- Analyzes the sentiment of news content (positive or negative).
- Displays results in a structured table with time, reference, and link.
- Provides a summarized conclusion based on the analysis.

## Demo

![Demo Screenshot](demo.png) _(Add a screenshot of the app interface here)_

## Technologies Used

- **Python**
- **Streamlit** - For the web interface
- **OpenAI API (local deployment)** - For sentiment analysis
- **Requests** - For fetching news data

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/crypto-news-sentiment-analyzer.git
   cd crypto-news-sentiment-analyzer
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Start the **G4F** package by running the local OpenAI server:

   ```bash
   python -m g4f.server
   ```

2. Enter a cryptocurrency symbol (e.g., BTC, ADA, ETH) in the input box.
3. Click the **Analyze** button.
4. View the sentiment analysis in a table format along with a conclusion.

## Configuration

- The OpenAI API is locally deployed, so no API key is required. Ensure your local OpenAI server is running at `http://localhost:1337/v1`.

## Project Structure

```
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── demo.png             # Demo screenshot (optional)
```

## Dependencies

- streamlit
- openai
- requests

Install them via:

```bash
pip install streamlit openai requests
```

## Future Improvements

- Add support for more data sources.
- Improve sentiment analysis accuracy.
- Implement error handling for API failures.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [TradingView](https://www.tradingview.com/) for market data.
- [OpenAI](https://openai.com/) for language model APIs.

---

Feel free to contribute and make this tool even better!
