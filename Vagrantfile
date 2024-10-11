# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  config.vm.box = "archlinux/archlinux"

  
  config.vm.network "forwarded_port", guest: 5000, host: 8080
  
  
  config.vm.provision "file", source: "./hello.py", destination: "/vagrant/hello.py"
  
  
  config.vm.provision "shell", inline: <<-SHELL
    
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm git nano vim python python-virtualenv

    
    cd /home/vagrant
    
    
    python -m venv flask_venv
    
    
    source /home/vagrant/flask_venv/bin/activate && pip install flask

    
    cp /vagrant/hello.py /home/vagrant/hello.py

    
    source /home/vagrant/flask_venv/bin/activate && FLASK_APP=hello.py flask run --host=0.0.0.0
  SHELL

  # Additional optional configurations (uncomment if needed)
  # config.vm.provider "virtualbox" do |vb|
  #   vb.memory = "1024"
  # end
end
