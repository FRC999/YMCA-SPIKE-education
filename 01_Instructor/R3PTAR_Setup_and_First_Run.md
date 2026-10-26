# R3PTAR connection and first autonomous run

Use **LEGO MINDSTORMS EV3 Home Edition**, already installed on this Windows computer. Its **R3PTAR Mission 3 — Hunting** includes a finished autonomous program. No microSD card, Python installation or alternative operating system is needed. The standard EV3 firmware stores and runs the downloaded program in the brick's internal memory.

Alex reported the robot assembled on October 26, 2026. These instructions were checked against the installed LEGO mission files, program port settings and LEGO manuals. The application process launched, but screen capture was unavailable; the click labels below come from the installed mission content. USB connection, transfer and physical behavior remain untested.

## 1. Connect the robot's cables

With the brick switched off, trace each EV3 cable from the motor or sensor to its labeled brick socket. R3PTAR has one drive motor and a separate steering motor; do not use the SPIKE course's A/B drive wiring.

| Brick socket | Connection | Official build reference |
|---|---|---|
| **A** | **Medium motor** for steering/slithering | Step 16, PDF page 54 |
| **B** | **Large motor** driving the robot along the floor | Step 11, PDF page 40 |
| **D** | **Large motor** operating the raised head/strike mechanism | Step 20, PDF page 64 |
| **4** | **Infrared sensor** in the head | Step 40, PDF page 94 |
| **C, 1, 2, 3** | Leave unused for the standard missions | No extra sensor required |

Motor sockets have letters A–D; sensor sockets have numbers 1–4. Use the labels on the brick rather than its orientation.

## 2. Connect the brick to the computer

1. Check that the brick has working batteries or its charged EV3 battery pack. USB is the data connection, not a replacement for battery power.
2. Press the brick's **center button** and wait for the normal menu.
3. Use the original EV3 **USB-A to Mini-USB Type-B data cable**. Mini-USB is the older, thicker connector; Micro-USB and USB-C do not fit the brick.
4. Plug Mini-USB into the small **PC socket next to motor port D**.
5. Plug the other end into the laptop. Use a suitable USB adapter if the laptop only has USB-C sockets.
6. Leave the brick's large rectangular USB host socket and microSD slot unused. Bluetooth pairing is unnecessary for this procedure.

## 3. Open the finished program

1. Click Windows **Start**, type **LEGO MINDSTORMS EV3**, and open **LEGO MINDSTORMS EV3 Home Edition**. Use this legacy app, not SPIKE App or EV3 Classroom.
2. In the **Lobby**, select the **R3PTAR** snake and click **Build and Program**.
3. If the project opens to its properties (robot picture, description and an empty Programs list), click the large **open-book icon at the top-right**, above the robot video. This opens the **Content Editor**, which displays the mission pages. In **Mission Overview**, click the third tile, **Mission 3 — Hunting**.
4. Click **Command your robot**. If already on the command page, continue below.
5. Click the illustrated button beneath **Open the finished program**. The other option is the exercise for building the program yourself.
6. Confirm the program tab is **R3PTAR 03** and contains connected blocks. A tab named only **Program** may be the blank exercise; select **R3PTAR 03**.
7. Choose **File → Save Project As…** and save a working copy in Documents as **R3PTAR_First_Run.ev3**. This saves on the PC, not on the brick.

For reference, the installed Mission 3 template is located here (do not open it directly):

```text
C:\Program Files (x86)\LEGO Software\LEGO MINDSTORMS EV3 Home Edition\Resources\ContentPacks\Retail\en-US\LEGO\pack3\projects\3.ev3
```

**Installed templates cannot be opened through File → Open Project…** EV3 shows a message requiring new projects to be created through the Lobby. If this happens, click **OK**, cancel the file dialog if it remains open, return to the **R3PTAR** overview project and click its top-right **open-book icon** to reveal Mission Overview. Select Mission 3 there. **Open Project…** is for saved working projects, not these installed templates. A `.ev3` file contains program blocks and assets; it is not Python source or a file to drag onto the brick as if the brick were a USB flash drive.

The installed application is:

```text
C:\Program Files (x86)\LEGO Software\LEGO MINDSTORMS EV3 Home Edition\MindstormsEV3.exe
```

## 4. Confirm the connection and sensor

1. Find the **Hardware Page** at the **bottom-right** of the programming screen; expand it if collapsed.
2. Open **Available Bricks**. Look for the intended brick with a USB connection. If necessary, click **Refresh** and select/connect its USB entry.
3. The small **EV3** label turns **red** when connected. If no brick appears, use the troubleshooting section below.
4. Open **Port View**. Check for a medium motor on **A**, large motors on **B** and **D**, and infrared sensor **4**.
5. With the program stopped, move cardboard toward and away from the infrared sensor and watch its proximity reading change. This is a relative value, not centimeters. Keep fingers outside the head mechanism.

## 5. Transfer without starting the motors

1. Make **R3PTAR 03** the active program tab.
2. Hover over the bottom-right Hardware Page buttons until the tooltip says **Download**.
3. Click **Download** and wait for transfer to finish. Here, download means computer **to brick**.
4. For this first transfer, use **Download**, not **Download and Run** or **Download and Run Selected**: those start movement immediately, and the latter can run only part of the sequence.
5. After transfer finishes, disconnect USB so the moving robot cannot pull the cable or laptop.

## 6. Start and stop from the brick

1. Put the robot on a clear, smooth **floor** with space to move and reverse. Keep hands clear of the head and fangs; the supplied program uses a fast strike.
2. Use the brick's **Left/Right** buttons to select **File Navigation** (folder icon).
3. Use **Up/Down** to select the downloaded project folder, normally **R3PTAR 03** or your saved project's name. Press **Center** to open it.
4. Select **R3PTAR 03** inside the folder and press **Center** to run. The head may move immediately as the program resets the mechanism.
5. Let it move briefly, then present cardboard in front of the infrared sensor without touching the mechanism.
6. The factory Hunting program is designed to roam, detect an object, stop, hiss/strike, retract, reverse/turn and continue. Actual behavior depends on assembly, wiring, batteries and the floor.
7. Stop the first test after roughly **10–20 seconds** by pressing the brick's **Back button**, the separate button above the directional pad. Do not reach into the mechanism to stop it.
8. The program remains on the brick after unplugging USB. Start it again from **Run Recent** or **File Navigation**.

The factory program has an unlimited loop. It does **not** have the finite run-time limit required by our planned classroom demo. An adult must stop this first test. Verify the mechanism and sensor before adapting it for slower movement, a bounded run and the [classroom acceptance checks](../SESSION_PREP.md).

## 7. Other missions and isolated tests

| Mission | Title | Purpose |
|---|---|---|
| **1** | **Slither like a Snake** | Test drive/steering without the target-triggered strike |
| **2** | **Rattling R3PTAR** | Test rattling and sensor-triggered striking before roaming |
| **3** | **Hunting** | Autonomous moving demonstration |
| **4** | **Take Control** | Infrared remote-control driving |

For an isolated test, select Mission 1 or 2 from the overview, go to **COMMAND**, and select **Open the finished program**. Transfer/run using the same procedure. The installed projects are `1.ev3` and `2.ev3` beside `3.ev3`; their solution tabs are **R3PTAR 01** and **R3PTAR 02**.

## 8. Troubleshooting

- **No brick in Available Bricks:** confirm it is switched on at its normal menu, use the small PC socket next to D, reseat the data cable, try another laptop USB port and refresh. If still absent, record the exact software message and what Windows detects; do not jump straight to a firmware reset.
- **Only a Start block or no movement:** select the finished **R3PTAR 03** program rather than the blank **Program** exercise. Check that transfer completed and the correct program is selected on the brick.
- **Drive/strike behavior swapped:** stop and trace **B** and **D** physically. Both are large motors, so Port View alone cannot distinguish their mechanical jobs.
- **Moves but never reacts:** check sensor **4**, inspect proximity readings with cardboard, and confirm Mission **3**, not 1 or 4. The supplied threshold is **30**, a relative proximity value rather than 30 cm.
- **Jamming or grinding:** press **Back** immediately. Inspect the mechanism with the program stopped; do not force it against a powered motor.
- **Firmware prompt:** record the exact message first. This procedure requires no microSD image or operating-system change. Firmware updates can erase brick programs and are not a substitute for diagnosing the connection.

## Sources and verification

- [Official LEGO R3PTAR build PDF](https://www.lego.com/cdn/cs/set/assets/bltfa9d17de847b8936/31313_R3PTAR_2016.pdf), pages 40, 54, 64 and 94 for wiring.
- Installed LEGO EV3 Home Edition `pack3` projects: mission titles, button labels, program names, A/B/D and sensor 4 settings, threshold and unlimited loop were inspected October 26, 2026.
- Installed LEGO EV3 Home user guide, `Resources\EditorHelp\Retail\en-US\ev3_user_guide.pdf`, pages 7, 9, 18, 25, 38, 42–44: stop button, connectors, USB, brick navigation, missions, download controls and the open-book Content Editor button. The user screenshots confirmed the **Build and Program**, **Open Project…**, **Save Project As…** labels and direct-template opening restriction.
- [LEGO Hardware Page help](https://ev3-help-online.api.education.lego.com/Retail/en-us/page.html?Path=editor/HardwarePage.html): download controls and connection status.

This repository supplies the walkthrough. The LEGO factory program is part of installed EV3 Home software, not a new custom program in `04_Python`. Classroom tuning and physical validation remain separate work.
