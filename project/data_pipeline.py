import pandas as pd

def load_data(file_path, date_column_format='%d.%m.%Y'):
    data = pd.read_csv(file_path, sep=';')
    data['date'] = pd.to_datetime(data['Termin'], format=date_column_format)
    return data

def preprocess_weather(weather_data, year):
    filtered_data = weather_data[weather_data['date'].dt.year == year]
    filtered_data = filtered_data.rename(columns={'Termin': 'Date', 'Temperatur-Mittel': 'Temperature average',
                                                  'Niederschlag': 'Precipitation', 'Gesamtschnee': 'Total Snow',
                                                  'Luftdruck': 'Air Pressure'})
    return filtered_data

def preprocess_bike_traffic(bike_data):
    bike_data = bike_data.drop(['uhrzeit_start', 'uhrzeit_ende', 'zaehlstelle', 'richtung_1', 'richtung_2'], axis=1)
    bike_data = bike_data.rename(columns={'datum': 'Date', 'gesamt': 'Total'})
    bike_data['Date'] = pd.to_datetime(bike_data['Date'], format='%Y.%m.%d').dt.strftime('%d.%m.%Y')
    bike_data['Date'] = pd.to_datetime(bike_data['Date'], format='%d.%m.%Y')
    bike_data = bike_data.groupby('Date')['Total'].sum().reset_index()
    return bike_data

def main():
    # Load weather data
    munich_weather = load_data("munich_weather/history_weather_munich.csv")

    # Load bike traffic data
    bike_traffic = load_data("bike_traffic/rad_15min.csv", date_column_format='%Y.%m.%d')

    # Preprocess weather data for a specific year (e.g., 2017)
    munich_2017 = preprocess_weather(munich_weather, year=2017)

    # Preprocess bike traffic data
    preprocessed_bike_traffic = preprocess_bike_traffic(bike_traffic)

    # Filter bike traffic data for dates before '2017-05-31'
    bike_traffic_filtered = preprocessed_bike_traffic[preprocessed_bike_traffic['Date'] < '2017-05-31']

    # Perform further processing or analysis as needed

if __name__ == "__main__":
    main()
