from PIL import Image
import piexif
import datetime

# Neues Bild erstellen
img = Image.new("RGB", (640, 480), color=(0, 255, 213))

# EXIF-Daten definieren
exif_dict = {
    "0th": {
        piexif.ImageIFD.Make: u"BylickiLabs",
        piexif.ImageIFD.Model: u"Github.com/bylickilabs",
        piexif.ImageIFD.Software: u"Engine 1.0",
    },
    "Exif": {
        piexif.ExifIFD.DateTimeOriginal: datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S"),
    },
    "GPS": {
        piexif.GPSIFD.GPSLatitudeRef: b"N",
        piexif.GPSIFD.GPSLatitude: [(50, 1), (56, 1), (0, 1)],
        piexif.GPSIFD.GPSLongitudeRef: b"E",
        piexif.GPSIFD.GPSLongitude: [(6, 1), (57, 1), (0, 1)],
    }
}

exif_bytes = piexif.dump(exif_dict)
img.save("bylickilabs.jpg", "jpeg", exif=exif_bytes)
print("[OK] bylickilabs.jpg erfolgreich gespeichert.")
