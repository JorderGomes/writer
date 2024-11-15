import os

def delete_all_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Removed file: {file_path}")
        except Exception as e:
            print(f"Error removing {file_path}: {e}")

def delete_all():
    folder_audio_path = 'assets/audio'
    folder_chunk_path = 'assets/audio_chunks'
    folder_texts_path = 'assets/texts'

    delete_all_files_in_folder(folder_audio_path)
    delete_all_files_in_folder(folder_chunk_path)
    delete_all_files_in_folder(folder_texts_path)