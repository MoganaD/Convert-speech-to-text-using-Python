#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install SpeechRecognition moviepy


# In[3]:


import speech_recognition as sr 
import moviepy.editor as mp


# In[70]:


clip = mp.VideoFileClip(r"Documents/yoges/video5.mp4")


# In[71]:


clip.audio.write_audiofile(r"Documents/yoges/video5.wav")


# In[72]:


r = sr.Recognizer()


# In[73]:


audio = sr.AudioFile("Documents/yoges/video5.wav")


# In[77]:


with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)


# In[76]:


result


# In[79]:


# exporting the result 
with open('Documents/yoges/text5.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")


# In[ ]:




