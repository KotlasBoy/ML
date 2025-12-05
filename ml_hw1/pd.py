import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Data format is
Male,175.34171018344816,78.71803828490611,167/91,279.11818371486874,
25.603762285595344,156.57731630067428,0.7043186405810278,0.5786248104846515,43.926229989441296,
High,Never,Occasional,Low-carb,Hypertension,
None,Hypertension,60.89211411373161,Poor,Insomnia,
8.013912909815714,4.624967546286713,3.745137600727811,High School,High,66

sex, height, weight, blood pressure /, cholesterol,
Body Mass Index, Blood Glucose, Bone Density, Vision Sharpness, Hearing Ability,
Phisical Activity, Smoking status, Alcohol, Diet, Chronic Disease,
Medication use, Family history, Cognitive Function, Mental Health Status, Sleep Patterns,
Stress levels, Pollution exposure, Sun exposure, Education, Income
"""



def main():
    df = pd.read_csv('data.csv')
    print(df.columns.to_list())
    #print(df["Weight (kg)"].mean())

    """all_amount_of_people = df["Gender"].value_counts()
    male_cnt= all_amount_of_people.get('Male')
    female_cnt = all_amount_of_people.get('Female')
    print(f"Соотношение мужчин и женщин в наборе данных: {male_cnt / (male_cnt + female_cnt):.3f} : {female_cnt / (male_cnt + female_cnt):.3f}")"""

    """ df[['sys', 'dias']] = df['Blood Pressure (s/d)'].str.split('/', expand=True).astype(float)
    df["dp mean"] = df["dias"] + (df["sys"] - df["dias"]) / 3
    df_sorted = df.sort_values("Stress Levels", ascending=False)
    top_100_stressed = df_sorted.head(100)
    top_100_calm = df_sorted.tail(100)
    mean_stressed = top_100_stressed["dp mean"].mean()
    mean_calm = top_100_calm["dp mean"].mean()
    print(f"Среднее АД с высоким стрессом:{mean_stressed:.3f}",
            f"Среднее АД с низким стрpессом: {mean_calm:.3f}", sep="\n")"""

    """cholesterol_by_gender = df.groupby("Gender")["Cholesterol Level (mg/dL)"].mean()
    male_cnt = cholesterol_by_gender.get('Male')
    female_cnt = cholesterol_by_gender.get('Female')
    print(f"Male cholestretol level: {male_cnt}",
            f"Female cholesterol level: {female_cnt}",
             f"Отличаются, но не сильно", sep="\n")"""
    
    """women_df = df[df["Gender"] == "Female"]
    young = women_df[women_df["Age (years)"] <= 30]
    old = women_df[women_df["Age (years)"] >= 60]
    young_cog = young["Cognitive Function"].mean()
    old_cog = old["Cognitive Function"].mean()
    print(f"Когнитивные способности в юности: {young_cog}",
            f"Когнитивные способности в возрасте: {old_cog}", sep="\n")"""

    """old_df = df[df["Age (years)"] > 50]
    weight_by_activity = old_df.groupby("Physical Activity Level")["Weight (kg)"].mean()
    print(f"Ppl over 50 with High activity level median weight: {weight_by_activity.get("High"):.3f}",
            f"Ppl over 50 with Moderate activity level median weight: {weight_by_activity.get("Moderate"):.3f}",
            f"Ppl over 50 with Low activity level median weight: {weight_by_activity.get("Low"):.2f}", sep="\n")"""
    
    """min_weight = df.groupby("Income Level")["Weight (kg)"].min()
    print(f"High income level man's min weight: {min_weight.get("High"):.3f} kg",
            f"Low income level man's min weight: {min_weight.get("Low"):.3f} kg", sep="\n")"""
    
    """    high_income = df[df["Income Level"] == "High"]
    low_income = df[df["Income Level"] == "Low"]

    h_i_activity = high_income["Physical Activity Level"].value_counts()
    l_i_activity = low_income["Physical Activity Level"].value_counts()

    print(f"процент людей с высоким заработком и высокой активностью {h_i_activity["High"] / len(high_income) * 100:.3f}",
          f"процент людей с высоким заработком и средней активностью {h_i_activity["Moderate"] / len(high_income) * 100:.3f}",
          f"процент людей с высоким заработком и низкой активностью {h_i_activity["Low"] / len(high_income) * 100:.3f}", sep="\n", end="\n\n")

    print(f"процент людей с низким заработком и высокой активностью {l_i_activity["High"] / len(low_income) * 100:.3f}",
          f"процент людей с низким заработком и средней активностью {l_i_activity["Moderate"] / len(low_income) * 100:.3f}",
          f"процент людей с низким заработком и низкой активностью {l_i_activity["Low"] / len(low_income) * 100:.3f}", sep="\n")
    """


    #print(f"{(h_i_activity.get("High") / high_income.count()[0]):.3f}")
    #  f"{h_i_activity.get("High") / high_income.count()[0]:.3f}") #{h_i_activity.get("Moderate") / high_income.count()[0]:.3f} {h_i_activity.get("Low") / high_income.count()[0]:.3f}")
    #print(high_income.count()[0], low_income.count()[0])
    #print(h_i_activity, l_i_activity, sep="\n\n")


    #sunny_men = df[(df["Gender"] == "Male") & (df["Sun Exposure"] > 5)]
    #a = sunny_men[sunny_men["Income Level"] == "High"]
    #print(f"{len(a) / len(sunny_men):.3f}")


    #bmi_75 = df["BMI"].quantile(0.75)
    #bmi_60 = df["BMI"].quantile(0.60)
    #bmi_30 = df["BMI"].quantile(0.30)
    #high = df[df["BMI"] > bmi_75]
    #middle = df[(df["BMI"] >= bmi_30) & (df["BMI"] < bmi_60)]
    #chronic_high = len(high[high["Chronic Diseases"].notna()])
    #chronic_middle = len(middle[middle["Chronic Diseases"].notna()])
    #print(f"{chronic_high / len(high):.3f}, {chronic_middle / len(middle):.3f}")

    """%matplotlib inline
    v_c = df["Chronic Diseases"].value_counts()
    print(v_c)

    plt.figure(figsize=(10,6))
    v_c.plot(kind="bar")
    plt.title("Частота встречаемых хронических заболеваний")
    plt.ylabel("Кол-во людей")
    plt.xlabel("Заболевания")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()"""

    #%matplotlib inline

    """plt.figure(figsize=(10,6))
    plt.title("Связь собственных когнитивных функций с уровнем стресса")
    plt.xlabel("Уровень стресса")
    plt.ylabel("Оценка когнитивных способностей")

    plt.scatter(df["Stress Levels"], df["Cognitive Function"])
    plt.grid(True)

    line = np.polyfit(df["Stress Levels"], df["Cognitive Function"], 3)
    p = np.poly3d(line)
    plt.plot(df["Stress Levels"], p(df["Stress Levels"]), "r--")
    plt.tight_layout()
    plt.legend()
    plt.show()"""

    """plt.figure(figsize=(10,6))
    plt.title("Зависимость веса от роста человека")
    plt.xlabel("вес")
    plt.ylabel("рост")
    plt.scatter(df["Height (cm)"], df["Weight (kg)"])
    plt.grid(True)

    line = np.polyfit(df["Height (cm)"], df["Weight (kg)"], 1)
    p = np.poly1d(line)
    plt.plot(df["Weight (kg)"], p(df["Weight (kg)"]), "r--")
    plt.tight_layout()
    plt.show()"""

    """plt.figure(figsize=(10,6))
    df.boxplot(column="Stress Levels", by="Income Level", grid=False)
    plt.title('Распределение уровня стресса по уровням дохода')
    plt.suptitle('')  # Убираем автоматический заголовок
    plt.xlabel('Уровень дохода')
    plt.ylabel('Уровень стресса')
    plt.tight_layout()
    plt.show()"""

    """========================================================="""

    #print(np.diag([1, 2, 3, 4], k=-1))
    #squad = np.diag([1, 1])
    #print(np.tile(squad, (2, 2)))
    #print(np.arange("2016-07", "2016-08", dtype="datetime64[D]"))
    #print(np.random.randint(0, 4, (5, 5)))
    #print(np.random.rand(10))
    m = np.random.randint(0, 5, (5, 5))
    print(m)
    n = 3
    indexes = np.argsort(m[:, n])
    print(m[indexes])


if __name__ == "__main__":
    main()