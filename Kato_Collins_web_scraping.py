from bs4 import BeautifulSoup
import requests
import json

def species_data(query):
     url = f"https://xeno-canto.org/api/2/recordings?query={query}"
     response = requests.get(url)

     if response.status_code == 200:
         data = response.json()
         species_list = []

         for recording in data['recordings']:
             species_name = recording['en']
             family_name = f"{recording['gen']} {recording['sp']}"
             country = recording['cnt']

             # Append the information to the list in the form of a dictionary.
             species_list.append({
                 'species_name': species_name,
                 'family_name': family_name,
                 'country': country,
             })

         return species_list
     else:
         print(f"Failed to fetch data. Status code: {response.status_code}")
         return []
     
     
if __name__ == "__main__":
    query = "cnt:Kenya"
    song = species_data(query)

    if song:
        json_filename = "bird_species.json"
        with open(json_filename, 'w') as json_file:
            json.dump(song, json_file, indent=3)
        print(f"Data saved to {json_filename}.")
    else:
        print("No data retrieved.")
     
     
# 2. Extract all the bird songs from the website.

def bird_songs():
    base_url = "https://xeno-canto.org/api/2/recordings"
    page = 1
    song = []

    while True:
        url = f"{base_url}?query=X&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total = int(data['numRecordings'])

            for recording in data['recordings']:
                song.append({
                    'song_name': recording['en'],
                    'bird_family': f"{recording['gen']} {recording['sp']}",
                    'country': recording['cnt'],
                    'audio_url': recording['file']
                })

            if len(song) >= total:
                break

            page += 1
        else:
            print(f"Failed to fetch data for page {page}. Status code: {response.status_code}")
            break

    return song

if __name__ == "__main__":
    song = bird_songs()

    if song:
        json_filename = "bird_songs.json"
        with open(json_filename, 'w') as json_file:
            json.dump(song, json_file, indent=4)
        print(f"Data saved to {json_filename}.")
    else:
        print("No data retrieved.")

