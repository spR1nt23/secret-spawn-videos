# Secret Spawn - 17 Nov 2026 content
# Sources (checked 16 Nov 2026; roblox.com / devforum / news sites were not fetchable here, so search snippets were used):
#  Grow a Garden Anubis Part 2 (~Nov 14): Ancient Trials (submit fruits with a trait that rotates hourly, fill the bar
#    alone or with the server, one of 3 obbies, open ~20 min), Golden Chest + Anubis Crafting Bench at the end,
#    Anubis Seed Pack (5 possible seeds):
#    sportskeeda.com/roblox-news/grow-garden-anubis-part-2-update-patch-notes ; part 2 preview: gamer.org/grow-a-garden-anubis-event-new-seeds-pets-gears-cosmetics/
#  A Bizarre Run Stage 3 + Scary Monsters update (Nov 13 UTC): third racing stage, automatic teammate assignment,
#    Scary Monsters and Wired stands: sportskeeda.com/roblox-news/a-bizarre-run-stage-3-scary-monsters-update-patch-notes
#  Free creator Roblox Plus grant ends Nov 19 2026, upgrade by Dec 19 to keep it without interruption:
#    create.roblox.com/updates (search snippet)
#  Codes:
#    Beyond Nen 1MVISITS (20 spins), 50KFAVS (15 spins), RANKED! (15 spins + reset orb), join group:
#      gamesradar.com/games/rpg/beyond-nen-codes/, destructoid.com/beyond-nen-codes/ (Nov 15), beebom.com/beyond-nen-codes/
#    A Bizarre Run WIRED, SCARYMONSTERS, SHUTDOWNSORRY (arrows + Rokakaka; amounts differ by source):
#      pcgamesn.com/roblox/a-bizarre-run-codes (Nov 15), pockettactics.com/a-bizarre-run-codes, thenews.com.pk (Stage 3 codes)
#    Shibuya 5MVISITS, sryforsd, balancepatch2 (rerolls; tied to the character you're editing):
#      gamerant.com/shibuya-codes-roblox/ (Nov 15), destructoid shibuya codes (Nov 15, via worldplace.ai), mrguider.org (sryforsd, Nov 15)
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("GROW A GARDEN", "white"), ("ANUBIS PART 2", "yellow")], "tag": "OUT NOW",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Grow a Garden* just dropped *Anubis Part Two*. Here are *three* things to know."},
   {"type": "item", "n": 1, "bg": "green", "acc": "green", "game": "GROW A GARDEN", "icon": "pyramid", "badge": "NEW",
    "title": "ANCIENT TRIALS",
    "vo": "Number *one*. Turn in fruits with the *right trait* to open the *Ancient Trials*. The trait *changes every hour*."},
   {"type": "item", "n": 2, "bg": "navy", "acc": "yellow", "game": "ANCIENT TRIALS", "icon": "bolt", "badge": "20 MIN",
    "title": "TEAM UP FOR AN OBBY",
    "vo": "Number *two*. Your *whole server* can fill the bar together, then beat one of *three obbies* in about *twenty minutes*."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "GROW A GARDEN", "icon": "mystery", "badge": "REWARDS",
    "title": "GOLDEN CHEST + CRAFTING",
    "vo": "Number *three*. Finish it for a *Golden Chest* and the *Anubis Crafting Bench*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WILL YOU", "white"), ("TRY IT?", "yellow")],
    "vo": "Are you running the *trials* tonight? Tell me *below*."},
  ]},
 "short2": {
  "title_lines": [("3 NEW ROBLOX", "white"), ("CODES", "yellow")], "tag": "FRESH DROP",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Three* fresh Roblox codes for *free spins* and *rerolls*. Grab them *before* they *expire*."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "BEYOND NEN", "icon": "gem", "badge": "NEW",
    "title": "20 FREE SPINS", "code": "1MVISITS",
    "vo": "First, *Beyond Nen*. Code *one M visits* gives *twenty spins*."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "purple", "game": "A BIZARRE RUN", "icon": "bolt", "badge": "NEW",
    "title": "ARROWS + ROKAS", "code": "WIRED",
    "vo": "Next, *A Bizarre Run*. Code *wired* gives *arrows* and *Rokakaka* fruit."},
   {"type": "item", "n": 3, "bg": "red", "acc": "pink", "game": "SHIBUYA", "icon": "swords", "badge": "NEW",
    "title": "FREE REROLLS", "code": "5MVISITS",
    "vo": "*Shibuya*. Code *five M visits* gives *free rerolls*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("FIRST?", "yellow")],
    "vo": "Codes *expire fast*, so redeem them *now*. Which game are *you* playing *first*?"},
  ]},
 "short3": {
  "title_lines": [("3 MORE ROBLOX", "white"), ("CODES", "yellow")], "tag": "LATE NIGHT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Still up? Here are *three more* Roblox codes. Type them in *exactly*."},
   {"type": "item", "n": 1, "bg": "green", "acc": "green", "game": "BEYOND NEN", "icon": "trophy", "badge": "NEW",
    "title": "SPINS + RESET ORB", "code": "RANKED!",
    "vo": "First, *Beyond Nen*. Code *ranked*, with an *exclamation mark*, gives *fifteen spins* and a *reset orb*."},
   {"type": "item", "n": 2, "bg": "navy", "acc": "yellow", "game": "A BIZARRE RUN", "icon": "mystery", "badge": "NEW",
    "title": "ARROWS + ROKAS", "code": "SCARYMONSTERS",
    "vo": "*A Bizarre Run*. Code *scary monsters* gives *arrows* and *Rokas*."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "SHIBUYA", "icon": "flame", "badge": "NEW",
    "title": "FREE REROLLS", "code": "sryforsd",
    "vo": "*Shibuya*. Code *S R Y for S D*, all *lowercase*, gives *rerolls*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT DID", "white"), ("YOU GET?", "yellow")],
    "vo": "Redeem them *fast*, they can *expire*. What did *you* get? Tell me *below*."},
  ]},
}

LONG = {
 "thumb": [("ANUBIS PART 2", "white"), ("+ 9 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 17",
   "vo": "Here's today's *Roblox news*. *Grow a Garden* opened the *Ancient Trials*, *A Bizarre Run* added *Stage Three*, free creator *Plus* is almost over, and I've got *nine new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "green", "acc": "green", "game": "GROW A GARDEN", "icon": "pyramid", "badge": "PART 2",
   "title": "ANUBIS PART 2 IS OUT",
   "bullets": ["ANCIENT TRIALS: TURN IN FRUITS", "TRAIT CHANGES EVERY HOUR", "GOLDEN CHEST + CRAFTING BENCH"],
   "vo": "Number *one*. *Grow a Garden* released *Anubis Part Two*. Turn in fruits with the *right trait* to open the *Ancient Trials*, and the trait *changes every hour*. Your *server* can team up, then beat one of *three obbies* in about *twenty minutes* for a *Golden Chest* and the *Anubis Crafting Bench*."},
  {"type": "item", "n": 2, "bg": "violet", "acc": "purple", "game": "A BIZARRE RUN", "icon": "bolt", "badge": "STAGE 3",
   "title": "STAGE 3 + NEW STANDS",
   "bullets": ["NEW THIRD RACING STAGE", "AUTO TEAMMATE ASSIGNMENT", "SCARY MONSTERS + WIRED STANDS"],
   "vo": "Number *two*. *A Bizarre Run* added *Stage Three*, a *new racing stage*. Teammates are now *assigned automatically*, and there are *two new stands*, *Scary Monsters* and *Wired*."},
  {"type": "item", "n": 3, "bg": "blue", "acc": "yellow", "game": "ROBLOX PLUS", "icon": "tag", "badge": "NOV 19",
   "title": "FREE CREATOR PLUS ENDS",
   "bullets": ["FREE 6-MONTH GRANT ENDS NOV 19", "UPGRADE BY DEC 19", "TO KEEP PLUS WITHOUT A BREAK"],
   "vo": "Number *three*. If you got *free Roblox Plus* as a *creator*, it ends this *Thursday*, *November nineteenth*. Roblox says you have until *December nineteenth* to *upgrade* and keep it *without a break*."},
  {"type": "item", "n": 4, "bg": "navy", "acc": "blue", "game": "BEYOND NEN", "icon": "gem", "badge": "CODES",
   "title": "50 FREE SPINS", "code": "1MVISITS",
   "bullets": ["1MVISITS: 20 SPINS", "50KFAVS: 15 SPINS", "RANKED!: 15 SPINS + RESET ORB"],
   "vo": "Now, *codes*. Number *four*. *Beyond Nen* has *one M visits*, *fifty K favs*, and *ranked* with an *exclamation mark*. That's *fifty spins* total. Join the *group* first."},
  {"type": "item", "n": 5, "bg": "maroon", "acc": "orange", "game": "A BIZARRE RUN", "icon": "mystery", "badge": "CODES",
   "title": "ARROWS + ROKAS", "code": "WIRED",
   "bullets": ["WIRED: ARROWS + ROKAS", "SCARYMONSTERS: ARROWS + ROKAS", "SHUTDOWNSORRY: ARROWS + ROKAS"],
   "vo": "Number *five*. *A Bizarre Run* has *wired*, *scary monsters*, and *shutdown sorry*, for *arrows* and *Rokakaka* fruit."},
  {"type": "item", "n": 6, "bg": "red", "acc": "pink", "game": "SHIBUYA", "icon": "swords", "badge": "CODES",
   "title": "FREE REROLLS", "code": "5MVISITS",
   "bullets": ["5MVISITS: REROLLS", "sryforsd: REROLLS", "balancepatch2: REROLLS"],
   "vo": "And number *six*. *Shibuya* has *five M visits*, *S R Y for S D*, and *balance patch two*, all for *rerolls*. Codes count for the *character* you're editing."},
  {"type": "list", "bg": "green", "acc": "green", "head": "COMING UP",
   "rows": [("FREE CREATOR PLUS ENDS", "NOV 19"), ("INCUBATOR DEADLINE", "DEC 7"),
            ("GAME AWARDS ON ROBLOX", "DEC 10"), ("PLUS UPGRADE DEADLINE", "DEC 19")],
   "vo": "Coming up. Free creator *Plus* ends *November nineteenth*, the *Incubator* deadline is *December seventh*, *The Game Awards* hit Roblox on *December tenth*, and the *Plus upgrade* window closes *December nineteenth*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH UPDATE", "white"), ("WINS?", "yellow")],
   "vo": "That's *today's* news. Which update are *you* playing first? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-17_1900_Short_AnubisPart2", "schedule_ist": "2026-11-17 19:00",
            "title": "Grow a Garden Anubis Part 2 Is Here! 🏺 #roblox #shorts",
            "description": "Grow a Garden released Anubis Part 2. Turn in fruits with the right trait (it changes every hour) to open the Ancient Trials, team up with your server, and beat one of three obbies in about 20 minutes for a Golden Chest and the Anubis Crafting Bench.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #growagarden #shorts"},
 "long": {"file": "SS_2026-11-17_2300_Long_NewsToday", "schedule_ist": "2026-11-17 23:00",
          "title": "Roblox News Today: Grow a Garden Anubis Part 2, A Bizarre Run Stage 3 & 9 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: Grow a Garden released Anubis Part 2 with the new Ancient Trials, A Bizarre Run added Stage 3 with the Scary Monsters and Wired stands, the free 6-month Roblox Plus grant for creators ends Thursday, November 19 (upgrade by December 19 to keep it), and 3 games have new codes.\n\nChapters:\n0:00 Intro\n0:12 Grow a Garden Anubis Part 2\n0:30 A Bizarre Run Stage 3\n0:41 Free Creator Plus Ends\n0:54 Beyond Nen Codes\n1:05 A Bizarre Run + Shibuya Codes\n1:23 Coming Up\n1:37 Outro\n\nCodes in this video:\nBeyond Nen: 1MVISITS (20 spins), 50KFAVS (15 spins), RANKED! (15 spins + reset orb)\nA Bizarre Run: WIRED (arrows + Rokakaka), SCARYMONSTERS (arrows + Rokakaka), SHUTDOWNSORRY (arrows + Rokakaka)\nShibuya: 5MVISITS (rerolls), sryforsd (rerolls), balancepatch2 (rerolls)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "grow a garden", "grow a garden anubis", "a bizarre run", "roblox plus", "beyond nen codes", "a bizarre run codes", "shibuya codes", "secret spawn", "roblox news today", "grow a garden update"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-18_0100_Short_NewCodes", "schedule_ist": "2026-11-18 01:00",
            "title": "3 Fresh Roblox Codes for Free Spins & Rerolls! 🎁 #roblox #shorts",
            "description": "3 Roblox codes:\nBeyond Nen: 1MVISITS (20 spins)\nA Bizarre Run: WIRED (arrows + Rokakaka)\nShibuya: 5MVISITS (rerolls)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-18_0300_Short_LateNightCodes", "schedule_ist": "2026-11-18 03:00",
            "title": "3 More Roblox Codes Before They Expire! ⏰ #roblox #shorts",
            "description": "3 more Roblox codes:\nBeyond Nen: RANKED! (15 spins + reset orb)\nA Bizarre Run: SCARYMONSTERS (arrows + Rokakaka)\nShibuya: sryforsd (rerolls)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
}
