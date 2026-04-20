import webbrowser
import time

youtube_url = "https://www.youtube.com/shorts/kwZAu1YZwa4"

repeats = 10
delay_seconds = 10  # How long to wait before reopening

for i in range(repeats):
    print(f"Opening video - round {i+1}")
    webbrowser.open(youtube_url)
    time.sleep(delay_seconds)
