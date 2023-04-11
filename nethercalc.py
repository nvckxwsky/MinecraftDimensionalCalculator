#MinecraftDimensionCalculator.
#Author: Mikołaj "nvckxwsky" Pusz.
#LICENSE: GNU GPL v3. 
#source: github.com/nvckxwsky/MinecraftDimensionalCalculator.

exit_val = int(0)
while exit_val==0:
    print("Minecraft Dimensional Calculator!\n"+"Choose your destiny:\n"+"1.Overworld to nether conversion.\n"+"2.Nether to overworld conversion.\n"+"3.Exit!")

    destiny = int(input("What you want to do?"))

    if destiny==1:
        x_overworld = float(input("Input x coordinate in overworld:"))
        z_overworld = float(input("Input z coordinate in overworld:"))

        x_nether = float(x_overworld/8)
        z_nether = float(z_overworld/8)

        print("Your cords in nether are:\n"+"x: "+ str(x_nether) +"\n"+"z: "+ str(z_nether) +"\n")
        x_overworld=0;z_overworld=0;x_nether=0;z_nether=0;

    if destiny==2:
        x_nether = float(input("Input x coordinate in nether:"))
        z_nether = float(input("Input z coordinate in nether:"))

        x_overworld = float(x_nether*8)
        z_overworld = float(z_nether*8)
        print("Your cords in overworld are:\n"+"x: "+ str(x_overworld) +"\n"+"z: "+ str(z_overworld) +"\n")
        x_overworld=0;z_overworld=0;x_nether=0;z_nether=0;
    if destiny==3:
        exit_val=1;print("Thanks for using my program :)")
   
