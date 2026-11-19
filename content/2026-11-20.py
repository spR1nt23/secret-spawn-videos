# Secret Spawn - 20 Nov 2026 content
# Sources (checked 19 Nov 2026; devforum / create.roblox.com / fandom / news & code sites were not fetchable here,
# so web search snippets were used):
#  The Takeback (Roblox mini event, Nov 16-23, 2026; Emergency Hamburg -> Notoriety -> Jailbreak, start in The Block,
#    free UGC: Elbe Jewels Diamond Chain, Gold Metallic Comedy Mask, Diamond Duffel Bag; Jailbreak quest ends
#    Nov 23 19:00 UTC = 2:00 PM ET):
#    roblox.fandom.com/wiki/The_Takeback ; jailbreak.fandom.com/wiki/The_Takeback_Event ;
#    x.com/Blox_Feed/status/2122330716986057026 ; progameguides.com/roblox/how-to-get-the-gold-metallic-comedy-mask-in-the-takeback-roblox-event/ ;
#    u7buy.com/blog/roblox-the-takeback-event-guide/ ; aprasi.com/blogs/trending-topics/roblox-the-takeback-event
#  Revolver Arena Thanksgiving event (scheduled Sun Nov 22, 1:00 PM ET -> Nov 29, 1:00 PM ET; Roblox event listing):
#    allthings.how/?p=356515 (updated Nov 14) - single source, said as "scheduled"
#  Studio: Copy and Paste Instances as JSON (Nov 18; instances, properties, attributes, tags; no descendants yet):
#    devforum.roblox.com/t/copy-and-paste-instances-as-json-in-studio/4996012 ; create.roblox.com/updates
#  Codes:
#    Start Your Blue Lock Career MANYFIXES (10 Weapon Spins, 10 Flow Spins, 4 Lucky Weapon Spins, 4 Lucky Flow Spins):
#      progameguides.com/roblox/start-your-blue-lock-career-codes/ (Nov 18), destructoid.com/start-your-blue-lock-career-codes/,
#      mrguider.org/roblox/start-your-blue-lock-career-codes/ (added Nov 17)
#    RIVALS FREE205 (3 Keys): progameguides.com/roblox/rivals-codes/ , ofzenandcomputing.com/roblox-rivals-codes/ ,
#      igeeksblog.com/roblox-rivals-codes/ (FREE206 only one source -> not used)
#    Salvation PERMCLASSRESET (Class Reset Token), HEREISPERMPATHRESET (1 Locked Path Reset):
#      progameguides.com/roblox/salvation-codes/ (Nov 18), destructoid.com/salvation-codes/, twinfinite.net/codes/salvation-codes/
#    Cultivation Unbound ABZZBIRTHDAY (1M Silver + 20 Primordial Stones):
#      progameguides.com/roblox/cultivation-unbound-codes/ , pcgamesn.com/roblox/cultivation-unbound-codes (Nov 18)
#    Stand Out SORRY4SHUTDOWN (500 Dalas + 2 Mysterious Arrows): beebom.com/stand-out-codes/ (new Nov 16),
#      dexerto.com/roblox/stand-out-codes-3429244/ (Nov 18), rosenberryrooms.com/?p=373691
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("THE TAKEBACK", "white"), ("FREE ITEMS", "yellow")], "tag": "EVENT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Roblox has a secret *heist event* with *three free items*, and it ends *Monday*."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "EMERGENCY HAMBURG", "icon": "gem", "badge": "FREE",
    "title": "DIAMOND CHAIN",
    "vo": "Number *one*. Start in *The Block*, then finish *Emergency Hamburg* for a free *diamond chain*."},
   {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "NOTORIETY", "icon": "mystery", "badge": "CHAPTER 2",
    "title": "GOLD COMEDY MASK",
    "vo": "Number *two*. Chapter two in *Notoriety* gives a *gold comedy mask*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "JAILBREAK", "icon": "car", "badge": "ENDS NOV 23",
    "title": "DIAMOND DUFFEL BAG",
    "vo": "Number *three*. Finish *Jailbreak* for a *diamond duffel bag*, before *two P M Eastern* on *Monday*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ITEM", "white"), ("DO YOU WANT?", "yellow")],
    "vo": "Which item do *you* want most? Tell me *below*."},
  ]},
 "short2": {
  "title_lines": [("3 ROBLOX CODES", "white"), ("JUST DROPPED", "yellow")], "tag": "NEW TODAY",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Three* Roblox codes just *dropped* for *spins*, *silver* and *resets*. Type them *exactly*."},
   {"type": "item", "n": 1, "bg": "green", "acc": "green", "game": "START YOUR BLUE LOCK CAREER", "icon": "ball", "badge": "NEW",
    "title": "FREE FLOW SPINS", "code": "MANYFIXES",
    "vo": "First, *Blue Lock Career*. Code *many fixes* gives *weapon spins* and *flow spins*."},
   {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "CULTIVATION UNBOUND", "icon": "flame", "badge": "NEW",
    "title": "1M SILVER", "code": "ABZZBIRTHDAY",
    "vo": "Next, *Cultivation Unbound*. Code *A B Z Z birthday* gives *one million silver*."},
   {"type": "item", "n": 3, "bg": "navy", "acc": "blue", "game": "SALVATION", "icon": "scroll", "badge": "ALPHA",
    "title": "FREE PATH RESET", "code": "HEREISPERMPATHRESET",
    "vo": "And *Salvation*. Code *here is perm path reset* gives a *locked path reset*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("FIRST?", "yellow")],
    "vo": "Codes *expire fast*, so redeem them *now*. Which one is *first*?"},
  ]},
 "short3": {
  "title_lines": [("3 LATE NIGHT", "white"), ("ROBLOX CODES", "yellow")], "tag": "LATE NIGHT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Can't *sleep*? Grab these *three* Roblox codes *before* they're gone."},
   {"type": "item", "n": 1, "bg": "red", "acc": "pink", "game": "RIVALS", "icon": "swords", "badge": "NEW",
    "title": "3 FREE KEYS", "code": "FREE205",
    "vo": "First, *Rivals*. Code *free two oh five* gives *three keys*."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "purple", "game": "STAND OUT", "icon": "arrow", "badge": "NEW",
    "title": "500 DALAS", "code": "SORRY4SHUTDOWN",
    "vo": "*Stand Out*. Code *sorry for shutdown* gives *five hundred Dalas* and *two arrows*."},
   {"type": "item", "n": 3, "bg": "blue", "acc": "yellow", "game": "SALVATION", "icon": "shield", "badge": "ALPHA",
    "title": "CLASS RESET", "code": "PERMCLASSRESET",
    "vo": "And *Salvation*. Code *perm class reset* gives a *class reset token*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT DID", "white"), ("YOU GET?", "yellow")],
    "vo": "Redeem them *fast*, they can *expire*. What did *you* get?"},
  ]},
}

LONG = {
 "thumb": [("THE TAKEBACK EVENT", "white"), ("+ 4 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 20",
   "vo": "Here's today's *Roblox news*. A secret *heist event* is giving out *free items*, *Revolver Arena* has a *Thanksgiving* event coming, *Studio* got a handy new trick, and I've got *four new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "THE TAKEBACK", "icon": "gem", "badge": "ENDS NOV 23",
   "title": "THE TAKEBACK EVENT",
   "bullets": ["START IN THE BLOCK", "HAMBURG > NOTORIETY > JAILBREAK", "3 FREE AVATAR ITEMS"],
   "vo": "Number *one*. *The Takeback* is a Roblox *mini event* across *three games*. You start in *The Block*, then play *Emergency Hamburg*, *Notoriety*, and *Jailbreak* in order. Each chapter gives a free item, like a *diamond chain*, a *gold comedy mask*, and a *diamond duffel bag*. It wraps up *Monday* at *two P M Eastern*."},
  {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "REVOLVER ARENA", "icon": "cake", "badge": "NOV 22",
   "title": "THANKSGIVING EVENT",
   "bullets": ["STARTS SUN NOV 22, 1 PM ET", "RUNS FOR ONE WEEK", "ENDS NOV 29"],
   "vo": "Number *two*. *Revolver Arena* has a *Thanksgiving event* scheduled for *Sunday*. It's set to start at *one P M Eastern* on *November twenty second*. It runs for a *full week*, until *November twenty ninth*."},
  {"type": "item", "n": 3, "bg": "green", "acc": "yellow", "game": "ROBLOX STUDIO", "icon": "scroll", "badge": "NEW",
   "title": "COPY AS JSON",
   "bullets": ["COPY PARTS AS PLAIN TEXT", "PROPERTIES, ATTRIBUTES, TAGS", "NO CHILD OBJECTS YET"],
   "vo": "Number *three*, for *creators*. *Studio* can now *copy and paste* objects as plain text called *JSON*. That includes their *properties*, *attributes* and *tags*, so you can *edit lots of parts* at once. Child objects aren't supported *yet*."},
  {"type": "item", "n": 4, "bg": "navy", "acc": "green", "game": "START YOUR BLUE LOCK CAREER", "icon": "ball", "badge": "CODE",
   "title": "FREE SPINS", "code": "MANYFIXES",
   "bullets": ["MANYFIXES: 10 WEAPON + 10 FLOW SPINS", "+ 4 LUCKY WEAPON + 4 LUCKY FLOW"],
   "vo": "Now, *codes*. Number *four*. *Start Your Blue Lock Career* has *many fixes* for *weapon spins*, *flow spins*, and *lucky spins*."},
  {"type": "item", "n": 5, "bg": "red", "acc": "pink", "game": "RIVALS", "icon": "swords", "badge": "CODE",
   "title": "3 FREE KEYS", "code": "FREE205",
   "bullets": ["FREE205: 3 KEYS"],
   "vo": "Number *five*. *Rivals* has *free two oh five* for *three keys*."},
  {"type": "item", "n": 6, "bg": "violet", "acc": "purple", "game": "SALVATION", "icon": "shield", "badge": "ALPHA",
   "title": "FREE RESETS", "code": "PERMCLASSRESET",
   "bullets": ["PERMCLASSRESET: CLASS RESET", "HEREISPERMPATHRESET: PATH RESET"],
   "vo": "And number *six*. *Salvation* is in *early alpha*. Use *perm class reset* for a *class reset*, and *here is perm path reset* for a *path reset*."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("REVOLVER ARENA THANKSGIVING", "NOV 22"), ("THE TAKEBACK ENDS", "NOV 23"),
            ("INCUBATOR DEADLINE", "DEC 7"), ("GAME AWARDS ON ROBLOX", "DEC 10")],
   "vo": "Coming up. *Revolver Arena's* Thanksgiving event starts *Sunday*, *The Takeback* ends *Monday*, the *Incubator* deadline is *December seventh*, and *The Game Awards* hit Roblox on *December tenth*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("DID YOU GET", "white"), ("THE ITEMS?", "yellow")],
   "vo": "That's *today's* news. Did *you* get the Takeback items? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-20_1900_Short_TheTakeback", "schedule_ist": "2026-11-20 19:00",
            "title": "Roblox's Secret Heist Event Has 3 FREE Items! 💎 #roblox #shorts",
            "description": "The Takeback is a Roblox mini event across Emergency Hamburg, Notoriety and Jailbreak. Start in The Block, finish each chapter and get a free Diamond Chain, Gold Comedy Mask and Diamond Duffel Bag. It ends Monday, Nov 23 at 2 PM ET (times are in Eastern Time and can change).\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long": {"file": "SS_2026-11-20_2300_Long_NewsToday", "schedule_ist": "2026-11-20 23:00",
          "title": "Roblox News Today: The Takeback Event, Revolver Arena Thanksgiving & 4 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: The Takeback mini event gives 3 free avatar items across Emergency Hamburg, Notoriety and Jailbreak (ends Nov 23, 2 PM ET), Revolver Arena's Thanksgiving event is scheduled for Sunday, Nov 22 at 1 PM ET, Roblox Studio can now copy and paste objects as JSON, and 3 games have new codes.\n\nChapters:\n0:00 Intro\n0:13 The Takeback Event\n0:34 Revolver Arena Thanksgiving\n0:47 Copy as JSON in Studio\n1:02 Blue Lock Career + RIVALS Codes\n1:14 Salvation Codes\n1:23 Coming Up\n1:36 Outro\n\nCodes in this video:\nStart Your Blue Lock Career: MANYFIXES (10 Weapon Spins, 10 Flow Spins, 4 Lucky Weapon Spins, 4 Lucky Flow Spins)\nRIVALS: FREE205 (3 Keys)\nSalvation: PERMCLASSRESET (Class Reset Token), HEREISPERMPATHRESET (1 Locked Path Reset)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "the takeback roblox", "roblox free items", "jailbreak", "emergency hamburg", "notoriety", "revolver arena", "roblox thanksgiving", "blue lock career codes", "rivals codes", "salvation codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-21_0100_Short_CodesJustDropped", "schedule_ist": "2026-11-21 01:00",
            "title": "3 Roblox Codes That Just Dropped 💎 #roblox #shorts",
            "description": "3 Roblox codes:\nStart Your Blue Lock Career: MANYFIXES (10 Weapon Spins, 10 Flow Spins, 4 Lucky Weapon Spins, 4 Lucky Flow Spins)\nCultivation Unbound: ABZZBIRTHDAY (1M Silver + 20 Primordial Stones)\nSalvation: HEREISPERMPATHRESET (1 Locked Path Reset)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-21_0300_Short_LateNightCodes", "schedule_ist": "2026-11-21 03:00",
            "title": "Grab These 3 Roblox Codes Before They're Gone ⏰ #roblox #shorts",
            "description": "3 more Roblox codes:\nRIVALS: FREE205 (3 Keys)\nStand Out: SORRY4SHUTDOWN (500 Dalas + 2 Mysterious Arrows)\nSalvation: PERMCLASSRESET (Class Reset Token)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
}
