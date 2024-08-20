import logging
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.const import UnitOfTemperature
from .const import VERSION, DOMAIN

_LOGGER = logging.getLogger(__name__)

SENSOR_TYPES = {
    "abv": "Alcohol By Volume (ABV)",
    "brewing_temperature": "Brewing Temperature",
    "fermentation_temperature": "Fermentation Temperature",
    "ambient_temperature": "Ambient Temperature",
    "fermentation_duration": "Fermentation Duration",
    "current_phase": "Current Phase",
    "gravity_trend": "Gravity Trend",
    "current_gravity": "Current Gravity",
    "version": "Brewing Monitor Version"
}

TEMPERATURE_SENSORS = {
    "brewing_temperature",
    "fermentation_temperature",
    "ambient_temperature"
}

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Brewing Monitor sensors."""
    sensors = [BrewingMonitorSensor(entry, sensor_type) for sensor_type in SENSOR_TYPES]
    async_add_entities(sensors)

class BrewingMonitorSensor(SensorEntity):
    """Representation of a Brewing Monitor Sensor."""

    def __init__(self, entry: ConfigEntry, sensor_type: str):
        """Initialize the sensor."""
        self._entry = entry
        self._sensor_type = sensor_type
        self._attr_name = SENSOR_TYPES.get(sensor_type, "Unknown Sensor")
        self._attr_native_value = self._initialize_sensor_value(sensor_type)
        self._attr_unique_id = f"{DOMAIN}_{entry.entry_id}_{sensor_type}"

        if sensor_type in TEMPERATURE_SENSORS:
            self._attr_device_class = SensorDeviceClass.TEMPERATURE
            self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS  # or UnitOfTemperature.FAHRENHEIT depending on your system

        _LOGGER.debug(f"BrewingMonitorSensor initialized: {self._attr_name} with unique ID: {self._attr_unique_id}")

    def _initialize_sensor_value(self, sensor_type):
        """Initialize the sensor value."""
        if sensor_type == "version":
            return VERSION
        # Add other initialization logic for other sensors if needed
        return None

    @property
    def unique_id(self):
        """Return a unique ID for this sensor."""
        return self._attr_unique_id

    @property
    def device_info(self):
        """Return device information about this sensor."""
        return {
            "identifiers": {(DOMAIN, self._entry.entry_id)},
            "name": "Brewing Monitor",
            "manufacturer": "Custom Components",
            "model": "BrewingSensor",
            "sw_version": VERSION,
        }

    async def async_update(self):
        """Fetch new state data for the sensor."""
        # Add logic to update each sensor's state
        if self._sensor_type == "brewing_temperature":
            self._attr_native_value = self.get_brewing_temperature()
        elif self._sensor_type == "fermentation_temperature":
            self._attr_native_value = self.get_fermentation_temperature()
        elif self._sensor_type == "ambient_temperature":
            self._attr_native_value = self.get_ambient_temperature()
        # Add similar logic for other sensors

    def get_brewing_temperature(self):
        """Simulate fetching the brewing temperature."""
        # Replace with real fetching logic
        return 68.0

    def get_fermentation_temperature(self):
        """Simulate fetching the fermentation temperature."""
        # Replace with real fetching logic
        return 64.0

    def get_ambient_temperature(self):
        """Simulate fetching the ambient temperature."""
        # Replace with real fetching logic
        return 70.0
