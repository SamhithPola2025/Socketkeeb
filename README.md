# Socketkeeb
Socketkeeb (keyboard) is a custom keyboard I designed in 4 days from PCB to CAD for HackClub's Highway program.
This keyboard was inspired by my need for a keyboard that had low profile switches because those are my favorite type of switches but I could not find a budget one anywhere, so I said why not just make it myself, because that's the solution to most things in life unless its rocket science.

# Challenges
- Designing a PCB compatible with both RP2040 and Kailh Choc switches  
- Sourcing components from multiple vendors while managing shipping costs  
- Ensuring 3D printed keycaps fit properly on low-profile switches  
- Aligning stabilizers and switches without a plate (plateless design quirks)  

# Why I made this
- I wanted a fully custom keyboard with low-profile Choc switches and RP2040 brain  
- I wanted to learn about PCB design, BOM creation, and firmware flashing  
- I like the idea of 3D printing keycaps for a unique personal touch  
- It’s a fun project to build something that’s truly mine from scratch  

# What went good
- Successfully generated a clean BOM and Markdown table for GitHub  
- Found all parts at reasonable prices from trusted vendors  
- 3D printed keycaps turned out better than expected using PLA  
- The design workflow in CAD + PCB tools was smoother than I thought

# BOM: (In BOM.csv too)
| Reference | Quantity | Value | Footprint | Manufacturer | Part Number | Description | Unit Price (USD) | Total Price (USD) | Source Link |
|-----------|----------|--------|------------|--------------|--------------|-------------|------------------|------------------|-------------|
| STAB | 1 set | n/a | PCB Mount | Gateron | n/a | Gateron PCB-mounted stabilizer set (various sizes) | 8.00 | 8.00 | [Gateron](https://www.gateron.com/products/gateron-pcb-mounted-stabilizer?VariantsId=10208) |
| U1 | 1 | RP2040 | Pico W | Raspberry Pi | SC0918 | Raspberry Pi Pico W microcontroller | 7.65 | 7.65 | [DigiKey](https://www.digikey.com/en/products/detail/raspberry-pi/SC0918/16608263) |
| SW1-SW70 | 70 | Kailh Choc Violet | Kailh PG1350 | Kailh | PG1350 | Kailh low-profile Choc Violet switch (70 pcs) | 44.74 | 44.74 | [AliExpress](https://www.aliexpress.us/item/3256806826186563.html) |
| D1-D200 | 200 | 1N4148 | DO-35 | ON Semi | 1N4148 | 1N4148 100V 200mA diode (200 pcs) | 6.76 | 6.76 | [DigiKey](https://www.digikey.com/en/products/detail/onsemi/1N4148/458603) |
| KC1-KC70 | 70 | n/a | n/a | 3D printed | n/a | Custom 3D printed keycaps | 0.00 | 0.00 | n/a |
| **Subtotal** |  |  |  |  |  |  |  | **67.15** |  |
| **Estimated total (with shipping/tax rounded)** |  |  |  |  |  |  |  | **100.00** |  |

# Pictures:
![image](https://github.com/user-attachments/assets/0c2b3d44-9a00-4dfe-a43d-a4d7d46aee11)
![image](https://github.com/user-attachments/assets/02e37ef2-6147-4235-89ba-2cb975b90a06)
![Screenshot 2025-06-27 at 9 40 19 PM](https://github.com/user-attachments/assets/efe2a784-03e8-4bb0-acbe-552fa9638b23)

