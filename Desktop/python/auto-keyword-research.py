import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_keyword(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.find_all("div", class_="yuRUbf")

    data = []
    for result in search_results:
        title = result.find("h3").text
        url = result.find("a")["href"]
        headings = result.find_all("h3")
        
        headings_text = [heading.text for heading in headings]

        data.append([title, url, headings_text])

    df = pd.DataFrame(data, columns=["ページタイトル", "URL", "見出しタグ"])

    # 結果をエクセルファイルに保存
    filename = f"{keyword}_検索結果.xlsx"
    df.to_excel(filename, index=False)
    print(f"検索結果が '{filename}' という名前のエクセルファイルに保存されました。")

# キーワードを指定して検索を実行
keyword = "ペット保険"  # 検索したいキーワードをここに入力
search_keyword(keyword)
