# Biometric EVM (Fingerprint-Based Authentication Voting System)

## Overview

Biometric_EVM is a secure electronic voting system prototype that integrates biometric authentication with fingerprint based identity verification. The objective of this project is to enhance election security by preventing impersonation, duplicate voting, and improve voter mobility using biometric validation.
---

## Problems in Current Voting Systems

Despite improvements in electronic voting machines, several challenges still exist:

- Voter impersonation using fake or borrowed identity cards  
- Possibility of duplicate voting  
- Manual verification errors  
- Long verification queues at polling booths  
- Limited real time identity validation
- Voting still remains a location dependant process

These issues reduce trust, transparency, and efficiency in the election process.

---

## Proposed Solution

This project introduces Fingerprint-based biometric authentication before allowing a voter to cast their vote.

### Core Idea

- Each voter’s biometric data is securely stored in R307s's buffer.
- During voting, the voter places his finger on the fingerprint scanner.
- The fingerprint scanner captures biometric data.
- The system verifies the fingerprint against Aadhaar-linked data (prototype-level simulation).
- If verified and not already voted, access to the voting interface is granted.

This ensures:

- One person = One vote  
- No impersonation  
- No duplicate voting  
- Strong identity verification  

---

## System Workflow

### 1. Identity Authentication

1. Voter places his finger on the fingerprint scanner.
2. Fingerprint is scanned.
3. Biometric data is verified against stored Aadhaar-linked records.
4. If authentication succeeds, voting access is granted.
5. If authentication fails, access is denied.

---

### 2. Vote Casting

1. Candidate list appears on display.
2. Voter selects preferred candidate.
3. Vote is recorded securely.
4. System marks voter as "Voted" to prevent duplicate voting.

---

### 3. Vote Storage

- Votes are stored in secure memory.
- Identity data is separated from vote data.
- A voter status flag prevents re-voting.
- Results can be tallied after the election ends.

---

## Technical Architecture

### Hardware Components

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

### Software Modules

#### 1. Authenticator
- Captures fingerprint
- Matches biometric template
- Returns verification status
- Prevents duplicate voting

#### 2. EVM
- Displays candidate list
- Accepts vote input
- Confirms vote submission

#### 3. VVPAT
- Stores votes securely
- Maintains voter status flag

---

## Security Considerations

- Biometric data is encrypted before storage and only stored in R307s's buffer.
- Identity and vote records remain separated to maintain voter anonymity.
- System operates offline to prevent remote cyber attacks.
- Secure audit logs maintained.

---

## How to Run the Project

1. Connect hardware as shown in circuit diagram

2. Clone the repository:
   ```bash
   git clone https://github.com/Hemant-Khurana-007/Biometric_EVM.git
   ```

3. Install required dependencies.

4. Upload the code in folders to their respective microcontroller.

5. Change basepath in main.py (RPI zero 2 w) to wherever your images are stored

6. Power on the system and begin authentication and voting process.

---

## Advantages

- Prevents impersonation
- Eliminates duplicate voting
- Faster voter verification
- Improved transparency
- Enhanced election security

---

## Future Improvements

- Integration with secure government authentication APIs  
- Integrating a CSN A5 printer with VVPAT
- Integrating a iris scanner 

---

## Disclaimer

This project is developed for academic and prototype purposes only.  
Real world implementation would require strict compliance with data privacy laws, government regulations, and secure integration with official Aadhaar authentication systems.

---

## Developed By
Team Multiplexers  
Maharaja Agrasen Institute of Technology
