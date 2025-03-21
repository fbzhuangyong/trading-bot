import pandas as pd
import pandas_ta as ta

# 生成测试数据（收盘价序列）
prices = pd.Series([30, 31, 29, 32, 31, 33])

# 计算双均线
sma_fast = ta.sma(close=prices, length=3)
sma_slow = ta.sma(close=prices, length=5)

# 生成交易信号
signal = "持有" if sma_fast.iloc[-1] > sma_slow.iloc[-1] else "观望"

# 输出结果
print("\n=== 双均线策略信号 ===")
print(f"最新价格: {prices.iloc[-1]}")
print(f"快线 (SMA3): {sma_fast.dropna().tolist()}")
print(f"慢线 (SMA5): {sma_slow.dropna().tolist()}")
print(f"操作建议: {signal}")