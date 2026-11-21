# Secret Spawn - 22 Nov 2026 content
# Sources (checked 21 Nov 2026; devforum / create.roblox.com / sportskeeda / code sites were not fetchable here,
# so web search snippets were used):
#  Dandy's World 1.0 (BlushCrunch Studio; leaves Alpha Fri Nov 20, 20:00 UTC = 3 PM ET; Roblox "Dandy's World 1.0 Release"
#    event runs to Nov 30; new mode The Labs with 11 Floors + Labs Break Room, new currency Ambrosia, two new Lethals
#    only in The Labs, Ichorlings, 30+ achievements; Alpha Player badge no longer earnable, holders get Alpha Player
#    title + 500 Ambrosia + 2 Ambrosia Vials; Toons menu renamed Loadout):
#    sportskeeda.com/roblox-news/dandy-s-world-update-1-0-patch-notes ; endgametools.com/en/roblox/news/roblox-dandys-world-1-0 ;
#    gamingroute.com/dandys-world-1-0-update/ ; beebom.com/dandys-world-1-0-release-time-countdown/ ;
#    aprasi.com/blogs/trending-topics/dandys-world-update ; allkeyshop.com/blog/dandys-world-1-0-update-release-news-d/
#  Toilet Tower Defense Thanksgiving Event 2026 (released Nov 14, 2026; 7 quests from the Turkey Cameraman -> Camera Turkey
#    unit; Thanksgiving Table mode Easy..Nightmare; 11 hidden turkeys: 5 lobby/event area + 6 in a match):
#    progameguides.com/roblox/all-turkey-locations-in-toilet-tower-defense-thanksgiving-2026-event-guide/ ;
#    toilet-tower-defense-game.fandom.com/wiki/Thanksgiving_Event_2026 ; games.gg/roblox/guides/all-turkey-locations-in-toilet-tower-defense/
#  game.ServerRegion (DevForum announcement Nov 19, 2026: read the region of live servers, uppercase IATA airport codes
#    like "LAX"/"LHR"; empty string in Studio, play solo and client scripts):
#    devforum.roblox.com/t/read-your-games-server-region-with-new-api/4996710 ; create.roblox.com/docs/reference/engine/classes/DataModel
#  List: The Takeback ends Nov 23 19:00 UTC = 2 PM ET (roblox.fandom.com/wiki/The_Takeback);
#    TextChatService rule Dec 3 (create.roblox.com/updates); Game Awards on Roblox Dec 10 (earlier sets)
#  Codes:
#    Net a Fish 10Mvisits (1 Trait Roll + 15 min 2x Luck / 2x Money / 2x Fish Caught; lowercase "visits"):
#      destructoid.com/roblox-net-a-fish-codes/ (Nov 20), dexerto.com/roblox/net-a-fish-codes-3426845/ ,
#      progameguides.com/roblox/net-a-fish-codes/ (Nov 20), timesaver.gg/blog/net-a-fish-codes
#    Branded 600MEMBERS (15 Race Rerolls, 5 Gift Rerolls, 2 Brand Rerolls; added Nov 18):
#      destructoid.com/branded-codes/ , progameguides.com/roblox/branded-codes/ (Nov 18)
#    Dandy's World ICHOR (50 Ichor), AD2026 (American Dream 2026 Profile Print):
#      robloxden.com/game-codes/dandy-s-world (checked Nov 20), gamesradar.com/games/survival/dandys-world-codes/ , dexerto
#    RIVALS COMMUNITY28 (1 Community Wrap, random weapon; follow a dev to redeem):
#      progameguides.com/roblox/rivals-codes/ (Nov 18), techwiser.com/roblox-rivals-codes/ , tryhardguides.com/rivals-codes/
#    Ishin fixedlol (rerolls; GamesRadar says Yen -> said as "rerolls" per Destructoid + BloxInformer; join group + 1 h playtime):
#      destructoid.com/ishin-codes/ (Nov 20), ishin.bloxinformer.com/codes/
#    Grab and Decorate BEGINNER (3 Shelf Tables + 4 Coffee Tables):
#      destructoid.com/grab-and-decorate-codes/ (Nov 20), progameguides.com/roblox/grab-and-decorate-codes/ (Nov 20), mrguider
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("DANDY'S WORLD", "white"), ("1.0 IS HERE", "yellow")], "tag": "OUT OF ALPHA",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Dandy's World* just left *Alpha* with its big *one point oh* update, and here are *three* things that changed."},
   {"type": "item", "n": 1, "bg": "green", "acc": "green", "game": "DANDY'S WORLD", "icon": "flask", "badge": "NEW MODE",
    "title": "THE LABS",
    "vo": "Number *one*. A brand new mode called *The Labs* adds *eleven* new *floors* to survive."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "pink", "game": "DANDY'S WORLD", "icon": "gem", "badge": "NEW",
    "title": "AMBROSIA CURRENCY",
    "vo": "Number *two*. Inside The Labs, you earn a brand new currency called *Ambrosia*."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "DANDY'S WORLD", "icon": "trophy", "badge": "BADGE",
    "title": "ALPHA PLAYER REWARD",
    "vo": "Number *three*. *Alpha Player* badge owners get a *title* and *five hundred* Ambrosia."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("TRIED THE", "white"), ("LABS YET?", "yellow")],
    "vo": "So, have *you* tried *The Labs* yet? Tell me in the *comments* below."},
  ]},
 "short2": {
  "title_lines": [("3 SUNDAY", "white"), ("ROBLOX CODES", "yellow")], "tag": "NEW CODES",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Here are *three* fresh Roblox codes for your *Sunday*, so type them *exactly* as you see them."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "NET A FISH", "icon": "fish", "badge": "NEW",
    "title": "TRAIT ROLL + BOOSTS", "code": "10Mvisits",
    "vo": "First, *Net a Fish*. Code *ten M visits* gives a *trait roll* plus *double luck* boosts."},
   {"type": "item", "n": 2, "bg": "red", "acc": "yellow", "game": "RIVALS", "icon": "swords", "badge": "ACTIVE",
    "title": "FREE WEAPON WRAP", "code": "COMMUNITY28",
    "vo": "Next, *Rivals*. Code *community twenty eight* gives a free *community wrap* for a weapon."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "ISHIN", "icon": "dice", "badge": "NEW",
    "title": "FREE REROLLS", "code": "fixedlol",
    "vo": "And *Ishin*. Code *fixed lol*, all lowercase, gives free *rerolls*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("WORKED?", "yellow")],
    "vo": "Codes can *expire* at any time, so be *quick*. Which one *worked* for you?"},
  ]},
 "short3": {
  "title_lines": [("3 FREE CODES", "white"), ("BEFORE BED", "yellow")], "tag": "LATE NIGHT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Before you go to *bed*, grab these *three* free Roblox codes that still *work*."},
   {"type": "item", "n": 1, "bg": "maroon", "acc": "orange", "game": "BRANDED", "icon": "flame", "badge": "NEW",
    "title": "22 FREE REROLLS", "code": "600MEMBERS",
    "vo": "First, *Branded*. Code *six hundred members* gives *twenty two* free rerolls in total."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "purple", "game": "DANDY'S WORLD", "icon": "mystery", "badge": "ACTIVE",
    "title": "50 FREE ICHOR", "code": "ICHOR",
    "vo": "Next, *Dandy's World*, which just hit one point oh. Code *ichor* gives *fifty ichor*."},
   {"type": "item", "n": 3, "bg": "navy", "acc": "green", "game": "GRAB AND DECORATE", "icon": "frame", "badge": "ACTIVE",
    "title": "FREE FURNITURE", "code": "BEGINNER",
    "vo": "And *Grab and Decorate*. Code *beginner* gives *seven* free pieces of *furniture*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT DID", "white"), ("YOU GET?", "yellow")],
    "vo": "Redeem them *fast*, because they can *expire*. What did *you* get?"},
  ]},
}

LONG = {
 "thumb": [("DANDY'S WORLD 1.0", "white"), ("+ 4 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 22",
   "vo": "Here's today's *Roblox news*. *Dandy's World* finally left *Alpha*, *Toilet Tower Defense* has a *Thanksgiving* hunt, creators got a new *server region* tool, and I've got *four new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "green", "acc": "green", "game": "DANDY'S WORLD", "icon": "flask", "badge": "1.0",
   "title": "DANDY'S WORLD 1.0",
   "bullets": ["OUT OF ALPHA, NOV 20", "THE LABS: 11 NEW FLOORS", "NEW CURRENCY: AMBROSIA", "ALPHA BADGE: 500 AMBROSIA"],
   "vo": "Number *one*. *Dandy's World* hit version *one point oh* on *Friday*. The big addition is *The Labs*, a new mode with *eleven* new floors and new *Lethal* toons. You earn a new currency called *Ambrosia* there. And *Alpha Player* badge owners get a special *title* and *five hundred Ambrosia*. Also, the *Toons* menu is now called *Loadout*."},
  {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "TOILET TOWER DEFENSE", "icon": "camera", "badge": "EVENT",
   "title": "THANKSGIVING HUNT",
   "bullets": ["7 QUESTS FROM TURKEY CAMERAMAN", "REWARD: CAMERA TURKEY UNIT", "11 HIDDEN TURKEYS"],
   "vo": "Number *two*. *Toilet Tower Defense* has its *Thanksgiving* event. Talk to the *Turkey Cameraman* and finish *seven* quests to earn the *Camera Turkey* unit. Quests include beating *Thanksgiving Table* mode and finding *eleven* hidden *turkeys*. *Five* are in the *lobby* and event area, and *six* are inside a *match*."},
  {"type": "item", "n": 3, "bg": "blue", "acc": "yellow", "game": "ROBLOX STUDIO", "icon": "globe", "badge": "CREATORS",
   "title": "SERVER REGION API",
   "bullets": ["NEW: GAME.SERVERREGION", "RETURNS CODES LIKE \"LAX\"", "EMPTY IN STUDIO TESTS"],
   "vo": "Number *three*, for *creators*. A new property called *server region* tells your game *where* its live server is running. It gives an *airport* code like *L A X*. It stays *empty* in *Studio* tests, so check it in a *live* game."},
  {"type": "item", "n": 4, "bg": "navy", "acc": "blue", "game": "NET A FISH", "icon": "fish", "badge": "CODE",
   "title": "TRAIT ROLL + BOOSTS", "code": "10Mvisits",
   "bullets": ["10Mvisits: TRAIT ROLL + 15 MIN BOOSTS"],
   "vo": "Now, *codes*. Number *four*. *Net a Fish* has *ten M visits* for a *trait roll* and *fifteen minute* boosts for *luck*, *money*, and *fish caught*. Type *visits* in *lowercase*."},
  {"type": "item", "n": 5, "bg": "red", "acc": "pink", "game": "BRANDED", "icon": "flame", "badge": "CODE",
   "title": "22 FREE REROLLS", "code": "600MEMBERS",
   "bullets": ["600MEMBERS: 15 RACE, 5 GIFT, 2 BRAND REROLLS"],
   "vo": "Number *five*. *Branded* has *six hundred members* for *twenty two* rerolls. That's *fifteen race*, *five gift*, and *two brand* rerolls."},
  {"type": "item", "n": 6, "bg": "violet", "acc": "purple", "game": "DANDY'S WORLD", "icon": "mystery", "badge": "CODES",
   "title": "FREE ICHOR", "code": "ICHOR",
   "bullets": ["ICHOR: 50 ICHOR", "AD2026: PROFILE PRINT"],
   "vo": "And number *six*. *Dandy's World* has *ichor* for *fifty ichor*, and *A D twenty twenty six* for a *profile print*."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("THE TAKEBACK ENDS", "NOV 23"), ("DANDY'S WORLD 1.0 EVENT", "NOV 30"),
            ("TEXT CHAT RULE ENFORCED", "DEC 3"), ("GAME AWARDS ON ROBLOX", "DEC 10")],
   "vo": "Coming up. *The Takeback* ends *Monday*, the *Dandy's World* release event runs to *November thirtieth*, the *chat rule* starts *December third*, and *The Game Awards* hit Roblox on *December tenth*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WILL YOU TRY", "white"), ("THE LABS?", "yellow")],
   "vo": "That's *today's* news. Will *you* try *The Labs*? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-22_1900_Short_DandysWorld10", "schedule_ist": "2026-11-22 19:00",
            "title": "Dandy's World 1.0 Is FINALLY Here! 🧪 #roblox #shorts",
            "description": "Dandy's World left Alpha with its 1.0 update on Friday, Nov 20 (3 PM ET). It adds The Labs, a new mode with 11 new floors, plus a new currency called Ambrosia. Alpha Player badge owners get a special title and 500 Ambrosia.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long": {"file": "SS_2026-11-22_2300_Long_NewsToday", "schedule_ist": "2026-11-22 23:00",
          "title": "Roblox News Today: Dandy's World 1.0, TTD Thanksgiving & 4 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: Dandy's World left Alpha with its 1.0 update (The Labs with 11 new floors, the new Ambrosia currency and rewards for Alpha Player badge owners), Toilet Tower Defense's Thanksgiving event lets you earn the Camera Turkey unit from 7 Turkey Cameraman quests, creators can now read where their live servers run with the new game.ServerRegion property, and 3 games have new codes.\n\nChapters:\n0:00 Intro\n0:13 Dandy's World 1.0\n0:33 Toilet Tower Defense Thanksgiving\n0:52 New Server Region API\n1:05 Net a Fish Code\n1:16 Branded + Dandy's World Codes\n1:31 Coming Up\n1:44 Outro\n\nCodes in this video:\nNet a Fish: 10Mvisits (1 Trait Roll + 15 min 2x Luck, 2x Money and 2x Fish Caught)\nBranded: 600MEMBERS (15 Race Rerolls, 5 Gift Rerolls, 2 Brand Rerolls)\nDandy's World: ICHOR (50 Ichor), AD2026 (Profile Print)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "dandys world", "dandys world 1.0", "dandys world the labs", "toilet tower defense thanksgiving", "camera turkey", "roblox server region", "net a fish codes", "branded codes", "dandys world codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-23_0100_Short_SundayCodes", "schedule_ist": "2026-11-23 01:00",
            "title": "3 Sunday Roblox Codes That Just Dropped 💎 #roblox #shorts",
            "description": "3 Roblox codes:\nNet a Fish: 10Mvisits (1 Trait Roll + 15 min boosts; type \"visits\" in lowercase)\nRIVALS: COMMUNITY28 (1 Community Wrap; follow a RIVALS developer first)\nIshin: fixedlol (Rerolls; type it in lowercase, join the group first)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-23_0300_Short_BeforeBedCodes", "schedule_ist": "2026-11-23 03:00",
            "title": "3 FREE Roblox Codes to Grab Before Bed 🌙 #roblox #shorts",
            "description": "3 more Roblox codes:\nBranded: 600MEMBERS (15 Race Rerolls, 5 Gift Rerolls, 2 Brand Rerolls)\nDandy's World: ICHOR (50 Ichor)\nGrab and Decorate: BEGINNER (3 Shelf Tables + 4 Coffee Tables)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
}
