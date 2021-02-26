import pandas as pd

def label_rows(data):
    labeled_data = []
    for i in data.index.to_list():
        print("feedback: {}".format(data.loc[i].text))
        category = input("keyword: ")
        sentiment = int(input("sentiment [-1, 1]: "))

        if sentiment not in (-1, 1):
            with open("last_index_used.txt", "w") as file:
                file.write(str(i))
            file.close()

            raise AssertionError("sentiment has to be either negative (-1) or positive (1)")

        labeled_data.append([data.loc[i].text, category, sentiment])
        print("\n")

    df = pd.DataFrame(labeled_data,
        columns=["text_orig", "category", "sentiment"]
        )

    return df
