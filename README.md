clone of https://patchstorage.com/fluidloops/ for me to mess around with :)

## changes

* libfluidsynth.so.1 is the version for organelle-m
* improvements to parseSoundfonts.py

## update nov 2024 - organelle OS 4.2

* Install instructions below still work - sorry it's still not a zip or a zop
  I no longer remember what, if anything, we were supposed to do with libfluidsynth.so.1,
  but I didn't do anything, and the patch works, so, OK!
* Gave up trying to get parseSoundfonts.py to work on the device anymore, but
  with a little tweak it now runs locally with py3 and sf2utils installed.
  Then it's up to you to copy the files it adds/changes to the /sf2/ dir on
  organelle. `git diff` and `git status` can help identify that

## install

```bash
ssh music@organellem.local
cd /sdcard/Patches
git clone https://github.com/rupa/fluidloops-organellem.git fluidloops
```

## use

* patch should make some noise and the included sf2s should work
* adding sf2s is a bit involved:
    * have the repo checked out on another computer, python on organelle is
      too old and busted to install the `sf2utils` dependency.
    * put the `.sf2` file in the `sf2` directory
    * run `parseSoundfonts.py`. it scans the `sf2` dir and writes metadata
      for all of the soundfonts it finds. Each `.sf2` gets a corresponding
      txt file that's an index of the sounds it contains, and then there's
      a `list.txt` that's an index of all of the soundfonts.
      From organelle perspective, adding a new `.sf2` means you would upload
      three files to the `sf2` dir:
        * `mysoundfont.sf2` - the soundfont itself
        * `mysoundfont.txt` - the index file for the soundfont
        * `list.txt`        - updates the main index to include the new soundfont
