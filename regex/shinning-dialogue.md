# The Shinning Regex

**This wraps the title of the movie.**

Find:```^"(.+)```

Replace:```<title>\0</title>```

**This wraps every speaker in an element.**
Find:```^([A-Z]{2,})```

Replace```<speaker>\0</speaker>```

**This wraps the lines of text following the speaker elements.**
Find:```^([A-z])+[!]*(.+)```

Replace:```<dialogue>\0</dialogue>```