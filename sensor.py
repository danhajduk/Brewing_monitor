from homeassistant.helpers.entity import Entity

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Brewing Monitor sensor platform."""
    async_add_entities([BrewingTemperatureSensor()])

class BrewingTemperatureSensor(Entity):
    """Representation of a Brewing Monitor Temperature Sensor."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Brewing Temperature"

    @property
    def state(self):
        """Return the state of the sensor."""
        return 20  # Replace with actual temperature reading logic
