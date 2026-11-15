# Secret Spawn - 16 Nov 2026 content
# Sources (checked 15 Nov 2026):
#  The Game Awards on Roblox (Dec 10, 18+ only, The Block, vote + virtual merch, first time):
#    animenewsnetwork.com/press-release/2026-11-13/roblox-to-stream-the-game-awards-2026-live-on-december-10/.243808
#    beebom.com/the-game-awards-2026-is-coming-to-roblox-with-a-catch/, vgtimes.com/gaming-news/174553-the-game-awards-2026-will-stream-on-roblox-but-only-for-viewers-18.html,
#    powerupgaming.co.uk/2026/11/14/game-awards-roblox-adults-only-watch-party/
#  IARC age ratings in Australia (starts Jan 26 2027; Kids & Select games need IARC questionnaire; ratings by end of Dec;
#    other games answer one question -> 16+ if no restricted content):
#    devforum.roblox.com/t/introducing-iarc-age-ratings-in-australia/4985897 (via search snippets; DevForum blocked here)
#  Experiment metrics (Rewarded Video Ads set + Custom set, up to 3 own metrics from custom/economy/funnel events):
#    Weekly Recap Nov 9-13 2026 on devforum.roblox.com (search snippets)
#  Codes: Ishin COOKING / COOKING2 / DELAYSRY (rerolls, new Nov 14): pockettactics.com/ishin-codes, rallycodes.com/games/ishin/
#         Gokudo MIZUHASHI / RIDECRASH / CITYGARDEN (30 rerolls each): twinfinite.net/codes/gokudo-codes-roblox/,
#           progameguides.com/roblox/roblox-gokudo-codes/ (Nov 14), robloxden.com/game-codes/gokudo
#         The Forge SORRYFORBUGS!!! (10-15 rerolls, sources differ): beebom.com/roblox-the-forge-codes/ (Nov 13),
#           gamesradar.com/games/rpg/the-forge-codes/, dexerto.com/roblox/the-forge-codes-3287134/
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("GAME AWARDS", "white"), ("ON ROBLOX", "yellow")], "tag": "DEC 10",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*The Game Awards* are coming to *Roblox*, but there's a *big catch*. *Three* things to know."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "yellow", "game": "THE GAME AWARDS", "icon": "trophy", "badge": "DEC 10",
    "title": "LIVE ON ROBLOX",
    "vo": "Number *one*. The show streams *live* on Roblox on *December tenth*, for the *first time* ever."},
   {"type": "item", "n": 2, "bg": "red", "acc": "pink", "game": "THE GAME AWARDS", "icon": "shield", "badge": "18+",
    "title": "18+ VIEWERS ONLY",
    "vo": "Number *two*. Only players *eighteen* and *older* can watch it in *The Block*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "THE BLOCK", "icon": "gem", "badge": "FREE",
    "title": "VOTE + VIRTUAL MERCH",
    "vo": "Number *three*. Fans there can *vote* and claim *virtual merch*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("SHOULD IT BE", "white"), ("FOR EVERYONE?", "yellow")],
    "vo": "Should *everyone* be able to watch? Tell me *below*."},
  ]},
 "short2": {
  "title_lines": [("3 FREE ROBLOX", "white"), ("CODES", "yellow")], "tag": "JUST DROPPED",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Three* Roblox codes that *just dropped* today. Grab them *fast*, before they *expire*."},
   {"type": "item", "n": 1, "bg": "navy", "acc": "yellow", "game": "GOKUDO", "icon": "flame", "badge": "NEW",
    "title": "30 FREE REROLLS", "code": "MIZUHASHI",
    "vo": "First, *Gokudo*. Code *mizu hashi* gives you *thirty free rerolls*."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "purple", "game": "ISHIN", "icon": "swords", "badge": "NEW",
    "title": "FREE REROLLS", "code": "COOKING",
    "vo": "Next, *Ishin*. Code *cooking* gives you *free rerolls* for your build."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "THE FORGE", "icon": "hammer", "badge": "NEW",
    "title": "FREE REROLLS", "code": "SORRYFORBUGS!!!",
    "vo": "*The Forge*. Code *sorry for bugs*, with *three* exclamation marks, gives *rerolls*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("FIRST?", "yellow")],
    "vo": "Codes *expire fast*, so redeem them *now*. Which one are *you* using *first*? Tell me *below*."},
  ]},
 "short3": {
  "title_lines": [("3 MORE ROBLOX", "white"), ("CODES", "yellow")], "tag": "LATE NIGHT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Still up? Here are *three more* Roblox codes for *free rerolls*. Copy them *exactly*."},
   {"type": "item", "n": 1, "bg": "green", "acc": "green", "game": "GOKUDO", "icon": "car", "badge": "NEW",
    "title": "30 FREE REROLLS", "code": "RIDECRASH",
    "vo": "First, *Gokudo*. Code *ride crash* gives you *thirty free rerolls*."},
   {"type": "item", "n": 2, "bg": "blue", "acc": "blue", "game": "GOKUDO", "icon": "fruit", "badge": "NEW",
    "title": "30 MORE REROLLS", "code": "CITYGARDEN",
    "vo": "Then use code *city garden* in *Gokudo* for *thirty more*."},
   {"type": "item", "n": 3, "bg": "red", "acc": "pink", "game": "ISHIN", "icon": "swords", "badge": "NEW",
    "title": "FREE REROLLS", "code": "DELAYSRY",
    "vo": "*Ishin*. Code *delay sorry*, spelled *D E L A Y S R Y*, gives *rerolls*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT DID", "white"), ("YOU ROLL?", "yellow")],
    "vo": "Redeem them *fast*, they can *expire*. What did *you* roll? Tell me *below*."},
  ]},
}

LONG = {
 "thumb": [("GAME AWARDS", "white"), ("+ 7 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 16",
   "vo": "Here's today's *Roblox news*. *The Game Awards* are coming to Roblox, game *ratings* are changing in *Australia*, creators get *new test tools*, and I've got *seven new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "blue", "acc": "yellow", "game": "THE GAME AWARDS", "icon": "trophy", "badge": "DEC 10",
   "title": "THE GAME AWARDS ON ROBLOX",
   "bullets": ["LIVE ON THURSDAY, DEC 10", "18+ VIEWERS ONLY", "WATCH IN THE BLOCK: VOTE + MERCH"],
   "vo": "Number *one*. *The Game Awards* will stream *live* on Roblox on *Thursday*, *December tenth*. It's the *first time* an outside awards show streams on Roblox. But only players *eighteen* and *older* can watch, inside a venue called *The Block*, where fans can *vote* and claim *virtual merch*."},
  {"type": "item", "n": 2, "bg": "green", "acc": "green", "game": "AGE RATINGS", "icon": "scroll", "badge": "JAN 26",
   "title": "NEW RATINGS IN AUSTRALIA",
   "bullets": ["IARC RATINGS START JAN 26, 2027", "KIDS & SELECT GAMES NEED A QUESTIONNAIRE", "RATINGS DUE BY END OF DECEMBER"],
   "vo": "Number *two*. Roblox is switching to *I A R C* age ratings, starting in *Australia* on *January twenty sixth*. Games for *Kids* and *Select* accounts must fill out a *questionnaire* to stay playable there. Other games answer just *one question*."},
  {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "ROBLOX STUDIO", "icon": "binoculars", "badge": "NEW",
   "title": "NEW EXPERIMENT METRICS",
   "bullets": ["REWARDED VIDEO AD METRICS", "UP TO 3 CUSTOM METRICS", "TEST UPDATES BEFORE FULL LAUNCH"],
   "vo": "Number *three*. *Experiments* got *new metrics*. Creators can now track *rewarded video ads*, and add up to *three custom* metrics from their own *events*. That helps creators *test* changes on *some players* first. That means *better tested* updates for *you*."},
  {"type": "item", "n": 4, "bg": "violet", "acc": "purple", "game": "ISHIN", "icon": "swords", "badge": "CODES",
   "title": "3 CODES FOR REROLLS", "code": "COOKING",
   "bullets": ["COOKING: REROLLS", "COOKING2: REROLLS", "DELAYSRY: REROLLS"],
   "vo": "Now, *codes*. Number *four*. *Ishin* has *cooking*, *cooking two*, and *delay sorry*, all for *free rerolls*. Open the *menu*, hit *codes*, and type them in *exactly*."},
  {"type": "item", "n": 5, "bg": "navy", "acc": "yellow", "game": "GOKUDO", "icon": "car", "badge": "CODES",
   "title": "90 FREE REROLLS", "code": "MIZUHASHI",
   "bullets": ["MIZUHASHI: 30 REROLLS", "RIDECRASH: 30 REROLLS", "CITYGARDEN: 30 REROLLS"],
   "vo": "Number *five*. *Gokudo* has *mizu hashi*, *ride crash*, and *city garden*, each for *thirty rerolls*. That's *ninety rerolls* total."},
  {"type": "item", "n": 6, "bg": "red", "acc": "pink", "game": "THE FORGE", "icon": "hammer", "badge": "CODES",
   "title": "FREE REROLLS", "code": "SORRYFORBUGS!!!",
   "bullets": ["SORRYFORBUGS!!!: REROLLS"],
   "vo": "And number *six*. *The Forge* code *sorry for bugs*, with *three* exclamation marks, gives *rerolls*."},
  {"type": "list", "bg": "green", "acc": "green", "head": "COMING UP",
   "rows": [("FREE CREATOR PLUS ENDS", "NOV 19"), ("INCUBATOR DEADLINE", "DEC 7"),
            ("GAME AWARDS ON ROBLOX", "DEC 10"), ("AUSTRALIA RATINGS", "JAN 26")],
   "vo": "Mark your *calendar*. Free creator *Plus* ends *November nineteenth*, the *Incubator* deadline is *December seventh*, *The Game Awards* hit Roblox on *December tenth*, and the new *Australia* ratings start *January twenty sixth*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WOULD YOU", "white"), ("WATCH IT?", "yellow")],
   "vo": "That's *today's* news. Would *you* watch *The Game Awards* on Roblox? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-16_1900_Short_GameAwards", "schedule_ist": "2026-11-16 19:00",
            "title": "The Game Awards Are Coming to Roblox! 🏆 #roblox #shorts",
            "description": "The Game Awards will stream live on Roblox for the first time on Thursday, December 10. The catch: only players 18 and older can watch in The Block, where fans can vote and claim virtual merch.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long": {"file": "SS_2026-11-16_2300_Long_NewsToday", "schedule_ist": "2026-11-16 23:00",
          "title": "Roblox News Today: The Game Awards on Roblox, New Age Ratings & 7 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: The Game Awards will stream live on Roblox for the first time on Thursday, December 10 (18+ viewers only, in The Block), Roblox is starting IARC age ratings in Australia on January 26, 2027, Experiments get new metrics for rewarded video ads and custom events, and 3 games have new codes.\n\nChapters:\n0:00 Intro\n0:12 The Game Awards on Roblox\n0:30 New Age Ratings in Australia\n0:46 New Experiment Metrics\n1:01 Ishin Codes\n1:11 Gokudo + The Forge Codes\n1:26 Coming Up\n1:41 Outro\n\nCodes in this video:\nIshin: COOKING (rerolls), COOKING2 (rerolls), DELAYSRY (rerolls)\nGokudo: MIZUHASHI (30 rerolls), RIDECRASH (30 rerolls), CITYGARDEN (30 rerolls)\nThe Forge: SORRYFORBUGS!!! (rerolls)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "the game awards roblox", "game awards 2026", "roblox age ratings", "roblox iarc", "roblox experiments", "ishin codes", "gokudo codes", "the forge codes", "secret spawn", "roblox news today"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-17_0100_Short_NewCodes", "schedule_ist": "2026-11-17 01:00",
            "title": "3 Roblox Codes That Just Dropped! 💎 #roblox #shorts",
            "description": "3 Roblox codes:\nGokudo: MIZUHASHI (30 rerolls)\nIshin: COOKING (rerolls)\nThe Forge: SORRYFORBUGS!!! (rerolls)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-17_0300_Short_LateNightCodes", "schedule_ist": "2026-11-17 03:00",
            "title": "3 More Roblox Codes You Probably Missed! 👀 #roblox #shorts",
            "description": "3 more Roblox codes:\nGokudo: RIDECRASH (30 rerolls), CITYGARDEN (30 rerolls)\nIshin: DELAYSRY (rerolls)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
}
