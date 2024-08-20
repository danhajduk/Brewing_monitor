import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import entity_registry
from homeassistant.const import ENTITY_MATCH_ALL
from .const import DOMAIN

@callback
def configured_instances(hass):
    """Return a set of configured Brewing Monitor instances."""
    return set(entry.title for entry in hass.config_entries.async_entries(DOMAIN))

class BrewingMonitorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Brewing Monitor."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            if user_input["name"] in configured_instances(self.hass):
                errors["base"] = "name_exists"
            else:
                # Store the name and proceed to the entity selection step
                self.name = user_input["name"]
                return await self.async_step_select_entity()

        data_schema = vol.Schema(
            {
                vol.Required("name", default="Brewing Monitor"): str
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )

    async def async_step_select_entity(self, user_input=None):
        """Allow the user to select an entity for Current Gravity."""
        entity_registry_obj = await entity_registry.async_get_registry(self.hass)
        entities = [entity.entity_id for entity in entity_registry_obj.entities.values()]

        data_schema = vol.Schema(
            {
                vol.Required("current_gravity_entity", default=ENTITY_MATCH_ALL): vol.In(entities)
            }
        )

        if user_input is not None:
            # Save the selected entity and create the config entry
            return self.async_create_entry(title=self.name, data=user_input)

        return self.async_show_form(
            step_id="select_entity", data_schema=data_schema
        )
