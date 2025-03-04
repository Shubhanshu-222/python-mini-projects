import imageio.v2 as imageio
from PIL import Image, ImageDraw, ImageFont
import glob
import os

# ========== CUSTOMIZATION SETTINGS ==========
desired_size = (500, 500)  # Resize all images to this resolution
gif_duration = 1.0  # Time each frame is displayed (in seconds)
loop_count = 0  # 0 = Infinite loop, Any other number = number of loops
reverse_gif = False  # Set to True to reverse the GIF order
add_text_overlay = True  # Set to True to add a watermark/text overlay
output_filename = "customized_gif.gif"  # Output GIF filename
font_path = "arial.ttf"  # Change to a valid font path if needed
text_content = "Shubhanshu"  # Text to overlay
text_position = (20, 20)  # Text position (x, y)
text_color = "white"  # Text color

# ========== FETCH IMAGES ==========
image_files = sorted(glob.glob("images/*.jpg"))  # Change to your folder path

# Reverse frames if enabled
if reverse_gif:
    image_files.reverse()

# ========== CREATE GIF ==========
with imageio.get_writer(output_filename, mode="I", duration=gif_duration, loop=loop_count) as writer:
    for filename in image_files:
        image = Image.open(filename).convert("RGBA")  # Convert to RGBA for transparency
        image = image.resize(desired_size, Image.LANCZOS)  # Resize with best quality

        # Apply Text Overlay / Watermark
        if add_text_overlay:
            draw = ImageDraw.Draw(image)
            try:
                font = ImageFont.truetype(font_path, 30)  # Load font
            except:
                font = ImageFont.load_default()  # Fallback font

            draw.text(text_position, text_content, fill=text_color, font=font)

        # Save temporarily and read again
        temp_filename = "temp_resized.png"
        image.save(temp_filename)

        # Add to GIF
        writer.append_data(imageio.imread(temp_filename))

# Cleanup temp files
if os.path.exists("temp_resized.png"):
    os.remove("temp_resized.png")

print(f"GIF '{output_filename}' created successfully with custom settings!")
