def create_youtube_video(title,description):
	youtube_video={"title":title,"description":description,"likes":0,"dislikes":0, "comments":{}}
	return youtube_video

def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"]+=1

def dislike(youtube_video):
	if "likes" in youtube_video:
		youtube_video["dislikes"]+=1

def add_comment(youtube_video,username,comment_text):
	youtube_video["comments"][username]=comment_text


x=create_youtube_video("hello","this is a description")

like(x)
dislike(x)
add_comment(x,"hellokity","i am a commenter")

print(x)