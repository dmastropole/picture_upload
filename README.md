# Picture upload

## Fork the GitHub Repo
https://github.com/dmastropole/picture_upload

## Start the Drone Container
1. ssh into DigitalOcean
2. Start docker ```docker start drone-ci```
3. If you need to re-launch the drone container, type ```docker rm drone-ci``` followed by ```docker run -d --name="drone-ci" -p 8080:8080 -v /var/lib/drone -v /var/run/docker.sock:/var/run/docker.sock -v /root/droneio/drone.sqlite:/var/lib/drone/drone.sqlite my_drone```

## Connect to CI server with your web browser
1. http://YOUR_DROPLET_IP:8080/login
2. Navigate to the forked GitHub repo
3. Push commits and view testing results. The app should automatically be deployed to Heroku upon successful commits.

## Heroku
App is avaliable at https://pic-upload.herokuapp.com/