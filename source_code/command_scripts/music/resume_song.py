import subprocess
import hotword


def pause_song():
    # resume the previously paused mplayer process
    subprocess.call(["kill -CONT $(pgrep mplayer)"], shell=True)
    return None


def main():
    pause_song()
    hotword.detect_hotword()
    

if __name__ == "__main__":
    main()