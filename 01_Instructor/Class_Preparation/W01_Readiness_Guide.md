# First session: ready to leave

October 27, 2026 | 12 children | Four teams of three | Two SPIKE robots

Start now: charge both SPIKE hubs and all four laptops. While they charge, print the class packet and prepare/test SPIKE App on the two robot laptops. The EV3 snake has a different battery system; check it separately.

## 1. Print this exact set

Print **ONE copy of [W01_Class_Print_Packet.pdf](../../02_Student/Printouts/W01_Class_Print_Packet.pdf)**: US Letter, single-sided, actual size. It already contains every copy below: **30 pages total**. Do not also print the individual files unless you need replacements.

| Paper | Copies/pages to bring | Packet pages | Use |
|---|---|---|---|
| [Baseline](../../02_Student/Printouts/Baseline.pdf) | 14 one-page copies | 1-14 | One per child plus two spares; before coaching |
| [Week 1 team sheet](../../02_Student/Printouts/W01_signal_Team_Sheet.pdf) | 5 one-page copies | 15-19 | One per team plus one spare |
| [Week 1 build card](../../02_Student/Printouts/W01_signal_Build_Card.pdf) | 4 one-page copies | 20-23 | One per team |
| [Attendance](../../02_Student/Printouts/Attendance.pdf) | 1 page | 24 | One class record |
| [Role cards](../../02_Student/Printouts/Role_Cards.pdf) | Two copies of both pages: 4 sheets | 25-28 | Cut into 12 cards; one set per station |
| [Hub color guide](../../06_References/SPIKE_Hub_Color_Guide.pdf) | 2 one-page copies | 29-30 | One per robot station |

Black and white is usable; color is helpful for pages 29-30. Keep the role cards and hub guides for later weeks. Write student IDs on assessment papers and keep completed records private.

Print **one copy of [this readiness guide](W01_Readiness_Guide.pdf)** for yourself if useful: four more sheets, **34 sheets including the class packet**. It replaces the need to print the older one-page packing checklist today.

Keep the [detailed speaker notes](../Speaker_Notes/W01_signal_Speaker_Notes.md) available digitally; a printed [Word copy](../Speaker_Notes/W01_signal_Speaker_Notes.docx) for the lead is optional. Display the [six-slide deck](../../03_Presentations/W01_signal.pdf); do not print a deck or full workbook for every child. Hand-label four station signs and four team trays T1-T4.

<!-- pagebreak -->

## 2. Power: charge before leaving

### Both SPIKE Prime teaching robots

- [ ] Each hub has its special removable LEGO rechargeable pack fitted. SPIKE Prime does **not** take AA batteries. Motors and sensors get power from the hub and need no separate batteries.
- [ ] Plug the supplied **micro-USB cable into the hub**, with the pack installed. Plug the other end into a suitable USB charger or powered computer. Charge both hubs at the same time if possible.
- [ ] Allow roughly **2 hours** with a suitable dedicated charging port; a standard lower-power port can take **4.5-5 hours** from empty. Start now; a few minutes plugged into a laptop is not a full charge.
- [ ] Check the battery indication in SPIKE App before disconnecting. Aim for full charge. A green center button only establishes at least 20% charge, not a full battery. Flashing orange means below 20%.
- [ ] After testing, turn hubs off for transport. Pack both charging cables and USB power supplies. Use the original cables where possible; program transfer requires a tested data cable.

Charging times and light meanings: [LEGO SPIKE Prime FAQ](https://education.lego.com/en-au/product-resources/spike-prime/troubleshooting/faqs/).

### EV3 R3PTAR demonstration

- [ ] Check the underside of the EV3 brick. A normal AA compartment takes **six 1.5 V AA alkaline batteries**. If battery condition is uncertain, fit a fresh matching set and bring **six spare AAs**. Do not mix old and new cells. Regular alkaline AAs are replaced, not charged.
- [ ] If an optional **LEGO EV3 rechargeable battery pack** is fitted instead, charge it using its compatible EV3 charger and pack that charger. Do not assume the Home set contains this pack.
- [ ] The EV3 **mini-USB computer cable does not recharge its batteries**. It is different from the SPIKE micro-USB cable. No microSD card or remote-control beacon is needed for the installed Hunting program.
- [ ] Power the snake on, run its saved program, stop it, and turn it off for transport. Pack it in a supported box with a cardboard target and its mini-USB cable.

Battery references: [LEGO EV3 FAQ](https://education.lego.com/en-us/product-resources/mindstorms-ev3/troubleshooting/faqs/) and [EV3 user guide, battery section](https://www.lego.com/cdn/cs/set/assets/bltbef4d6ce0f40363c/LMSUser_Guide_LEGO_MINDSTORMS_EV3_11_Tablet_ENUS.pdf).

### Laptops

- [ ] Fully charge all four laptops and bring all four chargers. Pack the required USB adapters, display cable/adapter, and a venue-approved power strip/extension lead if needed. Keep power cables outside walking and robot lanes.

<!-- pagebreak -->

## 3. Software: prepare before arriving

Use the **current LEGO Education SPIKE App (App 3 Python)** on the two robot-control laptops. Download it from the [official SPIKE App page](https://education.lego.com/en-us/downloads/spike-app/software/) and select the installer for each laptop's operating system. Installation may require an administrator. Finish it on your own internet connection before class.

The other two laptops only show build/reference PDFs and need a working PDF viewer. Installing SPIKE on all four is useful for backup but optional. The presentation laptop needs a PDF viewer for the slide PDF, or PowerPoint if using the PPTX with Presenter View. No separate Python installation, VS Code, Git, repository clone or LEGO account workflow is part of this lesson setup.

### Prepare each robot-control laptop

1. Open SPIKE App, select **SPIKE Prime**, and create a **Python** project. Do not choose SPIKE Legacy or Word Blocks for the supplied Python file.
2. Download [W01_signal.py](../../04_Python/W01_signal.py) and [00_mentor_smoke_test.py](../../04_Python/00_mentor_smoke_test.py). On GitHub use the raw-file download, not a saved HTML webpage.
3. Open the source file as text and paste the **entire W01_signal.py file** into the Python editor, replacing the default example. The three student lines alone are not a complete program.
4. Connect the charged hub by its tested USB data cable. If the app requests a Hub OS update, complete it **before class** and keep the cable connected until finished. Update only when requested; allow time to retest.
5. Label the physical hubs and matching projects clearly: **Robot A** and **Robot B**. Trace the cables: **left wheel motor A, right wheel motor B**, viewed from behind the robot. Leave the auxiliary motor unplugged. Week 1 needs no distance or color sensor.
6. With wheels raised, run the mentor smoke test in a separate project. Then run the complete Week 1 project: display **Y**, pause, and make one short movement. Set the robot down in a clear lane and verify that forward really is forward. Repeat on the second base.
7. Prove the intended classroom connection on both stations. If using Bluetooth, pair from inside SPIKE App and test; keep USB as backup. Do not let a moving robot pull a tethered laptop.
8. Save/export a known-good starter and demonstrate how mentors will save team copies. Reopen the saved project and run it. Then disconnect internet and confirm the app, projects and references still open.

### Save these files offline

- Both robot laptops: complete Week 1 source, smoke test, saved starter project and [hub guide](../../06_References/SPIKE_Hub_Color_Guide.pdf).
- Both reference laptops: [build card](../../02_Student/Printouts/W01_signal_Build_Card.pdf), hub guide and [base assembly reference](../../06_References/LEGO_Practice_Driving_Base.pdf).
- Presentation/lead laptop: [slide PDF](../../03_Presentations/W01_signal.pdf) or [PPTX with notes](../../03_Presentations/W01_signal_with_speaker_notes.pptx), [speaker notes DOCX](../Speaker_Notes/W01_signal_Speaker_Notes.docx), and this guide. Copy backups to a USB drive.

The snake already has its program. Keep the working **LEGO MINDSTORMS EV3 Home Edition** installation on the computer used yesterday if bringing it for troubleshooting; do not install it on student laptops. Test that R3PTAR starts directly from its brick after power-off. It then needs no laptop to perform. The SPIKE app does not program EV3.

<!-- pagebreak -->

## 4. Pack, rehearse and set the room

### Pack the complete class kit

- [ ] Two assembled SPIKE driving bases, charged and labeled A/B; their two kit boxes and necessary spare parts. Keep both bases assembled for student use.
- [ ] Four charged laptops/four chargers; two tested SPIKE USB data cables plus one spare; two hub charging supplies; any USB/display adapters; slides/display arrangement and power access.
- [ ] Four equal labeled team build packs and four trays. Include spare small Technic beams/pins; keep chassis parts out. Provide four mounting/clearance templates traced from the actual robot and two tested lightweight mentor mascots.
- [ ] Six pre-cut card faces/name flags (four teams plus two examples), 12 brace strips, one box of 12 crayons/markers, two rolls craft tape, two supervised child-safe scissors.
- [ ] 14 sharpened pencils, 14 erasers, two sharpeners, four rulers, two measuring tapes and two rolls removable floor-safe tape.
- [ ] Four clipboards/firm writing surfaces, four labeled storage bags, one private records folder, four station signs and two timers (phone timers are fine).
- [ ] The 30-sheet class packet, optional four-sheet lead guide, transport boxes, and a bag for personal parts to return.
- [ ] R3PTAR, its batteries/charger as applicable, cardboard target and mini-USB cable only after the demonstration rehearsal passes. Keep it separate from student robot lanes.

### Rehearse before departure

- [ ] Both SPIKE bases run the Week 1 sequence using the actual teaching laptops. Mentors can connect, start, stop and save. No required update or installation is left for the classroom.
- [ ] Each mascot attaches to a **stopped** base, clears wheels/buttons/cables, and survives a gentle hand tilt/tap. Prepare the two mentor examples for the teams that use robots before building.
- [ ] Snake: check response to the cardboard target, strike/retraction, retreat/turn, repeatability and the EV3 Back-button stop. Movement alone is not proof of the whole behavior. The stock Hunting program loops indefinitely; the planned automatic time limit remains unimplemented/unverified. Use a brief continuously supervised demonstration only if reliable, stop it manually, and park it. Otherwise use the SPIKE demonstration.

Confirmed October 26: EV3 download and movement. SPIKE tests and the full snake reaction remain unreported.

### Arrive about 30 minutes early

- [ ] Confirm room, adult lead and 4-6 student instructors. Assign two robot mentors and two build mentors; extras float. Confirm attendance/pickup arrangements with YMCA staff and prepare student IDs privately.
- [ ] Set Robot A, Build A, Robot B and Build B stations; T1/T2 share A and T3/T4 share B. Clear two robot lanes. Place all power leads away from feet and wheels.
- [ ] Open saved slides/projects, test the display and one short run per base, place role cards and supplies, and set the baseline sheets aside for the opening activity.

### The hour and closeout

0-5 baseline/welcome; 5-10 demonstrations; 10-14 code/prediction; 14-26 first robot/build turn; 26-38 switch; 38-44 T1/T3 retest; 44-50 T2/T4 retest; 50-54 reflection; 54-60 save/reset. Give the baseline before teaching code. Rotate three roles every four minutes in initial turns and every two minutes in retests.

Save four team projects; collect attendance, baseline and team sheets privately; bag four labeled builds; count parts; switch off hubs; assign who takes each hub/laptop home and charges it for the next session. Keep both teaching bases assembled.
