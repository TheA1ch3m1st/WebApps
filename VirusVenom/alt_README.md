# VirusVenom

VirusVenom is a malware checker WebApp made for CS50's Introduction to Computer Science. It was submitted as the Final Project.

## Installation and Usage
This project uses CS50's library and hence is not able to run on a regular machine (unless of course the library is installed).

## How does it work?
Note: the WebApp is **very** unsecure.*


Of course, I didn't build an entire engine for detecting malware. VirusVenom functions in a very simple manner. The file is uploaded, the hash of the file is checked against a database, if there is a match, the alarm goes off. The database of hashes was taken from VirusShare. I only took the first entry of MD5 hashes, as it would've been a redundant pain to go through each of them.

The frontend was made using Mobirise (for the most part). The backend was made entirely by me with the help of the CS50 library.

As I have (at the time of writing this) acquired frontend web design skills, I have considered remaking this project. However, this is likely not going to happen. The WebApp is extremely messy (so messy that if the file's hash exists, it simply redirects you to a picture of a big X. Yup.) as I made it in a jiffy to get done with the course.

To make testing safer (and easier), I added a hash to the database which was the previous README file of this project. I will not update the hash, but feel free to do so. The reason it had to be the README file and not a junk binary/exe or some other type of file is because the webserver on the CS50 IDE has a file size upload limit, and I couldn't change that because I was in a docker.

*There is no upload sanitization whatsoever, which makes it EXTREMELY easy to gain access to the server running the WebApp.

## License
This project does not currently have a license.