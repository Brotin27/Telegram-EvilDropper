import requests


BOT_TOKEN = "8033547455:AAEe6tHnDDW_NXR5a-i6sDL6FrsET9OJGJA"
CHAT_ID = "Enter_your_chat_ID"


html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get it on Google Play</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .app-container {
            background: #fff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 320px;
        }
        .app-logo {
            width: 100px;
            border-radius: 20%;
        }
        .app-title {
            font-size: 22px;
            font-weight: bold;
            margin: 10px 0;
        }
        .app-desc {
            color: #666;
            font-size: 14px;
            margin-bottom: 15px;
        }
        .playstore-badge {
            width: 200px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div class="app-container">
        <img src="https://hackersking.b-cdn.net/Images/icons/apple-touch-icon.png" alt="App Logo" class="app-logo">
        <div class="app-title">Hackersking eLearning</div>
        <div class="app-desc">Learn practical hacking and cybersecurity.</div>
        <a href="https://elearning.hackersking.com" target="https://elearning.hackersking.com">
            <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg" 
                 alt="Get it on Google Play" class="playstore-badge">
        </a>
    </div>

</body>
</html>

"""


html_path = "testv.mp4"
with open(html_path, "w") as file:
    file.write(html_content)


files = {
    "video": (
        "a.htm",
        open(html_path, "rb"),  
        "video/mp4"
    )
}


url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"


data = {"chat_id": CHAT_ID, "supports_streaming": False}
response = requests.post(url, data=data, files=files)

if response.status_code == 200:
    print("message send")
else:
    print(f"Hata: {response.text}")
