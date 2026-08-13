import requests

# Deployment URL and API key
url = "https://predict-6a7d93e4779f754db6b741bb-dproatj77a-em.a.run.app/predict"
api_key = "ul_8bb10cdd8f7f73a18efdaeafb64176ed0cd1a1e7"

# Optional inference parameters (conf, iou, imgsz)
args = {"conf": 0.25, "iou": 0.7, "imgsz": 640}

with open("image.jpg", "rb") as f:
    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        data=args,
        files={"file": f},
    )

print(response.json())