import os
import pandas as pd
import talib
from binance import Client

# 初始化客户端
client = Client(
    api_key=os.environ['BINANCE_API_KEY'],
    api_secret=os.environ['BINANCE_SECRET_KEY']
)

def get_data(symbol='BTCUSDT', interval='15m', limit=100):
    """获取K线数据"""
    klines = client.futures_klines(
        symbol=symbol,
        interval=interval,
        limit=limit
    )
    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close',
        'volume', 'close_time', 'quote_volume',
        'trades', 'taker_buy_base', 'taker_buy_quote', 'ignore'
    ])
    df['close'] = df['close'].astype(float)
    return df

def analyze_rsi(df, period=14):
    """计算RSI指标"""
    df['rsi'] = talib.RSI(df['close'], timeperiod=period)
    return df

if __name__ == "__main__":
    print("=== 实时交易信号 ===")
    data = get_data()
    analyzed_data = analyze_rsi(data)
    latest_rsi = analyzed_data['rsi'].iloc[-1]
    print(f"时间: {analyzed_data['timestamp'].iloc[-1]}")
    print(f"最新RSI: {latest_rsi:.2f}")
    print("建议操作:", "买入" if latest_rsi < 30 else "卖出" if latest_rsi > 70 else "持有")
