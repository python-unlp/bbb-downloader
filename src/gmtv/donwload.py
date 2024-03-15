import requests
import os
import tempfile


def deskshare(hash):
    deskshare_url = f"https://bigbluebutton.linti.unlp.edu.ar/presentation/{hash}/deskshare/deskshare.webm"
    print("⬇️  Start donwloading deskshare file!")
    return do_request(deskshare_url, "deskshare")


def webcams(hash):
    webcams_url = f"https://bigbluebutton.linti.unlp.edu.ar/presentation/{hash}/video/webcams.webm"
    print("⬇️  Start donwloading webcams file!")
    return do_request(webcams_url, "webcams")


def do_request(url, name):
    try:
        response = requests.get(url)
        response.raise_for_status()

        file_extension = os.path.splitext(url)[1]
        tmp_dir = tempfile.mkdtemp()
        tmp_file_path = os.path.join(tmp_dir, f"{name}{file_extension}")

        with open(tmp_file_path, "wb") as tmp_file:
            tmp_file.write(response.content)

        print(f"💾 File downloaded to: {tmp_file_path}")

        return tmp_file_path
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading the file: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
