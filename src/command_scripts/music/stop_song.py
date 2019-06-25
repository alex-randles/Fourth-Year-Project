import subprocess
import hotword

def main():
    # completely kill mplayer process
    subprocess.call(["sudo kill -9 $(pgrep mplayer)"], shell=True)
    hotword.detect_hotword()

if __name__ == "__main__":
    main()