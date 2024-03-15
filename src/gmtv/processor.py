import subprocess


def run(deskshare_input, webcams_input, output_path):
    command = [
        "ffmpeg",
        "-y",
        "-i",
        deskshare_input,
        "-i",
        webcams_input,
        "-c",
        "copy",
        "-strict",
        "experimental",
        output_path,
    ]
    subprocess.run(command)
