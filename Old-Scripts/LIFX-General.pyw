# Get API Key Here: https://cloud.lifx.com/settings
# Get Scene UUID Here: https://api.developer.lifx.com/docs/activate-scene
import pifx

p = pifx.PIFX(api_key='cf63ed4685e0d94bc6d4c617e6716d9dc8a3978847c9fe434f805b7330233ab1')

p.activate_scene(scene_uuid='f5cbf540-4801-4e6c-9621-98517873e3d3', duration=0.2)
