if [ $(id -u) -ne 0 ]
then
   echo "L'installation doit être lancé en tant que root"
   exit 1
fi

apt update -y
apt upgrade -y
