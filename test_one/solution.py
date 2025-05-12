# We have forecasts that can come in for different locations at different times
# We want to be able to get the forecast for a specific location and time

def main():
    """Many ways to do this just here is one version"""
    # Example forecast data
    forecasts = [
        {"location": "FCRN", "time": "2025-10-01T05:00:00Z", "value": 1000},
        {"location": "SPP", "time": "2025-10-01T05:00:00Z", "value": 2000},
        {"location": "WAPA", "time": "2025-10-02T05:00:00Z", "value": 1500},
        {"location": "WAPA", "time": "2025-10-02T10:00:00Z", "value": 150000},
    ]

    forecasts_path = "test_one/testing_forecast_csv.csv"
    import pandas as pd
    # Read the CSV file into a DataFrame
    df = pd.read_csv(forecasts_path)
    # Display the DataFrame
    print("Forecast DataFrame:")
    df["forecast_load"] = df["forecast_load"].astype(float).round(2)


    print(df)



    # Get forecast for WAPA from 5 AM
    wapa_forecast = list(filter(lambda x: x["location"] == "WAPA" and x["time"] == "2025-10-02T05:00:00Z", forecasts))
    print("WAPA Forecast at 5 AM:", wapa_forecast)

    # Get the most recent forecast from all locations
    most_recent_forecast = max(forecasts, key=lambda x: x["time"])
    print("Most Recent Forecast:", most_recent_forecast)

    # Get the most recent forecast from WAPA
    wapa_forecasts = list(filter(lambda x: x["location"] == "WAPA", forecasts))
    most_recent_wapa_forecast = max(wapa_forecasts, key=lambda x: x["time"])
    print("Most Recent WAPA Forecast:", most_recent_wapa_forecast)

    # Convert WAPA's value from watts to kilowatts
    forecasts_in_kw = list(map(lambda x: {**x, "value": x["value"] / 1000} if x["location"] == "WAPA" else x, forecasts))
    print("Forecasts with WAPA in kW:", forecasts_in_kw)

    print("You got this!")

if __name__ == "__main__":
    main()


