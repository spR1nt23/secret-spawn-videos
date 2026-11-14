# Secret Spawn - 15 Nov 2026 content
# Sources (checked 14 Nov 2026):
#  Next era of creation (Nov 13): about.roblox.com/newsroom/2026/11/building-the-next-era-of-creation-on-roblox
#    (80%+ of top-100 games' creators use AI tools; Assistant + Build to merge = longer-term goal; Roblox Everywhere)
#  Build US rollout Dec / 70,000+ games: Q3 2026 shareholder letter s27.q4cdn.com/984876518/files/content_files/Q3-2026-Earnings-Shareholder-Letter.pdf,
#    fool.com/earnings/call-transcripts/2026/10/30/roblox-rblx-q3-2026-earnings-call-transcript/
#  MM2 Halloween ends Nov 16 18:00 UTC (1 PM ET): gamingroute.com/mm2-halloween-2026/, dropmarket.gg/murder-mystery-2/events/halloween-2026,
#    progameguides.com/roblox/complete-murder-mystery-2-halloween-event-guide/ (candies, 30-tier pass, Emberbow, Emberscythe craft)
#  Codes: Kontra MILLIONVISITS: gamertweak.com/kontra-codes (checked Nov 14), progameguides.com/roblox/roblox-kontra-codes, robloxden.com
#         The Forge AIDASAYSSORRY: destructoid.com/the-forge-codes (Nov 10), progameguides.com/roblox/the-forge-codes
#         Anime Apocalypse THEESPER / TRUEWARRIORHOTFIX: igeeksblog.com/anime-apocalypse-codes, progameguides.com/roblox/anime-apocalypse-codes (Nov 9),
#           nerdschalk.com/anime-apocalypse-codes-3
#         Survive Your Ideas BIG5: dexerto.com/roblox/survive-your-ideas-codes-3425583 (Nov 11), axeetech.com/survive-your-ideas-codes
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("ROBLOX BUILD", "white"), ("COMES TO THE US", "yellow")], "tag": "DECEMBER",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Roblox wants *way more* players making games on their *phone*. *Three* things to know."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "ROBLOX BUILD", "icon": "phone", "badge": "DECEMBER",
    "title": "BIGGER US RELEASE",
    "vo": "Number *one*. *Build* gets a *bigger US release* in *December*, then goes *global* in *twenty twenty seven*."},
   {"type": "item", "n": 2, "bg": "green", "acc": "green", "game": "ROBLOX BUILD", "icon": "gamepad", "badge": "70,000+",
    "title": "70,000 GAMES ALREADY",
    "vo": "Number *two*. Testers have already published over *seventy thousand* games with it."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "ROBLOX STUDIO", "icon": "bolt", "badge": "LATER",
    "title": "PHONE TO PC ONE DAY",
    "vo": "Number *three*. Someday, Roblox *wants* Build and *Assistant* in *one tool*, from *phone* to *PC*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT WOULD", "white"), ("YOU BUILD?", "yellow")],
    "vo": "What *game* would *you* build first? Tell me *below*."},
  ]},
 "short2": {
  "title_lines": [("3 FREE ROBLOX", "white"), ("CODES", "yellow")], "tag": "SUNDAY DROP",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Three* Roblox codes for your *Sunday*. Redeem them *fast*."},
   {"type": "item", "n": 1, "bg": "navy", "acc": "yellow", "game": "KONTRA", "icon": "shield", "badge": "LIMITED",
    "title": "500 FREE KREDITS", "code": "MILLIONVISITS",
    "vo": "*Kontra*. Code *million visits* gives *five hundred kredits*, but it has *limited uses*."},
   {"type": "item", "n": 2, "bg": "violet", "acc": "purple", "game": "ANIME APOCALYPSE", "icon": "swords", "badge": "NEW",
    "title": "300K COINS + SPINS", "code": "THEESPER",
    "vo": "*Anime Apocalypse*. Code *the esper* gives *three hundred thousand coins*, *raid tickets* and *lucky spins*."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "THE FORGE", "icon": "hammer", "badge": "NEW",
    "title": "5 FREE REROLLS", "code": "AIDASAYSSORRY",
    "vo": "*The Forge*. Code *aida says sorry* gives *five rerolls*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("FIRST?", "yellow")],
    "vo": "Codes *expire fast*, so redeem them *now*. Which one are *you* using *first*?"},
  ]},
 "short3": {
  "title_lines": [("MM2 HALLOWEEN", "white"), ("ENDS TOMORROW", "yellow")], "tag": "LAST CHANCE",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Murder Mystery Two* Halloween is almost *over*. Here's what to do *before* it ends."},
   {"type": "item", "n": 1, "bg": "red", "acc": "pink", "game": "MURDER MYSTERY 2", "icon": "moon", "badge": "MON 1PM ET",
    "title": "ENDS MONDAY 1 PM ET",
    "vo": "Number *one*. The event ends *Monday*, *November sixteenth*, at *one P M Eastern*."},
   {"type": "item", "n": 2, "bg": "navy", "acc": "orange", "game": "MURDER MYSTERY 2", "icon": "flame", "badge": "CANDY",
    "title": "SPEND YOUR CANDY",
    "vo": "Number *two*. Spend your *candy* on the *battle pass* or the *Halloween box*. It won't help you *after* the event."},
   {"type": "item", "n": 3, "bg": "violet", "acc": "purple", "game": "MURDER MYSTERY 2", "icon": "swords", "badge": "CRAFT",
    "title": "EMBERSCYTHE CRAFT",
    "vo": "Number *three*. The *Emberscythe* is *crafted* in the *cauldron* from the *Embersickle* and the *Emberbow*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("DID YOU", "white"), ("FINISH THE PASS?", "yellow")],
    "vo": "Did *you* finish the *battle pass*? Tell me *below*."},
  ]},
}

LONG = {
 "thumb": [("ROBLOX BUILD", "white"), ("+ 5 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 15",
   "vo": "Here's today's *Roblox news*. Roblox shared its *AI plans*, *Build* is coming to more *US* players, *MM2 Halloween* ends *tomorrow*, and I've got *five new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "ROBLOX", "icon": "bolt", "badge": "NOV 13",
   "title": "THE NEXT ERA OF CREATION",
   "bullets": ["80%+ OF TOP 100 GAMES USE AI TOOLS", "ASSISTANT + BUILD: ONE TOOL LATER", "ROBLOX EVERYWHERE: STANDALONE APPS"],
   "vo": "Number *one*. On *Friday*, Roblox said creators of over *eighty percent* of the *top one hundred* games now use *AI tools*. It wants *Assistant* and *Build* in *one tool* someday, but that's a *future goal*. And *Roblox Everywhere* will let creators ship games as their *own apps* on *mobile*, *PC* and *console*, with Roblox running the tech *underneath*."},
  {"type": "item", "n": 2, "bg": "green", "acc": "green", "game": "ROBLOX BUILD", "icon": "phone", "badge": "DECEMBER",
   "title": "BUILD COMES TO MORE OF THE US",
   "bullets": ["BIGGER US RELEASE IN DECEMBER", "GLOBAL LAUNCH IN 2027", "70,000+ GAMES MADE IN TESTING"],
   "vo": "Number *two*. *Build*, the tool for making games on your *phone*, gets a *bigger US release* in *December*, with a *global* launch in *twenty twenty seven*. Testers in places like *New Zealand* and *Thailand* have already published over *seventy thousand* games with it."},
  {"type": "item", "n": 3, "bg": "red", "acc": "pink", "game": "MURDER MYSTERY 2", "icon": "flame", "badge": "MON 1PM ET",
   "title": "HALLOWEEN ENDS TOMORROW",
   "bullets": ["ENDS MON NOV 16, 1 PM ET", "SPEND YOUR CANDY NOW", "EMBERSCYTHE = CAULDRON CRAFT"],
   "vo": "Number *three*. *MM2 Halloween* ends *Monday* at *one P M Eastern*. Spend your *candy* on the *battle pass* or the *Halloween box* before then. The *Emberscythe* isn't a box drop. You *craft* it in the *cauldron* from the *Embersickle* and the *Emberbow*."},
  {"type": "item", "n": 4, "bg": "navy", "acc": "yellow", "game": "KONTRA", "icon": "shield", "badge": "CODES",
   "title": "500 FREE KREDITS", "code": "MILLIONVISITS",
   "bullets": ["MILLIONVISITS: 500 KREDITS", "LIMITED USES"],
   "vo": "Now, *codes*. Number *four*. *Kontra* code *million visits* gives *five hundred kredits*, but it has *limited uses*. Kontra codes are *case sensitive*, so copy them *exactly*."},
  {"type": "item", "n": 5, "bg": "violet", "acc": "purple", "game": "ANIME APOCALYPSE", "icon": "swords", "badge": "CODES",
   "title": "COINS + LUCKY SPINS", "code": "THEESPER",
   "bullets": ["THEESPER: 300K COINS + SPINS", "TRUEWARRIORHOTFIX: COINS + SPINS"],
   "vo": "Number *five*. *Anime Apocalypse* has *the esper* and *true warrior hotfix*, both for *coins* and *lucky spins*."},
  {"type": "item", "n": 6, "bg": "maroon", "acc": "orange", "game": "THE FORGE", "icon": "hammer", "badge": "CODES",
   "title": "5 FREE REROLLS", "code": "AIDASAYSSORRY",
   "bullets": ["AIDASAYSSORRY: 5 REROLLS"],
   "vo": "Number *six*. *The Forge* code *aida says sorry* gives *five rerolls*."},
  {"type": "item", "n": 7, "bg": "green", "acc": "green", "game": "SURVIVE YOUR IDEAS", "icon": "mystery", "badge": "CODES",
   "title": "5 LUCKY SPINS", "code": "BIG5",
   "bullets": ["BIG5: 5 LUCKY SPINS"],
   "vo": "And number *seven*. *Survive Your Ideas* code *big five* gives *five lucky spins*."},
  {"type": "list", "bg": "red", "acc": "pink", "head": "COMING UP",
   "rows": [("MM2 HALLOWEEN ENDS", "NOV 16"), ("FREE CREATOR PLUS ENDS", "NOV 19"),
            ("INCUBATOR DEADLINE", "DEC 7"), ("BUILD: BIGGER US RELEASE", "DEC")],
   "vo": "Mark your *calendar*. *MM2 Halloween* ends *tomorrow*, free creator *Plus* ends *November nineteenth*, the *Incubator* deadline is *December seventh*, and *Build* expands in *December*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT WOULD", "white"), ("YOU BUILD?", "yellow")],
   "vo": "That's *today's* news. What would *you* build with *Roblox Build*? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-15_1900_Short_RobloxBuild", "schedule_ist": "2026-11-15 19:00",
            "title": "Roblox Build Is Coming to More of the US! 📱 #roblox #shorts",
            "description": "Roblox Build, the tool for making games on your phone, gets a bigger US release in December, with a global launch planned for 2027. Testers have already published over 70,000 games with it, and Roblox says it wants Build and Assistant in one tool in the future.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxstudio #shorts"},
 "long": {"file": "SS_2026-11-15_2300_Long_NewsToday", "schedule_ist": "2026-11-15 23:00",
          "title": "Roblox News Today: Roblox AI Plans, Build Coming to the US & 5 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: Roblox says creators of over 80% of the top 100 games now use AI tools and wants to merge Assistant and Build into one tool in the future, Build gets a bigger US release in December (global launch in 2027), MM2 Halloween ends Monday, November 16 at 1 PM ET, and 4 games have new codes.\n\nChapters:\n0:00 Intro\n0:12 Roblox's AI Plans\n0:35 Roblox Build Comes to the US\n0:51 MM2 Halloween Ends Tomorrow\n1:06 Kontra Code\n1:18 Anime Apocalypse, The Forge + Survive Your Ideas Codes\n1:35 Coming Up\n1:47 Outro\n\nCodes in this video:\nKontra: MILLIONVISITS (500 Kredits, limited uses)\nAnime Apocalypse: THEESPER (300,000 coins, raid tickets + lucky spins), TRUEWARRIORHOTFIX (coins + lucky spins)\nThe Forge: AIDASAYSSORRY (5 rerolls)\nSurvive Your Ideas: BIG5 (5 lucky spins)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "roblox build", "roblox ai", "roblox everywhere", "mm2 halloween", "murder mystery 2", "kontra codes", "anime apocalypse codes", "the forge codes", "survive your ideas codes", "secret spawn", "roblox news today"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-16_0100_Short_SundayCodes", "schedule_ist": "2026-11-16 01:00",
            "title": "3 FREE Roblox Codes for Your Sunday! 🎁 #roblox #shorts",
            "description": "3 Roblox codes:\nKontra: MILLIONVISITS (500 Kredits, limited uses)\nAnime Apocalypse: THEESPER (300,000 coins, raid tickets + lucky spins)\nThe Forge: AIDASAYSSORRY (5 rerolls)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-16_0300_Short_MM2HalloweenEnds", "schedule_ist": "2026-11-16 03:00",
            "title": "MM2 Halloween Ends Tomorrow! Last Chance 🎃 #roblox #shorts",
            "description": "The Murder Mystery 2 Halloween event ends Monday, November 16 at 1 PM ET. Spend your candy on the battle pass or the Halloween box before it ends. The Emberscythe is crafted in the cauldron from the Embersickle and the Emberbow.\n\nEvent times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #mm2 #shorts"},
}
