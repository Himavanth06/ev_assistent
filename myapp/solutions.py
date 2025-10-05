# myapp/solutions.py

SOLUTIONS = {
    # ---------------- Battery ----------------
    ("battery", "battery not charging"): {
    "steps": [
        "Ensure the charger and power source are functional.",
        "Check that the battery is correctly seated and locked in place.",
        "Inspect the battery connectors and dock for dust or moisture — clean with a dry cloth.",
        "Press and hold the battery power button for 2 seconds before charging.",
        "If LEDs show fault (red blinking), swap the battery at the nearest SUN Mobility station."
    ],
    "steps_audio": "solutions/battery_not_charging_steps.mp3",#done
    "video": "solutions/battrynotcharging.mp4",
    "voice": "solutions/battery_not_charging.mp3"
},

("battery", "range drops suddenly"): {
    "steps": [
        "Check tyre pressure — Front: 25 psi, Rear: 33 psi.",
        "Avoid Turbo mode; use Eco mode for longer range.",
        "Avoid carrying heavy loads or riding uphill continuously.",
        "Ensure smooth acceleration and braking for optimal energy use.",
        "Check battery health in the scooter app or swap at a SUN Mobility station if old."
    ],
    "steps_audio": "solutions/range_drop_steps.mp3",
    "video": "solutions/battryrangedrop.mp4",
    "voice": "solutions/range_drop.mp3"
},

("battery", "battery heating up"): {
    "steps": [
        "Turn off the scooter and allow the battery to cool down.",
        "Avoid parking or charging in direct sunlight.",
        "Do not continue riding if temperature exceeds 50°C.",
        "After cooling, restart with the physical key.",
        "If the issue repeats, swap the battery at a SUN Mobility station."
    ],
    "steps_audio": "solutions/battery_hot_steps.mp3",
    "video": "solutions/battery_hot.mp4",
    "voice": "solutions/battery_hot.mp3"
},

    # ---------------- Motor ----------------
    ("motor", "motor making noise"): {
    "steps": [
        "Ensure there are no loose bolts or mounting parts around the motor housing.",
        "Check if any debris, mud, or stones are caught near the rear wheel or hub motor.",
        "Inspect brake pads to ensure they’re not rubbing continuously on the disc.",
        "Avoid aggressive acceleration if the sound changes with speed.",
        "If the noise persists, visit the nearest authorized service center for inspection."
    ],
    "steps_audio": "solutions/motor_noise_steps.mp3",
    "image": "solutions/motor_noise.png",
    "video": "solutions/motor_noise.mp4",
    "voice": "solutions/motor_noise.mp3",
},

("motor", "motor not responding"): {
    "steps": [
        "Ensure the Kill Switch is turned ON and the scooter is not in Park mode.",
        "Check the dashboard for any fault codes — especially 12C2 or 12C3 (motor start or lock issue).",
        "Inspect motor wiring and connectors near the hub for looseness or damage.",
        "Turn off the scooter, wait 10 seconds, and restart with the physical key.",
        "If still unresponsive, contact service support or visit a SUN Mobility center."
    ],
    "steps_audio": "solutions/motor_off_steps.mp3",
    "image": "solutions/motor_off1.png",
    "video": "solutions/motor_off1.mp4",
    "voice": "solutions/motor_off.mp3",
},

("motor", "motor overheating"): {
    "steps": [
        "Stop the scooter immediately and park it safely in shade.",
        "Let the motor cool for at least 10–15 minutes before restarting.",
        "Avoid riding in Turbo mode or uphill for long durations.",
        "Check that no mud or debris is blocking air ventilation near the motor area.",
        "If the issue continues or DTC 12C5 appears, contact service for cooling inspection."
    ],
    "steps_audio": "solutions/motor_overheat_steps.mp3",
    "image": "solutions/motor_overheat.png",
    "video": "solutions/motor_overheat.mp4",
    "voice": "solutions/motor_overheat.mp3",
},

    # ---------------- Brake ----------------
    ("brake", "brake stuck"): {
    "steps": [
        "Check if the brake lever returns smoothly after pressing.",
        "Ensure there is no mud or rust around the brake caliper or disc area.",
        "Gently move the scooter back and forth to release pressure if the wheel is jammed.",
        "Lubricate lever joints and pivot points lightly if motion feels stiff.",
        "If still stuck, avoid riding and contact the service center for brake bleeding or pad replacement."
    ],
    "steps_audio": "solutions/brake_stuck_steps.mp3",
    "image": "solutions/brake_stuck.png",
    "video": "solutions/brake_stuck.mp4",
    "voice": "solutions/brake_stuck.mp3",
},

("brake", "brake lever loose"): {
    "steps": [
        "Inspect brake fluid level in the reservoir — it should be above the lower mark.",
        "Tighten any loose bolts on the lever or handlebar mount.",
        "Check hydraulic lines for leakage or air bubbles.",
        "Top up using only DoT-4 or DoT-3 brake fluid if needed.",
        "Test the brake at low speed before regular use; if still soft, contact service."
    ],
    "steps_audio": "solutions/brake_loose_steps.mp3",
    "image": "solutions/brake_loose.png",
    "video": "solutions/brake_loose.mp4",
    "voice": "solutions/brake_loose.mp3",
},

    # ---------------- Temperature ----------------
    ("scooter overheating", "temperature"): {
        "steps": [
            "Turn off scooter and let it cool.",
            "Avoid charging in hot environments.",
            "Contact service if problem persists."
        ],
        "steps_audio": "solutions/temp_overheat_steps.mp3",
        "image": "solutions/temp_overheat.png",
        "video": "solutions/temp_overheat.mp4",
        "voice": "solutions/temp_overheat.mp3",
    },

    # ---------------- General / Misc ----------------
    ("scooter overheating", "temperature"): {
    "steps": [
        "Turn off the scooter immediately and move it to a shaded area.",
        "Allow both battery and motor to cool naturally — do not pour water.",
        "Avoid charging or riding until temperature drops below normal.",
        "Check that air vents near the motor and battery dock are not blocked.",
        "If overheating occurs repeatedly, visit an authorized service center."
    ],
    "steps_audio": "solutions/temp_overheat_steps.mp3",
    "image": "solutions/temp_overheat.png",
    "video": "solutions/temp_overheat.mp4",
    "voice": "solutions/temp_overheat.mp3",
},

# ---------------- General / Misc ----------------
("general", "scooter not starting"): {
    "steps": [
        "Ensure the Kill Switch is ON and the scooter is in ‘Ready’ mode.",
        "Check that the battery is properly locked and dashboard shows SOC percentage.",
        "Turn the key OFF and ON again to reset the controller.",
        "Check fuses (60A main, 7.5A DIU, 20A AUX) for damage and replace if necessary.",
        "If the issue persists, note any DTC code on the display and contact service support."
    ],
    "steps_audio": "solutions/scooter_off_steps.mp3",
    "image": "solutions/scooter_off.png",
    "video": "solutions/scooter_off.mp4",
    "voice": "solutions/scooter_off.mp3",
},

("general", "warning lights on"): {
    "steps": [
        "Check the dashboard display for any active fault codes (e.g., 12C5, 1010, 1400).",
        "Note the error code shown in the scrolling window at the bottom of the screen.",
        "Restart the scooter using the physical key to clear temporary warnings.",
        "If the warning persists, refer to the manual section on DTC codes or contact service.",
        "Avoid riding with flashing fault lights until the issue is resolved."
    ],
    "steps_audio": "solutions/warning_light_steps.mp3",
    "image": "solutions/warning_light.png",
    "video": "solutions/warning_light.mp4",
    "voice": "solutions/warning_light.mp3",
},
}



def get_solution(problem_type, major_problem):
    """Normalize keys before lookup."""
    if not problem_type or not major_problem:
        return None
    key = (str(problem_type).strip().lower(), str(major_problem).strip().lower())
    return SOLUTIONS.get(key)
