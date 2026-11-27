# Secret Spawn - 28 Nov 2026 content (Saturday after Thanksgiving)
# Sources (checked 27 Nov 2026; devforum, create.roblox.com, roblox.com, timesaver.gg, ggrecon and the code sites were
# not fetchable from this machine, so web search snippets were used):
#  RIVALS Black Friday sale (first one; up to 40% off select bundles per the game's Roblox listing; 7 bundles: Balloon,
#    Prop (40%), Medkit, Exogun, Nostalgia (30%), Pirate (20%), Standard Weapons; Skin Cases + Key bundles not discounted;
#    runs to Dec 1, 2026 05:00 UTC = Dec 1 12:00 AM ET; start date Nov 24/25 differs by source):
#    roblox.com/games/17625359962/RIVALS ; timesaver.gg/blog/roblox-rivals-black-friday-sale ;
#    u7buy.com/blog/rivals-black-friday-sale/ ; newgame.co.jp/metaverse/en/roblox/17625359962/rivals/events/
#  RIVALS Season 4 Part 2 (live Nov 21 02:00 UTC = Nov 20 9 PM ET): Holodome (dome shield that can't be shot through
#    from inside or outside; 40 Keys; early access for Standard Weapons Bundle owners), Shield Surge mode (1v1/2v2/3v3,
#    50 HP shield), experimental Clash map:
#    u7buy.com/blog/roblox-rivals-season-4/ ; u7buy.com/blog/rivals-holodome-guide/ ;
#    mmoexp.com/News/roblox-rivals-part-2-update-guide-new-clash-map-shield-surge-mode-hollow-dome-weapon-dark-matter.html
#  Overflow (kyo squad) update log Nov 26, 2026 (developer post on the DevForum Bulletin Board): Scythe rework (42 cards
#    + 5 Eclipse cards, 19 new animations, Final Harvest ultimate, new mesh with violet edge), new free Tidecaller Rod
#    (unlocks after catching 10 different fish species; rare+ catch weights x1.5, 15% wider reel zone), style decks now
#    47 cards (was 77+5): devforum.roblox.com/t/overflow-beta-update-log-nov-26-2026/5005208 ;
#    roblox.com/games/75535615558301/Overflow
#  Web Play goes WebGPU (DevForum "Sharper Web Play Rendering With WebGPU", Nov 19, 2026; Weekly Recap Nov 16-20):
#    fixes distorted avatars, missing grass, lighting problems, blurry icons; some test devices without WebGPU dropped;
#    still Creator Beta only (launched Oct 29 in Chrome), no date for players:
#    devforum.roblox.com/t/sharper-web-play-rendering-with-webgpu/4996719 ;
#    devforum.roblox.com/t/weekly-recap-november-16%E2%80%9320-2026/4998199 ;
#    webgpu.com/stories/roblox-web-play-now-renders-with-webgpu/ ; player.one (Web Play beta moves to WebGPU)
#  List: RIVALS sale ends Dec 1 12 AM ET; Fischgiving ends Dec 1 12 PM ET (fischcalculator); Pass Free Trials Dec 2
#    (devforum.roblox.com/t/introducing-pass-free-trials/4995943); Incubator applications due Dec 7 (create.roblox.com)
#  Codes:
#    Overflow FORGOTSCYTHESORRY (30 Style Rolls + 25 Passive Rolls), UPDATEYAY (25 Style + 25 Passive Rolls),
#      ILOVEFISHINGLOL (15 Style + 15 Passive Rolls + 30 min 2x Mastery EXP); join kyo squad group, redeem in Customize:
#      pockettactics.com/overflow-codes ; destructoid.com/overflow-codes/ ; pcgamesn.com/roblox/overflow-codes ;
#      bloxarchive.com/overflow-codes (checked Nov 27)
#    Beyond Nen DECAYSICK (35 Spins; new Nov 26), DECAYGIFT (Clear Negative Nen Orb + Reset Orb + 10 Spins; GamesRadar
#      says 10 Spins + Nen Color Reroll Orb): destructoid.com/beyond-nen-codes/ ; robloxden.com/game-codes/beyond-nen ;
#      mrguider.org/roblox/beyond-nen-codes/ ; tryhardguides.com/beyond-nen-codes/
#    Stand Out THANKFULFORSTANDOUT, REAL200KLIKES (arrows + Dalas; amounts differ: Beebom 3 Mysterious Arrows + 1 Lucky
#      Arrow + 3 Arrow Parts + 333 Dalas; RobloxDen 3 Mysterious Arrows + 500 Dalas + 2x EXP / 2 Bizarre Arrows + 4,000
#      Dalas; Studio Umbra: Europa group + tutorial): beebom.com/stand-out-codes/ (Nov 27) ; robloxden.com/game-codes/stand-out
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("RIVALS BLACK", "white"), ("FRIDAY SALE", "yellow")], "tag": "SALE",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*RIVALS* just got its *first* ever *Black Friday* sale. Here are *three* things to know."},
   {"type": "item", "n": 1, "bg": "red", "acc": "yellow", "game": "RIVALS", "icon": "tag", "badge": "40% OFF",
    "title": "UP TO 40% OFF",
    "vo": "Number *one*. Select *bundles* are up to *forty percent* off until *December first*."},
   {"type": "item", "n": 2, "bg": "blue", "acc": "blue", "game": "RIVALS", "icon": "shield", "badge": "NEW",
    "title": "THE HOLODOME",
    "vo": "Number *two*. The new *Holodome* makes a *shield dome* that bullets can't get *through*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "orange", "game": "RIVALS", "icon": "bolt", "badge": "NEW MODE",
    "title": "SHIELD SURGE",
    "vo": "Number *three*. *Shield Surge* is a new mode in *one v one*, *two v two*, and *three v three*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WILL YOU BUY", "white"), ("A BUNDLE?", "yellow")],
    "vo": "So, are *you* grabbing a *bundle*? Tell me in the *comments*."},
  ]},
 "short2": {
  "title_lines": [("3 NEW ROBLOX", "white"), ("SPIN CODES", "yellow")], "tag": "NEW CODES",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Here are *three* brand new Roblox codes you *missed* this week."},
   {"type": "item", "n": 1, "bg": "maroon", "acc": "yellow", "game": "BEYOND NEN", "icon": "sparkles", "badge": "NEW",
    "title": "35 FREE SPINS", "code": "DECAYSICK",
    "vo": "First, *Beyond Nen*. Code *decay sick* gives *thirty five* free *spins*."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "pink", "game": "BEYOND NEN", "icon": "gem", "badge": "NEW",
    "title": "ORBS + 10 SPINS", "code": "DECAYGIFT",
    "vo": "Next, code *decay gift* gives two *orbs* and *ten* more *spins*."},
   {"type": "item", "n": 3, "bg": "blue", "acc": "orange", "game": "STAND OUT", "icon": "arrow", "badge": "NEW",
    "title": "FREE ARROWS", "code": "THANKFULFORSTANDOUT",
    "vo": "And *Stand Out*. Code *thankful for stand out* gives free *arrows* and *Dalas*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("WORKED?", "yellow")],
    "vo": "Codes can *expire* fast, so be *quick*. Which one *worked* for you?"},
  ]},
 "short3": {
  "title_lines": [("3 OVERFLOW", "white"), ("CODES", "yellow")], "tag": "NEW CODES",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Overflow* just updated, and it dropped *three* new codes. Here they *are*."},
   {"type": "item", "n": 1, "bg": "navy", "acc": "pink", "game": "OVERFLOW", "icon": "dice", "badge": "NEWEST",
    "title": "55 FREE ROLLS", "code": "FORGOTSCYTHESORRY",
    "vo": "Number *one*. *Forgot scythe sorry* gives *fifty five* style and passive *rolls*."},
   {"type": "item", "n": 2, "bg": "green", "acc": "yellow", "game": "OVERFLOW", "icon": "card", "badge": "NEW",
    "title": "50 FREE ROLLS", "code": "UPDATEYAY",
    "vo": "Number *two*. *Update yay* gives *twenty five* of each *roll*."},
   {"type": "item", "n": 3, "bg": "blue", "acc": "blue", "game": "OVERFLOW", "icon": "fish", "badge": "2X EXP",
    "title": "ROLLS + 2X EXP", "code": "ILOVEFISHINGLOL",
    "vo": "Number *three*. *I love fishing lol* gives rolls and *double* mastery *EXP*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT STYLE", "white"), ("DID YOU GET?", "yellow")],
    "vo": "What *style* did *you* roll? Tell me *below*."},
  ]},
}

LONG = {
 "thumb": [("RIVALS SALE", "white"), ("+ 7 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 28",
   "vo": "Here's today's *Roblox news*. *RIVALS* has its first *Black Friday* sale, *Overflow* reworked the *scythe*, Web Play got *sharper*, and I've got *seven new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "red", "acc": "yellow", "game": "RIVALS", "icon": "tag", "badge": "40% OFF",
   "title": "BLACK FRIDAY SALE",
   "bullets": ["UP TO 40% OFF 7 BUNDLES", "NO SALE ON SKIN CASES OR KEYS", "NEW: HOLODOME + SHIELD SURGE", "SALE ENDS DEC 1, 12 AM ET"],
   "vo": "Number *one*. *RIVALS* is running its *first* ever *Black Friday* sale, with up to *forty percent* off *seven* bundles. Skin *cases* and *key* bundles are not on sale. This comes right after *Season four Part two*, which added the *Holodome* shield and a new *Shield Surge* mode. The sale runs until *December first*."},
  {"type": "item", "n": 2, "bg": "navy", "acc": "pink", "game": "OVERFLOW", "icon": "swords", "badge": "NOV 26",
   "title": "SCYTHE REWORK",
   "bullets": ["SCYTHE: 42 CARDS + 5 ECLIPSE", "19 NEW ANIMATIONS", "FREE TIDECALLER ROD", "CATCH 10 FISH SPECIES"],
   "vo": "Number *two*. *Overflow* posted a big *update* log on *November twenty sixth*. The *scythe* got a full rework, with *nineteen* new animations and a new *ultimate*. There's also a free *Tidecaller Rod*. It unlocks when you catch *ten* different *fish* species."},
  {"type": "item", "n": 3, "bg": "blue", "acc": "green", "game": "WEB PLAY", "icon": "globe", "badge": "BETA",
   "title": "WEB PLAY GETS SHARPER",
   "bullets": ["NOW RENDERS WITH WEBGPU", "FIXES AVATARS, GRASS + LIGHTING", "STILL CREATOR BETA ONLY"],
   "vo": "Number *three*. Roblox *Web Play* now uses *WebGPU*. That fixes weird *avatars*, missing *grass*, and *lighting* bugs in the browser. It's still a *creator beta*, so players can't use it *yet*, and there's no *release* date."},
  {"type": "item", "n": 4, "bg": "green", "acc": "yellow", "game": "OVERFLOW", "icon": "dice", "badge": "3 CODES",
   "title": "FREE STYLE ROLLS", "code": "FORGOTSCYTHESORRY",
   "bullets": ["FORGOTSCYTHESORRY: 55 ROLLS", "UPDATEYAY: 50 ROLLS", "ILOVEFISHINGLOL: ROLLS + 2X EXP"],
   "vo": "Now, *codes*. Number *four*. *Overflow* has *three*: *forgot scythe sorry*, *update yay*, and *I love fishing lol*, for free style and passive *rolls*."},
  {"type": "item", "n": 5, "bg": "maroon", "acc": "orange", "game": "BEYOND NEN", "icon": "sparkles", "badge": "2 CODES",
   "title": "FREE SPINS + ORBS", "code": "DECAYSICK",
   "bullets": ["DECAYSICK: 35 SPINS", "DECAYGIFT: 2 ORBS + 10 SPINS"],
   "vo": "Number *five*. *Beyond Nen* has *decay sick* for *thirty five* spins, and *decay gift* for two *orbs* and *ten* spins."},
  {"type": "item", "n": 6, "bg": "violet", "acc": "blue", "game": "STAND OUT", "icon": "arrow", "badge": "2 CODES",
   "title": "FREE ARROWS", "code": "REAL200KLIKES",
   "bullets": ["THANKFULFORSTANDOUT: ARROWS + DALAS", "REAL200KLIKES: ARROWS + DALAS"],
   "vo": "And number *six*. *Stand Out* has *thankful for stand out* and *real two hundred K likes*, for free *arrows* and *Dalas*."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("RIVALS SALE ENDS", "DEC 1"), ("FISCHGIVING ENDS", "DEC 1"),
            ("PASS FREE TRIALS GO LIVE", "DEC 2"), ("INCUBATOR DEADLINE", "DEC 7")],
   "vo": "Coming up. The *RIVALS* sale and *Fischgiving* both end *December first*, pass *free trials* go live *December second*, and *Incubator* applications close *December seventh*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT ARE YOU", "white"), ("PLAYING TODAY?", "yellow")],
   "vo": "That's *today's* news. What are you playing this *weekend*? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-28_1900_Short_RivalsBlackFriday", "schedule_ist": "2026-11-28 19:00",
            "title": "RIVALS Has Its First Black Friday Sale! 🛒 #roblox #shorts",
            "description": "RIVALS is running its first Black Friday sale: up to 40% off select bundles until Dec 1 (12 AM ET). It comes after Season 4 Part 2, which added the Holodome shield and the new Shield Surge mode in 1v1, 2v2 and 3v3. Times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long": {"file": "SS_2026-11-28_2300_Long_NewsToday", "schedule_ist": "2026-11-28 23:00",
          "title": "Roblox News Today: RIVALS Black Friday Sale, Overflow Scythe Rework & 7 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: RIVALS is running its first Black Friday sale with up to 40% off 7 bundles (ends Dec 1, 12 AM ET) after Season 4 Part 2 added the Holodome and Shield Surge, Overflow's Nov 26 update reworked the Scythe and added a free Tidecaller Rod, and Roblox Web Play (still a creator beta) now renders with WebGPU for sharper avatars, grass and lighting. Plus 3 games have 7 new codes.\n\nChapters:\n0:00 Intro\n0:11 RIVALS Black Friday Sale + Season 4 Part 2\n0:30 Overflow Scythe Rework + Tidecaller Rod\n0:46 Roblox Web Play Switches to WebGPU\n1:01 Overflow, Beyond Nen + Stand Out Codes\n1:26 Coming Up + Outro\n\nCodes in this video:\nOverflow: FORGOTSCYTHESORRY (30 Style Rolls + 25 Passive Rolls), UPDATEYAY (25 Style Rolls + 25 Passive Rolls), ILOVEFISHINGLOL (15 Style Rolls + 15 Passive Rolls + 30 min 2x Mastery EXP)\nBeyond Nen: DECAYSICK (35 Spins), DECAYGIFT (Clear Negative Nen Orb + Reset Orb + 10 Spins)\nStand Out: THANKFULFORSTANDOUT, REAL200KLIKES (free Arrows + Dalas; amounts vary by source; join the Studio Umbra: Europa group)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "rivals", "rivals black friday", "roblox black friday", "overflow", "overflow update", "roblox web play", "overflow codes", "beyond nen codes", "stand out codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-29_0100_Short_SpinCodes", "schedule_ist": "2026-11-29 01:00",
            "title": "3 New Roblox Codes You Missed This Week 👀 #roblox #shorts",
            "description": "3 Roblox codes:\nBeyond Nen: DECAYSICK (35 Spins)\nBeyond Nen: DECAYGIFT (Clear Negative Nen Orb + Reset Orb + 10 Spins)\nStand Out: THANKFULFORSTANDOUT (free Arrows + Dalas; join the Studio Umbra: Europa group)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-29_0300_Short_OverflowCodes", "schedule_ist": "2026-11-29 03:00",
            "title": "3 FREE Overflow Codes Just Dropped 💎 #roblox #shorts",
            "description": "3 Overflow codes after the Nov 26 Scythe update:\nOverflow: FORGOTSCYTHESORRY (30 Style Rolls + 25 Passive Rolls)\nOverflow: UPDATEYAY (25 Style Rolls + 25 Passive Rolls)\nOverflow: ILOVEFISHINGLOL (15 Style Rolls + 15 Passive Rolls + 30 min 2x Mastery EXP)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
}
