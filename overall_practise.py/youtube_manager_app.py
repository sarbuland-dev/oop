





# import json
# def load_data():
#     try:
#         with open("youtube.txt","r") as file:
#             return json.load(file)

#     except FileNotFoundError:
#         return[]
    
# def save_data_helper(videos):
#     with open("youtube.txt","w") as file:
#         json.dump(videos,file)


# def delete_videos(videos):
#     pass
# def update_videos(videos):
#     pass
# def add_videos(videos):
#     name=input("enter your name  ")
#     time=input("enter your time  ")
#     videos.append({"name":name,"time":time})
#     save_data_helper(videos)
# def list_all_videos(videos):
#    for index,videos in enumerate(videos,start=1):
#        print(f"{index}. Name: {videos['name']}, Time: {videos['time']}")

# videos=load_data()
# def main():
#     while True:
#         print(" youtube manager app")
#         print("1. list all videos ")
#         print("2.add a youtube videos")
#         print("3.update a youtube video details")
#         print("4.delete a youtube video")
#         print("5.eixt youtube app")
#         choice=input("enter your choice    ")
#         match choice:
#             case 1:
#                 list_all_videos(videos)
#             case 2:
#                 add_videos(videos)
#             case 3:
#                 update_videos(videos)
#             case 4:
#                 delete_videos(videos)
#             case 5:
#                 break
#             case _:
#                  print("invalid choice ")

# if __name__ == "__main__":
#     main()
            


import json

# Load data from file
def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to file
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file, indent=4)

# Add a new video
def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print(" Video added successfully!")

# List all videos
def list_all_videos(videos):
    if not videos:
        print(" No videos found.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. Name: {video['name']}, Time: {video['time']}")

# Placeholder functions (to be implemented later)
def delete_videos(videos):
    print(" Delete function not implemented yet.")

def update_videos(videos):
    print(" Update function not implemented yet.")

# Main app loop
def main():
    videos = load_data()

    while True:
        print("\n YouTube Manager App")
        print("1. List all videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit")
        choice = input("Enter your choice (1–5): ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                print(" Exiting... Bye!")
                break
            case _:
                print(" Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
