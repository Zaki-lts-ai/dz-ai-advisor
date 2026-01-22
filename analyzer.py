import json
import os

def start_analysis():
    os.system('clear')
    print("========================================")
    print("   🛡️ نظام مستشار الرقمنة المؤمن - الجزائر   ")
    print("========================================\n")

    # نظام حماية بسيط (Security Gate)
    secret_pin = "2026"  # يمكنك تغيير هذا الرمز لاحقاً
    user_input = input("🔒 أدخل رمز الدخول للأمان: ")

    if user_input != secret_pin:
        print("\n❌ وصول مرفوض! الرمز خاطئ.")
        return

    try:
        with open("dz.json", "r", encoding='utf-8') as f:
            db = json.load(f)

        institutions = db.get("institutions", {})
        
        print("\n✅ تم التحقق.. المؤسسات المتاحة: " + ", ".join(institutions.keys()))
        query = input("\n🔎 أدخل اسم المؤسسة للتحليل: ").strip().lower()

        if query in institutions:
            data = institutions[query]
            print(f"\n📊 التقرير التقني لـ {data['name']}:")
            print(f"----------------------------------------")
            print(f"🏛️ الخدمة: {data['service']}")
            print(f"🌐 الحالة: {data['status']}")
            print(f"💡 نصيحة تقنية: {data['tech_tip']}")
            print(f"----------------------------------------")
        else:
            print(f"\n❌ المؤسسة '{query}' غير مسجلة.")

    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    start_analysis()
