"""Constants for MCP23017 integration."""
DOMAIN = "mcp23017"

MODE_UP = "UP"
MODE_DOWN = "NONE"

CONF_I2C_ADDRESS = "i2c_address"
CONF_PINS = "pins"

CONF_INVERT_LOGIC = "invert_logic"
CONF_PULL_MODE = "pull_mode"

CONF_FLOW_PLATFORM = "platform"
CONF_FLOW_PIN_NUMBER = "pin_number"
CONF_FLOW_PIN_NAME = "pin_name"

DEFAULT_SCAN_RATE = 0.1  # seconds
DEFAULT_I2C_BUS = 1  # use /dev/i2c-{DEFAULT_I2C_BUS}
DEFAULT_I2C_ADDRESS = 0x20

DEFAULT_INVERT_LOGIC = False
DEFAULT_PULL_MODE = MODE_UP
