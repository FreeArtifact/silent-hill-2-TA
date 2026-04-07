# Jacob's Ladder Markdown

I first started with finding all the extra new lines.

Find:```\n\n\n``` replaced with ```\n```

Find:```\n\n``` replaced with ```\n```

I then found all the text inside parethesis.

Find:```\t[(][A-z][^)]*[)]```

Replace:```<parenthetical>\0</parenthetical>```

Next I grabbed the title and writer of the movie (there was deffinetly a better way to grab everything - my code is really long!).

Find:```^["][A-z]+['][A-z]+\s[A-Z]+["]\n[a-z]+\n[A-z]+\s[A-z]+\s[A-z]+```

Replace:```<title>\0</title>```

I also wrapped the scene directions.

Find:```^[A-Z]+[.]\s*[A-z]+\s[-]\s[A-z]+```

Replace:```<SceneHeading>\0</SceneHeading>```

Next I wrapped all the text after each speaker into dialouge tags.

Find:```\t\t(.+)```

Replace:```<dialogue>\0</dialogue>```

The last step was removing the extra spaces after the first dialouge tag.

Find:```<dialogue>\t\t```

Replace:```<dialogue>```