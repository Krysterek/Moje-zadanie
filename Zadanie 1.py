print("Lista zakupów")

shopping = {"piekarnia": "chleb, bułki, pączek", "warzywniak": "marchew, seler, rukola"}
shopping_dict = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
    }
for key in shopping:
    list = shopping[key]
    print("Idę do:", key.capitalize(),"i kupuję tu następujące rzeczy", list.title())