def create_youtube_video(title,description):
	youtube_video={"title":title,"description":description,"likes":0,"dislikes":0, "comments":{}}
	return dict1

def like(youtube_video):
	if "likes" in dict1:
		dict1["likes"]+=1

def dislike(youtube_video):
	if "likes" in dict1:
		dict1["dislikes"]+=1

def add_comment(youtube_video,username,comment_text):
