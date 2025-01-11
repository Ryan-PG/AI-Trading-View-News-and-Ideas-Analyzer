from openai import OpenAI
import streamlit as st


symbol = st.text_input("Enter the symbol. (like BTC,ADA,ETH)").upper().strip()
button = st.button("Analyze")

if button and symbol != "":
  news = requests.get(f'https://www.tradingview.com/symbols/{symbol}USD/ideas/?component-data-only=1&sort=recent').json()
  ideas = requests.get(f'https://news-headlines.tradingview.com/v2/view/headlines/symbol?client=landing&lang=en&section=&streaming=true&symbol=BITSTAMP%3A{symbol}USD').json()['items']
  
  prompt = f"""
  Analyze the news I provide for you and tell me that the result is positive or negative?
  Output must be a table containing the time, reference and link of the news.
  At the end, give me a conclusion.
  
  news:
  ```
  {json.dumps(news)}
  ```
  """
  
  client = OpenAI(
    api_key="NO_NEED_TO_API_KEY",
    base_url="http://localhost:1337/v1",
  )

  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {
        "role": "user",
        "content": prompt,
      }
    ]
  )

  st.markdown(response.choices[0].message.content)