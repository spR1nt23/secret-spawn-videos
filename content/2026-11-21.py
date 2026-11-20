# Secret Spawn - 21 Nov 2026 content
# Sources (checked 20 Nov 2026; devforum / create.roblox.com / about.roblox.com / news & code sites were not
# fetchable here, so web search snippets were used):
#  Classmates on Roblox (announced Wed Nov 18, 2026; U.S. college students 18-24, verify with school email + 6-digit code,
#    mobile & desktop apps; earlier pilot in Nevada/Alabama; Roblox clubs at 100+ colleges in 30 states):
#    about.roblox.com/newsroom/2026/11/introducing-classmates-a-new-way-for-us-college-students-to-connect-on-roblox ;
#    en.help.roblox.com/hc/en-us/articles/52432178088084-Classmates-on-Roblox ;
#    happygamer.com/roblox-classmates-verified-us-college-students-175813/ ;
#    gamesbeat.com/roblox-clubs-have-been-popping-up-on-college-campuses-across-the-nation-why-now/
#  TextChatService requirement enforced from Dec 3 (Creator Updates entry Nov 20: games sending player text outside
#    TextChatService without a rate limit get limited to 1 message per player every 60 s):
#    create.roblox.com/updates ; create.roblox.com/docs/chat/guidelines ;
#    devforum.roblox.com/t/important-textchatservice-updates-how-to-test-and-what's-next/4948433
#  Steal An Egg Update 14 "Turkey Takeover" (Thanksgiving; scheduled Sat Nov 21, 15:00 UTC = 10:00 AM ET):
#    timesaver.gg (Steal An Egg guides, countdown) ; eggping.com/live (countdown "Update 14: TURKEY TAKEOVER! Nov 21, 2026")
#    -> fan trackers only, said as "set to start"
#  Codes:
#    99 Nights in the Forest forestwakesup26 (15 Diamonds + flames; flame set differs by source), afterparty (15 Diamonds):
#      pockettactics.com/99-nights-in-the-forest-codes , destructoid.com/99-nights-in-the-forest-codes/ ,
#      rocodes.gg/codes/99-nights-in-the-forest (3 active as of Nov 16)
#    Vantage NEWUPDATE (7,000 Credits): progameguides.com/roblox/valoblox-codes/ (Nov 19), destructoid.com/valoblox-codes/ (Nov 19)
#    Arcane 101 TYSM1500LIKES (20 Race Rerolls; finish tutorial + join Lucky's Pals group):
#      destructoid.com/arcane-101-codes/ (Nov 16), mrguider.org/roblox/arcane-101-codes/ (added Nov 14),
#      progameguides.com/roblox/arcane-101-codes/ (Nov 19)
#    SLAYER FIFTYK (50,000 Yen): progameguides.com/roblox/slayer-codes/ (Nov 19), robloxden.com/game-codes/slayer ,
#      supercheats.com/slayer-codes
#    Blind but Dangerous REWORKTIME (400 Tix): progameguides.com/roblox/blind-but-dangerous-codes/ (Nov 19),
#      destructoid.com/blind-but-dangerous-codes/ (Nov 19)
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("3 ROBLOX CHANGES", "white"), ("THIS WEEK", "yellow")], "tag": "NEW",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Three* Roblox changes this week, and one is *only* for *college* players."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "CLASSMATES", "icon": "card", "badge": "U.S. ONLY",
    "title": "FIND YOUR CLASSMATES",
    "vo": "Number *one*. *Classmates* lets verified *college students* find players from their *own school*."},
   {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "TEXT CHAT", "icon": "phone", "badge": "DEC 3",
    "title": "CHAT RULE ENFORCED",
    "vo": "Number *two*. From *December third*, games with custom chat get *one message* per *minute*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "STEAL AN EGG", "icon": "egg", "badge": "NOV 21",
    "title": "TURKEY TAKEOVER",
    "vo": "Number *three*. *Steal An Egg's* Thanksgiving update is set for *Saturday*, *ten A M Eastern*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("MATTERS MOST?", "yellow")],
    "vo": "Which change matters *most* to *you*? Tell me *below*."},
  ]},
 "short2": {
  "title_lines": [("3 ROBLOX CODES", "white"), ("YOU MISSED", "yellow")], "tag": "NEW CODES",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "You probably *missed* these *three* Roblox codes, so type them *exactly* as you see them."},
   {"type": "item", "n": 1, "bg": "navy", "acc": "blue", "game": "VANTAGE", "icon": "bolt", "badge": "NEW",
    "title": "7,000 CREDITS", "code": "NEWUPDATE",
    "vo": "First, *Vantage*. Code *new update* gives *seven thousand credits*."},
   {"type": "item", "n": 2, "bg": "red", "acc": "pink", "game": "SLAYER", "icon": "swords", "badge": "TESTING",
    "title": "50,000 YEN", "code": "FIFTYK",
    "vo": "Next, *Slayer*. Code *fifty K* gives *fifty thousand yen*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "yellow", "game": "99 NIGHTS IN THE FOREST", "icon": "flame", "badge": "ACTIVE",
    "title": "15 DIAMONDS", "code": "afterparty",
    "vo": "And *Ninety Nine Nights*. Code *after party* gives *fifteen diamonds*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("FIRST?", "yellow")],
    "vo": "Codes can *expire*, so be *quick*. Which one is *first*?"},
  ]},
 "short3": {
  "title_lines": [("3 FREE ROBLOX", "white"), ("CODES TONIGHT", "yellow")], "tag": "LATE NIGHT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Still *awake*? Here are *three* free Roblox codes for *tonight*."},
   {"type": "item", "n": 1, "bg": "violet", "acc": "purple", "game": "ARCANE 101", "icon": "mystery", "badge": "NEW",
    "title": "20 RACE REROLLS", "code": "TYSM1500LIKES",
    "vo": "First, *Arcane one oh one*. Code *T Y S M fifteen hundred likes* gives *twenty race rerolls*."},
   {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "BLIND BUT DANGEROUS", "icon": "binoculars", "badge": "NEW",
    "title": "400 FREE TIX", "code": "REWORKTIME",
    "vo": "Next, *Blind but Dangerous*. Code *rework time* gives *four hundred Tix*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "99 NIGHTS IN THE FOREST", "icon": "flame", "badge": "ACTIVE",
    "title": "DIAMONDS + FLAMES", "code": "forestwakesup26",
    "vo": "And *Ninety Nine Nights*. Code *forest wakes up twenty six* gives *diamonds* and *flames*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT DID", "white"), ("YOU GET?", "yellow")],
    "vo": "Redeem them *fast*, they can *expire*. What did *you* get?"},
  ]},
}

LONG = {
 "thumb": [("ROBLOX CLASSMATES", "white"), ("+ 4 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 21",
   "vo": "Here's today's *Roblox news*. Roblox launched *Classmates* for *college students*, a *chat rule* gets enforced next month, *Steal An Egg* has a *Thanksgiving* update, and I've got *four new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "CLASSMATES", "icon": "card", "badge": "NEW",
   "title": "CLASSMATES ON ROBLOX",
   "bullets": ["U.S. COLLEGE STUDENTS, 18-24", "VERIFY WITH SCHOOL EMAIL", "MOBILE AND DESKTOP APPS"],
   "vo": "Number *one*. Roblox announced *Classmates* on *Wednesday*. It's for *U S college students* aged *eighteen* to *twenty four*. You verify with your *school email*, then find and play with people from your *own school*. Roblox says fan clubs already exist at over *one hundred colleges*."},
  {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "TEXT CHAT", "icon": "phone", "badge": "DEC 3",
   "title": "CHAT RULE ENFORCED",
   "bullets": ["STARTS DECEMBER 3", "CUSTOM CHAT OUTSIDE TEXTCHATSERVICE", "LIMIT: 1 MESSAGE PER MINUTE"],
   "vo": "Number *two*, for *creators*. Starting *December third*, Roblox will *enforce* its *text chat* rule. If a game lets players send text *outside* the normal chat system with *no limit*, it gets slowed to *one message* per player every *sixty seconds*. So builders, check your *custom chat* now."},
  {"type": "item", "n": 3, "bg": "green", "acc": "yellow", "game": "STEAL AN EGG", "icon": "egg", "badge": "SATURDAY",
   "title": "TURKEY TAKEOVER",
   "bullets": ["UPDATE 14, THANKSGIVING", "SAT NOV 21, 10 AM ET", "TIME FROM FAN TRACKERS"],
   "vo": "Number *three*. *Steal An Egg's* update *fourteen*, called *Turkey Takeover*, is set for *Saturday*. Fan trackers have it at *ten A M Eastern*. It's a *Thanksgiving* themed update, so expect a *turkey* twist."},
  {"type": "item", "n": 4, "bg": "navy", "acc": "green", "game": "99 NIGHTS IN THE FOREST", "icon": "flame", "badge": "CODES",
   "title": "FREE DIAMONDS", "code": "forestwakesup26",
   "bullets": ["forestwakesup26: 15 DIAMONDS + FLAMES", "afterparty: 15 DIAMONDS"],
   "vo": "Now, *codes*. Number *four*. *Ninety Nine Nights* has *forest wakes up twenty six* and *after party*, each for *fifteen diamonds*."},
  {"type": "item", "n": 5, "bg": "red", "acc": "pink", "game": "VANTAGE", "icon": "bolt", "badge": "CODE",
   "title": "7,000 CREDITS", "code": "NEWUPDATE",
   "bullets": ["NEWUPDATE: 7,000 CREDITS"],
   "vo": "Number *five*. *Vantage* has *new update* for *seven thousand credits*."},
  {"type": "item", "n": 6, "bg": "violet", "acc": "purple", "game": "ARCANE 101", "icon": "mystery", "badge": "CODE",
   "title": "20 RACE REROLLS", "code": "TYSM1500LIKES",
   "bullets": ["TYSM1500LIKES: 20 RACE REROLLS", "FINISH TUTORIAL + JOIN GROUP"],
   "vo": "And number *six*. *Arcane one oh one* has *T Y S M fifteen hundred likes* for *twenty race rerolls*. Finish the *tutorial* first."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("STEAL AN EGG TURKEY TAKEOVER", "NOV 21"), ("THE TAKEBACK ENDS", "NOV 23"),
            ("TEXT CHAT RULE ENFORCED", "DEC 3"), ("GAME AWARDS ON ROBLOX", "DEC 10")],
   "vo": "Coming up. *Turkey Takeover* lands *Saturday*, *The Takeback* ends *Monday*, the *chat rule* kicks in *December third*, and *The Game Awards* hit Roblox on *December tenth*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WOULD YOU USE", "white"), ("CLASSMATES?", "yellow")],
   "vo": "That's *today's* news. Would *you* use Classmates one day? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-21_1900_Short_ClassmatesChatRule", "schedule_ist": "2026-11-21 19:00",
            "title": "3 Roblox Changes This Week You Should Know! 🎓 #roblox #shorts",
            "description": "Roblox launched Classmates, a way for verified U.S. college students to find players from their own school. From December 3, games with custom chat outside TextChatService get limited to one message per minute. And Steal An Egg's Thanksgiving update, Turkey Takeover, is set for Saturday, Nov 21 at 10 AM ET (times are in Eastern Time and can change).\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxstudio #shorts"},
 "long": {"file": "SS_2026-11-21_2300_Long_NewsToday", "schedule_ist": "2026-11-21 23:00",
          "title": "Roblox News Today: Classmates for College, New Chat Rule & 4 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: Roblox launched Classmates, a way for verified U.S. college students (18-24) to find players from their own school, Roblox will enforce its TextChatService rule from December 3 (custom chat outside TextChatService with no rate limit gets limited to one message per player per minute), Steal An Egg's Thanksgiving Update 14, Turkey Takeover, is set for Saturday, Nov 21 at 10 AM ET (per fan trackers), and 3 games have new codes.\n\nChapters:\n0:00 Intro\n0:13 Classmates on Roblox\n0:30 Text Chat Rule (Dec 3)\n0:48 Steal An Egg Turkey Takeover\n1:01 Codes: 99 Nights, Vantage, Arcane 101\n1:23 Coming Up\n1:34 Outro\n\nCodes in this video:\n99 Nights in the Forest: forestwakesup26 (15 Diamonds + flames), afterparty (15 Diamonds)\nVantage: NEWUPDATE (7,000 Credits)\nArcane 101: TYSM1500LIKES (20 Race Rerolls; finish the tutorial and join the group first)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "roblox classmates", "roblox college", "textchatservice", "roblox chat rule", "steal an egg", "steal an egg thanksgiving", "99 nights in the forest codes", "vantage codes", "arcane 101 codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-22_0100_Short_CodesYouMissed", "schedule_ist": "2026-11-22 01:00",
            "title": "3 Roblox Codes You Probably Missed 👀 #roblox #shorts",
            "description": "3 Roblox codes:\nVantage: NEWUPDATE (7,000 Credits)\nSLAYER: FIFTYK (50,000 Yen)\n99 Nights in the Forest: afterparty (15 Diamonds, type it in lowercase)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-22_0300_Short_LateNightCodes", "schedule_ist": "2026-11-22 03:00",
            "title": "3 Late Night Roblox Codes Still Working 🌙 #roblox #shorts",
            "description": "3 more Roblox codes:\nArcane 101: TYSM1500LIKES (20 Race Rerolls; finish the tutorial and join the group first)\nBlind but Dangerous: REWORKTIME (400 Tix)\n99 Nights in the Forest: forestwakesup26 (15 Diamonds + flames, type it in lowercase)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
}
