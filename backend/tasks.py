from functools import partial
from crewai import Task
from textwrap import dedent


class YoutubeAutomationTasks():

    def manage_youtube_video_creation(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Oversee the YouTube prepration process including market research, title ideation, 
                description creation, and email creation reqired to make a YouTube video. The ultimate goal is for you to generate 
                a report including a research table, potential high click-through-rate titles, 
                a YouTube video description, and an emails newsletter update about the new video.
                               
                The video topic is: {video_topic}
                The video details are: {video_details}  

                 
                Here is an example report that you can use as a template:
                - It is important to note that the example report only contains 2 videos, 
                    but the final report should contain 15 videos.
                - It is important to note that the example report only contains 3 potential high CTRO titles,
                     but the final report should contain 10 titles.               
                
                Example Report(Only contains 2 videos but the actual report much have 15):
                # YouTube Competition Research Table:
                - Video 1:
                    - Title: "How to Make a YouTube Video"
                    - View Count: 100,000
                    - Days Since Published: 30
                    - Channel Subscriber Count: 1,000
                    - Video URL: https://www.youtube.com/watch?v=1234
                - Video 2:
                    - Title: "How to Make a YouTube Video"
                    - View Count: 100,000
                    - Days Since Published: 30
                    - Channel Subscriber Count: 1,000
                    - Video URL: https://www.youtube.com/watch?v=1234
                ...
                                    
                # Potential High CTRO Titles:
                - How to Make a YouTube Video in 2024
                - How to Make a YouTube Video for Beginners
                - Why is AI so powerful
                [THE REST OF THE POTENTIAL HIGH CTRO TITLES GO HERE]
                                    
                # YouTube Video Description:
                Download the Source Code Here:
                
                👍 Don't forget to like, comment, and share this video! Your support helps us bring more fantastic content your way!

                🔔 Follow us on Social Media:
                    Instagram: [Your Instagram]
                    Twitter: [Your Twitter]
                    Facebook: [Your Facebook]

                🛠️ Resources and Tools Mentioned:
                    [Resource 1]
                    [Resource 2]
                    [Resource 3]
                
            """),
            agent=agent,
            output_file="output/YouTube_Video_Creation_Report.txt",
            expected_output=dedent(f"""
                Generate a report that is formatted exactly like the example report provided to you earlier.
                Make sure the report contains 15 videos, 10 potential high CTRO titles, a YouTube video description.
                The researched video should have all the required details and valid URLs.
            """)
        )

    def manage_youtube_video_research(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""For a given video topic and description, search youtube videos to find 
                15 high-performing YouTube videos on the same topic. Once you have found the videos, 
                research the YouTube video details to finish populate the missing fields in the 
                research CSV. When delegating tasks to other agents, make sure you include the 
                URL of the video that you need them to research.
                            
                This research CSV which will be used by other agents to help them generate titles 
                and other aspects of the new YouTube video that we are planning to create.
                               
                Research CSV Outline:
                - Title of the video
                - View count
                - Days since published
                - Channel subscriber count
                - Video URL
                       
                The video topic is: {video_topic}
                The video details is: {video_details}

                Important Notes: 
                - Make sure the CSV uses ; as the delimiter
                - Make sure the final Research CSV Outline doesn't contain duplicate videos
                - It is SUPER IMPORTANT that you properly match up view counts, subscriber counts, 
                    and everything else to the video URL.
                - It is SUPER IMPORTANT that you only populate the research CSV with real YouTube videos 
                    and YouTube URLs that actually link to the YouTube Video.
                """),
            agent=agent,
            expected_output=dedent(f"""
                Video Title; View Count; Days Since Published; Channel Subscriber Count; Video URL
                How to Make a YouTube Video; 100,000; 30; 1,000; https://www.youtube.com/watch?v=1234;
                How to Get Your First 1000 Subscribers; 100,000; 30; 1,000; https://www.youtube.com/watch?v=1234;
                       ...              
                """)
        )

    def create_youtube_video_title(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Create 10 potential titles for a given YouTube video topic and description. 
                It is also very important to use researched videos to help you generate the titles.
                The titles should be less than 70 characters and should have a high click-through-rate.
                               
                Video Topic: {video_topic}
                Video Details: {video_details}
                """),
            agent=agent,
            expected_output=dedent(f"""
                - How I used AI to gain an unfair advantage in 2024
                - 5 ridiculous ways to make money using AI
                - The number one thing you should focus on in 2024
                - Why procrastication is hard to overcome and how to fix it
                ...                
                """),
        )

    def create_youtube_video_description(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Create a description for a given YouTube video topic and description.     
                Video Topic: {video_topic}
                Video Details: {video_details}
                """),
            agent=agent,
            expected_output=dedent(f"""
                Download the Source Code Here:
                
                👍 Don't forget to like, comment, and share this video! Your support helps us bring more fantastic content your way!

                🔔 Follow us on Social Media:
                    Instagram: [Your Instagram]
                    Twitter: [Your Twitter]
                    Facebook: [Your Facebook]

                🛠️ Resources and Tools Mentioned:
                    [Resource 1]
                    [Resource 2]
                    [Resource 3]
                                       
                🕐 Timestamps: 
                    [LEAVE BLANK]
            """),
        )
