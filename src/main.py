import csv

#csvファイルを読み込む関数を定義
def read_csv(file_path):
    #file_pathで指定されたファイルをUTF-8で開き、以降fとして使う
    with open(file_path, encoding="utf-8") as f:
        #csvの内容を辞書形式で読めるように変換
        reader = csv.DictReader(f)
        #CSVの1行ずつを順番に取り出して表示
        for row in reader:
            print(row)


def main():
    file_path = "data/sample.csv"
    read_csv(file_path)


if __name__ == "__main__":
    main()