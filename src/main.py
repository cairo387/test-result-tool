#CSVを扱うための標準機能読み込み
import csv

#statusをカウントするための関数を定義
def count_status(file_path):
    #空の辞書を作成
    result = {}
    #file_pathで指定されたファイルをUTF-8で開き、以降fとして使う
    with open(file_path, encoding="utf-8") as f:
        #csvの内容を辞書形式で読めるように変換
        reader = csv.DictReader(f)
        #CSVを1行ずつを順番に取り出す
        for row in reader:
            #その行のstatus列だけを取り出す
            status = row["status"]
            #"status"=出てきた回数、{"status":回数}になるように計算処理
            result[status] = result.get(status, 0) + 1

    return result


def main():
    file_path = "data/sample.csv"
    result = count_status(file_path)
    print(result)


if __name__ == "__main__":
    main()