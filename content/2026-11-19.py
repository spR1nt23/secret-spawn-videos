# Secret Spawn - 19 Nov 2026 content
# Sources (checked 18 Nov 2026; about.roblox.com / create.roblox.com / sportskeeda / pcgamesn / progameguides were not
# fetchable here, so search snippets were used):
#  Adventure Time RPG spotlight: Roblox newsroom roundup "New Standout Games to Check Out on Roblox This Month" (Nov 16)
#    highlights Adventure Time RPG [Beta] by Oh My Glob Games (Cartoon Network Games); official listing: "Battle your way
#    through the Dungeon Train", buddies (companions), weapon upgrades, free to play, beta:
#    player.one/roblox-spotlights-its-official-adventure-time-rpg-dungeon-train-battles-playable-characters-164517 (Nov 17) ;
#    roblox.com/games/118915268278945/Adventure-Time-RPG ; adventuretime.fandom.com/wiki/Adventure_Time_RPG
#  Roblox Wallet replaces DevEx next year (Baszucki x Bloxy News interview, newsroom Nov 9):
#    about.roblox.com/newsroom/2026/11/david-baszucki-sits-down-with-bloxy-news ; Wallet rolls out late 2026 for individual
#    US creators 18+, global 2027; Roblox Card (spend balance directly) begins rollout 2027:
#    about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play ; invenglobal.com/articles/25918 ;
#    devforum.roblox.com/t/rdc26-what-we-announced/4865880 (daily payouts each business day)
#  Stand Out (new stand battler, public alpha, live Nov 14 per ggrecon; codes drop at like milestones):
#    ggrecon.com/articles/fastest-growing-new-roblox-games-november-2026/ ; allthings.how stand-out beginners guide ;
#    destructoid.com/stand-out-codes/ (Nov 17) ; gamerant.com/roblox-codes-stand-out-codes-discord-server-links/ ;
#    techwiser.com/roblox-stand-out-codes/ ; pcgamesn.com/roblox/stand-out-codes (100KLIKESHUGE new, Nov 17)
#  Codes:
#    Stand Out 100KLIKESHUGE (Mysterious Arrows + Lucky Arrow + Arrow Parts + Dalas; Dalas amount differs by source)
#    Stand Dice BIZARRE (2 Jackpot Rolls, 2 Roll Luck V Potions, 1 Void Jackpot Roll I), OVERHEAVEN (1 Jackpot Roll,
#      3 Roll Luck IV Potions, 5 Trait Rerolls, 5 Grade Gems): twinfinite.net/codes/stand-dice-codes/ (Nov 17),
#      mrguider.org/roblox/stand-dice-codes/ (added Nov 16), destructoid.com/stand-dice-codes/ (Nov 17)
#    Submerged 1000PLAYERS (5,000 Credits), UPDATE1 (1,500 Credits), HERTZ (500 Credits):
#      destructoid.com/submerged-codes/ (Nov 17), twinfinite.net/codes/submerged-codes/, mrguider.org/roblox/submerged-codes/
#    Roblox is Unbreakable 6MILLZOMBIES (24h EXP booster, 4 Pure Arrows, 8 Mastery DISCs):
#      pcgamesn.com/roblox-is-unbreakable/codes (Nov 17), pockettactics.com/roblox-is-unbreakable-codes (Nov 17),
#      destructoid.com/roblox-is-unbreakable-codes/
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("ADVENTURE TIME", "white"), ("RPG", "yellow")], "tag": "SPOTLIGHT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Roblox just put the official *Adventure Time RPG* in the *spotlight*. Here are *three* things to know."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "ADVENTURE TIME RPG", "icon": "trophy", "badge": "NOV 16",
    "title": "ROBLOX SPOTLIGHT",
    "vo": "Number *one*. Roblox picked it as a *standout new game* this month, and it's *free* to play."},
   {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "ADVENTURE TIME RPG", "icon": "train", "badge": "BOSS FIGHTS",
    "title": "DUNGEON TRAIN",
    "vo": "Number *two*. You battle through the *Dungeon Train* and take on *bosses*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "ADVENTURE TIME RPG", "icon": "swords", "badge": "BETA",
    "title": "BUDDIES AND WEAPONS",
    "vo": "Number *three*. Level up your *weapons* and bring *buddies*. It's still in *beta*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WILL YOU", "white"), ("PLAY IT?", "yellow")],
    "vo": "Are *you* trying it? Tell me *below*."},
  ]},
 "short2": {
  "title_lines": [("3 FREE ROBLOX", "white"), ("CODES", "yellow")], "tag": "NEW TODAY",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Three* free Roblox codes for *rolls*, *credits* and *arrows*. Type them *exactly*."},
   {"type": "item", "n": 1, "bg": "red", "acc": "pink", "game": "STAND DICE", "icon": "dice", "badge": "NEW",
    "title": "FREE JACKPOT ROLLS", "code": "BIZARRE",
    "vo": "First, *Stand Dice*. Code *bizarre* gives *jackpot rolls* and *luck potions*."},
   {"type": "item", "n": 2, "bg": "blue", "acc": "blue", "game": "SUBMERGED", "icon": "fish", "badge": "NEW",
    "title": "5,000 CREDITS", "code": "1000PLAYERS",
    "vo": "Next, *Submerged*. Code *one thousand players* gives *five thousand credits*."},
   {"type": "item", "n": 3, "bg": "green", "acc": "green", "game": "ROBLOX IS UNBREAKABLE", "icon": "shield", "badge": "NEW",
    "title": "PURE ARROWS", "code": "6MILLZOMBIES",
    "vo": "And *Roblox is Unbreakable*. Code *six mill zombies* gives *pure arrows* and an *EXP boost*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("FIRST?", "yellow")],
    "vo": "Codes *expire fast*, so redeem them *now*. Which one is *first*?"},
  ]},
 "short3": {
  "title_lines": [("3 HIDDEN ROBLOX", "white"), ("CODES", "yellow")], "tag": "LATE NIGHT",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "Up *late*? Here are *three* Roblox codes most players *missed*."},
   {"type": "item", "n": 1, "bg": "violet", "acc": "purple", "game": "STAND OUT", "icon": "arrow", "badge": "NEW",
    "title": "FREE ARROWS", "code": "100KLIKESHUGE",
    "vo": "First, *Stand Out*. Code *one hundred K likes huge* gives *arrows* and *Dalas*."},
   {"type": "item", "n": 2, "bg": "maroon", "acc": "orange", "game": "STAND DICE", "icon": "dice", "badge": "NEW",
    "title": "TRAIT REROLLS", "code": "OVERHEAVEN",
    "vo": "*Stand Dice*. Code *over heaven* gives a *jackpot roll* and *five trait rerolls*."},
   {"type": "item", "n": 3, "bg": "navy", "acc": "yellow", "game": "SUBMERGED", "icon": "fish", "badge": "NEW",
    "title": "1,500 CREDITS", "code": "UPDATE1",
    "vo": "And *Submerged*. Code *update one* gives *fifteen hundred credits*."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHAT DID", "white"), ("YOU GET?", "yellow")],
    "vo": "Redeem them *fast*, they can *expire*. What did *you* get?"},
  ]},
}

LONG = {
 "thumb": [("ADVENTURE TIME RPG", "white"), ("+ 7 NEW CODES", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 19",
   "vo": "Here's today's *Roblox news*. Roblox spotlighted the *Adventure Time RPG*, *Roblox Wallet* is replacing *DevEx*, a new *stand battler* is blowing up, and I've got *seven new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "ADVENTURE TIME RPG", "icon": "train", "badge": "SPOTLIGHT",
   "title": "ADVENTURE TIME RPG",
   "bullets": ["PICKED AS A STANDOUT NEW GAME", "BATTLE THE DUNGEON TRAIN", "BUDDIES + WEAPON UPGRADES"],
   "vo": "Number *one*. Roblox picked the official *Adventure Time RPG* as a *standout new game* this month. You battle through the *Dungeon Train* and fight *bosses*. You level up your *weapons* and bring *buddies* along. It's *free*, and it's still in *beta*."},
  {"type": "item", "n": 2, "bg": "green", "acc": "yellow", "game": "ROBLOX WALLET", "icon": "card", "badge": "COMING",
   "title": "WALLET REPLACES DEVEX",
   "bullets": ["DAILY PAYOUTS FOR CREATORS", "REPLACES DEVEX NEXT YEAR", "ROBLOX CARD IN 2027"],
   "vo": "Number *two*, for *creators*. Roblox's CEO said the new *Roblox Wallet* will *replace DevEx* next year. Wallet pays out earnings *every business day*. It starts with *US creators* over *eighteen*, and a *Roblox Card* to spend that money comes in *twenty twenty seven*."},
  {"type": "item", "n": 3, "bg": "violet", "acc": "purple", "game": "STAND OUT", "icon": "arrow", "badge": "ALPHA",
   "title": "STAND OUT IS BLOWING UP",
   "bullets": ["NEW STAND BATTLE GAME", "STILL IN PUBLIC ALPHA", "CODE: 100KLIKESHUGE"],
   "vo": "Number *three*. *Stand Out* is a new *stand battle* game, and it's one of the *hottest* new games right now. It's still in *public alpha*. New codes drop at *like goals*, and code *one hundred K likes huge* gives *arrows* and *Dalas*."},
  {"type": "item", "n": 4, "bg": "maroon", "acc": "orange", "game": "STAND DICE", "icon": "dice", "badge": "CODES",
   "title": "FREE JACKPOT ROLLS", "code": "BIZARRE",
   "bullets": ["BIZARRE: JACKPOT ROLLS + POTIONS", "OVERHEAVEN: TRAIT REROLLS + GEMS"],
   "vo": "Now, *codes*. Number *four*. *Stand Dice* has *bizarre* for *jackpot rolls* and *luck potions*, and *over heaven* for *trait rerolls* and *grade gems*."},
  {"type": "item", "n": 5, "bg": "navy", "acc": "blue", "game": "SUBMERGED", "icon": "fish", "badge": "CODES",
   "title": "FREE CREDITS", "code": "1000PLAYERS",
   "bullets": ["1000PLAYERS: 5,000 CREDITS", "UPDATE1: 1,500 CREDITS", "HERTZ: 500 CREDITS"],
   "vo": "Number *five*. *Submerged* has *one thousand players* for *five thousand credits*, *update one* for *fifteen hundred*, and *hertz* for *five hundred*."},
  {"type": "item", "n": 6, "bg": "red", "acc": "pink", "game": "ROBLOX IS UNBREAKABLE", "icon": "shield", "badge": "CODE",
   "title": "FREE PURE ARROWS", "code": "6MILLZOMBIES",
   "bullets": ["6MILLZOMBIES: 4 PURE ARROWS", "+ EXP BOOST + MASTERY DISCS"],
   "vo": "And number *six*. *Roblox is Unbreakable* code *six mill zombies* gives *four pure arrows*, *mastery discs*, and an *EXP boost*."},
  {"type": "list", "bg": "purple", "acc": "yellow", "head": "COMING UP",
   "rows": [("FREE CREATOR PLUS ENDS", "TODAY"), ("INCUBATOR DEADLINE", "DEC 7"),
            ("GAME AWARDS ON ROBLOX", "DEC 10"), ("PLUS UPGRADE DEADLINE", "DEC 19")],
   "vo": "Coming up. Free creator *Plus* ends *today*. The *Incubator* deadline is *December seventh*, *The Game Awards* hit Roblox on *December tenth*, and the *Plus upgrade* window closes *December nineteenth*."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH GAME", "white"), ("IS NEXT?", "yellow")],
   "vo": "That's *today's* news. Which game are *you* playing next? Tell me in the *comments*, and *subscribe* to *Secret Spawn*. See you *tomorrow*."},
 ]}

UPLOAD = {
 "short1": {"file": "SS_2026-11-19_1900_Short_AdventureTimeRPG", "schedule_ist": "2026-11-19 19:00",
            "title": "Roblox Just Spotlighted the Adventure Time RPG! ⚔️ #roblox #shorts",
            "description": "Roblox picked the official Adventure Time RPG as a standout new game this month. Battle through the Dungeon Train, fight bosses, level up your weapons and bring buddies along. It's free to play and still in beta.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long": {"file": "SS_2026-11-19_2300_Long_NewsToday", "schedule_ist": "2026-11-19 23:00",
          "title": "Roblox News Today: Adventure Time RPG, Roblox Wallet & 7 New Codes 🚨 #roblox",
          "description": "Today's Roblox news: Roblox spotlighted the official Adventure Time RPG (Dungeon Train, buddies, weapon upgrades, still in beta), Roblox's CEO confirmed the new Roblox Wallet will replace DevEx next year with daily payouts for creators and a Roblox Card coming in 2027, the new stand battler Stand Out is one of the hottest new games, and 4 games have new codes.\n\nChapters:\n0:00 Intro\n0:13 Adventure Time RPG Spotlight\n0:28 Roblox Wallet Replaces DevEx\n0:45 Stand Out + Code\n1:00 Stand Dice Codes\n1:10 Submerged + Roblox is Unbreakable Codes\n1:28 Coming Up\n1:41 Outro\n\nCodes in this video:\nStand Out: 100KLIKESHUGE (Mysterious Arrows, Lucky Arrow, Arrow Parts + Dalas)\nStand Dice: BIZARRE (2 Jackpot Rolls, 2 Roll Luck V Potions, 1 Void Jackpot Roll I), OVERHEAVEN (1 Jackpot Roll, 3 Roll Luck IV Potions, 5 Trait Rerolls, 5 Grade Gems)\nSubmerged: 1000PLAYERS (5,000 Credits), UPDATE1 (1,500 Credits), HERTZ (500 Credits)\nRoblox is Unbreakable: 6MILLZOMBIES (4 Pure Arrows, 8 Mastery DISCs, 24h EXP booster)\n\nCodes may expire at any time, so redeem them fast! Event times are in Eastern Time and can change.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
          "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "roblox studio", "secret spawn", "roblox news today", "adventure time rpg", "roblox adventure time", "roblox wallet", "roblox devex", "stand out roblox", "stand out codes", "stand dice codes", "submerged codes", "roblox is unbreakable codes"],
          "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_2026-11-20_0100_Short_FreeCodesToday", "schedule_ist": "2026-11-20 01:00",
            "title": "3 FREE Roblox Codes You Need Today! 🎁 #roblox #shorts",
            "description": "3 Roblox codes:\nStand Dice: BIZARRE (2 Jackpot Rolls, 2 Roll Luck V Potions, 1 Void Jackpot Roll I)\nSubmerged: 1000PLAYERS (5,000 Credits)\nRoblox is Unbreakable: 6MILLZOMBIES (4 Pure Arrows, 8 Mastery DISCs, 24h EXP booster)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
 "short3": {"file": "SS_2026-11-20_0300_Short_HiddenCodes", "schedule_ist": "2026-11-20 03:00",
            "title": "3 Hidden Roblox Codes Most Players Missed 🤫 #roblox #shorts",
            "description": "3 more Roblox codes:\nStand Out: 100KLIKESHUGE (arrows + Dalas)\nStand Dice: OVERHEAVEN (1 Jackpot Roll, 3 Roll Luck IV Potions, 5 Trait Rerolls, 5 Grade Gems)\nSubmerged: UPDATE1 (1,500 Credits)\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxcodes #shorts"},
}
