from homeassistant.core import HomeAssistant # type: ignore
from homeassistant.helpers.typing import ConfigType # type: ignore

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Brewing Monitor integration."""
    # Setup code for your integration goes here
    return True
