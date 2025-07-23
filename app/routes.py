from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import Optional, Literal, List
from pydantic import BaseModel
from app.utils import (
    scramble_text_basic,
    scramble_text_seeded,
    caesar_cipher,
    caesar_decipher,
    rot13,
    reverse_text,
    pig_latin,
    vigenere_cipher,
    base64_encode,
    base64_decode,
    morse_encode,
    morse_decode,
    binary_encode,
    binary_decode,
    leet_speak,
    synonym_replace,
    emoji_replace
)

router = APIRouter()

SCRAMBLE_MODELS = Literal[
    'basic', 'seeded', 'caesar', 'rot13', 'reverse', 'piglatin',
    'vigenere', 'base64', 'morse', 'binary', 'leet', 'synonym', 'emoji'
]

class TextInput(BaseModel):
    text: str
    model: SCRAMBLE_MODELS
    shift: Optional[int] = 3
    seed: Optional[int] = 42
    keyword: Optional[str] = "secret"  # For vigenere

class BatchInput(BaseModel):
    texts: List[str]
    model: SCRAMBLE_MODELS
    shift: Optional[int] = 3
    seed: Optional[int] = 42
    keyword: Optional[str] = "secret"

def apply_scrambler(text: str, model: str, shift: int = 3, seed: int = 42, keyword: str = "secret"):
    try:
        match model:
            case "basic":
                return scramble_text_basic(text)
            case "seeded":
                return scramble_text_seeded(text, seed)
            case "caesar":
                return caesar_cipher(text, shift)
            case "rot13":
                return rot13(text)
            case "reverse":
                return reverse_text(text)
            case "piglatin":
                return pig_latin(text)
            case "vigenere":
                return vigenere_cipher(text, keyword)
            case "base64":
                return base64_encode(text)
            case "morse":
                return morse_encode(text)
            case "binary":
                return binary_encode(text)
            case "leet":
                return leet_speak(text)
            case "synonym":
                return synonym_replace(text)
            case "emoji":
                return emoji_replace(text)
            case _:
                raise ValueError("Unsupported scramble model")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Scrambling failed: {str(e)}")

@router.post("/scramble")
def scramble(input: TextInput):
    result = apply_scrambler(
        text=input.text,
        model=input.model,
        shift=input.shift,
        seed=input.seed,
        keyword=input.keyword
    )
    return {
        "model": input.model,
        "original": input.text,
        "scrambled": result
    }

@router.post("/scramble/batch")
def scramble_batch(input: BatchInput):
    results = [
        {
            "original": text,
            "scrambled": apply_scrambler(
                text, input.model, input.shift, input.seed, input.keyword
            )
        }
        for text in input.texts
    ]
    return {"model": input.model, "results": results}

@router.post("/scramble/upload")
async def scramble_file(
    model: SCRAMBLE_MODELS,
    shift: Optional[int] = 3,
    seed: Optional[int] = 42,
    keyword: Optional[str] = "secret",
    file: UploadFile = File(...)
):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are supported")

    contents = await file.read()
    try:
        text = contents.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File must be UTF-8 encoded text.")

    scrambled = apply_scrambler(text, model, shift, seed, keyword)
    return {
        "filename": file.filename,
        "model": model,
        "scrambled": scrambled
    }

@router.post("/encrypt")
def encrypt(input: TextInput):
    encrypted = caesar_cipher(input.text, shift=input.shift)
    return {
        "original": input.text,
        "encrypted": encrypted
    }

@router.post("/decrypt")
def decrypt(input: TextInput):
    decrypted = caesar_decipher(input.text, shift=input.shift)
    return {
        "original": input.text,
        "decrypted": decrypted
    }
