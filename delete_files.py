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

# Use o caminho da pasta que deseja limpar
folder_audio_path = 'ignored-files/audio'
folder_texts_path = 'ignored-files/texts'
folder_chunk_path = 'ignored-files/audio_chunks'

delete_all_files_in_folder(folder_audio_path)
delete_all_files_in_folder(folder_texts_path)
delete_all_files_in_folder(folder_chunk_path)
