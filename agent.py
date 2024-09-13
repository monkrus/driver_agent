import random
import time
from playsound import playsound
import os

# Paths to audio files (replace with actual paths to .mp3/.wav files on your system)
TTS_AUDIO_FILE = 'ask_driver.mp3'  # "Would you like me to play something relaxing?" audio file
JAZZ_PLAYLIST_FILE = 'jazz_playlist.mp3'  # Jazz music file
YES_RESPONSE_FILE = 'yes_response.mp3'  # "Yes" audio file (for simulating the driver’s response)
NO_RESPONSE_FILE = 'no_response.mp3'  # "No" audio file

def play_audio(file_path):
    """Play audio using the playsound library."""
    if os.path.exists(file_path):
        playsound(file_path)
    else:
        print(f"Audio file {file_path} not found, skipping audio simulation.")

def detect_stress():
    """Simulate stress detection using random values."""
    stress_score = random.randint(0, 100)
    print(f"Simulated Stress Score: {stress_score}")
    return stress_score > 70  # Threshold for stress

def control_car_system():
    """Simulate dimming the display and lowering the volume in the car."""
    print("Simulating: Dimming the infotainment display and lowering the volume...")

def ask_driver():
    """Simulate asking the driver if they want something relaxing."""
    print("Simulating: Asking the driver: 'Would you like me to play something relaxing?'")
    play_audio(TTS_AUDIO_FILE)  # Play the TTS simulation audio

def get_driver_response():
    """Simulate voice recognition by randomly selecting 'Yes' or 'No'."""
    response = random.choice(['yes', 'no'])
    print(f"Simulated Driver Response: {response}")
    if response == 'yes':
        play_audio(YES_RESPONSE_FILE)  # Simulate driver saying "Yes"
    else:
        play_audio(NO_RESPONSE_FILE)  # Simulate driver saying "No"
    return response == 'yes'

def play_jazz_playlist():
    """Simulate playing a jazz playlist."""
    print("Simulating: Playing a jazz playlist...")
    play_audio(JAZZ_PLAYLIST_FILE)  # Play the jazz playlist simulation audio

def main():
    """Run the demo simulation."""
    print("Starting the Driver Stress Detection Demo...")
    time.sleep(2)  # Simulate time before detecting stress
    
    # Step 1: Detect stress
    stress_detected = detect_stress()
    
    if stress_detected:
        print("Stress detected!")
        
        # Step 2: Dim display and lower volume
        control_car_system()
        time.sleep(1)  # Simulate car system adjustment time
        
        # Step 3: Ask the driver if they want something relaxing
        ask_driver()
        
        # Step 4: Get driver's response
        if get_driver_response():
            # Step 5: Play a jazz playlist
            play_jazz_playlist()
        else:
            print("Simulating: Driver does not want music.")
    else:
        print("No stress detected.")
    
    print("Demo complete.")

if __name__ == "__main__":
    main()
