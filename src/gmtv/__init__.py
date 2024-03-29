from src.gmtv import donwload
from src.gmtv import processor


def run(hash, output="output.webm"):
    deskshare_input = donwload.deskshare(hash)
    webcams_input = donwload.webcams(hash)
    processor.run(deskshare_input, webcams_input, output)
