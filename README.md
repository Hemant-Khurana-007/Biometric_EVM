## Biometric EVM (Fingerprint Based Authentication Voting System)

### Overview

Biometric EVM is a secure electronic voting system prototype that integrates biometric authentication with fingerprint based identity verification. The objective of this project is to enhance election security by preventing impersonation, duplicate voting, and improve voter mobility using biometric validation.
---

### Problems in Current Voting Systems

Despite improvements in electronic voting machines, several challenges still exist:

- Voter impersonation using fake or borrowed identity cards  
- Possibility of duplicate voting  
- Manual verification errors  
- Long verification queues at polling booths  
- Limited real time identity validation
- Voting still remains a location dependant process

These issues reduce trust, transparency, and efficiency in the election process.

---

### Proposed Solution

This project introduces Fingerprint based biometric authentication before allowing a voter to cast their vote.

#### Core Idea

- Each voter’s biometric data is securely stored in R307s's buffer.
- During voting, the voter places his finger on the fingerprint scanner.
- The fingerprint scanner captures biometric data.
- The system verifies the fingerprint against Aadhaar linked data (prototype level simulation).
- If verified and not already voted, access to the voting interface is granted.

This ensures:

- One person = One vote  
- No impersonation  
- No duplicate voting  
- Strong identity verification  

---

### System Workflow

#### 1. Authenticator

1. Voter places his finger on the fingerprint scanner.
2. Fingerprint is scanned.
3. Biometric data is verified against stored Aadhaar-linked records.
4. Camera verifies if the person has already voted by checking if ink is detected on voter's finger
5. If authentication succeeds, Servo mechanism marks the finger with inedible ink and sends a UART signal to RPI pico stating the voters constituency.
6. If authentication fails, access is denied.

---

#### 2. EVM
1. As it recives the UART signal it fetches the partys and candidates for that particular constituency
2. Candidate and party list appears on 1602 i2c LCD display.
3. Party symbols appear on 0.96 inch OLED display
4. Voter selects preferred candidate.
5. It then sends a signal over USB stating the party and constituency for which the vote has been casted 
---

#### 3. Vote Storage
1. If it doesn't recieve anything on its USB it keeps displaying a black screen 
2. As the voter casts his/her vote RPI zero 2 w recieves a signal over usb that states the constituency and party the voter has voted for.
3. Votes are stored in dedicated CSV files of each constituency.
4. Image of casted vote is displayed on 3.3 inch tft display connected to RPI zero 2 w for voter's confirmation  
---

### Technical Architecture

#### Hardware Components

- R307s fingerprint Sensor Module  
- ESP32
- RPI pico
- RPI zero 2 w
- RPI 2b  
- 4 x  1602 i2c LCD display
- 4 x 0.96 inch OLED display
- 4 x Push Buttons 
- 4 x Led
- 2 x 3.5 inch 26 pin header tft display 
- 12 DC supply
- 2 x I2C Bi-Directional logic Level Converter- 4 Channel
- Passive buzzer
- mp1584 buck converter 
- mp1584en buck converter 
- 4v diaphragm pump
- 3mm tubing
- 2 x servo 
- 1 x USB camera
- 1 x mosfet module
- 1 x inkpot
---

#### Software Modules

##### 1. Authenticator
- Captures fingerprint
- Matches biometric template
- Returns verification status
- Prevents duplicate voting

##### 2. EVM
- Displays candidate list
- Accepts vote input
- Confirms vote submission

##### 3. VVPAT
- Stores votes securely
- Maintains voter status flag

---

### Security Considerations

- Biometric data is encrypted before storage and only stored in R307s's buffer.
- Identity and vote records remain separated to maintain voter anonymity.
- System operates offline to prevent remote cyber attacks.
- Secure audit logs maintained.

---

### How to Run the Project

1. Connect hardware as shown in circuit diagram

2. Clone the repository:
   ```bash
   git clone https://github.com/Hemant-Khurana-007/Biometric_EVM.git
   ```

3. Install required dependencies.

4. Upload the code in folders to their respective microcontroller.

5. Change basepath and votepath in main.py (RPI zero 2 w) to wherever your images are stored and wherever you want the votes to be stored

6. Power on the system and begin authentication and voting process.

---

### Advantages

- Prevents impersonation
- Eliminates duplicate voting
- Faster voter verification
- Improved transparency
- Enhanced election security

---

### Future Improvements

- Integration with secure government authentication APIs  
- Integrating a CSN A5 printer with VVPAT
- Integrating a iris scanner 

---

### Developed By
Team Multiplexers  
Maharaja Agrasen Institute of Technology
