from API.search import image

def main():
    titel = image("らぶいーず pc壁紙") # ここに検索したい画像のタイトルを入れる image.get_image(titel)
    image.get_image(titel)

if __name__ == "__main__":
    main()