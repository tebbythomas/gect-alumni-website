# gect-alumni-website
Django website created for the alumni from the 1984 batch of Government Engineering College, Thrissur.

[Website Link](https://tec84.in/)

## Technical Details
### Libraries And Tools:
- The project requirements are: [requirements](https://github.com/tebbythomas/gect-alumni-website/blob/master/requirements.txt)
- The project uses sqllite as its database.
- The project is deployed on a DigitalOcean Droplet running Ubuntu 18.04.3 (LTS) x64.
- It uses nginx as the reverse proxy and gunicorn as the wsgi.
- It uses HighCharts JS library to display interactive charts relevant to the batch members [Stats Page](https://tec84.in/stats/)
- It uses the Google Map API to place markers on the Google Maps Interface indicating what countries the batch members live in
- The admin portal has been enabled that uses Django's default admin portal
### Project Structure:
The project is divided into 4 apps:
1. **Accounts** - contains user account details of batch members that uses the default django.contrib.auth library
2. **Members** - contains custom details of each batch member like engineering branch, address, photo, etc
3. **News** - contains basic details of a news article like headline, brief description, photo
4. **Gallery** - contains basic details of each photo in the Gallery section like description.
