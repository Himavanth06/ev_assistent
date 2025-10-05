import os
from PIL import Image, ImageDraw, ImageFont
import subprocess

# Folder to create placeholders
base_dir = "myapp/static/solutions"
os.makedirs(base_dir, exist_ok=True)

# List of placeholder files
files = [
    "battery_check", "range_drop", "battery_hot",
    "motor_noise", "motor_off",
    "brake_stuck", "brake_loose",
    "temp_overheat", "motor_overheat",
    "scooter_off", "warning_light"
]

# Create placeholder images
for name in files:
    img_path = os.path.join(base_dir, f"{name}.png")
    if not os.path.exists(img_path):
        img = Image.new("RGB", (640, 480), color=(200, 200, 200))
        d = ImageDraw.Draw(img)
        text = name.replace("_", " ").title()
        try:
            font = ImageFont.truetype("Arial.ttf", 40)
        except:
            font = ImageFont.load_default()
        w, h = d.textsize(text, font=font)
        d.text(((640 - w) / 2, (480 - h) / 2), text, fill=(0, 0, 0), font=font)
        img.save(img_path)
        print(f"Created {img_path}")

# Create placeholder audio (silent .mp3)
for name in files:
    mp3_path = os.path.join(base_dir, f"{name}.mp3")
    if not os.path.exists(mp3_path):
        # 3 seconds of silence
        subprocess.run([
            "ffmpeg", "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
            "-t", "3", mp3_path, "-y"
        ])
        print(f"Created {mp3_path}")

# Create placeholder video (blank .mp4)
for name in files:
    mp4_path = os.path.join(base_dir, f"{name}.mp4")
    if not os.path.exists(mp4_path):
        subprocess.run([
            "ffmpeg", "-f", "lavfi", "-i", "color=c=gray:s=640x480:d=3",
            "-vf", f"drawtext=text='{name.replace('_',' ').title()}':fontcolor=white:fontsize=40:x=(w-text_w)/2:y=(h-text_h)/2",
            "-y", mp4_path
        ])
        print(f"Created {mp4_path}")

print("All placeholders created in myapp/static/solutions/")
