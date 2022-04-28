#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install SpeechRecognition moviepy


# In[3]:

#import modules
import speech_recognition as sr 
import moviepy.editor as mp


# In[70]:

#load video clip
clip = mp.VideoFileClip("Documents/video5.mp4")


# In[71]:

#convert video to audio
clip.audio.write_audiofile("Documents/video5.wav")


# In[72]:

#use recognizer to extract the audio
r = sr.Recognizer()


# In[73]:


audio = sr.AudioFile("Documents/video5.wav")


# In[77]:


with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)


# In[76]:

#display the text from the audio
result


# In[79]:

#export the text
# exporting the result 
with open('Documents/text5.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")


# In[ ]:




