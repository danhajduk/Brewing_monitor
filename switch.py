
from homeassistant.components.switch import SwitchEntity
from .const import DOMAIN, DEVICE_INFO

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Brewing Monitor switches from a config entry."""
    switches = [
        BrewingMonitorSwitch(entry, "Start Brewing"),
        BrewingMonitorSwitch(entry, "Start Fermentation")
    ]
    async_add_entities(switches)

class BrewingMonitorSwitch(SwitchEntity):
    """Representation of a Brewing Monitor switch."""

    def __init__(self, entry, name):
        """Initialize the switch."""
        self._attr_name = name
        self._attr_unique_id = f"{entry.entry_id}_{name.lower().replace(' ', '_')}"
        self._attr_device_info = DEVICE_INFO
        self._is_on = False

    @property
    def is_on(self):
        """Return the state of the switch."""
        return self._is_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self._is_on = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        self._is_on = False
        self.schedule_update_ha_state()

    def update(self):
        """Fetch the latest state of the switch."""
        pass
