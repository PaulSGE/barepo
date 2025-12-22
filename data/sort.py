import pandas as pd

neue_spaltennamen = [
    'ev_id', 'ev_model', 'range_km', 'charge',
    'start_date', 'start_time', 'end_date', 'end_time',
    'period', 'day', 'trip_km', 'trip_miles',
    'pickup', 'dropoff', 'fare', 'trip_total'
]

input_dateien = ['september_0.csv', 'september_1.csv', 'september_2.csv']
output_datei = 'FordFocus_100.csv'
such_wort = 'Ford_Focus'
such_spalte_index = 1

alle_gefilterten_daten = []

for datei_name in input_dateien:
    try:
        df = pd.read_csv(datei_name, header=None)

        if len(df.columns) == len(neue_spaltennamen):
            df.columns = neue_spaltennamen

        spalten_daten = df.iloc[:, such_spalte_index]
        filter_maske = spalten_daten.astype(str).str.contains(such_wort, case=False, na=False)
        gefilterter_df = df[filter_maske]
        alle_gefilterten_daten.append(gefilterter_df)
    except FileNotFoundError:
        print(f"Datei '{datei_name}' wurde nicht gefunden und übersprungen.")

if alle_gefilterten_daten:
    gesamt_df = pd.concat(alle_gefilterten_daten, ignore_index=True)

    gesamt_df.columns = neue_spaltennamen

    gesamt_df.to_csv(output_datei, index=False, header=True)

    print(f"Die Filterung über alle Dateien ist abgeschlossen.")
    print(f"Es wurden {len(gesamt_df)} Zeilen in die Datei '{output_datei}' kopiert, einschließlich der Header-Zeile.")
else:
    print("Es wurden keine Daten gefunden")