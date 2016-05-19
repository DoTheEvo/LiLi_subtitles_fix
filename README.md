![in action gif](http://i.imgur.com/cvyG6nN.gif)

subtitles from [subscene.com](https://subscene.com/) have occasionally this issue where lower case l is replaced with capital I, not everywhere just enough to be reaIIy annoying if your font shows the difference

this python3 script tries to fix that

**dependencies**: `pyenchant` `aspell`

* get the script
* make it executable or run with `python3 subtitles_fix.py ...`
* copy the subtitles to the same folder as the script
* run the fix passing the subtitles as argument
* words not recognized as valid are up to user to fix
    * `y` or `enter` will go with the new 'L' version
    * `n` will keep the original word
    * anything else written in the input will take its place
