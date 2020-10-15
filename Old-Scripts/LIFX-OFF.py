# Get API Key Here: https://cloud.lifx.com/settings
# Get Scene UUID Here: https://api.developer.lifx.com/docs/activate-scene
import pifx

p = pifx.PIFX(api_key='cf63ed4685e0d94bc6d4c617e6716d9dc8a3978847c9fe434f805b7330233ab1')

p.toggle_power()
