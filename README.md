## driver_stress_agent

### Description of the Flowchart (flow.png)

This flowchart represents an **automated driver assistance workflow** designed to respond to stress detection while driving. The process involves multiple steps where a system monitors the driver's state and takes actions based on the detected level of stress. Here’s a breakdown of the flow:

1. Start: 
   The workflow begins by monitoring the driver's condition, specifically looking for signs of stress.

2. Driver State Monitor (Detects Stress):
   The system analyzes the driver's emotional state using sensors (e.g., facial emotion detection or heart rate monitoring) to determine whether the driver is under stress.

3. Is Stress Detected?:
   A decision node evaluates whether stress is detected.
   - If **No** stress is detected, the workflow terminates, leading to the **End**.
   - If **Yes**, the system proceeds to intervene.

4. Machine Response Agent (Dim Display, Lower Volume):
   Upon detecting stress, the system automatically adjusts the car's settings to create a more relaxing environment. It dims the infotainment display and lowers the audio volume to reduce distractions.

5. Voice Interaction Agent (Ask: "Would you like something relaxing?"):
   The system asks the driver if they would like something relaxing, such as music, to help alleviate stress.

6. Driver Response: "Yes" or "No":
   The driver’s response determines the next step.
   - If the response is **No**, the system does nothing further, and the workflow ends.
   - If the response is **Yes**, the system moves to the next step.

7. Personalization Agent (Play Jazz Playlist):
   The system plays a jazz playlist based on the driver’s preferences as a soothing intervention to help reduce stress.

8. End:
   The workflow concludes, either after playing the music or when no further action is required.

**Installation**:

`pip install playsound`
