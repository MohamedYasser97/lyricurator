

# Lyricurator

A bot that scrapes the internet for song lyrics, song names and artists. This program can be either used as a CLI tool to add lyrics to your terminal, or it can be linked with a Twitter account and tweet lyrics automatically.


## Usage

After cloning this repository, you can run lyricurator in its most simple mode of operation with the CLI argument `-nt/--notwitter` which will print random lyrics in the terminal.

![enter image description here](https://i.imgur.com/Jmvp2ir.png)

In order to send lyrics to Twitter, you have to add the following credentials to the file `auth.json`.

![enter image description here](https://i.imgur.com/zs3LAkI.png)

Then you can start lyricurator with the `-t/--twitter` argument and a tweet will be sent.

![enter image description here](https://i.imgur.com/MSaqJdQ.png)
![enter image description here](https://i.imgur.com/agau4aq.png)

\* You can learn more about how to get your own Twitter application credentials by following [this guide](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app-with-python)'s first 2 steps.

\* Note that it's mandatory to use one of `-nt` or `-t`. The rest of the CLI arguments are optional.
#### CLI arguments you can use or combine:
- `-t/--twitter` tweet lyrics to linked Twitter account in `auth.json`.
- `-nt/--notwitter` prints lyrics to the console instead of tweeting them.
- `-la/--listartists` gets a list of all available artists.
- `-a/--artist` specifies artist to get lyrics for.
- `-fs/--fullsong` prints the entire lyrics of a song to the console.
- `-ls/--listsongs` lists all songs for random or user-selected artists.
- `-i/--interval` prints/tweets lyrics at specified interval in minutes


## Want to contribute?

Check out [CONTRIBUTING.md](https://github.com/MohamedYasser97/lyricurator/blob/master/CONTRIBUTING.md) for instructions.

