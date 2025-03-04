import os
from typing import Dict, List, Type
import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class VideoSearchResult(BaseModel):
    video_id: str
    title: str
    channel_id: str
    channel_title: str
    days_since_published: int


class VideoDetails(BaseModel):
    title: str
    view_count: int
    url: str


# Pydantic input for the tool
class YoutubeVideoSearchAndDetailsToolInput(BaseModel):
    keyword: str = Field(..., description="The search keyword.")
    max_results: int = Field(3, description="The maximum number of results to return.")


# Youtube Video Search Tool``
class YoutubeVideoSearchAndDetailsTool(BaseTool):
    name: str = "Search YouTube Videos"
    description: str = (
        "Searches YouTube videos based on a keyword and retrieves details for each video."
    )
    args_schema: Type[BaseModel] = YoutubeVideoSearchAndDetailsToolInput # additional argument we can use - inside crewAI's BaseTool - telling it we want the args_schema to look like the input schema we setup above 
    api_key: str = Field(default_factory=lambda: os.getenv("YOUTUBE_API_KEY"))

# Step 2 - fetch a specific video's snippets and statistics
    def fetch_video_details_sync(self, video_id: str) -> VideoDetails:
        url = "https://www.googleapis.com/youtube/v3/videos"
        params = {"part": "snippet,statistics", "id": video_id, "key": self.api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()

# Pull out info that we want from response
        item = response.json().get("items", [])[0]
        title = item["snippet"]["title"]
        view_count = int(item["statistics"]["viewCount"])
        video_url = f"https://youtube.com/watch?v={video_id}"
        return VideoDetails(title=title, view_count=view_count, url=video_url)
    
# step 1 - fetch results from youtube based on the keyword we pass in
    def _run(self, keyword: str, max_results: int = 3) -> List[Dict]:
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "q": keyword,
            "maxResults": max_results,
            "type": "video",
            "key": self.api_key,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        items = response.json().get("items", [])

        video_details = [
            self.fetch_video_details_sync(item["id"]["videoId"]) for item in items
        ]
        return [video.model_dump() for video in video_details]
