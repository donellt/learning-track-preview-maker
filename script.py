from pydub import AudioSegment
import os

def create_preview_files(folder_path):
    # Ensure the folder path ends with a slash
    if not folder_path.endswith('/'):
        folder_path += '/'

    # Create a new folder for previews if it doesn't exist
    previews_folder = folder_path + 'previews/'
    if not os.path.exists(previews_folder):
        os.makedirs(previews_folder)

    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter out only .mp3 and .m4a files
    audio_files = [file for file in files if file.endswith('.mp3') or file.endswith('.m4a')]

    # Print the list of audio files found
    print("Found the following audio files:")
    for audio_file in audio_files:
        print("- " + audio_file)

    for file in audio_files:
        # Load the full audio file
        full_audio = AudioSegment.from_file(folder_path + file)

        # Take the first 30 seconds
        preview_audio = full_audio[:30000]

        # Fade out the last 3 seconds if the audio is longer than 3 seconds
        if len(preview_audio) > 3000:
            preview_audio = preview_audio.fade_out(3000)

        # Export the preview audio with the new name to the previews folder
        preview_file_path = previews_folder + os.path.splitext(file)[0] + '-preview.mp3'
        print("Exporting preview file:", preview_file_path)
        preview_audio.export(preview_file_path, format='mp3')

if __name__ == "__main__":
    folder_path = "fullmixes"
    create_preview_files(folder_path)
