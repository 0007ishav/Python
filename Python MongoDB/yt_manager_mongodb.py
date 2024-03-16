from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://strnge:aYQ!xHPHY5fxejY@cluster0.3esvbnq.mongodb.net/")
# Not a good idea to include id & password in code files.

db = client["YTmanager"]

video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print("*" * 70)
        print(f"ID: {video['_id']}, Name: {video['name']} & Time: {video['time']}")
        print("*" * 70)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})
    print("*" * 70)
    print(f"Video added: {name}")
    print("*" * 70)

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {'$set': {"name": new_name, "time": new_time}})
    print("*" * 70)
    print(f"Video updated: {video_id}")
    print("*" * 70)



def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})
    print("*" * 70)
    print(f"Video deleted: {video_id}")
    print("*" * 70)


def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a  video")
        print("4. Delete a  video")
        print("5. Exit the app")
        print("*" * 70)
        choice = input("Enter your choice: ")
        print("*" * 70)
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the new  video id: ")
            name = input("Enter the new  video name: ")
            time = input("Enter the new video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to be delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("*" * 70)
            print("Invalid choice")
            print("*" * 70)

if __name__ == "__main__":
    main()