from bs4 import BeautifulSoup
import requests
import pandas as pd


major_data = []
degree_type = []
number_data = []
early_career = []
mid_career = []
high_meaning = []


for i in range(1, 35):
    response = requests.get(
        f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{i}"
    )

    soup = BeautifulSoup(response.text, "html.parser")

    table_row = [elements.find_all("tr", class_="data-table__row") for elements in soup.find_all("body")]

    for row in table_row:
        for elements in row:
            major_data.append(elements.find("td", class_="csr-col--school-name")
                              .find("span", class_="data-table__value").getText())
            degree_type.append(elements.find("td", class_="csr-col--school-type")
                               .find("span", class_="data-table__value").getText())
            number_data.append(elements.find_all("td", class_="csr-col--right"))

    for elements in number_data:
        for element in elements:
            if element.find("span", class_="data-table__title").getText() == "Early Career Pay:":
                early_career.append(int(element.find("span", class_="data-table__value").getText().replace(",", "").replace("$", "")))
            elif element.find("span", class_="data-table__title").getText() == "Mid-Career Pay:":
                mid_career.append(int(element.find("span", class_="data-table__value").getText().replace(",", "").replace("$", "")))
            else:
                try:
                    high_meaning.append(int(element.find("span", class_="data-table__value").getText().strip("%"))/100)
                except ValueError:
                    high_meaning.append(None)


pd.set_option('display.max_columns', None)
df = pd.DataFrame.from_dict(
    {"Major": major_data,
     "Degree type": degree_type,
     "Early Career Pay": early_career,
     "Mid-Career Pay": mid_career,
     "High Meaning": high_meaning}, orient="index"
).T


clean_df = df.dropna()


sorted_df = clean_df.sort_values(by=["High Meaning", "Mid-Career Pay"], ascending=[False, True])
print(sorted_df.head())
