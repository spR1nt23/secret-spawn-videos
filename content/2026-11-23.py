# Secret Spawn - 23 Nov 2026 content
# Sources (checked 22 Nov 2026; devforum / create.roblox.com / playadopt.me / fischipedia / fandom were not fetchable here,
# so web search snippets were used):
#  Adopt Me! Quality of Life update (official post Fri Nov 20, 2026; event Nov 20 16:05 UTC -> Nov 27 15:45 UTC = 10:45 AM ET;
#    25 new Pet Paints at the Salon, 7 new Mega Neon Paints (49 Robux each; older Mega Neon Paints leave the rotation for now),
#    Natural Color option to reset pet parts, pose pets with unlocked tricks on your profile, skip the neon-making animation,
#    shorter load times between buildings, Trading Hub Phone search/post from anywhere):
#    playadopt.me/news/quality-of-life-improvements ; playadopt.me/news/pet-paints-notes ;
#    elyxir.gg/news/adopt-me/adopt-me-quality-of-life-update-salon-colors-pet-poses-and-building-tools ;
#    nerdschalk.com/adopt-me-new-pet-colors-paint-prices ; u7buy.com/blog/adopt-me-quality-of-life-update/
#  Fisch Miscellaneous Update (v2.11.0, Nov 21, 2026; ends the Venue Encore, new quest NPC, new rare "Alpha" fish attribute
#    (like Shiny/Sparkling; a world event can boost the chance), Achievements in the Journal, consumables toggle + tooltips,
#    precursor to the Thanksgiving update; new code TurkeySoon):
#    sportskeeda.com/roblox-news/fisch-miscellaneous-update-patch-notes ; fischipedia.org/wiki/2.11 ;
#    treyexgaming.com/fisch-misc-update-guide/
#  Studio Beta: UI Particles / ParticleEmitter2D (DevForum Nov 19, 2026; File > Beta Features > UI Particles;
#    parent to any GuiObject; places using it cannot be published during the beta):
#    devforum.roblox.com/t/studio-beta-ui-particles/4996850 ; create.roblox.com/docs/ui/2D-particle-emitters
#  List: Thanksgiving Nov 26; Adopt Me QoL event ends Nov 27; Dandy's World 1.0 event ends Nov 30 (Nov 22 set);
#    TextChatService rule Dec 3 (create.roblox.com/updates); Incubator applications Dec 7 (devforum weekly recap Nov 9-13)
#  Codes:
#    Fisch TurkeySoon (Beebom: 1000 Coins, 50 Instant Catcher, 50 Luminous Larva, Alpha title; told as "coins and items"):
#      beebom.com/roblox-fisch-codes/ (Nov 22), sportskeeda patch notes, fischipedia 2.11, pocketgamer
#    TRENCH DECAY THANKSGIVINGFEAST, THANKSGIVINGMANIFEST (50 Turkey Legs each; sign up for 2 events first):
#      destructoid.com/trench-ww1-roblox-codes/ , progameguides.com/roblox/roblox-trench-ww1-codes/ (Nov 21), mrguider (Nov 20)
#    Ishin FOX, THANKSGIVING (rerolls + yen; join the luure group first):
#      pockettactics.com/ishin-codes (Nov 21), mrguider.org/roblox/ishin-codes/ (Nov 20), newgame.co.jp tracker (Nov 22)
#    Bigfoot BIGFOOTUPDATE1 (800 Bigfoot Coins; sadece short3):
#      destructoid.com/roblox-bigfoot-codes/ (Nov 21), progameguides.com/roblox/roblox-bigfoot-codes-2/ (Nov 21)
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("ADOPT ME", "white"), ("PAINT UPDATE", "yellow")], "tag": "NEW UPDATE",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Adopt Me* just dropped a big *quality of life* update, and here are *three* changes you'll love."},
   {"type": "item", "n": 1, "bg": "violet", "acc": "pink", "game": "ADOPT ME", "icon": "brush", "badge": "SALON",
    "title": "25 NEW PET PAINTS",
    "vo": "Number *one*. The *Salon* has *twenty five* new *pet paints* to recolor your pets."},
   {"type": "item", "n": 2, "bg": "blue", "acc": "blue", "game": "ADOPT ME", "icon": "gem", "badge": "NEW",
    "title": "7 MEGA NEON PAINTS",
    "vo": "Number *two*. *Seven* new *Mega Neon* paints are here, but the old ones are leaving *for now*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "ADOPT ME", "icon": "frame", "badge": "PROFILE",
    "title": "POSE YOUR PETS",
    "vo": "Number *three*. You can now *pose* pets on your *profile* using their *tricks*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT COLOR", "white"), ("WILL YOU PICK?", "yellow")],
    "vo": "So, what *color* will *you* paint your pet? Tell me in the *comments*."},
  ]},
 "short2": {
  "title_lines": [("3 THANKSGIVING", "white"), ("ROBLOX CODES", "yellow")], "tag": "NEW CODES",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Thanksgiving* week is here, so grab these *three* new Roblox codes before they're *gone*."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "FISCH", "icon": "fish", "badge": "NEW",
    "title": "FREE COINS + ITEMS", "code": "TurkeySoon",
    "vo": "First, *Fisch*. Code *turkey soon* gives free *coins* and *items*."},
   {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "TRENCH DECAY", "icon": "drumstick", "badge": "NEW",
    "title": "50 TURKEY LEGS", "code": "THANKSGIVINGFEAST",
    "vo": "Next, *Trench Decay*. Code *thanksgiving feast* gives *fifty* turkey legs."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "ISHIN", "icon": "dice", "badge": "NEW",
    "title": "REROLLS + YEN", "code": "THANKSGIVING",
    "vo": "And *Ishin*. Code *thanksgiving* gives free *rerolls* and *yen*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("WORKED?", "yellow")],
    "vo": "Codes can *expire* at any time, so be *quick*. Which one *worked* for you?"},
  ]},
 "short3": {
  "title_lines": [("3 CODES YOU", "white"), ("PROBABLY MISSED", "yellow")], "tag": "LATE NIGHT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Here are *three* new Roblox codes you probably *missed*, and they still *work*."},
   {"type": "item", "n": 1, "bg": "navy", "acc": "green", "game": "BIGFOOT", "icon": "binoculars", "badge": "NEW",
    "title": "800 FREE COINS", "code": "BIGFOOTUPDATE1",
    "vo": "First, *Bigfoot*. Code *bigfoot update one* gives *eight hundred* Bigfoot coins."},
   {"type": "item", "n": 2, "bg": "red", "acc": "yellow", "game": "ISHIN", "icon": "dice", "badge": "NEW",
    "title": "REROLLS + YEN", "code": "FOX",
    "vo": "Next, *Ishin*. Code *fox* gives more free *rerolls* and *yen*."},
   {"type": "item", "n": 3, "bg": "violet", "acc": "purple", "game": "TRENCH DECAY", "icon": "drumstick", "badge": "ACTIVE",
    "title": "50 TURKEY LEGS", "code": "THANKSGIVINGMANIFEST",
    "vo": "And *Trench Decay*. Code *thanksgiving manifest* gives *fifty* more turkey legs."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT DID", "white"), ("YOU GET?", "yellow")],
    "vo": "Redeem them *fast*, because they can *expire*. What did *you* get?"},
  ]},
}

LONG = {
 "thumb": [("ADOPT ME PAINTS", "white"), ("+ 5 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 23",
   "vo": "Here's today's *Roblox news*. *Adopt Me* got new *pet paints*, *Fisch* added a rare *Alpha* fish, creators can test *UI particles*, and I've got *five new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "violet", "acc": "pink", "game": "ADOPT ME", "icon": "brush", "badge": "UPDATE",
   "title": "QUALITY OF LIFE UPDATE",
   "bullets": ["25 NEW PET PAINTS AT THE SALON", "7 NEW MEGA NEON PAINTS", "POSE PETS ON YOUR PROFILE", "EVENT ENDS NOV 27"],
   "vo": "Number *one*. *Adopt Me* released a *quality of life* update on *Friday*. The *Salon* has *twenty five* new *pet paints*, plus *seven* new *Mega Neon* paints. The old Mega Neon paints are leaving the rotation *for now*. You can also *pose* pets on your *profile* with their tricks, and *skip* the neon animation. The update event runs until *November twenty seventh*."},
  {"type": "item", "n": 2, "bg": "blue", "acc": "blue", "game": "FISCH", "icon": "fish", "badge": "NOV 21",
   "title": "MISCELLANEOUS UPDATE",
   "bullets": ["NEW RARE ALPHA FISH", "ACHIEVEMENTS IN THE JOURNAL", "NEW QUEST NPC", "THANKSGIVING IS NEXT"],
   "vo": "Number *two*. *Fisch* got its *Miscellaneous Update* on *Saturday*. It adds a rare new *Alpha* fish attribute, like *Shiny* or *Sparkling*. Your *Journal* now has *achievements*, and there's a new *quest* character. The developers say it leads into a *Thanksgiving* update."},
  {"type": "item", "n": 3, "bg": "green", "acc": "yellow", "game": "ROBLOX STUDIO", "icon": "sparkles", "badge": "BETA",
   "title": "UI PARTICLES",
   "bullets": ["NEW: PARTICLEEMITTER2D", "SPARKLES AND BURSTS ON UI", "STUDIO BETA ONLY"],
   "vo": "Number *three*, for *creators*. A new *Studio beta* called *UI particles* lets you add *sparkles* and *bursts* to buttons and menus. It's *Studio only* for now, so you *can't* publish live games with it yet."},
  {"type": "item", "n": 4, "bg": "navy", "acc": "green", "game": "FISCH", "icon": "fish", "badge": "CODE",
   "title": "FREE COINS + ITEMS", "code": "TurkeySoon",
   "bullets": ["TurkeySoon: COINS + ITEMS"],
   "vo": "Now, *codes*. Number *four*. *Fisch* has *turkey soon* for free *coins* and *items*. Use a capital *T* and a capital *S*."},
  {"type": "item", "n": 5, "bg": "maroon", "acc": "orange", "game": "TRENCH DECAY", "icon": "drumstick", "badge": "CODES",
   "title": "100 TURKEY LEGS", "code": "THANKSGIVINGFEAST",
   "bullets": ["THANKSGIVINGFEAST: 50 TURKEY LEGS", "THANKSGIVINGMANIFEST: 50 TURKEY LEGS"],
   "vo": "Number *five*. *Trench Decay* has *thanksgiving feast* and *thanksgiving manifest*, for *fifty* turkey legs each. Sign up for *two* events first."},
  {"type": "item", "n": 6, "bg": "red", "acc": "pink", "game": "ISHIN", "icon": "dice", "badge": "CODES",
   "title": "REROLLS + YEN", "code": "THANKSGIVING",
   "bullets": ["THANKSGIVING: REROLLS + YEN", "FOX: REROLLS + YEN"],
   "vo": "And number *six*. *Ishin* has *thanksgiving* and *fox*, for *rerolls* and *yen*. Join the game's *group* first."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("THANKSGIVING", "NOV 26"), ("ADOPT ME UPDATE EVENT ENDS", "NOV 27"),
            ("DANDY'S WORLD 1.0 EVENT ENDS", "NOV 30"), ("TEXT CHAT RULE ENFORCED", "DEC 3")],
   "vo": "Coming up. *Thanksgiving* is *Thursday*, the *Adopt Me* update event ends *November twenty seventh*, the *Dandy's World* event ends *November thirtieth*, and the *chat rule* starts *December third*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT COLOR", "white"), ("IS YOUR PET?", "yellow")],
   "vo": "That's *today's* news. What *color* will you paint your *pet*? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-23_1900_Short_AdoptMePaints", "schedule_ist": "2026-11-23 19:00",
            "title": "Adopt Me Just Got 25 New Pet Paints! 🎨 #roblox #shorts",
            "description": "Adopt Me's Quality of Life update (Fri, Nov 20) adds 25 new Pet Paints at the Salon and 7 new Mega Neon Paints, while the older Mega Neon Paints leave the rotation for now. You can also pose your pets on your profile using their tricks. The update event runs until Nov 27 (10:45 AM ET).\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long": {"file": "SS_2026-11-23_2300_Long_NewsToday", "schedule_ist": "2026-11-23 23:00",
          "title": "Roblox News Today: Adopt Me Paints, Fisch Alpha Fish & 5 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: Adopt Me's Quality of Life update adds 25 new Pet Paints, 7 new Mega Neon Paints and pet poses on your profile (update event ends Nov 27, 10:45 AM ET), Fisch's Miscellaneous Update adds the rare Alpha fish attribute and Journal achievements ahead of Thanksgiving, creators can test UI Particles in a Studio-only beta, and 3 games have new codes.\n\nChapters:\n0:00 Intro\n0:11 Adopt Me Quality of Life Update\n0:34 Fisch Miscellaneous Update\n0:49 UI Particles Studio Beta\n1:02 Fisch + TRENCH DECAY Codes\n1:19 Ishin Codes + Coming Up\n1:38 Outro\n\nCodes in this video:\nFisch: TurkeySoon (free coins and items)\nTRENCH DECAY: THANKSGIVINGFEAST (50 Turkey Legs), THANKSGIVINGMANIFEST (50 Turkey Legs); sign up for 2 events first\nIshin: THANKSGIVING (rerolls + yen), FOX (rerolls + yen); join the group first\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "adopt me update", "adopt me pet paints", "mega neon paints", "fisch update", "fisch alpha", "roblox ui particles", "fisch codes", "trench decay codes", "ishin codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-24_0100_Short_ThanksgivingCodes", "schedule_ist": "2026-11-24 01:00",
            "title": "3 Thanksgiving Roblox Codes You Need Today! 🦃 #roblox #shorts",
            "description": "3 Roblox codes:\nFisch: TurkeySoon (free coins and items)\nTRENCH DECAY: THANKSGIVINGFEAST (50 Turkey Legs; sign up for 2 events first)\nIshin: THANKSGIVING (rerolls + yen; join the group first)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-24_0300_Short_MissedCodes", "schedule_ist": "2026-11-24 03:00",
            "title": "3 Roblox Codes You Probably Missed 👀 #roblox #shorts",
            "description": "3 more Roblox codes:\nBigfoot: BIGFOOTUPDATE1 (800 Bigfoot Coins)\nIshin: FOX (rerolls + yen; join the group first)\nTRENCH DECAY: THANKSGIVINGMANIFEST (50 Turkey Legs; sign up for 2 events first)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
}
