### COMPLETE TIME TAKEN: ~ HRS (so far)

This file is where I store all my journaling for my keyboard starting from day one to the end of the building, this will be updated occasionally (every day).

## DESIGNING (4 DAYS) 
## ~ HRS

# Day 1:
~ 3.5hrs
Today was just a bunch of schematic things and starting with my pcb layout, for the schematic I had to pull a funny and use a different MCU than what I used for hackpad since it was short by exactly 1 GPIO and I didnt want to remove a row or column from my matrix as this is already a 65% keyboard.
My PCB layout was pretty simple well I thought until I had to reset the entire thing like 4 times. I decided to go with some low profile switches which are the Kailh Choc switches (V1 even though its outdated I like its feel more). And I ultimately decided to go plateless since these switches are compatible with a plateless build and it would also be nice to not have to make a plate for this monstrosity of a layout that I had going on here.
![image](https://github.com/user-attachments/assets/fbfc4c22-0173-4fa2-bf30-10733a897184) (I also added some LEDS into the equation, and for some reason didnt use SW_PUSH 45 degree but used the normal ones that doesnt matter though.)
![image](https://github.com/user-attachments/assets/2f3b5c43-37e1-4204-8629-9e080d00ca5b) (I had to mess with some keepout zone related stuff in the PCB editor too because it just didnt work out since the keepout zone for my MCU is absolutely huge. And as you can see the routing is a complete mess that I decided to fix later)

# Day 2:
~ 5hrs
Today was finishing the full PCB layout and I plan for the next 2 days to be purely CAD related things. I also decided to do some work on my BOM and that turned out to be simple (check BOM.csv). The full PCB layout had some issues and I decided to go with the option of using some stabilisers but replacing some with dead switches that dont have any electrical connection, because it turns out the PCB mounted stabilisers that exist for the switch model that I am using is very old and is very expensive online for bigger sizes, so easy workaround.
But if we put aside the challenges that I had, the upsides were that I got to finish my layout today and export the model into CAD (didnt do anything else in CAD today). But I also spent a while looking for the perfect footprint and things so that I didnt have a shortage of actual parts to buy online. I decided not to go with hotswap because 1: Im not going to remove these keys and 2: I dont want to deal with the hotswap sockets for the type of switches Im using its a lot more of a pain than you would think and 3: Whats the fun in that when you could torture yourself into soldering on all of your switches individually?
![image](https://github.com/user-attachments/assets/10bd99d8-ce19-43c9-b81c-14fcd0ffbe1f) (The routing of my PCB took a very long time so I loaded it into freerouting which did like half of it before breaking so I spent another hour doing the other half and cleaning up the mess that freerouting made, lesson learned.)


## BUILDING (0 DAYS)
## ~ HRS
None of the parts arrived yet, sad. Will update this part when my parts arrive and I start building!
