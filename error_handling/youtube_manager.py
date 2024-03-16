import json
from json import JSONDecodeError
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test =  json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
        

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index , video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration : {video['time']}")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index  = int(input("Enter the video number to update :"))
    if 1 <= index <= len(videos):
        name = (input("Enter the new video name :"))
        time = (input("Enter the new video time :"))
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_videos(videos):
    list_all_videos(videos)
    index  = int(input("Enter the video name to be deleted "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        print(f"Video deleted no. {index}")
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List a all youtube videos ") 
        print("2. Add a youtube video ") 
        print("3. Update a youtube video details ") 
        print("4. Delete a youtube video ") 
        print("5. Exit the app ")
        choice = input("Enter you choice ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()