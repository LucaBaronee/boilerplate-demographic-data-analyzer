import pandas as pd


def calculate_demographic_data(print_data=True):
    # Leemos el archivo CSV y lo cargamos en un DataFrame (tabla de Pandas)
    df = pd.read_csv('adult.data.csv')

    # 1) Contamos cuántas personas hay de cada raza
    race_count = df['race'].value_counts()

    # 2) Filtramos a los hombres, tomamos la edad, sacamos el promedio y redondeamos
    is_male = df['sex'] == 'Male'
    average_age_men = round(df[is_male]['age'].mean(), 1)

    # 3) Porcentaje de personas con Bachelors (el promedio de True/False es la proporción)
    has_bachelors = df['education'] == 'Bachelors'
    percentage_bachelors = round(has_bachelors.mean() * 100, 1)

    # 4) y 5) Separamos a las personas con y sin educación avanzada
    advanced_levels = ['Bachelors', 'Masters', 'Doctorate']
    is_advanced = df['education'].isin(advanced_levels)

    # El símbolo ~ invierte la condición (los que NO tienen educación avanzada)
    higher_education = df[is_advanced]
    lower_education = df[~is_advanced]

    # Porcentaje de cada grupo que gana más de 50K
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # 6) Mínimo de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 7) Filtramos a los que trabajan el mínimo de horas
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    # Porcentaje de ese grupo que gana más de 50K
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8) Cantidad de personas que ganan más de 50K en cada país
    rich_per_country = df[df['salary'] == '>50K']['native-country'].value_counts()

    # Cantidad total de personas en cada país
    total_per_country = df['native-country'].value_counts()

    # Porcentaje de ricos por país (Pandas alinea los países automáticamente al dividir)
    country_percentage = rich_per_country / total_per_country * 100

    # idxmax() devuelve el país con el valor más alto; max() devuelve ese valor
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 9) Filtramos a las personas de India que ganan más de 50K (& = "y", cada condición entre paréntesis)
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    # Contamos las ocupaciones y nos quedamos con la más común
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
