open("memes_dataset.csv")
ft = open("memes_dataset.csv", encoding="utf-8")

while True:
    next(ft)
    print(ft.readline())