import pygame
import random
import time
import os

# Initialize pygame
pygame.init()

# Initialize pygame mixer for playing sound
pygame.mixer.init()

# Set up the display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Driver Stress Detection Simulation")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)
TRANSPARENT_BLUE = (135, 206, 250, 180)  # Light bluish with transparency

# Paths to audio files (replace with actual paths to .mp3/.wav files on your system)
TTS_AUDIO_FILE = 'audio/play_relaxing.mp3'
JAZZ_PLAYLIST_FILE = 'audio/jazz.wav'
YES_RESPONSE_FILE = 'audio/yes.mp3'
NO_RESPONSE_FILE = 'audio/no.mp3'

def play_audio(file_path):
    """Play audio using pygame mixer."""
    if os.path.exists(file_path):
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except pygame.error as e:
            print(f"Error playing {file_path}: {e}")
    else:
        print(f"Audio file {file_path} not found, skipping audio simulation.")

def detect_stress():
    """Simulate stress detection using random values."""
    stress_score = random.randint(0, 100)
    print(f"Simulated Stress Score: {stress_score}")
    return stress_score

def control_car_system():
    """Simulate dimming the display and lowering the volume in the car."""
    print("Simulating: Dimming the infotainment display and lowering the volume...")

def ask_driver():
    """Simulate asking the driver if they want something relaxing."""
    print("Simulating: Asking the driver: 'Would you like me to play something relaxing?'")
    play_audio(TTS_AUDIO_FILE)

def get_driver_response():
    """Simulate voice recognition by randomly selecting 'Yes' or 'No'."""
    response = random.choices(['yes', 'no'], weights=[0.5, 0.5], k=1)[0]
    print(f"Simulated Driver Response: {response}")
    if response == 'yes':
        play_audio(YES_RESPONSE_FILE)
    else:
        play_audio(NO_RESPONSE_FILE)
    return response == 'yes'

def play_jazz_playlist():
    """Simulate playing a jazz playlist."""
    print("Simulating: Playing a jazz playlist...")
    play_audio(JAZZ_PLAYLIST_FILE)

def draw_stress_meter(stress_score):
    """Draw a stress meter that fills up based on the stress level and show the score."""
    pygame.draw.rect(screen, RED, (50, 100, 200, 20), 2)  # Border of the stress meter
    fill_width = (stress_score / 100) * 200  # Fill based on stress level
    pygame.draw.rect(screen, GREEN, (50, 100, fill_width, 20))  # Filled part

    # Display the stress score as a number
    font = pygame.font.Font(None, 30)
    stress_text = font.render(f"Stress Level: {stress_score}%", True, WHITE)
    screen.blit(stress_text, (50, 130))

def draw_car_display(stress_detected, playing_music):
    """Draw a detailed car dashboard display seen through the eyes of the driver."""
    # Simulate car infotainment screen with transparent bluish color
    infotainment_rect = pygame.Surface((300, 180), pygame.SRCALPHA)  # Transparent screen surface
    infotainment_rect.fill((135, 206, 250, 180))  # Light bluish color with transparency
    screen.blit(infotainment_rect, (400, 100))  # Place it on the main screen

    # Show temperature control (driver side / passenger side)
    draw_text("Temp: 22°C", (420, 120), WHITE, 24)
    
    # Show music status
    if playing_music:
        draw_text("Now Playing:", (420, 160), WHITE, 24)
        draw_text("Jazz Vibes", (420, 190), GREEN, 24)
        draw_music_controls()
    else:
        draw_text("Music Off", (420, 160), WHITE, 24)

    # Show navigation
    draw_text("Navigation:", (420, 230), WHITE, 24)
    pygame.draw.rect(screen, BLUE, (420, 260, 100, 60))  # Simulated map
    draw_text("Route to Home", (530, 260), WHITE, 18)

    # Show icons like Wi-Fi, signal, and battery
    draw_icons()

    # If stress detected, show "Dimming display" message
    if stress_detected:
        dim_rect = pygame.Surface((300, 180), pygame.SRCALPHA)  # Surface for dimming overlay
        dim_rect.fill((100, 100, 100, 150))  # Semi-transparent dimming overlay
        screen.blit(dim_rect, (400, 100))
        draw_text("Dimming Display", (450, 150), WHITE)

def draw_music_controls():
    """Draw music controls (play/pause, volume, progress bar)."""
    # Play/pause button (simple circle as an icon)
    pygame.draw.circle(screen, GREEN, (500, 220), 15)  # Play/pause button
    draw_text("||", (492, 210), WHITE, 20)  # Pause icon (or play triangle)

    # Volume level
    draw_text("Volume:", (540, 220), WHITE, 20)
    pygame.draw.rect(screen, WHITE, (610, 220, 80, 10))  # Volume bar
    pygame.draw.rect(screen, GREEN, (610, 220, 60, 10))  # Volume fill

    # Progress bar for the current track
    pygame.draw.rect(screen, WHITE, (420, 300, 260, 10))  # Progress bar
    pygame.draw.rect(screen, GREEN, (420, 300, 130, 10))  # Progress fill (halfway through the song)

def draw_icons():
    """Draw icons for signal strength, Wi-Fi, and battery."""
    # Signal strength
    pygame.draw.rect(screen, WHITE, (720, 110, 10, 10))  # First bar
    pygame.draw.rect(screen, WHITE, (730, 105, 10, 15))  # Second bar
    pygame.draw.rect(screen, WHITE, (740, 100, 10, 20))  # Third bar
    pygame.draw.rect(screen, WHITE, (750, 95, 10, 25))   # Fourth bar

    # Wi-Fi symbol
    pygame.draw.arc(screen, WHITE, (720, 135, 20, 10), 3.14, 0)  # Wi-Fi curve

    # Battery icon
    pygame.draw.rect(screen, WHITE, (720, 155, 40, 20))  # Battery body
    pygame.draw.rect(screen, GREEN, (722, 157, 30, 16))  # Battery fill
    pygame.draw.rect(screen, WHITE, (760, 160, 5, 10))   # Battery head

def draw_text(text, pos, color=WHITE, font_size=30):
    """Draw text on the screen."""
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

def main():
    """Run the driver stress detection loop with enhanced visualization."""
    print("Starting the Driver Stress Detection Demo...")

    running = True
    clock = pygame.time.Clock()

    # Simulation state variables
    stress_score = 0
    stress_detected = False
    driver_response = None
    playing_music = False

    while running:
        # Event handling (for closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background
        screen.fill(BLACK)

        # Detect stress every few seconds
        if not stress_detected:
            time.sleep(2)
            stress_score = detect_stress()
            stress_detected = stress_score > 50

        # Step 1: Show stress level
        draw_text("Stress Level:", (50, 50))
        draw_stress_meter(stress_score)

        # Step 2: Simulate car display
        draw_car_display(stress_detected, playing_music)

        if stress_detected and not playing_music:
            print("Stress detected!")

            # Step 3: Simulate control of car system
            control_car_system()

            # Step 4: Ask driver
            ask_driver()
            driver_response = get_driver_response()

            if driver_response:
                print("Driver said yes, playing jazz music...")
                draw_text("Playing jazz...", (50, 200))
                play_jazz_playlist()
                playing_music = True
            else:
                print("Driver said no.")
                draw_text("Driver declined music.", (50, 200))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
