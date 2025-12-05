from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hidden Fees Explainer API is running!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "uploaded"}

@app.post("/extract")
async def extract_text():
    return {"message": "OCR endpoint placeholder"}

@app.post("/analyze")
async def analyze_fees():
    return {"message": "Analysis endpoint placeholder"}
