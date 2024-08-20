
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS
from homeassistant.components.sensor import SensorDeviceClass
from .const import DOMAIN, DEVICE_INFO

VERSION = "0.0.1"

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Brewing Monitor sensors from a config entry."""
    sensors = [
        BrewingMonitorSensor(entry, "Brewing Temp", SensorDeviceClass.TEMPERATURE),
        BrewingMonitorSensor(entry, "Fermenting Temp", SensorDeviceClass.TEMPERATURE),
        BrewingMonitorSensor(entry, "Ambient Temp", SensorDeviceClass.TEMPERATURE)
    ]
    async_add_entities(sensors)

class BrewingMonitorSensor(SensorEntity):
    """Representation of a Brewing Monitor temperature sensor."""

    def __init__(self, entry, sensor_type, device_class):
        """Initialize the sensor."""
        self._attr_name = f"{sensor_type}"
        self._attr_unique_id = f"{entry.entry_id}_{sensor_type.lower().replace(' ', '_')}"
        self._sensor_type = sensor_type
        self._attr_device_info = DEVICE_INFO
        self._attr_device_class = device_class
        self._attr_state = None

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._attr_state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    def update(self):
        """Update the sensor state."""
        # This method should fetch the latest temperature data
        pass
