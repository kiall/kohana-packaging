# Kohana Packaging

Currently providing .deb's of kohana 3.0 and 3.1. RPMs might come in someone donates a .spec file!

## Debian/Ubuntu Packages

To use these packages on debian/ubuntu run the following:

1. `wget -q -O - http://apt.managedit.ie/public.key | sudo apt-key add -`
2. `sudo apt-add-repository 'deb http://apt.managedit.ie/ kohana main'`
3. `sudo apt-get update`
4. `sudo apt-get install kohana3.0`

