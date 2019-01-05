REM https://www.jetbrains.com/help/clion/how-to-use-wsl-development-environment-in-clion.html
REM Sudo install c compliers and essentials
sudo apt-get install cmake gcc clang gdb build-essential
REM ssh-server script
wget https://raw.githubusercontent.com/JetBrains/clion-wsl/master/ubuntu_setup_env.sh && bash ubuntu_setup_env.sh
REM check up ssh connections (Remember to change username and localhost to the ones on computer)
ssh username@localhost -p2222
