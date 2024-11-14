import wave
import struct
import random
import string
import hashlib

headers = {"Content-Type": "application/json"}


def process_audio_data(audio_file):
    # Abre el archivo de audio
    with wave.open(audio_file, "rb") as audio:
        frames = audio.readframes(audio.getnframes())
        audio_hex = struct.unpack(
            f"{audio.getnframes() * audio.getnchannels()}h", frames
        )
        audio_hex_str = "".join(format(sample, "x") for sample in audio_hex)
    return audio_hex_str


def generate_complex_token(hex_str):
    processed_text = ""
    for char in hex_str:
        if char.isalpha():
            # Cambiar aleatoriamente entre minúsculas y mayúsculas
            processed_text += random.choice([char.lower(), char.upper()])
        else:
            # Mantener caracteres no alfabéticos sin cambios
            processed_text += char

    # Agregar caracteres especiales aleatorios para mayor complejidad
    special_characters = string.punctuation + string.digits
    for _ in range(10):
        processed_text += random.choice(special_characters)

    # Calcular el hash SHA-256 del texto procesado
    token = hashlib.sha256(processed_text.encode()).hexdigest()
    return token


def generate_token_from_audio(audio_file):
    # Procesar los datos del audio y obtener la cadena hexadecimal
    audio_hex_str = process_audio_data(audio_file)

    # Generar un token complejo a partir de la cadena hexadecimal
    token = generate_complex_token(audio_hex_str)
    return token
