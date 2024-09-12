## driver_stress_agent

1. Installation
`npx n8n`

2. Install small model
`ollama run phi3.5`

3. Flow

   
   
   [Start]
    --> [Driver State Monitor (Detects Stress)]
          |
          v
      [Is Stress Detected?] --No--> [End]
          |
         Yes
          |
          v
[Machine Response Agent (Dim Display, Lower Volume)]
          |
          v
[Voice Interaction Agent (Ask: "Would you like something relaxing?")]
          |
          v
[Driver Response: "Yes" or "No"] --No--> [End]
          |
         Yes
          |
          v
[Personalization Agent (Play Jazz Playlist)]
          |
          v
       [End] 
