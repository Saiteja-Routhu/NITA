import struct
import pvporcupine
import pyaudio


hotword_path = r"C:\Users\saite\NITA\NITA\models\hey-nita.ppn"
access_key = "716/SO7Ctaa5KO5veGMsSXYSqaUX2UriRWp8WdRNmmsTueshgQakxA=="


def listen_for_hotword():
    """Listen for the 'Hey NITA' hotword."""
    porcupine = None
    pa = None
    audio_stream = None

    try:
        porcupine = pvporcupine.create(
            access_key=access_key,
            keyword_paths=[hotword_path]
        )

        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("Listening for 'Hey NITA' hotword...")
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Hotword detected!")
                return True
    except KeyboardInterrupt:
        print("Stopping hotword detection.")
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()
