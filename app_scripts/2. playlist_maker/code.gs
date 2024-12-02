function createYouTubePlaylist() {
  const playlistTitle = "Title "; // Replace with your desired playlist name
  const playlistDescription = "Description"; // Add a description
  const videoTitles = []; // Write video titles in string

  // Authenticate YouTube API
  const playlist = YouTube.Playlists.insert({
    snippet: {
      title: playlistTitle,
      description: playlistDescription
    },
    status: {
      privacyStatus: "unlisted"
    }
  }, "snippet,status");

  const playlistId = playlist.id;

  // Add videos to the playlist
  for (let i = 0; i < videoTitles.length; i++) {
    try {
      const searchResults = YouTube.Search.list("id", {
        q: videoTitles[i],
        maxResults: 1
      });

      if (searchResults.items.length > 0) {
        const videoId = searchResults.items[0].id.videoId;
        YouTube.PlaylistItems.insert({
          snippet: {
            playlistId: playlistId,
            resourceId: {
              kind: "youtube#video",
              videoId: videoId
            }
          }
        }, "snippet");
      }
    } catch (e) {
      Logger.log("Error adding video: " + videoTitles[i] + " - " + e.message);
    }
  }
}
