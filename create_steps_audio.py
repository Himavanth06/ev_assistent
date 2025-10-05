# create_steps_audio.py
from gtts import gTTS
import os

# ✅ Define all problems and their steps
steps_dict = {
    "Battery not charging": [
        "Check if the battery is properly connected.",
        "Ensure charger is plugged in and functional.",
        "Restart the scooter if needed."
    ],
    "Range drops suddenly": [
        "Check tire pressure and weight load.",
        "Avoid harsh acceleration.",
        "Check battery health in the scooter app."
    ],
    "Battery heating up": [
        "Turn off the scooter and let it cool.",
        "Avoid charging in hot environments.",
        "Contact service if the problem persists."
    ],
    "Motor making noise": [
        "Check for debris stuck in the motor.",
        "Lubricate the motor bearings if required.",
        "If noise continues, contact service."
    ],
    "Motor not responding": [
        "Check wiring connections to the motor.",
        "Restart the scooter controller.",
        "If still unresponsive, contact service."
    ],
    "Brake stuck": [
        "Check if the brake lever is jammed.",
        "Release pressure slowly.",
        "Lubricate the brake cable if needed."
    ],
    "Brake feels loose": [
        "Tighten the brake lever screw.",
        "Check brake fluid or cable tension.",
        "Contact service if brakes remain ineffective."
    ],
    "Scooter overheating": [
        "Stop the scooter and turn it off.",
        "Let it cool in a shaded area.",
        "Avoid riding on steep slopes continuously."
    ],
    "Motor overheating": [
        "Stop riding immediately.",
        "Check for heavy load or steep incline.",
        "Restart only after motor cools down."
    ],
    "Scooter not starting": [
        "Check if the battery is charged.",
        "Ensure the power button is pressed correctly.",
        "Check the fuse or contact service."
    ],
    "Warning light on dashboard": [
        "Note the warning light symbol.",
        "Check the scooter manual for details.",
        "If unresolved, contact customer support."
    ]
}

# ✅ Output directory for audio files
output_dir = "myapp/static/solutions/"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# ✅ Generate TTS for each problem
for problem, steps in steps_dict.items():
    text = " ".join(steps)  # join steps into a single string
    tts = gTTS(text=text, lang="en")  # change lang="hi"/"kn" for Hindi/Kannada
    safe_name = problem.replace(" ", "_").lower()
    file_path = os.path.join(output_dir, f"{safe_name}_steps.mp3")
    tts.save(file_path)
    print(f"✅ Created steps audio for: {problem} → {file_path}")

print("🎉 All steps audio files generated successfully!")
