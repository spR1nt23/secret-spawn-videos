# Secret Spawn - 29 Nov 2026 content (Sunday after Thanksgiving)
# Sources (checked 28 Nov 2026; devforum, create.roblox.com, playadopt.me, progameguides, fandom, tubefilter, gamezebo
# were not fetchable from this machine, so web search snippets were used):
#  The Great Build (Roblox's own Thanksgiving event, listed under Roblox Presents; Nov 25-30, 2026; no exact closing
#    hour on the listing, hub reportedly live ~1 PM ET Nov 25): place one free "gratitude" block every hour with a
#    thank-you message in a shared community tower; when the community hits a milestone you must have placed 5 blocks
#    to claim it (Patchbrick Cap 1M, Snowcapped Brick Tails 5M, Terracotta Skyserpent 10M, The Ascendant Bloom 20M);
#    Skybound Monarch from the event obby; scavenger hunt / time trial details provisional:
#    tubefilter.com/2026/11/24/roblox-the-great-build-thanksgiving-event/ ; streamscharts.com/news/roblox-great-build ;
#    gamezebo.com/walkthroughs/the-great-build-prizes/ ; progameguides.com/roblox/roblox-the-great-build-event-guide/ ;
#    techwiser.com/roblox-the-great-build-event-guide/ ; roblox.fandom.com/wiki/The_Great_Build
#  Adopt Me Gingerbread Mansion update (Nov 27, 2026): new Gingerbread Mansion house + house items (oven, sink, door,
#    window), snow falling on Adoption Island, Hooray (Ultra Rare; Crystal Egg + Basic Egg), Tilcayo (Legendary;
#    Gemstone Egg), bug fixes (Ghost Bunny head movement, paint picker scaling). Mansion price not in official notes:
#    playadopt.me/news/gingerbread-mansion-notes ; sportskeeda.com/roblox-news/adopt-me-gingerbread-mansion-update-patch-notes ;
#    sportskeeda.com/roblox-news/adopt-me-hooray-pet-guide ; sportskeeda.com/roblox-news/adopt-me-tilcayo-pet-guide
#  Pixel art stays sharp (DevForum announcement "Keep Pixel Art Sharp on Meshes, Decals, and Textures"; Creator Updates
#    Nov 24): new Pixelated option for ResampleMode on SurfaceAppearance, Decal and Texture; upload pixel art at original
#    size (non power-of-2 ok); stored uncompressed, no streaming; some low-end devices may still look blurry:
#    devforum.roblox.com/t/keep-pixel-art-sharp-on-meshes-decals-and-textures/5003488 ; create.roblox.com/updates
#  List: Great Build ends Nov 30; RIVALS Black Friday sale ends Dec 1 12 AM ET (see 2026-11-28.py); Pass Free Trials
#    Dec 2 (devforum.roblox.com/t/introducing-pass-free-trials/4995943); Incubator applications due Dec 7
#  Codes:
#    RIVALS FREE208 (3 Keys; follow devs @Nosniy / @SenseiWarrior; added Nov 26/27):
#      robloxden.com/game-codes/rivals ; gamsgo.com/blog/roblox-rivals-codes ; game.guide/roblox-codes/rivals
#    Anime Crusaders X HAPPYTHANKSGIVINGAC (Trait Remnants + Gems; Beebom/Dexerto/wiki 50 Trait Remnants + 1,000 Gems,
#      Tech Basket 75 Trait Remnants; join the community group): beebom.com/anime-crusaders-codes/ ;
#      dexerto.com/roblox/anime-crusaders-codes-3292373/ ; thetechbasket.com/anime-crusaders-x-codes/
#    Overflow 3000LIKES (20 Style + 20 Passive Rolls + 5 Variant + 10 Race Rerolls), 2500LIKES (15 Style + 15 Passive
#      + 5 Race Rerolls); join kyo squad, redeem in Customize: destructoid.com/overflow-codes/ (Nov 27) ;
#      robloxden.com/game-codes/overflow ; ofcodes.com ; progameguides.com/roblox/roblox-overflow-codes/
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("ROBLOX'S GIANT", "white"), ("TOWER EVENT", "yellow")], "tag": "LIVE",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Roblox is building one *giant* tower, and you can still get *free* prizes. Here's *how*."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "yellow", "game": "THE GREAT BUILD", "icon": "blocks", "badge": "EVERY HOUR",
    "title": "1 FREE BLOCK AN HOUR",
    "vo": "Number *one*. Open *The Great Build* and place one free *block* every *hour*."},
   {"type": "item", "n": 2, "bg": "green", "acc": "orange", "game": "THE GREAT BUILD", "icon": "hat", "badge": "FREE",
    "title": "PLACE 5 BLOCKS",
    "vo": "Number *two*. Place *five* blocks to claim the *free* items when the tower hits a *goal*."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "pink", "game": "THE GREAT BUILD", "icon": "bolt", "badge": "NOV 30",
    "title": "ENDS NOVEMBER 30",
    "vo": "Number *three*. The event ends *November thirtieth*, so don't *wait*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("HOW MANY", "white"), ("BLOCKS SO FAR?", "yellow")],
    "vo": "How many *blocks* have *you* placed? Tell me in the *comments*."},
  ]},
 "short2": {
  "title_lines": [("3 ROBLOX CODES", "white"), ("FOR SUNDAY", "yellow")], "tag": "NEW CODES",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Three* new Roblox codes from *three* different games. Grab them *now*."},
   {"type": "item", "n": 1, "bg": "red", "acc": "yellow", "game": "RIVALS", "icon": "tag", "badge": "NEW",
    "title": "3 FREE KEYS", "code": "FREE208",
    "vo": "First, *RIVALS*. Code *free two oh eight* gives *three* keys. Follow the *devs* first."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "pink", "game": "ANIME CRUSADERS X", "icon": "gem", "badge": "THANKSGIVING",
    "title": "GEMS + TRAITS", "code": "HAPPYTHANKSGIVINGAC",
    "vo": "Next, *Anime Crusaders X*. *Happy thanksgiving A C* gives *gems* and trait *remnants*."},
   {"type": "item", "n": 3, "bg": "navy", "acc": "green", "game": "OVERFLOW", "icon": "dice", "badge": "NEW",
    "title": "ROLLS + REROLLS", "code": "3000LIKES",
    "vo": "And *Overflow*. Code *three thousand likes* gives *forty* rolls plus *fifteen* rerolls."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("WORKED?", "yellow")],
    "vo": "Codes can *expire* fast. Which one *worked* for you?"},
  ]},
 "short3": {
  "title_lines": [("ADOPT ME", "white"), ("WINTER IS HERE", "yellow")], "tag": "NEW UPDATE",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Adopt Me* just started *winter*. Here are *three* new things to *find*."},
   {"type": "item", "n": 1, "bg": "maroon", "acc": "yellow", "game": "ADOPT ME", "icon": "house", "badge": "NEW HOUSE",
    "title": "GINGERBREAD MANSION",
    "vo": "Number *one*. A new *Gingerbread Mansion* house, and *snow* is falling on *Adoption Island*."},
   {"type": "item", "n": 2, "bg": "blue", "acc": "pink", "game": "ADOPT ME", "icon": "egg", "badge": "ULTRA RARE",
    "title": "HOORAY PET",
    "vo": "Number *two*. *Hooray* is a new *ultra rare* pet from the *Crystal* and *Basic* eggs."},
   {"type": "item", "n": 3, "bg": "green", "acc": "orange", "game": "ADOPT ME", "icon": "paw", "badge": "LEGENDARY",
    "title": "TILCAYO PET",
    "vo": "Number *three*. *Tilcayo* is a new *legendary* pet from the *Gemstone* egg."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH PET", "white"), ("DO YOU WANT?", "yellow")],
    "vo": "Which *pet* are *you* hatching? Tell me *below*."},
  ]},
}

LONG = {
 "thumb": [("GREAT BUILD", "white"), ("+ 4 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 29",
   "vo": "Here's today's *Roblox news*. *The Great Build* is almost over, *Adopt Me* started *winter*, pixel art just got *sharper*, and I've got *four new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "blue", "acc": "yellow", "game": "THE GREAT BUILD", "icon": "blocks", "badge": "ENDS NOV 30",
   "title": "THE GREAT BUILD",
   "bullets": ["ROBLOX'S THANKSGIVING EVENT", "1 FREE BLOCK EVERY HOUR", "PLACE 5 BLOCKS TO CLAIM PRIZES", "ENDS NOV 30"],
   "vo": "Number *one*. *The Great Build* is Roblox's own *Thanksgiving* event, where everyone adds to one giant *tower*. You can place one free *block* every *hour*, with a *thank you* message. When the tower hits a *goal*, you need *five* placed blocks to claim the *free* item. It ends *November thirtieth*, so check the *countdown*."},
  {"type": "item", "n": 2, "bg": "maroon", "acc": "pink", "game": "ADOPT ME", "icon": "house", "badge": "NOV 27",
   "title": "GINGERBREAD MANSION",
   "bullets": ["NEW GINGERBREAD MANSION HOUSE", "SNOW ON ADOPTION ISLAND", "HOORAY: ULTRA RARE", "TILCAYO: LEGENDARY"],
   "vo": "Number *two*. *Adopt Me* dropped the *Gingerbread Mansion* update on *November twenty seventh*. Snow is now falling on *Adoption Island*. *Hooray* is a new *ultra rare* pet from the *Crystal* and *Basic* eggs. And *Tilcayo* is a new *legendary* from the *Gemstone* egg."},
  {"type": "item", "n": 3, "bg": "green", "acc": "orange", "game": "ROBLOX STUDIO", "icon": "brush", "badge": "CREATORS",
   "title": "SHARP PIXEL ART",
   "bullets": ["NEW PIXELATED RESAMPLE MODE", "DECALS, TEXTURES + MESHES", "NO MORE BLURRY SPRITES"],
   "vo": "Number *three*, for *creators*. Roblox added a new *Pixelated* option for *decals*, *textures*, and *meshes*. Every pixel now shows as a crisp *square*, so retro art stops looking *blurry*. Some *low end* devices may still blur it a little."},
  {"type": "item", "n": 4, "bg": "red", "acc": "yellow", "game": "RIVALS", "icon": "tag", "badge": "1 CODE",
   "title": "3 FREE KEYS", "code": "FREE208",
   "bullets": ["FREE208: 3 KEYS", "FOLLOW THE DEVS FIRST"],
   "vo": "Now, *codes*. Number *four*. *RIVALS* has *free two oh eight* for *three* keys. Follow the *developers* first."},
  {"type": "item", "n": 5, "bg": "violet", "acc": "blue", "game": "ANIME CRUSADERS X", "icon": "gem", "badge": "1 CODE",
   "title": "GEMS + TRAITS", "code": "HAPPYTHANKSGIVINGAC",
   "bullets": ["HAPPYTHANKSGIVINGAC: GEMS + TRAIT REMNANTS"],
   "vo": "Number *five*. *Anime Crusaders X* has *happy thanksgiving A C* for *gems* and trait *remnants*."},
  {"type": "item", "n": 6, "bg": "navy", "acc": "green", "game": "OVERFLOW", "icon": "dice", "badge": "2 CODES",
   "title": "FREE ROLLS", "code": "3000LIKES",
   "bullets": ["3000LIKES: 40 ROLLS + 15 REROLLS", "2500LIKES: 30 ROLLS + 5 REROLLS"],
   "vo": "And number *six*. *Overflow* has *three thousand likes* and *twenty five hundred likes*, for free style and passive *rolls*."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("THE GREAT BUILD ENDS", "NOV 30"), ("RIVALS SALE ENDS", "DEC 1"),
            ("PASS FREE TRIALS GO LIVE", "DEC 2"), ("INCUBATOR DEADLINE", "DEC 7")],
   "vo": "Coming up. *The Great Build* ends *November thirtieth*, the *RIVALS* sale ends *December first*, pass *free trials* go live *December second*, and *Incubator* applications close *December seventh*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("HOW MANY", "white"), ("BLOCKS DID YOU PLACE?", "yellow")],
   "vo": "That's *today's* news. How many *blocks* did you place? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-29_1900_Short_GreatBuild", "schedule_ist": "2026-11-29 19:00",
            "title": "Roblox's Giant Tower Event Ends Soon! 🧱 #roblox #shorts",
            "description": "The Great Build is Roblox's own Thanksgiving event: place one free block every hour in a shared community tower, and place 5 blocks to claim the free items when the tower hits each goal. It ends Nov 30, so check the in-game countdown. Times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long": {"file": "SS_2026-11-29_2300_Long_NewsToday", "schedule_ist": "2026-11-29 23:00",
          "title": "Roblox News Today: The Great Build, Adopt Me Gingerbread Mansion & 4 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: The Great Build, Roblox's own Thanksgiving tower event, ends Nov 30 (one free block every hour, place 5 blocks to claim milestone prizes), Adopt Me's Nov 27 Gingerbread Mansion update brought snow plus the new Hooray (Ultra Rare) and Tilcayo (Legendary) pets, and creators can now keep pixel art sharp with the new Pixelated resample mode for decals, textures and meshes. Plus 3 games have 4 new codes.\n\nChapters:\n0:00 Intro\n0:10 The Great Build: Roblox's Thanksgiving Tower Event\n0:30 Adopt Me Gingerbread Mansion Update\n0:46 Sharp Pixel Art for Creators\n1:01 RIVALS, Anime Crusaders X + Overflow Codes\n1:23 Coming Up + Outro\n\nCodes in this video:\nRIVALS: FREE208 (3 Keys; follow the developers first)\nAnime Crusaders X: HAPPYTHANKSGIVINGAC (Gems + Trait Remnants; amounts vary by source)\nOverflow: 3000LIKES (20 Style Rolls + 20 Passive Rolls + 5 Variant Rerolls + 10 Race Rerolls), 2500LIKES (15 Style Rolls + 15 Passive Rolls + 5 Race Rerolls)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "the great build", "roblox thanksgiving event", "adopt me", "adopt me gingerbread mansion", "adopt me update", "roblox pixel art", "rivals codes", "anime crusaders x codes", "overflow codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-30_0100_Short_SundayCodes", "schedule_ist": "2026-11-30 01:00",
            "title": "3 Roblox Codes to Grab This Sunday 🎁 #roblox #shorts",
            "description": "3 Roblox codes:\nRIVALS: FREE208 (3 Keys; follow the developers first)\nAnime Crusaders X: HAPPYTHANKSGIVINGAC (Gems + Trait Remnants)\nOverflow: 3000LIKES (20 Style Rolls + 20 Passive Rolls + 5 Variant Rerolls + 10 Race Rerolls)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-30_0300_Short_AdoptMeWinter", "schedule_ist": "2026-11-30 03:00",
            "title": "Adopt Me Winter Just Started! ❄️ #roblox #shorts",
            "description": "Adopt Me's Gingerbread Mansion update (Nov 27) added a new Gingerbread Mansion house, snow on Adoption Island, Hooray (a new Ultra Rare pet from the Crystal and Basic Eggs) and Tilcayo (a new Legendary pet from the Gemstone Egg).\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
}
