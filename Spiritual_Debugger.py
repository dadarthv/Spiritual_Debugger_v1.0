import time

def run_spiritual_debugger():
    while True: # 開啟無限迴圈
        print("\n" + "="*40)
        print("--- 靈性辨識系統 Spiritual Debugger v1.0 啟動中 ---")
        print("="*40)
        time.sleep(0.5)
        
        # 0. 身分錨點 (Anchor Check)
        print("\n[Step 0: 身分錨點檢查]")
        is_daughter = input("妳是否記得自己是天父寵愛的公主？(y/n): ").lower()
        
        if is_daughter != 'y':
            print("\n>> ⚠️ 偵測到身分認知 Bug！正在重定向至『恩典修復程序』...")
            print(">> 提醒：妳的價值不在於妳『知道什麼』，而在於妳『是誰的女兒』。")
            break # 如果身分不對，強制停止程式去休息

        # 1. 核心準則驗證 (The Core API)
        print("\n[Step 1: 核心準則驗證 (The Core API)]")
        insight = input("請簡述妳收到的靈感或資訊: ")
        
        has_peace = input("這是否帶給妳真實的『平安』，而非焦慮？(y/n): ").lower()
        has_love = input("這是否讓妳更愛上帝與身邊的人？(y/n): ").lower()

        # 2. 功能測試 (Unit Test)
        print("\n[Step 2: 功能測試 (Unit Test)]")
        is_humble = input("這是否讓妳保持謙卑，而非自覺高人一等？(y/n): ").lower()
        is_practical = input("這是否能幫助妳更好地生活與工作(God's work)？(y/n): ").lower()

        # 3. 最終編譯結果 (Final Result)
        print("\n" + "-"*30)
        if has_peace == 'y' and has_love == 'y' and is_humble == 'y' and is_practical == 'y':
            print("✅ 編譯成功：這是一個可以收下的『浪漫驚喜』！")
            print(f"紀錄：『{insight}』已存入公主的靈感資料庫。")
        else:
            print("❌ 偵測到代碼衝突 (Conflict)：這可能是雜訊或 Bug。")
            print(">> 建議操作：將此內容【註解掉 (Comment out)】。")
            print(">> 回到『鍾愛』的身邊，享受單純的平安。")
        print("-"*30)

        # 詢問是否進行下一輪
        again = input("\n是否再進行下一輪辨識？(y/n): ").lower()
        if again != 'y':
            print("\n感謝使用。願上帝的平安與妳同在，回見，公主！")
            break # 退出迴圈，結束程式

if __name__ == "__main__":
    run_spiritual_debugger()

