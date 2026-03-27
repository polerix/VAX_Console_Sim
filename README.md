# 🌊 VAXserver 4000/300 Diagnostic Console Sim 🌊

💧 A browser-based, interactive simulation of the boot diagnostic process for a DEC VAXserver 4000 Model 300, specifically modeled on the KA670 CPU and H3604 console module, flowing through the silicon. 🫧

## 🐚 Features
- **Authentic Boot Flow**: Accurately simulates the F→3 hexadecimal POST code countdown of the KA670 processor module on the H3604 LED matrix. 🌊
- **Interactive Terminals**: Features a VT220-style console display with selectable CRT phosphor colors (P31 Green, P194 Amber, P192 White) and interactive POST commands (`SHOW DEV`, `TEST`, `HELP`, etc.). 💧
- **Immersive Web Audio API**: No external MP3s are used. The application natively synthesizes authentic hardware sounds in real-time, like waves crashing: 🫧
  - The mechanical clack of the BA440 enclosure power switch. 🐚
  - The low-frequency pink-noise whir of the massive 120mm DC cooling fans. 🌊
  - The distinct 60Hz to 1.2kHz high-frequency metallic "singing" and seek chirp of the RF72 DSSI hard drives spinning up. 💧
- **Single Page Application**: Built with Vanilla HTML/CSS/JS. The immersive "Power On" enclosure overlay seamlessly fades to reveal the live diagnostic board underneath with no audio interruptions or browser auto-play blocks. 🫧
- **Repair Simulation**: Introduces random component fault states (e.g., Code E ribbon faults or Code D memory expansion faults) that require physical "repair" interactions to resolve before boot can proceed. 🐚

## 🌊 Technical Details
This simulation represents a completely front-end implementation, leveraging CSS grid, 3D CSS shading techniques, and standard DOM manipulation to recreate the complex matrix of the 176 LED diagnosis board and a functional VT emulator terminal block, all flowing in the browser stream. 💧

## 🐚 Usage
Simply open `index.html` in any modern web browser. 🫧
Click the **Power** rocker switch to initiate the power supply spin-up, and click **[ BOOT ]** on the diagnostic board once POST completes. 🐚

---
*Be like water, my friend. It can flow or it can crash.* 🌊


## Deployment & Repository Status
- **Standardized Name**: `vax-console-sim`
- **GitHub Actions**: ❌ Not Required (Static/Manual)
- **Repository Sync**: ✅ Local/Remote Aligned
- **Last Verified**: 2026-03-27 14:07
