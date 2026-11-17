# Secret Spawn - 18 Nov 2026 content
# Sources (checked 17 Nov 2026; sportskeeda / gamesbeat were not fetchable here, so search snippets were used):
#  Steal An Egg Update 13 (Nov 14, 3:00 PM UTC) (takip): Stormlands biome (9th biome, between Prehistoric and Cosmic),
#    Skyfall event every 30 min (:00/:30, ~5 min) -> smash rocks for Thunderstones -> limited Stormy Egg,
#    Thunderous mutation (x2.75) from Rumble the Mole for Sparks, Black Market dealer Slick Rick (Blacklisted mutation):
#    sportskeeda.com/roblox-news/steal-an-egg-update-13-patch-notes ; holdtoreset.com/steal-an-egg-stormlands-update-13-guide/ ;
#    timesaver.gg/blog/steal-an-egg-black-market-dealer ; gameboost.com/blog/steal-an-egg-slick-rick-update-guide
#  Fisch Companion Hats update (Nov 14): hats for companions, new NPC Crazy Stylist in Moosewood (quest: bring any hat ->
#    Crazy Styles Cap & Shades), hats from fishing / shops / traveling merchant, code CompanionHatTime:
#    sportskeeda.com/roblox-news/fisch-companion-hats-update-patch-notes ; beebom.com/all-fisch-companion-hats/ ;
#    roonby.com/2026/11/14/all-companion-hats-in-fisch-guide-and-how-to-get-them/ ; fischipedia.org/wiki/2.10
#  Roblox automatic image translation beta (Nov 9): translates text inside in-game images, 7 languages (French, German,
#    Indonesian, Italian, Korean, Portuguese, Spanish), Creator Hub > Audience > Localization, moderated, beta until early 2027:
#    devforum.roblox.com/t/beta-translate-text-in-your-in-game-images-automatically/4984692 ; create.roblox.com/updates
#  Team Test Client Logs (Nov 13): see collaborators' output in Output window, LogService:GetLogHistoryAsync: create.roblox.com/updates
#  Codes:
#    The Forge FIRSTADMINEVENT (25 rerolls), PRISMATICSHARDS (Twilight Shards; 1,000 per several sources), 90KCCU (rerolls; 10 or 15):
#      destructoid.com/the-forge-codes/ (Nov 16), beebom.com/roblox-the-forge-codes/ (Nov 16), gamesradar the-forge-codes, joytify (Nov 17)
#    Pixel Blue Lock REORELEASE (4 Lucky Style Spins + 4 Style Spins + 1,500 Coins), KUNIGAMI (4 Lucky Flow Spins + 4 Flow Spins),
#      NIGHTMARE (4 Lucky Awakening Spins + 500 Ego Shards, Story Mode); join the group first:
#      destructoid.com/pixel-blue-lock-codes/ (Nov 16), mrguider.org/roblox/pixel-blue-lock-codes/, robloxden.com
#    Fisch CompanionHatTime (free companion hat): rocodes.gg/codes/fisch (Nov 17), pocketgamer.com/roblox/fisch-codes/, beebom hats guide
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("STEAL AN EGG", "white"), ("UPDATE 13", "yellow")], "tag": "OUT NOW",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Steal an Egg* just got *Update Thirteen*, and a *storm* is coming. Here are *three* things to know."},
   {"type": "item", "n": 1, "bg": "navy", "acc": "blue", "game": "STEAL AN EGG", "icon": "egg", "badge": "NEW",
    "title": "STORMLANDS BIOME",
    "vo": "Number *one*. A new *ninth biome* called *Stormlands* sits between *Prehistoric* and *Cosmic*."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "yellow", "game": "SKYFALL EVENT", "icon": "bolt", "badge": "EVERY 30 MIN",
    "title": "STORMY EGG",
    "vo": "Number *two*. *Skyfall* hits every *thirty minutes*. Smash rocks for *Thunderstones* and buy the *Stormy Egg*."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "STEAL AN EGG", "icon": "gem", "badge": "X2.75",
    "title": "THUNDEROUS MUTATION",
    "vo": "Number *three*. The new *Thunderous* mutation gives a *two point seven five* times boost."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("GOT A", "white"), ("STORMY EGG?", "yellow")],
    "vo": "Did you get a *Stormy Egg* yet? Tell me *below*."},
  ]},
 "short2": {
  "title_lines": [("3 ROBLOX CODES", "white"), ("JUST DROPPED", "yellow")], "tag": "FRESH DROP",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Three* Roblox codes *just dropped* for *rerolls*, *spins* and a *free hat*. Go *fast*."},
   {"type": "item", "n": 1, "bg": "maroon", "acc": "orange", "game": "THE FORGE", "icon": "hammer", "badge": "NEW",
    "title": "25 FREE REROLLS", "code": "FIRSTADMINEVENT",
    "vo": "First, *The Forge*. Code *first admin event* gives *twenty five rerolls*."},
   {"type": "item", "n": 2, "bg": "blue", "acc": "blue", "game": "PIXEL BLUE LOCK", "icon": "ball", "badge": "NEW",
    "title": "FREE STYLE SPINS", "code": "REORELEASE",
    "vo": "Next, *Pixel Blue Lock*. Code *Reo release* gives *style spins* and *coins*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "FISCH", "icon": "hat", "badge": "NEW",
    "title": "FREE COMPANION HAT", "code": "CompanionHatTime",
    "vo": "And *Fisch*. Code *companion hat time* gives a *free hat* for your *companion*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("FIRST?", "yellow")],
    "vo": "Codes *expire fast*, so redeem them *now*. Which one are *you* using *first*?"},
  ]},
 "short3": {
  "title_lines": [("3 MORE ROBLOX", "white"), ("CODES", "yellow")], "tag": "LATE NIGHT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Can't sleep? Here are *three more* Roblox codes. Type them in *exactly*."},
   {"type": "item", "n": 1, "bg": "violet", "acc": "purple", "game": "THE FORGE", "icon": "gem", "badge": "NEW",
    "title": "TWILIGHT SHARDS", "code": "PRISMATICSHARDS",
    "vo": "First, *The Forge*. Code *prismatic shards* gives *Twilight Shards*."},
   {"type": "item", "n": 2, "bg": "navy", "acc": "yellow", "game": "PIXEL BLUE LOCK", "icon": "ball", "badge": "NEW",
    "title": "FREE FLOW SPINS", "code": "KUNIGAMI",
    "vo": "*Pixel Blue Lock*. Code *Kunigami* gives *eight flow spins*."},
   {"type": "item", "n": 3, "bg": "red", "acc": "pink", "game": "PIXEL BLUE LOCK", "icon": "moon", "badge": "STORY MODE",
    "title": "AWAKENING SPINS", "code": "NIGHTMARE",
    "vo": "And code *nightmare* gives *awakening spins* and *Ego Shards* for *Story Mode*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT DID", "white"), ("YOU GET?", "yellow")],
    "vo": "Redeem them *fast*, they can *expire*. What did *you* get? Tell me *below*."},
  ]},
}

LONG = {
 "thumb": [("STORM IN STEAL AN EGG", "white"), ("+ 7 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 18",
   "vo": "Here's today's *Roblox news*. *Steal an Egg* brought a *storm*, *Fisch* companions can wear *hats*, Roblox can now *translate images*, and I've got *seven new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "navy", "acc": "blue", "game": "STEAL AN EGG", "icon": "egg", "badge": "UPDATE 13",
   "title": "STORMLANDS + SKYFALL",
   "bullets": ["NEW 9TH BIOME: STORMLANDS", "SKYFALL EVERY 30 MIN", "STORMY EGG + THUNDEROUS MUTATION"],
   "vo": "Number *one*. *Steal an Egg* Update *Thirteen* added *Stormlands*, the *ninth biome*. A *Skyfall* event hits every *thirty minutes*. Smash rocks for *Thunderstones* and trade them for the *Stormy Egg*. There's also a *Thunderous* mutation with a *two point seven five* times boost."},
  {"type": "item", "n": 2, "bg": "green", "acc": "green", "game": "FISCH", "icon": "hat", "badge": "NEW",
   "title": "COMPANION HATS",
   "bullets": ["HATS FOR YOUR COMPANIONS", "NEW NPC: CRAZY STYLIST", "FISH, SHOPS + MERCHANTS"],
   "vo": "Number *two*. *Fisch* added *Companion Hats*. A new *Crazy Stylist* in *Moosewood* gives a *quest*, and finishing it unlocks the *Crazy Styles* cap. Other hats come from *fishing*, *shops*, and the *traveling merchant*."},
  {"type": "item", "n": 3, "bg": "violet", "acc": "yellow", "game": "ROBLOX STUDIO", "icon": "frame", "badge": "BETA",
   "title": "AUTO IMAGE TRANSLATION",
   "bullets": ["TEXT IN IMAGES GETS TRANSLATED", "7 LANGUAGES IN BETA", "TEAM TEST CLIENT LOGS TOO"],
   "vo": "Number *three*, for *creators*. Roblox can now *translate text* inside your *game images* in *seven languages*. It's a *beta* you turn on in *Creator Hub*. Plus, *Team Test* now shows your *teammates' logs* in the *Output* window."},
  {"type": "item", "n": 4, "bg": "maroon", "acc": "orange", "game": "THE FORGE", "icon": "hammer", "badge": "CODES",
   "title": "FREE REROLLS", "code": "FIRSTADMINEVENT",
   "bullets": ["FIRSTADMINEVENT: 25 REROLLS", "PRISMATICSHARDS: TWILIGHT SHARDS", "90KCCU: REROLLS"],
   "vo": "Now, *codes*. Number *four*. *The Forge* has *first admin event* for *twenty five rerolls*, *prismatic shards* for *Twilight Shards*, and *ninety K C C U* for more *rerolls*."},
  {"type": "item", "n": 5, "bg": "blue", "acc": "pink", "game": "PIXEL BLUE LOCK", "icon": "ball", "badge": "CODES",
   "title": "FREE SPINS", "code": "REORELEASE",
   "bullets": ["REORELEASE: STYLE SPINS + COINS", "KUNIGAMI: FLOW SPINS", "NIGHTMARE: AWAKENING SPINS"],
   "vo": "Number *five*. *Pixel Blue Lock* has *Reo release*, *Kunigami*, and *nightmare* for *style*, *flow* and *awakening spins*. Join the *group* first."},
  {"type": "item", "n": 6, "bg": "green", "acc": "green", "game": "FISCH", "icon": "fish", "badge": "CODE",
   "title": "FREE COMPANION HAT", "code": "CompanionHatTime",
   "bullets": ["CompanionHatTime: FREE HAT"],
   "vo": "And number *six*. *Fisch* code *companion hat time* gives a *free hat* for your *companion*."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("FREE CREATOR PLUS ENDS", "NOV 19"), ("INCUBATOR DEADLINE", "DEC 7"),
            ("GAME AWARDS ON ROBLOX", "DEC 10"), ("PLUS UPGRADE DEADLINE", "DEC 19")],
   "vo": "Coming up. Free creator *Plus* ends *tomorrow*, *November nineteenth*. The *Incubator* deadline is *December seventh*, *The Game Awards* hit Roblox on *December tenth*, and the *Plus upgrade* window closes *December nineteenth*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH UPDATE", "white"), ("WINS?", "yellow")],
   "vo": "That's *today's* news. Which update are *you* playing first? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-18_1900_Short_StealAnEggStorm", "schedule_ist": "2026-11-18 19:00",
            "title": "Steal an Egg Update 13 Brought a Storm! ⛈️ #roblox #shorts",
            "description": "Steal an Egg Update 13 added Stormlands, the new 9th biome. A Skyfall event hits every 30 minutes: smash rocks for Thunderstones and get the limited Stormy Egg. There's also a new Thunderous mutation (x2.75).\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #stealanegg #shorts"},
 "long": {"file": "SS_2026-11-18_2300_Long_NewsToday", "schedule_ist": "2026-11-18 23:00",
          "title": "Roblox News Today: Steal an Egg Storm, Fisch Companion Hats & 7 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: Steal an Egg Update 13 added the Stormlands biome, a Skyfall event every 30 minutes with the Stormy Egg and a new Thunderous mutation, Fisch added Companion Hats and the Crazy Stylist NPC, Roblox launched a beta that automatically translates text inside in-game images into 7 languages (plus Team Test Client Logs in Studio), and 3 games have new codes.\n\nChapters:\n0:00 Intro\n0:12 Steal an Egg Update 13\n0:28 Fisch Companion Hats\n0:41 Image Translation Beta + Team Test Logs\n0:56 The Forge Codes\n1:08 Pixel Blue Lock + Fisch Codes\n1:23 Coming Up\n1:38 Outro\n\nCodes in this video:\nThe Forge: FIRSTADMINEVENT (25 rerolls), PRISMATICSHARDS (Twilight Shards), 90KCCU (rerolls)\nPixel Blue Lock: REORELEASE (4 Lucky Style Spins + 4 Style Spins + 1,500 Coins), KUNIGAMI (4 Lucky Flow Spins + 4 Flow Spins), NIGHTMARE (4 Lucky Awakening Spins + 500 Ego Shards, Story Mode) - join the group first\nFisch: CompanionHatTime (free companion hat)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "steal an egg", "steal an egg update 13", "fisch", "fisch companion hats", "roblox image translation", "the forge codes", "pixel blue lock codes", "fisch codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-19_0100_Short_CodesJustDropped", "schedule_ist": "2026-11-19 01:00",
            "title": "3 Roblox Codes That Just Dropped 💎 #roblox #shorts",
            "description": "3 Roblox codes:\nThe Forge: FIRSTADMINEVENT (25 rerolls)\nPixel Blue Lock: REORELEASE (style spins + coins, join the group first)\nFisch: CompanionHatTime (free companion hat)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-19_0300_Short_LateNightCodes", "schedule_ist": "2026-11-19 03:00",
            "title": "3 More Roblox Codes You Probably Missed 👀 #roblox #shorts",
            "description": "3 more Roblox codes:\nThe Forge: PRISMATICSHARDS (Twilight Shards)\nPixel Blue Lock: KUNIGAMI (4 Lucky Flow Spins + 4 Flow Spins)\nPixel Blue Lock: NIGHTMARE (4 Lucky Awakening Spins + 500 Ego Shards, Story Mode)\n\nJoin the Pixel Blue Lock group first.\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
}
