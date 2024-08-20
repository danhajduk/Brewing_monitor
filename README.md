
# Brewing Monitor

**Brewing Monitor** is a custom Home Assistant integration that provides a set of sensors to monitor various aspects of the brewing and fermentation process. This integration is designed to give homebrewers real-time insights into their brewing environment.

## Features

- **Alcohol By Volume (ABV)**: Measures the alcohol content of the brew.
- **Brewing Temperature**: Monitors the temperature during the brewing process.
- **Fermentation Temperature**: Monitors the temperature during the fermentation process.
- **Ambient Temperature**: Monitors the ambient temperature where brewing/fermentation occurs.
- **Fermentation Duration**: Tracks the duration of the fermentation process.
- **Current Phase**: Indicates the current phase of the brewing or fermentation process.
- **Gravity Trend**: Tracks the trend in gravity readings over time, useful for monitoring fermentation progress.
- **Current Gravity**: Measures the specific gravity of the brew, used to calculate ABV and monitor fermentation progress.
- **Version**: Indicates the current version of the Brewing Monitor integration.

## Installation

1. **Download the Integration:**
   - Download the `brewing_monitor` directory and place it in your `custom_components` directory in your Home Assistant configuration folder.

2. **Configure Home Assistant:**
   - Add the following to your `configuration.yaml` file to enable debugging if needed:
   ```yaml
   logger:
     default: warning
     logs:
       custom_components.brewing_monitor: debug
   ```

3. **Restart Home Assistant:**
   - After placing the integration in the correct folder, restart Home Assistant to load the new integration.

4. **Add the Integration:**
   - Go to **Settings > Devices & Services > Add Integration** and search for "Brewing Monitor". Follow the prompts to complete the setup.

## Sensors Provided

The following sensors are provided by the Brewing Monitor integration:

1. **Alcohol By Volume (ABV)**
   - **Name:** `sensor.alcohol_by_volume`
   - **Description:** Measures the alcohol content of the brew.

2. **Brewing Temperature**
   - **Name:** `sensor.brewing_temperature`
   - **Description:** Monitors the temperature during the brewing process.
   - **Device Class:** `temperature`
   - **Unit:** Celsius (or Fahrenheit)

3. **Fermentation Temperature**
   - **Name:** `sensor.fermentation_temperature`
   - **Description:** Monitors the temperature during the fermentation process.
   - **Device Class:** `temperature`
   - **Unit:** Celsius (or Fahrenheit)

4. **Ambient Temperature**
   - **Name:** `sensor.ambient_temperature`
   - **Description:** Monitors the ambient temperature where brewing/fermentation occurs.
   - **Device Class:** `temperature`
   - **Unit:** Celsius (or Fahrenheit)

5. **Fermentation Duration**
   - **Name:** `sensor.fermentation_duration`
   - **Description:** Tracks the duration of the fermentation process.

6. **Current Phase**
   - **Name:** `sensor.current_phase`
   - **Description:** Indicates the current phase of the brewing or fermentation process.

7. **Gravity Trend**
   - **Name:** `sensor.gravity_trend`
   - **Description:** Tracks the trend in gravity readings over time, useful for monitoring fermentation progress.

8. **Current Gravity**
   - **Name:** `sensor.current_gravity`
   - **Description:** Measures the specific gravity of the brew, used to calculate ABV and monitor fermentation progress.

9. **Version**
   - **Name:** `sensor.brewing_monitor_version`
   - **Description:** Indicates the current version of the Brewing Monitor integration.

## Configuration

- **Unique IDs:** Each sensor is assigned a unique ID, allowing Home Assistant to track and manage the sensors across updates and restarts.
- **Device Info:** Sensors are associated with a "Brewing Monitor" device in Home Assistant, which consolidates the sensors under one device for easy management.

## Development and Contributions

If you'd like to contribute to the development of the Brewing Monitor integration, feel free to fork the repository and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
