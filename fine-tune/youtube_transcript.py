from youtube_transcript_api import YouTubeTranscriptApi

def get_formatted_transcript(video_id):
  try:
    complete_video_transcript = ""
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    for item in transcript:
      complete_video_transcript += f" {item['text']}"
    return complete_video_transcript
  
  except SyntaxError:
    print("Something went wrong!")
    return

  
def get_transcripts():
  video_ids = [
    # an array of strings of youtube video ids to generate transcript
  ]

  all_videos_transcript = ""

  for id in video_ids:
    all_videos_transcript += get_formatted_transcript(id)

  file = open('transcripts.txt', 'w')
  file.write(all_videos_transcript)
  file.close()

get_transcripts()