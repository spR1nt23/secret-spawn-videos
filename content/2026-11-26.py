# Secret Spawn - 26 Nov 2026 content (Thanksgiving Day)
# Sources (checked 25 Nov 2026; devforum, sportskeeda, beebom, destructoid, progameguides and all other news/code sites were
# not fetchable from this machine, so web search snippets were used):
#  Fisch "Fischgiving 3" Thanksgiving update (live Tue Nov 24, 2026 17:00 UTC = 12:00 PM ET; ends Dec 1, 2026 17:00 UTC
#    = 12:00 PM ET per fischcalculator citing the Roblox event listing): 14 unique Turkeys to catch across the sea, the Great
#    Turkey spawns in the center of the Ocean every in-game hour, Turkey Tim near the giant Gravy Boat (trade at least 5
#    Turkeys to other players -> global milestone rewards: Gobbler title, Soaring Turkey Glider, Turkey Halo), Pilgrim quest
#    at the Cozy Lodge in Moosewood (bring 12 families together), code TurkeyTime:
#    sportskeeda.com/roblox-news/fischgiving-update-patch-notes ; fischcalculator.com/events/fischgiving/ ;
#    progameguides.com/roblox/all-14-turkey-locations-in-fischgiving-3-bestiary-2026-fisch/
#  Anime Adventures Update 21.5 "Misty Village" (Nov 23, 2026): new Secret unit Misty (event banner, Dawn Coins), Haze
#    evolution needs a Mist Blade, new quests from Misty and Lovey:
#    bloxdex.gg/games/anime-adventures/updates ; sportskeeda.com/roblox-news/anime-adventures-misty-unit-guide ;
#    itemlevel.net/guide-to-anime-adventures-update-21-5-everything-you-need-to-know/
#  30 of the 99 games on Roblox's Top Playing Now chart were created in October or November (chart checked Nov 18;
#    42 of 99 made in 2026 with ~37% of players; Hyper Realistic Ragdoll (Oct 29) ranked 10th, Ragdoll Soccer (Oct 13)
#    17th; 11 pre-2020 games still hold 19% of players, led by Adopt Me!):
#    ggrecon.com/articles/roblox-top-games-didnt-exist-before-october/ (Nov 19, 2026)
#  List: Fischgiving ends Dec 1; pass free trials go live Dec 2 (devforum.roblox.com/t/introducing-pass-free-trials/4995943);
#    TextChatService rule enforced Dec 3 (Creator Updates Nov 20); Incubator applications due Dec 7 (create.roblox.com)
#  Codes:
#    Fisch TurkeyTime (level 25+; 50 Mini Pinecones + 50 Pumpkin Pie Bits + 50 Stuffing Pieces bait, "gobble gobble yo" title,
#      30 min Lucky boost; listed expiry Dec 1 17:00 UTC): fischipedia.org/wiki/Codes ; tryhardguides.com/fisch-codes/ ;
#      sportskeeda Fischgiving patch notes
#    Collect Cat Cards THANKSGIVING (100 Acorns), TURKEY (30 Acorns; added Nov 21): destructoid.com/collect-cat-cards-codes/ ;
#      robloxden.com/game-codes/collect-cat-cards ; mrguider.org/roblox/collect-cat-cards-codes/
#    Hunty Zombie GRANDMASTER, NOGUILDNEEDED (free Lucky Spins + Traits per Beebom Nov 24; Destructoid says NOGUILDNEEDED =
#      100 Lucky Weapon Spins): beebom.com/hunty-zombies-codes/ ; destructoid.com/hunty-zombies-codes/ ;
#      progameguides.com/roblox/hunty-zombies-codes/
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("FISCHGIVING", "white"), ("IS LIVE", "yellow")], "tag": "LIVE NOW",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Happy *Thanksgiving*! *Fisch* just started its *turkey* event, and here are *three* things to know."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "FISCH", "icon": "fish", "badge": "14 TURKEYS",
    "title": "CATCH 14 TURKEYS",
    "vo": "Number *one*. There are *fourteen* different *turkeys* to catch all over the sea."},
   {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "FISCH", "icon": "drumstick", "badge": "EVERY HOUR",
    "title": "THE GREAT TURKEY",
    "vo": "Number *two*. The *Great Turkey* shows up in the middle of the *Ocean* every in-game *hour*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "yellow", "game": "FISCH", "icon": "trophy", "badge": "TRADE 5",
    "title": "GLOBAL REWARDS",
    "vo": "Number *three*. Trade *five* turkeys to other players to help unlock a *glider* and a turkey *halo*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("HOW MANY TURKEYS", "white"), ("DID YOU CATCH?", "yellow")],
    "vo": "So, how many *turkeys* have *you* caught? Tell me in the *comments*."},
  ]},
 "short2": {
  "title_lines": [("3 TURKEY DAY", "white"), ("ROBLOX CODES", "yellow")], "tag": "NEW CODES",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Here are *three* fresh Roblox codes for *Thanksgiving* weekend."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "FISCH", "icon": "fish", "badge": "LEVEL 25+",
    "title": "BAIT + LUCK BOOST", "code": "TurkeyTime",
    "vo": "First, *Fisch*. Code *turkey time* gives holiday *bait*, a new *title*, and a luck *boost*."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "pink", "game": "COLLECT CAT CARDS", "icon": "paw", "badge": "NEW",
    "title": "100 FREE ACORNS", "code": "THANKSGIVING",
    "vo": "Next, *Collect Cat Cards*. Code *thanksgiving* gives *one hundred* free *acorns*."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "yellow", "game": "HUNTY ZOMBIE", "icon": "swords", "badge": "NEW",
    "title": "FREE LUCKY SPINS", "code": "NOGUILDNEEDED",
    "vo": "And *Hunty Zombie*. Code *no guild needed* gives free *lucky* spins."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("WORKED?", "yellow")],
    "vo": "Codes can *expire* fast, so be *quick*. Which one *worked* for you?"},
  ]},
 "short3": {
  "title_lines": [("30 TOP GAMES", "white"), ("ARE BRAND NEW", "yellow")], "tag": "TRENDING",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Roblox's *top* games chart just changed *fast*. Here's what *happened*."},
   {"type": "item", "n": 1, "bg": "navy", "acc": "blue", "game": "TOP PLAYING NOW", "icon": "chart", "badge": "30 OF 99",
    "title": "30 NEW HITS",
    "vo": "Number *one*. *Thirty* of the top *ninety nine* games didn't exist before *October*."},
   {"type": "item", "n": 2, "bg": "red", "acc": "yellow", "game": "HYPER REALISTIC RAGDOLL", "icon": "ball", "badge": "#10",
    "title": "RAGDOLL TOP 10",
    "vo": "Number *two*. *Hyper Realistic Ragdoll* came out *October twenty ninth* and already hit the *top ten*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "OLDER GAMES", "icon": "trophy", "badge": "19%",
    "title": "CLASSICS HOLD ON",
    "vo": "Number *three*. Games from before *twenty twenty* still have about *one fifth* of the players."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("NEW GAMES OR", "white"), ("OLD CLASSICS?", "yellow")],
    "vo": "Do *you* play *new* games or old *classics*? Tell me *below*."},
  ]},
}

LONG = {
 "thumb": [("FISCHGIVING", "white"), ("+ 5 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 26",
   "vo": "Happy *Thanksgiving*! Here's today's *Roblox news*. *Fisch* started *Fischgiving*, *Anime Adventures* added a new *secret* unit, *thirty* top games are brand *new*, and I've got *five new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "FISCH", "icon": "fish", "badge": "LIVE",
   "title": "FISCHGIVING IS LIVE",
   "bullets": ["14 TURKEYS TO CATCH", "GREAT TURKEY EVERY GAME HOUR", "TRADE 5 FOR GLOBAL REWARDS", "ENDS DEC 1, 12 PM ET"],
   "vo": "Number *one*. *Fisch* started *Fischgiving* on *Tuesday*. There are *fourteen* turkeys to catch, and the *Great Turkey* spawns in the middle of the *Ocean* every in-game hour. Trade *five* turkeys to other players to help unlock *global* rewards, like a *glider* and a turkey *halo*. It ends *December first*."},
  {"type": "item", "n": 2, "bg": "violet", "acc": "pink", "game": "ANIME ADVENTURES", "icon": "swords", "badge": "UPD 21.5",
   "title": "MISTY VILLAGE UPDATE",
   "bullets": ["NEW SECRET UNIT: MISTY", "EVENT BANNER WITH DAWN COINS", "NEW VILLAGE QUESTS"],
   "vo": "Number *two*. *Anime Adventures* dropped update *twenty one point five*, called *Misty Village*. It adds a new *secret* unit named *Misty* on an event *banner*. You summon with *Dawn Coins*, and there are new *quests* in the village."},
  {"type": "item", "n": 3, "bg": "navy", "acc": "orange", "game": "TOP PLAYING NOW", "icon": "chart", "badge": "30 OF 99",
   "title": "30 NEW TOP GAMES",
   "bullets": ["30 OF TOP 99 MADE OCT OR NOV", "RAGDOLL GAME AT #10", "PRE-2020 GAMES: 19% OF PLAYERS"],
   "vo": "Number *three*. A chart check found that *thirty* of Roblox's top *ninety nine* games didn't exist before *October*. *Hyper Realistic Ragdoll* was already number *ten*. Older classics like *Adopt Me* still hold about *one fifth* of the players."},
  {"type": "item", "n": 4, "bg": "maroon", "acc": "yellow", "game": "FISCH", "icon": "drumstick", "badge": "LEVEL 25+",
   "title": "BAIT + LUCK BOOST", "code": "TurkeyTime",
   "bullets": ["TURKEYTIME: 150 BAIT + TITLE", "30 MIN LUCK BOOST"],
   "vo": "Now, *codes*. Number *four*. *Fisch* has *turkey time*, for holiday *bait*, a *title*, and a *luck* boost. You need level *twenty five*."},
  {"type": "item", "n": 5, "bg": "green", "acc": "orange", "game": "COLLECT CAT CARDS", "icon": "paw", "badge": "NEW",
   "title": "FREE ACORNS", "code": "THANKSGIVING",
   "bullets": ["THANKSGIVING: 100 ACORNS", "TURKEY: 30 ACORNS"],
   "vo": "Number *five*. *Collect Cat Cards* has *thanksgiving* for *one hundred* acorns, and *turkey* for *thirty* more."},
  {"type": "item", "n": 6, "bg": "red", "acc": "blue", "game": "HUNTY ZOMBIE", "icon": "shield", "badge": "NEW",
   "title": "FREE LUCKY SPINS", "code": "GRANDMASTER",
   "bullets": ["GRANDMASTER: SPINS + TRAITS", "NOGUILDNEEDED: LUCKY SPINS"],
   "vo": "And number *six*. *Hunty Zombie* has *grandmaster* and *no guild needed*, for free *lucky* spins."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("FISCHGIVING ENDS", "DEC 1"), ("PASS FREE TRIALS GO LIVE", "DEC 2"),
            ("TEXTCHATSERVICE RULE", "DEC 3"), ("INCUBATOR DEADLINE", "DEC 7")],
   "vo": "Coming up. *Fischgiving* ends *December first*, pass *free trials* go live *December second*, the new *chat* rule starts *December third*, and *Incubator* applications close *December seventh*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT ARE YOU", "white"), ("PLAYING TODAY?", "yellow")],
   "vo": "That's *today's* news. What are you playing this *Thanksgiving*? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-26_1900_Short_Fischgiving", "schedule_ist": "2026-11-26 19:00",
            "title": "Fischgiving Is Finally LIVE in Fisch! 🦃 #roblox #shorts",
            "description": "Fisch's Thanksgiving event Fischgiving is live: catch 14 different Turkeys, find the Great Turkey in the middle of the Ocean every in-game hour, and trade 5 Turkeys to other players to help unlock global rewards like a Soaring Turkey Glider and a Turkey Halo. It ends Dec 1 at 12 PM ET. Times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long": {"file": "SS_2026-11-26_2300_Long_NewsToday", "schedule_ist": "2026-11-26 23:00",
          "title": "Roblox News Today: Fischgiving, Anime Adventures Misty & 5 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: Fisch's Fischgiving event is live with 14 Turkeys, the hourly Great Turkey and global trading rewards (ends Dec 1), Anime Adventures Update 21.5 (Misty Village) adds the Secret unit Misty on a Dawn Coin event banner, and a chart check found 30 of Roblox's top 99 games were made in October or November. Plus 3 games have 5 new codes.\n\nChapters:\n0:00 Intro\n0:13 Fisch Fischgiving Is Live\n0:31 Anime Adventures Misty Village Update\n0:45 30 New Top Roblox Games\n1:01 Fisch, Collect Cat Cards + Hunty Zombie Codes\n1:22 Coming Up + Outro\n\nCodes in this video:\nFisch: TurkeyTime (50 Mini Pinecones, 50 Pumpkin Pie Bits, 50 Stuffing Pieces, a title and a 30 min luck boost; level 25+)\nCollect Cat Cards: THANKSGIVING (100 Acorns), TURKEY (30 Acorns)\nHunty Zombie: GRANDMASTER (Lucky Spins + Traits), NOGUILDNEEDED (Lucky Spins; rewards vary by source)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "fisch", "fischgiving", "fisch thanksgiving", "anime adventures", "anime adventures update 21.5", "roblox thanksgiving", "fisch codes", "collect cat cards codes", "hunty zombie codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-27_0100_Short_TurkeyDayCodes", "schedule_ist": "2026-11-27 01:00",
            "title": "3 Fresh Roblox Codes for Thanksgiving Weekend 🎁 #roblox #shorts",
            "description": "3 Roblox codes:\nFisch: TurkeyTime (holiday bait, a title and a 30 min luck boost; level 25+)\nCollect Cat Cards: THANKSGIVING (100 Acorns)\nHunty Zombie: NOGUILDNEEDED (free Lucky Spins)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-27_0300_Short_NewTopGames", "schedule_ist": "2026-11-27 03:00",
            "title": "30 of Roblox's Top Games Didn't Exist Before October! 📈 #roblox #shorts",
            "description": "A Nov 18 check of Roblox's Top Playing Now chart found 30 of the top 99 games were made in October or November. Hyper Realistic Ragdoll, released Oct 29, was already #10, while games from before 2020 still had about 19% of the players, led by Adopt Me!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
}
