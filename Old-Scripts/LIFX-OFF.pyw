# Get API Key Here: https://cloud.lifx.com/settings
# Get Scene UUID Here: https://api.developer.lifx.com/docs/activate-scene
import pifx

p = pifx.PIFX(api_key='add API key here')

p.toggle_power()
