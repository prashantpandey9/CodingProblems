# SOLID
# I : Interface Segregation Principle (ISP)
"""
No client should be forced to depend on interfaces they don't use

The main idea behind ISP is to prevent the creation of "Fat" and "bloated" interfaces 
that include methods  that are not required by all client

By segregating  interfaces into smaller, more specific ones, client only depend on the methods they
actually  need, promoting loose coupling and better code organization
"""

# Code Example
"""
Let's consider a scenario where we have a media player application that supports different types of media files, such as audio files (MP3, WAV) and video files (MP4, AVI).

Without applying the ISP, we might have a single interface like this:
"""

class MediaPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError
    
    def play_video(self, video_file):
        raise NotImplementedError

    def stop_audio(self):
        raise NotImplementedError
    
    def stop_video(self):
        raise NotImplementedError

    def adjust_audio_volume(self, volume):
        raise NotImplementedError
    
    def adjust_video_brightness(self, brightness):
        raise NotImplementedError

# Here they have to implement all the function, even if it doesn't need them.
# To adhere to the ISP, we can segregate the interface into smaller, more focused interfaces:

class AudioPlayer:
    def play_audio(self):
        raise NotImplementedError
    
    def stop_audio(self):
        raise NotImplementedError
    
    def adjust_audio_volume(self, volume):
        raise NotImplementedError


class VideoPlayer:
    def play_video(self):
        raise NotImplementedError
    
    def stop_video(self):
        raise NotImplementedError
    
    def adjust_video_brightness(self, brightness):
        raise NotImplementedError

# Now, we can have separate implementations for audio and video players:

class MP3Player(AudioPlayer):
    def play_audio(self, audio_file=""):
        # play audio
        pass

    def stop_audio(self):
        # stop audio
        pass
        
    def adjust_audio_volume(self, volume=""):
        # adjust audio
        pass


class AviVideoPlayer(VideoPlayer):
    def play_video(self):
        # play video
        pass
    
    def stop_video(self):
        # stop video
        pass
    
    def adjust_video_brightness(self, brightness):
        # adjust brightness of video
        pass
    

# If we need a class that supports both audio and video playback, we can create a new class that implements both interfaces:

class MultiMediaPlayer(AudioPlayer, VideoPlayer):
    pass