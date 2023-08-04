
docker rmi $(docker images -q) -f
sudo pacman -Rns docker
#sudo groupdel docker #if you think you need this, but then you have to recreate it, should be fine, right?
rm -rf ~/.docker
