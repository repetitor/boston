https://askubuntu.com/questions/1064619/how-can-i-compile-run-assembly-in-ubuntu-18-04

```shell
sudo apt install as31 nasm

nasm -f elf64 try.asm # assemble the program  
ld -s -o try try.o # link the object file nasm produced into an executable file  
./try # try is an executable file
```