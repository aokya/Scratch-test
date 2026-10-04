import os
import scratchattach as sa

# 1. Scratchにログイン
# ※安全のためパスワードは環境変数（SCRATCH_PASSWORD）から読み込む形にしています
password = os.environ.get("SCRATCH_PASSWORD", "ここにテスト用パスワードを入れても動きます")
session = sa.login("aokya2", password)

# 2. クラウド変数の監視を設定（最新版の小文字 cloud_events を使用）
events = sa.cloud_events.CloudEvents("1387897878")

# 3. クラウド変数が変わったときの処理
@events.event
def on_set(event):
    # 変更された変数名が「cloud_var」で、値が「1」だった場合
    if event.var == "cloud_var" and event.value == "1":
        print("💡 cloud_var が 1 になりました。2 に書き換えます。")
        
        # クラウド変数を 2 に変更
        try:
            session.connect_cloud("1387897878").set_var("cloud_var", "2")
            print("✅ 2 への書き換えに成功しました！")
        except Exception as e:
            print(f"❌ 書き換えに失敗しました: {e}")

# 4. 24時間監視をスタート
print("🚀 Scratchのクラウド変数監視を開始しました（aokya2）...")
events.start()
