
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS
from homeassistant.components.sensor import SensorDeviceClass
from .const import DOMAIN, DEVICE_INFO

VERSION = "0.0.1"

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Brewing Monitor sensors from a config entry."""
    sensors = [
        BrewingMonitorSensor(entry, "Brewing Temp", SensorDeviceClass.TEMPERATURE, "temperature"),
        BrewingMonitorSensor(entry, "Fermenting Temp", SensorDeviceClass.TEMPERATURE, "temperature"),
        BrewingMonitorSensor(entry, "Ambient Temp", SensorDeviceClass.TEMPERATURE, "temperature"),
        BrewingMonitorSensor(entry, "Current Gravity", None, "gravity"),
        BrewingMonitorSensor(entry, "Current Phase", None, "phase")
    ]
    async_add_entities(sensors)

class BrewingMonitorSensor(SensorEntity):
    """Representation of a Brewing Monitor sensor."""

    def __init__(self, entry, sensor_type, device_class, sensor_category):
        """Initialize the sensor."""
        self._attr_name = f"{sensor_type}"
        self._attr_unique_id = f"{entry.entry_id}_{sensor_type.lower().replace(' ', '_')}"
        self._sensor_type = sensor_type
        self._sensor_category = sensor_category
        self._attr_device_info = DEVICE_INFO
        self._attr_device_class = device_class
        self._attr_state = None
        self._current_gravity_entity = entry.data.get("current_gravity_entity")

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._attr_state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        if self._sensor_category == "temperature":
            return TEMP_CELSIUS
        elif self._sensor_category == "gravity":
            return "SG"  # Specific Gravity
        elif self._sensor_category == "phase":
            return None  # Phase might be a string value
        return None

    def update(self):
        """Update the sensor state."
        if self._sensor_category == "gravity":
            self._attr_state = self.hass.states.get(self._current_gravity_entity).state
