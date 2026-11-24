# Secret Spawn - 25 Nov 2026 content
# Sources (checked 24 Nov 2026; devforum / create.roblox.com / progameguides / destructoid / ffbooyah were not fetchable here,
# so web search snippets were used):
#  Net a Fish Thanksgiving update (scheduled Sat Nov 21, 2026 17:00 UTC; event to Dec 5 17:00 UTC per trackers):
#    Great Gobbler giant turkey boss (event recurs every 45 min in a server; first win = Gobbler Tamer title +
#    Harvest Hearth base skin), Bloodmaw = first World Boss, Corn event currency from contracts + 75-tier Thanksgiving Pass,
#    spent in the Thanksgiving Market:
#    nerdschalk.com/net-a-fish-thanksgiving-event-rewards ; sportskeeda.com/roblox-news/net-fish-great-gobbler-boss-guide ;
#    sportskeeda.com/roblox-news/net-fish-bloodmaw-boss-guide ; sportskeeda.com/roblox-news/when-next-net-a-fish-update ;
#    bloxnew.com/net-a-fish/updates/
#  Throw Food For Animals Thanksgiving event (live, replaced Dreamland; ends Nov 28, 2026; event every 30 min at :00/:30 for
#    ~5 min; collect ingredients, make sandwiches, throw them for Thanksgiving animals; 21 limited animals -> Feast Trail):
#    sportskeeda.com/roblox-news/throw-food-for-animals-thanksgiving-event-guide ; techwiser.com/throw-food-for-animals-thanksgiving-event-guide/ ;
#    nerdschalk.com/thanksgiving-feast-throw-food-for-animals ; ffbooyah.com/2026/11/22/throw-food-for-animals-thanksgiving-event-guide-sandwiches-animals-and-rewards/
#  Scare Your Favorite Streamer Thanksgiving event (until Nov 29, 2026; drumsticks -> Thanksgiving reward track; Robux-shop
#    Thanksgiving Egg with 6 pets): sportskeeda.com/roblox-news/scare-your-favorite-streamer-thanksgiving-event-guide
#  Highly Engaged Player threshold for Kids & Select lowered 250 -> 100 ([Update] Nov 19, 2026), HEP counts now update every
#    hour in Creator Hub (Publish Settings > Manage Audience):
#    devforum.roblox.com/t/highly-engaged-player-threshold-drops-to-250/4820164 ;
#    devforum.roblox.com/t/a-simpler-path-to-publish-plus-invite-early-testers/4930524 ;
#    devforum.roblox.com/t/making-publishing-easier-our-vision-and-whats-coming/4865780 (roadmap: 250 -> 100 in Nov 2026)
#  List: Thanksgiving Thu Nov 26; Throw Food For Animals event ends Nov 28; Scare Your Favorite Streamer event ends Nov 29;
#    pass free trials live Dec 2 (devforum.roblox.com/t/introducing-pass-free-trials/4995943)
#  Codes:
#    Net a Fish 20MVISITS (2 Trait Rolls + 15 min x2 Luck/Money/Pearls/Fish Caught), THANKSGIVING (15 min x2 Luck/Money/
#      Pearls/Fish Caught): beebom.com/net-a-fish-codes/ ; destructoid.com/roblox-net-a-fish-codes/ (Nov 23) ;
#      claimcodes.gg/roblox/net-a-fish/ (Nov 23)
#    Practical Basketball THANKSGIVING2026 (15,000 Coins + 2x Badge XP for 3 games; join the Practical's Games group):
#      beebom.com/practical-basketball-codes/ ; destructoid.com/practical-basketball-codes/ (Nov 22) ;
#      progameguides.com/roblox/practical-basketball-codes/ (Nov 21)
#    The Ditch Hotel THANKSGIVING (10k Cash + 1 Revive): progameguides.com/roblox/the-ditch-hotel-codes/ (Nov 21) ;
#      destructoid.com/ditch-hotel-codes/ (Nov 23)
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("3 THANKSGIVING", "white"), ("EVENTS LIVE", "yellow")], "tag": "LIVE NOW",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Three* Roblox games just started *Thanksgiving* events, and one has a *giant* turkey boss."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "NET A FISH", "icon": "fish", "badge": "LIVE",
    "title": "NET THE GREAT GOBBLER",
    "vo": "Number *one*. In *Net a Fish*, throw your net over the *Great Gobbler* for event *corn*."},
   {"type": "item", "n": 2, "bg": "green", "acc": "yellow", "game": "THROW FOOD FOR ANIMALS", "icon": "sandwich", "badge": "ENDS NOV 28",
    "title": "SANDWICH FEAST",
    "vo": "Number *two*. *Throw Food For Animals* lets you make *sandwiches* to get new *Thanksgiving* animals."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "SCARE YOUR FAVORITE STREAMER", "icon": "drumstick", "badge": "ENDS NOV 29",
    "title": "DRUMSTICK REWARDS",
    "vo": "Number *three*. *Scare Your Favorite Streamer* has a *drumstick* reward track until *November twenty ninth*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH EVENT", "white"), ("ARE YOU PLAYING?", "yellow")],
    "vo": "So, which *event* are *you* playing *first*? Tell me in the *comments*."},
  ]},
 "short2": {
  "title_lines": [("3 THANKSGIVING", "white"), ("ROBLOX CODES", "yellow")], "tag": "NEW CODES",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Here are *three* new *Thanksgiving* Roblox codes you probably *missed*."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "NET A FISH", "icon": "fish", "badge": "NEW",
    "title": "2 FREE TRAIT ROLLS", "code": "20MVISITS",
    "vo": "First, *Net a Fish*. Code *twenty M visits* gives *two* trait rolls and a *double* luck boost."},
   {"type": "item", "n": 2, "bg": "green", "acc": "orange", "game": "PRACTICAL BASKETBALL", "icon": "basketball", "badge": "NEW",
    "title": "15,000 FREE COINS", "code": "THANKSGIVING2026",
    "vo": "Next, *Practical Basketball*. Code *thanksgiving twenty twenty six* gives *fifteen thousand* coins."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "yellow", "game": "THE DITCH HOTEL", "icon": "drumstick", "badge": "NEW",
    "title": "10K CASH + REVIVE", "code": "THANKSGIVING",
    "vo": "And *The Ditch Hotel*. Code *thanksgiving* gives *ten thousand* cash and a *revive*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("WORKED?", "yellow")],
    "vo": "Codes can *expire* fast, so be *quick*. Which one *worked* for you?"},
  ]},
 "short3": {
  "title_lines": [("KIDS & SELECT", "white"), ("GOT EASIER", "yellow")], "tag": "CREATORS",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Roblox just made it *easier* for new games to reach *more* players. Here's what changed."},
   {"type": "item", "n": 1, "bg": "navy", "acc": "blue", "game": "KIDS & SELECT", "icon": "trophy", "badge": "250 TO 100",
    "title": "LOWER BAR TO ENTER",
    "vo": "Number *one*. Games now need *one hundred* highly engaged players, down from *two hundred fifty*."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "pink", "game": "CREATOR HUB", "icon": "bolt", "badge": "HOURLY",
    "title": "HOURLY COUNTS",
    "vo": "Number *two*. That player count now updates *every hour* in *Creator Hub*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "CREATOR HUB", "icon": "gamepad", "badge": "CHECK IT",
    "title": "MANAGE AUDIENCE",
    "vo": "Number *three*. Creators can check their count under *Manage Audience* in publish *settings*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("ARE YOU", "white"), ("MAKING A GAME?", "yellow")],
    "vo": "Are *you* making a Roblox *game*? Tell me what it is *below*."},
  ]},
}

LONG = {
 "thumb": [("TURKEY BOSS", "white"), ("+ 4 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 25",
   "vo": "Here's today's *Roblox news*. *Net a Fish* has a giant *turkey* boss, *Throw Food For Animals* has a Thanksgiving *feast*, new games can reach *Kids and Select* more easily, and I've got *four new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "NET A FISH", "icon": "fish", "badge": "LIVE",
   "title": "THANKSGIVING UPDATE",
   "bullets": ["GREAT GOBBLER TURKEY BOSS", "BLOODMAW WORLD BOSS", "EARN CORN, SPEND IN MARKET", "THANKSGIVING PASS"],
   "vo": "Number *one*. *Net a Fish* dropped its *Thanksgiving* update. A giant turkey called the *Great Gobbler* shows up about every *forty five* minutes, and you throw your *net* over it. There's also *Bloodmaw*, the game's first *world* boss. You earn *corn* from contracts and the *Thanksgiving Pass*, then spend it in the *Market*."},
  {"type": "item", "n": 2, "bg": "green", "acc": "yellow", "game": "THROW FOOD FOR ANIMALS", "icon": "sandwich", "badge": "ENDS NOV 28",
   "title": "THANKSGIVING FEAST",
   "bullets": ["COLLECT INGREDIENTS", "MAKE + THROW SANDWICHES", "21 LIMITED ANIMALS", "ENDS NOV 28"],
   "vo": "Number *two*. *Throw Food For Animals* has a *Thanksgiving* event. You collect *ingredients*, make special *sandwiches*, and throw them to get *limited* animals. There are *twenty one* to find, and the event ends *November twenty eighth*."},
  {"type": "item", "n": 3, "bg": "navy", "acc": "orange", "game": "KIDS & SELECT", "icon": "trophy", "badge": "250 TO 100",
   "title": "EASIER TO GET IN",
   "bullets": ["NOW 100 HIGHLY ENGAGED PLAYERS", "WAS 250 BEFORE", "COUNTS UPDATE EVERY HOUR"],
   "vo": "Number *three*, for creators. To reach *Kids and Select*, a game now needs *one hundred* highly engaged players, down from *two hundred fifty*. That count now updates *every hour* in *Creator Hub*, so new games can grow *faster*."},
  {"type": "item", "n": 4, "bg": "violet", "acc": "pink", "game": "NET A FISH", "icon": "fish", "badge": "CODES",
   "title": "TRAIT ROLLS + BOOSTS", "code": "20MVISITS",
   "bullets": ["20MVISITS: 2 TRAIT ROLLS + 2X BOOSTS", "THANKSGIVING: 15 MIN 2X BOOSTS"],
   "vo": "Now, *codes*. Number *four*. *Net a Fish* has *twenty M visits* for *two* trait rolls and boosts, and *thanksgiving* for fifteen minutes of *double* luck and money."},
  {"type": "item", "n": 5, "bg": "maroon", "acc": "orange", "game": "PRACTICAL BASKETBALL", "icon": "basketball", "badge": "NEW",
   "title": "15,000 FREE COINS", "code": "THANKSGIVING2026",
   "bullets": ["THANKSGIVING2026: 15K COINS + 2X BADGE XP"],
   "vo": "Number *five*. *Practical Basketball* has *thanksgiving twenty twenty six*, for *fifteen thousand* coins. Join the game's *group* first."},
  {"type": "item", "n": 6, "bg": "red", "acc": "yellow", "game": "THE DITCH HOTEL", "icon": "drumstick", "badge": "NEW",
   "title": "10K CASH + REVIVE", "code": "THANKSGIVING",
   "bullets": ["THANKSGIVING: 10K CASH + 1 REVIVE"],
   "vo": "And number *six*. *The Ditch Hotel* has *thanksgiving*, for *ten thousand* cash and a *revive*."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("THANKSGIVING", "NOV 26"), ("THROW FOOD EVENT ENDS", "NOV 28"),
            ("SCARE STREAMER EVENT ENDS", "NOV 29"), ("PASS FREE TRIALS GO LIVE", "DEC 2")],
   "vo": "Coming up. *Thanksgiving* is *Thursday*, the *Throw Food* event ends *Saturday*, *Scare Your Favorite Streamer's* event ends *Sunday*, and pass *free trials* go live *December second*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH EVENT", "white"), ("ARE YOU PLAYING?", "yellow")],
   "vo": "That's *today's* news. Which *Thanksgiving* event are you playing? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-25_1900_Short_ThanksgivingEvents", "schedule_ist": "2026-11-25 19:00",
            "title": "3 Roblox Thanksgiving Events Live Right Now! 🦃 #roblox #shorts",
            "description": "Three Roblox games have Thanksgiving events live: Net a Fish added the Great Gobbler turkey boss and event corn, Throw Food For Animals has a sandwich feast with limited animals (ends Nov 28), and Scare Your Favorite Streamer has a drumstick reward track (ends Nov 29). Dates can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long": {"file": "SS_2026-11-25_2300_Long_NewsToday", "schedule_ist": "2026-11-25 23:00",
          "title": "Roblox News Today: Net a Fish Turkey Boss, Easier Kids & Select & 4 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: Net a Fish's Thanksgiving update adds the Great Gobbler turkey boss, the Bloodmaw world boss, a Thanksgiving Pass and a corn Market, Throw Food For Animals has a Thanksgiving feast event with 21 limited animals (ends Nov 28), and games now need 100 Highly Engaged Players instead of 250 to reach Kids & Select, with counts updating every hour in Creator Hub. Plus 3 games have 4 new codes.\n\nChapters:\n0:00 Intro\n0:14 Net a Fish Thanksgiving Update\n0:32 Throw Food For Animals Thanksgiving Feast\n0:46 Kids & Select Threshold Drops to 100\n1:01 Net a Fish, Practical Basketball + The Ditch Hotel Codes\n1:20 Coming Up + Outro\n\nCodes in this video:\nNet a Fish: 20MVISITS (2 Trait Rolls + 15 min x2 Luck, Money, Pearls and Fish Caught), THANKSGIVING (15 min x2 Luck, Money, Pearls and Fish Caught)\nPractical Basketball: THANKSGIVING2026 (15,000 Coins + 2x Badge XP for 3 games; join the Practical's Games group first)\nThe Ditch Hotel: THANKSGIVING (10k Cash + 1 Revive)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "net a fish", "net a fish thanksgiving", "great gobbler", "throw food for animals", "roblox thanksgiving", "kids and select", "net a fish codes", "practical basketball codes", "the ditch hotel codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-26_0100_Short_ThanksgivingCodes", "schedule_ist": "2026-11-26 01:00",
            "title": "3 Thanksgiving Roblox Codes You Probably Missed 👀 #roblox #shorts",
            "description": "3 Roblox codes:\nNet a Fish: 20MVISITS (2 Trait Rolls + 15 min x2 Luck, Money, Pearls and Fish Caught)\nPractical Basketball: THANKSGIVING2026 (15,000 Coins + 2x Badge XP for 3 games; join the Practical's Games group first)\nThe Ditch Hotel: THANKSGIVING (10k Cash + 1 Revive)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-26_0300_Short_KidsSelectEasier", "schedule_ist": "2026-11-26 03:00",
            "title": "Roblox Just Made Kids & Select Easier to Reach! 🛠️ #roblox #shorts",
            "description": "Roblox lowered the Highly Engaged Player threshold for Kids & Select from 250 to 100. Highly Engaged Player counts now update every hour in Creator Hub, and creators can check theirs under Publish Settings > Manage Audience.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxstudio #shorts"},
}
