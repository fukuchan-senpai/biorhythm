import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 誕生日を入力し変数にセット
yyyy = input("Your Birthday Year (19xx): ")
mm = input("Your Birthday month (1-12): ")
dd = input("Your Birthday day (1-31): ")
dt_bd = datetime.datetime(year=int(yyyy), month=int(mm), day=int(dd))

# 現在日を取得
dt_now = datetime.datetime.now()

# 誕生日から現在日までの日数を計算
dt_diff = dt_now - dt_bd
dt_diff_days = dt_diff.days

# 今日の5日前から 誕生日の30日後まで 0.1 刻み
x = np.arange(dt_diff_days - 5, dt_diff_days + 30, 0.1)

# 身体
y1 = np.sin(2 * np.pi * x / 23)
plt.plot(x, y1, color="blue", label="P")

# 感情
y2 = np.sin(2 * np.pi * x / 28)
plt.plot(x, y2, color="red", label="S")

# 知性
y3 = np.sin(2 * np.pi * x / 33)
plt.plot(x, y3, color="green", label="I")

plt.title('福ちゃん先輩の「バイオリズム」', fontname="MS Gothic")

# X軸のフォーマットを設定
# ここを日付にしたい
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))

plt.xlabel('blue: physical, red: sensitivity, green: intellectual')
plt.savefig('my_biorhythm.png')
plt.show()
