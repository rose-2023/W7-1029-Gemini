
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="請產生一道適合 Python 初學者的輸入輸出選擇題，包含 A、B、C、D 四個選項，不要提供答案。"
)

print(response.text)
