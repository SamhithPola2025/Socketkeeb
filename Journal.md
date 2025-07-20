### COMPLETE TIME TAKEN: ~20 HRS (so far)

This file is where I store all my journaling for my keyboard starting from day one to the end of the building, this will be updated occasionally (every day).

## DESIGNING (4 DAYS) 
## ~30 HRS

# Day 1:
~ 4hrs
Monday, June 30th, 2025
Today was just a bunch of schematic things and starting with my pcb layout, for the schematic I had to pull a funny and use a different MCU than what I used for hackpad since it was short by exactly 1 GPIO and I didnt want to remove a row or column from my matrix as this is already a 65% keyboard.
My PCB layout was pretty simple well I thought until I had to reset the entire thing like 4 times. I decided to go with some low profile switches which are the Kailh Choc switches (V1 even though its outdated I like its feel more). And I ultimately decided to go plateless since these switches are compatible with a plateless build and it would also be nice to not have to make a plate for this monstrosity of a layout that I had going on here.
![image](https://github.com/user-attachments/assets/fbfc4c22-0173-4fa2-bf30-10733a897184) (I also added some LEDS into the equation, and for some reason didnt use SW_PUSH 45 degree but used the normal ones that doesnt matter though.)
![image](https://github.com/user-attachments/assets/2f3b5c43-37e1-4204-8629-9e080d00ca5b) (I had to mess with some keepout zone related stuff in the PCB editor too because it just didnt work out since the keepout zone for my MCU is absolutely huge. And as you can see the routing is a complete mess that I decided to fix later)

# Day 2:
~ 5hrs
Tuesday, July 1st, 2025
Today was finishing the full PCB layout and I plan for the next 2 days to be purely CAD related things. I also decided to do some work on my BOM and that turned out to be simple (check BOM.csv). The full PCB layout had some issues and I decided to go with the option of using some stabilisers but replacing some with dead switches that dont have any electrical connection, because it turns out the PCB mounted stabilisers that exist for the switch model that I am using is very old and is very expensive online for bigger sizes, so easy workaround.
But if we put aside the challenges that I had, the upsides were that I got to finish my layout today and export the model into CAD (didnt do anything else in CAD today). But I also spent a while looking for the perfect footprint and things so that I didnt have a shortage of actual parts to buy online. I decided not to go with hotswap because 1: Im not going to remove these keys and 2: I dont want to deal with the hotswap sockets for the type of switches Im using its a lot more of a pain than you would think and 3: Whats the fun in that when you could torture yourself into soldering on all of your switches individually?
![image](https://github.com/user-attachments/assets/10bd99d8-ce19-43c9-b81c-14fcd0ffbe1f) (The routing of my PCB took a very long time so I loaded it into freerouting which did like half of it before breaking so I spent another hour doing the other half and cleaning up the mess that freerouting made, lesson learned.)


# Day 3:
~ 5hrs
Wednesday, July 2nd, 2025
Today was a lot of CAD related things, and it took me a while to decide on a plateless design and I also spent a lot of time deleting things because that's just how CAD goes. I imported my PCB model into Onshape and started designing a case, I wanted this to be a unique but cool case so that I did not have to redo this because it was too "simple" like the other keyboards. I like this case design because it is simple and the rounded edges give it a sleek look, I used a little peg system to hold it together so it just slides like an apple box instead of screws which are kind of annoying in some ways, I can always integrate screws easily but since it stays on my desk I don't need something too permanent.
![image](https://github.com/user-attachments/assets/cafd7dfc-2283-49e9-bb85-91ea7e0be043)
Today I also refined the PCB a lot and changed some diodes and moved them around a lot because it took a while for me to get them right and for some reason some diodes ended up as LED's??? I dont even know how that ended up happening.

# Day 4:
~ 6hrs
Thursday, July 3rd, 2025
This might as well be the last day of my designing, this has been quite a ride and I learnt a lot from designing this, plus an awesome keyboard. Today was just a bunch of CAD stuff and polishing CAD and fixing any fixing issues, I also worked a lot on my final model that had all the switches and keycaps and I also found a lot of cheaper components online and updated my BOM. I made the final render that is in the ReadMe.md. I made the keycaps and stole a few and I will be 3D printing these to save costs. I also ran a quote on JLCPCB and added that to my BOM.
![Screenshot 2025-06-27 at 9 40 19 PM](https://github.com/user-attachments/assets/da271ff6-33dc-48ca-9067-6d708ee3ac5e)

## BUILDING (2 DAYS)
## ~ 10 HRS
None of the parts arrived yet, sad. Will update this part when my parts arrive and I start building!

# Day 5:
~ 4.5 hrs
Friday, July 17, 2025
First day of building, all the parts arrived, today was mostly just bending, twisting, putting in and soldering diodes, key switches were easy, and for the RP2035 board that I was using (Pi Pico 2W), it broke and I had to order another amazon overnight, but it came in time so I soldered that on today, 3 pads also ripped off when desoldering the old one but I was super lucky as all 3 of those pads were no connects, meaning there is no issue if they rip off, (though it is a sign I need to get better at soldering.) Today the entire PCB finished and I started some 3D prints. I also got the cap for the rotary encoder on because why not.
![IMG_1721](https://github.com/user-attachments/assets/ba389df9-8044-458f-a7b2-e0ee5c694f62)

# Day 6:
~ 5.5 hrs
Friday, July 18, 2025
Second day of building and hopefully last, ran into a few problems here, my printer broke down, not enough time for printing legion, have to go to Barcelona tommorow. Decided to 3D print what I could, and I got permission to submit demo form without keycaps, so that made things a lot easier. I used some other strong material to hold up the rest of the case, and I also uploaded some firmware, I used KMK and spent a while mapping keys, which is probably what took the most amount of time today. 
<img width="1082" height="1001" alt="image" src="https://github.com/user-attachments/assets/2b66ffd5-6a56-4849-aa4c-8ae0146385b2" />
![IMG_1722](https://github.com/user-attachments/assets/2b5e44a8-5be8-4e4c-971e-4e49abed0e2b)

