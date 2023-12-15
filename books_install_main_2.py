import requests
from PIL import Image
from io import BytesIO
###################################################
# 検索キーワード
search_query = "Oreilly"

#画像保存先フォルダ
save_dir = "C:/gitWork/pyBooks/books_image/Oreilly"

# 取得する画像の総数
total_results = 1000
####################################################
# 1回の検索で取得する結果の最大数
max_results_per_request = 40

# エラーが発生したポイントから再開するためのカウンター
start_index =  0
#637 * max_results_per_request

# 画像の保存済みカウンター
saved_counter = 0

# Google Books APIのURLを生成してデータを取得し、画像を保存
while saved_counter < total_results:
    # Google Books APIのURL
    url = f"https://www.googleapis.com/books/v1/volumes?q={search_query}&startIndex={start_index}&maxResults={max_results_per_request}"

    # APIリクエストを送信して検索結果を取得
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        # 取得した検索結果から画像を保存
        for i, item in enumerate(data["items"]):
            # 画像URLを取得
            image_link = item["volumeInfo"].get("imageLinks", {}).get("thumbnail")
            if image_link:
                # 画像をダウンロード
                image_response = requests.get(image_link)
                image_data = image_response.content

                # 画像をPillowのImageオブジェクトに変換
                image = Image.open(BytesIO(image_data))

                # 画像を保存
                image_filename = f"{str(saved_counter + 1).zfill(5)}.png"
                image.save(save_dir + "/" + image_filename)
                print(f"Saved {image_filename}")

                saved_counter += 1

                # 取得した画像の総数が目標数に達したらループを終了
                if saved_counter == total_results:
                    break
    else:
        # "items"キーが存在しない場合はループを終了
        print("No more search results.")
        break
    # エラーが発生したポイントから再開するためにカウンターを更新
    start_index += max_results_per_request

print("All images saved.")
