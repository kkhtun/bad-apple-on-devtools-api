# bad-apple-frames-api-ascii

1. Use pip install requirements.txt and install opencv + numpy (tested on python3.8.0)
2. Extract frames as ascii art from your video using main.py, give input path, output frames folder as arguments.
(eg. $ python main.py --input badapple.mp4 --output server/frames --height 40)
3. If all the frames are extracted, check server.php to see if the code is serving the correct path for extracted ascii texts.
4. Check index.html and make sure port and endpoint in fetch() is set.
5. Run the server at the specified port (for php, you can do $ php -S localhost:8000 -t . inside the server folder)
6. Get index.html in browser, open dev tools, click Play button on document.
7. You can adjust the speed of API calls and consequently frame updates by tweaking time variable in ms for the await sleep(time) function.