import yfinance as yf

symbol = input("أدخل رمز السهم: ")

try:
    ticker = yf.Ticker(symbol)
    # جلب بيانات آخر يومين للمقارنة
    hist = ticker.history(period="2d")
    
    if len(hist) < 2:
        print("بيانات غير كافية للمقارنة.")
    else:
        price_today = hist['Close'].iloc[-1]
        price_yesterday = hist['Close'].iloc[-2]
        
        # حساب الفرق
        diff = price_today - price_yesterday
        percent = (diff / price_yesterday) * 100

        print(f"\n--- تحليل السعر لـ {symbol} ---")
        print(f"السعر الحالي: {price_today:.2f}")
        print(f"التغير: {diff:+.2f} ({percent:+.2f}%)")
        
        # منطق بسيط (بمثابة ذكاء اصطناعي يدوي)
        if percent > 0:
            print("الحالة: صعود 📈")
        else:
            print("الحالة: هبوط 📉")

except Exception as e:
    print(f"حدث خطأ: {e}")

