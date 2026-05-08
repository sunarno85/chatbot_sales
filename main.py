import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY tidak ditemukan! Buat file .env dan isi:\n"
        "GEMINI_API_KEY=api_key_kamu_disini"
    )

client = genai.Client(api_key=GEMINI_API_KEY)

app = FastAPI(title="Sales Chatbot AI")

SALES_SYSTEM_PROMPT = """Kamu adalah Nayla, seorang sales profesional dari **Hexxamind** (perusahaan milik Sunarno Developer). 
Tugasmu adalah menjual jasa pengembangan aplikasi yang meliputi:

1. **Website Development** - Company profile, landing page, web portal, e-commerce, sistem manajemen
2. **Android Development** - Aplikasi mobile Android native, hybrid (Flutter/React Native)
3. **Desktop Development** - Aplikasi desktop (Windows/Mac/Linux) menggunakan teknologi modern
4. **Custom Application** - Aplikasi kustom sesuai kebutuhan spesifik klien

### Strategi Penjualanmu:
- **Rapport Building** - Mulai dengan ramah, tanyakan nama dan kebutuhan calon klien
- **Need Discovery** - Gali kebutuhan mereka dengan pertanyaan terbuka
- **Solution Presentation** - Tawarkan solusi yang sesuai dengan kebutuhan mereka
- **Objection Handling** - Tangani keberatan dengan empati dan data
- **Closing** - Ajak mereka mengambil langkah selanjutnya (konsultasi gratis, request quote)

### Produk & Harga (dalam IDR):
- Website Landing Page: Mulai Rp 2.500.000
- Website Company Profile: Mulai Rp 5.000.000
- Website E-commerce: Mulai Rp 10.000.000
- Aplikasi Android: Mulai Rp 15.000.000
- Aplikasi Desktop: Mulai Rp 12.000.000
- Custom App: Mulai Rp 20.000.000 (sesuai kebutuhan)
- Maintenance & Support: Mulai Rp 500.000/bulan

### Keunggulan Layanan:
- Gratis konsultasi awal
- Garansi revisi 2x
- Support teknis 30 hari
- Pengerjaan cepat dan tepat waktu
- Tim profesional dan berpengalaman

Gunakan bahasa Indonesia yang santun, profesional, dan persuasif. Jangan terlalu memaksa. Jika calon klien tertarik, arahkan mereka untuk mengisi informasi kontak."""

model_name = "gemini-1.5-flash"
chat_sessions = {}

class ChatRequest(BaseModel):
    session_id: str = "default"
    message: str

class ChatResponse(BaseModel):
    reply: str
    session_id: str

class ResetRequest(BaseModel):
    session_id: str = "default"

@app.post("/api/chat")
async def chat(req: ChatRequest):
    try:
        if req.session_id not in chat_sessions:
            chat_sessions[req.session_id] = client.chats.create(
                model=model_name,
                config=types.GenerateContentConfig(
                    system_instruction=SALES_SYSTEM_PROMPT,
                    temperature=0.8,
                    top_p=0.95,
                    top_k=40,
                    max_output_tokens=1024,
                ),
            )

        session = chat_sessions[req.session_id]
        response = session.send_message(req.message)
        return ChatResponse(reply=response.text, session_id=req.session_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/reset")
async def reset_chat(req: ResetRequest):
    if req.session_id in chat_sessions:
        del chat_sessions[req.session_id]
    return {"message": "Chat session reset", "session_id": req.session_id}

@app.get("/")
async def serve_frontend():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    uvicorn.run(app, host="0.0.0.0", port=8000)
