import subprocess


def run(deskshare_input, webcams_input, output_path):
    command = [
        "ffmpeg",
        "-y",
        "-i",
        deskshare_input,
        "-i",
        webcams_input,
        "-c:v",
        "libvpx",
        "-crf",
        "30",
        "-b:v",
        "1M",
        "-c:a",
        "copy",
        output_path,
    ]
    subprocess.run(command)
