# Docker notes

## notes on setting up the epictreasure docker image, running and using it

Your're only as good as your tools ... or something like that. So, don't be 
a massachist! Enjoy a productive exploit development environment, which 
the **epictreasure** docker image provides. It comes all ready with some 
very nice tools and libraries. The one thing that's missing? I would say 
a nice decompiler. Try **ghidra**, which will be easiest to install outside 
of the docker container, because it's a graphical program.

### installation and setup

Installing docker varies system to system. It is easiest on a unix-based 
system, and I can verify it's easy on ubuntu and fedora (probably not on 
arch, HAHA!), and do-able on OSX. On Windows it can get tricky, I think 
there is a provided option for windows that is really more of a vm, but 
it works. Once docker is installed, follow these steps:

1. start docker, it probably isn't started on boot so run 
   `sudo systemctl start docker`

2. pull the docker image
   `docker pull ctfhacker/epictreasure`

### running it

1. again, start docker because it probably isn't running:
   `sudo systemctl start docker`

2. you can pull to update the docker image (not required)
   `docker pull ctfhacker/epictreasure`

3. navigate to the directory you want to work in and share files in

3. run epictreasure `docker run -v `pwd`:/root/host-share --privileged -it --workdir=/root ctfhacker/epictreasure`

4. move to ~/host-share (in the docker image)

5. disable ASLR in the container, if needed (probably is)
   `echo 0 > /proc/sys/kernel/randomize_va_space`

6. use `wget` to get a binary to work on

7. setup corefiles `echo "core.%p" > /proc/sys/kernel/core_pattern`
