# -*- mode: ruby -*-
# vi: set ft=ruby :

ENV['VAGRANT_SERVER_URL'] = 'https://vagrant.elab.pro'
Vagrant.configure("2") do |config|
  # config.ssh.insert_key = false

  config.vm.define "vagrant1" do |vagrant1|
    vagrant1.vm.box = "ubuntu/focal64"
    vagrant1.vm.network :private_network, ip: "192.168.56.10"
    vagrant1.vm.network :forwarded_port, host: 8888, guest: 80
    vagrant1.vm.network :forwarded_port, host: 8443, guest: 443    
  end

  # config.vm.define "vagrant2" do |vagrant2|
  #   vagrant2.vm.box = "ubuntu/focal64"
  #   vagrant2.vm.network :forwarded_port, host: 8081, guest: 80
  #   vagrant2.vm.network :forwarded_port, host: 8444, guest: 443    
  # end


  # config.vm.box = "ubuntu/jammy64"
  # config.vm.hostname = "testserver"
  # config.vm.network "forwarded_port", id: 'ssh', guest: 22, 
  #   host: 2202, host_ip: "127.0.0.1", auto_correct: false
  # config.vm.network "forwarded_port", id: 'http', guest: 80, 
  #   host: 8080, host_ip: "127.0.0.1"
  # config.vm.network "forwarded_port", id: 'https', guest: 443, 
  #   host: 8443, host_ip: "127.0.0.1"
  # config.vm.provider "virtualbox" do |virtualbox|
  #   virtualbox.name = "ch03"
  # end
end
