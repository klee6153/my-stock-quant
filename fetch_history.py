import yfinance as yf
import pandas as pd

# 抓取加權指數 (TAIEX) 從最早可得的數據至今
# yfinance 的 TAIEX 資料大約從 1990 年代開始較完整
# 我們設定從 1960 年開始嘗試抓取
df = yf.download("^TWII", start="1960-01-01")

# 重整格式
df.reset_index(inplace=True)

# 存成一個獨立的檔案，方便回測使用
df.to_csv("taiex_history_full.csv", index=False)

print(f"歷史數據下載完成，共計 {len(df)} 筆資料！")
