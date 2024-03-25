import pandas as pd

df = pd.read_csv('test (2).csv')
df = df.drop(columns=['Suppressed', 'Series_reference', 'STATUS', 'UNITS', 'Magnitude','Subject', 'Group', 'Series_title_1', 'Series_title_3', 'Series_title_4', 'Series_title_5']).dropna()
df.to_csv('test.csv', index=False)


# Charger le fichier (ajustez le chemin et le séparateur selon vos besoins)
df = pd.read_csv('test.csv', sep=',')

# Définir les valeurs à conserver
valeurs_a_conserver = ['Credit', 'Debit', 'Services']

# Filtrer le DataFrame
df_filtre = df[df['Series_title_2'].isin(valeurs_a_conserver)]

# Si vous souhaitez sauvegarder le résultat dans un nouveau fichier
df_filtre.to_csv('test(3).csv', index=False)
