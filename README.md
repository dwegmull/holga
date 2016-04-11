# holga
workaround the date/time limitations of the Holga Digital camera
every time the Holga Digital camera is turned off and on, its clock is reset. It also sets the Exif time and date to a fixed value. As a result, image management software that depends on the date and time to organize images gets very confused.
This workaround updates the exif data and the file time stamps to be one second appart from each other. It's not perfect, but at least, if the pictures are imported soon after they are taken, they will have a semblance of organization.
This works for Linux (tested on Ubuntu 14.04). The Python script should run on any host. The "magic" part that launches the script upon plug-in of the memory card relies on udev.
