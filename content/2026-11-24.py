# Secret Spawn - 24 Nov 2026 content
# Sources (checked 23 Nov 2026; devforum / create.roblox.com / sportskeeda and all news/code sites were not fetchable here,
# so web search snippets were used):
#  Pass Free Trials (DevForum "Introducing Pass Free Trials", Weekly Recap Nov 16-20, 2026; creators opt in now in
#    Creator Hub > Monetization > Shop > Free Trials or per pass; live for players Dec 2, 2026; one game session,
#    one trial per pass per player; owners not eligible; new passes have trials off by default; don't grant permanent
#    items/currency/progress to trial users):
#    devforum.roblox.com/t/introducing-pass-free-trials/4995943 ; create.roblox.com/updates ;
#    create.roblox.com/docs/production/monetization/passes ; endgametools.com/en/roblox/news/roblox-game-pass-free-trials
#  Avatar Moments (DevForum Nov 20, 2026 "Create Avatar Moments to Showcase and Sell Your Items"; rolling out to eligible
#    users; avatar + owned emote + background + music from the Roblox library; posts to profile; shoppable looks;
#    gradually coming to the Moments tab; no voice recordings; eligibility not defined officially, 16+ per third parties
#    -> not stated in the video):
#    devforum.roblox.com/t/create-avatar-moments-to-showcase-and-sell-your-items/4997778 ;
#    en.help.roblox.com/hc/id/articles/55840112050196 ; happygamer.com (rollout article) ; endgametools.com/en/roblox/news/roblox-avatar-moments
#  Steal An Egg Update 14 "Turkey Takeover" (follow-up of Nov 21 set; live Sat Nov 21 15:00 UTC -> Fri Nov 27 18:00 UTC
#    = 1 PM ET; King Gobble turkey boss rampage every 30 min at :15 and :45, ~5 min; hit him for feathers; Turkey Shop:
#    Cornuclaw Egg 7,500 feathers, Mapleleaf Moose Egg 22,500 feathers; Golden King Gobble; Robux-only Royal Egg):
#    sportskeeda.com/roblox-news/steal-an-egg-update-14-patch-notes ; timesaver.gg/blog/steal-an-egg-turkey-takeover ;
#    techwiser.com/steal-an-egg-turkey-takeover-event-guide/ ; nerdschalk.com/steal-an-egg-turkey-event-shop ;
#    holdtoreset.com/steal-an-egg-turkey-rampage-update-14-guide/
#  List: Thanksgiving Thu Nov 26; Turkey Takeover ends Nov 27 1 PM ET; pass free trials live Dec 2;
#    TextChatService rule Dec 3 (create.roblox.com/updates)
#  Codes:
#    TRENCH DECAY THANKSGIVINGDANCE (2 Emote Crates), THANKSGIVINGRAFFLE (20 Vouchers); sign up for 2 events first:
#      progameguides.com/roblox/roblox-trench-ww1-codes/ (Nov 21) ; mrguider.org/roblox/trench-ww1-codes/ (Nov 20) ;
#      destructoid.com/trench-ww1-roblox-codes/ (Nov 22)
#    Pixel Z 25KLETSGO (1 Pack + 400 Coins): pockettactics.com/pixel-z-codes (Nov 22) ; pcgamesn.com/roblox/pixel-z-codes (Nov 22) ;
#      robloxden.com/game-codes/pixel-z ; officialcodezone.com (Nov 21)
#    Stand Out CRAZYDIAMOND (free Opal; RobloxDen: 1 Opal Roka + 20 Steel + 2,000 Dalas), 200KLIKESMASSIVE (arrows + more;
#      rewards differ by source); join the Studio Umbra: Europa group first; redeem in the in-game Phone > Gifts:
#      beebom.com/stand-out-codes/ ; robloxden.com/game-codes/stand-out ; standout-trello.com/codes
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("FREE TRIALS", "white"), ("FOR PASSES", "yellow")], "tag": "COMING DEC 2",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Roblox just announced *free trials* for game *passes*, and here are *three* things you need to know."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "GAME PASSES", "icon": "tag", "badge": "DEC 2",
    "title": "TRY BEFORE YOU BUY",
    "vo": "Number *one*. Starting *December second*, you can *try* some passes *before* you buy them."},
   {"type": "item", "n": 2, "bg": "green", "acc": "green", "game": "FREE TRIALS", "icon": "gamepad", "badge": "1 SESSION",
    "title": "ONE SESSION ONLY",
    "vo": "Number *two*. A trial lasts *one* game session, and you get *one* trial per *pass*."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "CREATORS", "icon": "hammer", "badge": "OPT IN",
    "title": "GAMES CHOOSE TO JOIN",
    "vo": "Number *three*. Each game's *creator* decides if their passes get a *trial*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH PASS", "white"), ("WOULD YOU TRY?", "yellow")],
    "vo": "So, which *pass* would *you* try *first*? Tell me in the *comments*."},
  ]},
 "short2": {
  "title_lines": [("3 ROBLOX CODES", "white"), ("WORTH GRABBING", "yellow")], "tag": "NEW CODES",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Here are *three* fresh Roblox codes worth grabbing *right now*."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "PIXEL Z", "icon": "card", "badge": "NEW",
    "title": "FREE PACK + 400 COINS", "code": "25KLETSGO",
    "vo": "First, *Pixel Z*. Code *twenty five K lets go* gives a free *pack* and *four hundred* coins."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "pink", "game": "STAND OUT", "icon": "gem", "badge": "NEW",
    "title": "FREE OPAL", "code": "CRAZYDIAMOND",
    "vo": "Next, *Stand Out*. Code *crazy diamond* gives a free *Opal*. Join the *group* first."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "TRENCH DECAY", "icon": "drumstick", "badge": "NEW",
    "title": "20 FREE VOUCHERS", "code": "THANKSGIVINGRAFFLE",
    "vo": "And *Trench Decay*. Code *thanksgiving raffle* gives *twenty* vouchers."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("WORKED?", "yellow")],
    "vo": "Codes can *expire* at any time, so be *quick*. Which one *worked* for you?"},
  ]},
 "short3": {
  "title_lines": [("GIANT TURKEY", "white"), ("BOSS IS HERE", "yellow")], "tag": "LIVE EVENT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "A giant *turkey* boss is taking over *Steal An Egg*, and here's how to *win*."},
   {"type": "item", "n": 1, "bg": "maroon", "acc": "orange", "game": "STEAL AN EGG", "icon": "drumstick", "badge": "EVERY 30 MIN",
    "title": "KING GOBBLE RAMPAGE",
    "vo": "Number *one*. *King Gobble* rampages every *thirty* minutes, at *fifteen* and *forty five* past the hour."},
   {"type": "item", "n": 2, "bg": "green", "acc": "yellow", "game": "STEAL AN EGG", "icon": "egg", "badge": "SHOP",
    "title": "FEATHERS BUY EGGS",
    "vo": "Number *two*. Hit him to earn *feathers*, then spend them on new *eggs* in the *Turkey Shop*."},
   {"type": "item", "n": 3, "bg": "navy", "acc": "blue", "game": "STEAL AN EGG", "icon": "flame", "badge": "NOV 27",
    "title": "ENDS FRIDAY 1 PM ET",
    "vo": "Number *three*. The event ends *Friday* at *one P M* Eastern, so *hurry*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("HOW MANY", "white"), ("FEATHERS?", "yellow")],
    "vo": "How many *feathers* do *you* have so far? Tell me *below*."},
  ]},
}

LONG = {
 "thumb": [("FREE PASS TRIALS", "white"), ("+ 5 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 24",
   "vo": "Here's today's *Roblox news*. Game passes are getting *free trials*, you can now share *Avatar Moments*, *Steal An Egg* has a giant *turkey* boss, and I've got *five new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "GAME PASSES", "icon": "tag", "badge": "DEC 2",
   "title": "PASS FREE TRIALS",
   "bullets": ["LIVE FOR PLAYERS DEC 2", "ONE GAME SESSION", "ONE TRIAL PER PASS", "CREATORS OPT IN NOW"],
   "vo": "Number *one*. Roblox announced *free trials* for game *passes*. Starting *December second*, you can try a pass for *one* game session before you *buy* it. You get *one* trial per pass, and if you already *own* it, you won't see one. Creators can *opt in* right now."},
  {"type": "item", "n": 2, "bg": "violet", "acc": "pink", "game": "AVATAR MOMENTS", "icon": "camera", "badge": "ROLLING OUT",
   "title": "SHARE YOUR LOOK",
   "bullets": ["AVATAR + EMOTE + MUSIC", "POST IT TO YOUR PROFILE", "OTHERS CAN SHOP THE LOOK"],
   "vo": "Number *two*. *Avatar Moments* are rolling out to *eligible* players. Pick your *avatar*, an *emote* you own, a *background* and some *music*, then post it to your *profile*. Other players can *shop* the items in your look. Roblox says they'll slowly come to the *Moments* tab too."},
  {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "STEAL AN EGG", "icon": "drumstick", "badge": "LIVE",
   "title": "TURKEY TAKEOVER",
   "bullets": ["KING GOBBLE EVERY 30 MIN", "FEATHERS FOR TURKEY SHOP EGGS", "ENDS NOV 27, 1 PM ET"],
   "vo": "Number *three*. *Steal An Egg's* *Turkey Takeover* is now *live*. A giant turkey called *King Gobble* rampages every *thirty* minutes. Hit him for *feathers* and spend them on new *eggs* in the *Turkey Shop*. It ends *Friday* at *one P M* Eastern."},
  {"type": "item", "n": 4, "bg": "green", "acc": "yellow", "game": "TRENCH DECAY", "icon": "drumstick", "badge": "CODES",
   "title": "CRATES + VOUCHERS", "code": "THANKSGIVINGDANCE",
   "bullets": ["THANKSGIVINGDANCE: 2 EMOTE CRATES", "THANKSGIVINGRAFFLE: 20 VOUCHERS"],
   "vo": "Now, *codes*. Number *four*. *Trench Decay* has *thanksgiving dance* for *two* emote crates, and *thanksgiving raffle* for *twenty* vouchers. Sign up for *two* events first."},
  {"type": "item", "n": 5, "bg": "navy", "acc": "blue", "game": "PIXEL Z", "icon": "card", "badge": "NEW",
   "title": "FREE PACK + 400 COINS", "code": "25KLETSGO",
   "bullets": ["25KLETSGO: 1 PACK + 400 COINS"],
   "vo": "Number *five*. *Pixel Z* has *twenty five K lets go*, for a free *pack* and *four hundred* coins."},
  {"type": "item", "n": 6, "bg": "red", "acc": "pink", "game": "STAND OUT", "icon": "arrow", "badge": "CODES",
   "title": "OPAL + ARROWS", "code": "CRAZYDIAMOND",
   "bullets": ["CRAZYDIAMOND: FREE OPAL", "200KLIKESMASSIVE: ARROWS + MORE"],
   "vo": "And number *six*. *Stand Out* has *crazy diamond* for a free *Opal*, and *two hundred K likes massive* for *arrows* and more. Join the game's *group* first."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("THANKSGIVING", "NOV 26"), ("STEAL AN EGG EVENT ENDS", "NOV 27"),
            ("PASS FREE TRIALS GO LIVE", "DEC 2"), ("TEXT CHAT RULE ENFORCED", "DEC 3")],
   "vo": "Coming up. *Thanksgiving* is *Thursday*, the *Steal An Egg* event ends *Friday*, pass *free trials* go live *December second*, and the *chat rule* starts *December third*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH PASS", "white"), ("WOULD YOU TRY?", "yellow")],
   "vo": "That's *today's* news. Which game *pass* would you try for *free*? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-24_1900_Short_PassFreeTrials", "schedule_ist": "2026-11-24 19:00",
            "title": "Roblox Game Passes Are Getting FREE Trials! 🎟️ #roblox #shorts",
            "description": "Roblox announced free trials for game passes. Starting December 2, players can try an opted-in pass for one game session before buying it, with one trial per pass. Creators choose which passes get a trial and can opt in now.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long": {"file": "SS_2026-11-24_2300_Long_NewsToday", "schedule_ist": "2026-11-24 23:00",
          "title": "Roblox News Today: Free Pass Trials, Avatar Moments & 5 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: game passes are getting free trials (live for players Dec 2; one game session and one trial per pass, and creators can opt in now), Avatar Moments let you post a shoppable avatar look with an emote, background and music to your profile, and Steal An Egg's Turkey Takeover is live with the King Gobble rampage every 30 minutes (event ends Nov 27, 1 PM ET). Plus 3 games have 5 new codes.\n\nChapters:\n0:00 Intro\n0:13 Pass Free Trials\n0:28 Avatar Moments\n0:45 Steal An Egg Turkey Takeover\n0:59 TRENCH DECAY Codes\n1:10 Pixel Z + Stand Out Codes\n1:26 Coming Up + Outro\n\nCodes in this video:\nTRENCH DECAY: THANKSGIVINGDANCE (2 Emote Crates), THANKSGIVINGRAFFLE (20 Vouchers); sign up for 2 events first\nPixel Z: 25KLETSGO (1 Pack + 400 Coins)\nStand Out: CRAZYDIAMOND (free Opal), 200KLIKESMASSIVE (arrows + more); join the Studio Umbra: Europa group first\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "roblox free trials", "roblox game passes", "avatar moments", "steal an egg", "steal an egg turkey takeover", "trench decay codes", "pixel z codes", "stand out codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-25_0100_Short_CodesWorthGrabbing", "schedule_ist": "2026-11-25 01:00",
            "title": "3 Roblox Codes Worth Grabbing Right Now! 🎁 #roblox #shorts",
            "description": "3 Roblox codes:\nPixel Z: 25KLETSGO (1 Pack + 400 Coins)\nStand Out: CRAZYDIAMOND (free Opal; join the Studio Umbra: Europa group first)\nTRENCH DECAY: THANKSGIVINGRAFFLE (20 Vouchers; sign up for 2 events first)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-25_0300_Short_TurkeyBoss", "schedule_ist": "2026-11-25 03:00",
            "title": "Steal An Egg's Giant Turkey Boss Is Here! 🦃 #roblox #shorts",
            "description": "Steal An Egg's Turkey Takeover (Update 14) is live. King Gobble rampages every 30 minutes (at :15 and :45), and hitting him earns feathers for new eggs in the Turkey Shop. The event ends Friday, Nov 27 at 1 PM ET. Times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
}
