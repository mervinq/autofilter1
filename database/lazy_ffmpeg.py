import time
import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def fix_thumb(c_thumb):
    width = 0
    height = 0
    try:
        if c_thumb is not None:
            metadata = extractMetadata(createParser(c_thumb))
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")
                Image.open(c_thumb).convert("RGB").save(c_thumb)
                img = Image.open(c_thumb)
                img.resize((320, height))
                img.save(c_thumb, "JPEG")
    except Exception as e:
        print(e)
        c_thumb = None

    return width, height, c_thumb

async def take_screen_shot(video_file, output_directory, ttl):
    output_file_name = f"{output_directory}/{time.time()}.jpg"
    file_generator_command = [
        "ffmpeg",
        "-ss",
        str(ttl),
        "-i",
        video_file,
        "-vframes",
        "1",
        output_file_name
    ]
    process = await asyncio.create_subprocess_exec(
        *file_generator_command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    error_response = stderr.decode().strip()
    terminal_response = stdout.decode().strip()
    if os.path.lexists(output_file_name):
        return output_file_name
    return None
