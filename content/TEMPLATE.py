# Secret Spawn - <DAY, e.g. 14 Nov 2026> content          (copy to content/YYYY-MM-DD.py)
#
# YYYY-MM-DD = the day of the 19:00 Short (day D). That file holds:
#   short1 -> D 19:00 | long -> D 23:00 | short2 -> D+1 01:00 | short3 -> D+1 03:00   (Europe/Istanbul)
#
# Narration rules ("vo"):
#   *word*  = highlighted in the accent colour in captions (asterisks are stripped for TTS)
#   write numbers/codes the way they should be SPOKEN ("three thousand", "thanks for likes"),
#   while on-screen fields (title/code/bullets/badge) use the real text ("3,000", "THX4LIKES").
#   EXP and RNG are auto-spelled by tts.py; spell other acronyms with spaces ("U P D twelve").
# Scene types:
#   intro  : bg, acc, vo  (+ long video: lines=[(text,colour),..], tag)
#   item   : n, bg, acc, game, icon, badge, title, [code], vo  (+ long video: bullets=[..] max 3-4)
#   list   : bg, acc, head, rows=[(left, right), ..] max 4, vo      (long video only)
#   outro  : bg, acc, q=[(line, colour), (line, colour)], vo
# bg   : purple navy green maroon red blue violet          (palette.PAL)
# acc  : yellow green blue orange purple pink               (palette.ACC)  colour names also valid in lines/q
# icon : see `python3 tools/icons.py sheet.png` (swords flame moon binoculars frame trophy gem mystery
#        fruit shield tag pyramid bolt scroll car drill bucket pause fish hammer ball camera gamepad
#        phone taco cake top soap). Never draw Roblox logos/characters; add new flat icons to icons.py.
# Length targets: Shorts 20-27 s (intro + 3 items + outro, one sentence each).
#                 Long ~3:00-3:30 (intro + 5 news items + 5 code items + list + outro).
from palette import PAL, ACC  # noqa: F401

SHORTS = {
 "short1": {
  "title_lines": [("3 BIG ROBLOX", "white"), ("CHANGES", "yellow")], "tag": "THIS WEEK",
  "scenes": [
   {"type": "intro", "bg": "purple", "acc": "yellow",
    "vo": "*Three* big *Roblox* changes you need to know *today*."},
   {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "GAME OR FEATURE", "icon": "bolt", "badge": "NEW",
    "title": "SHORT HEADLINE HERE",
    "vo": "Number *one*. One clear sentence with the key *fact* and *date*."},
   {"type": "item", "n": 2, "bg": "green", "acc": "green", "game": "GAME OR FEATURE", "icon": "gem", "badge": "NOV 14",
    "title": "SECOND HEADLINE",
    "vo": "Number *two*. One clear sentence."},
   {"type": "item", "n": 3, "bg": "maroon", "acc": "orange", "game": "GAME OR FEATURE", "icon": "trophy", "badge": "LIVE",
    "title": "THIRD HEADLINE",
    "vo": "Number *three*. One clear sentence."},
   {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("WHICH ONE", "white"), ("FIRST?", "yellow")],
    "vo": "Which one are *you* checking out *first*? Tell me *below*."},
  ]},
 # "short2": {...}, "short3": {...}   same structure. Code Shorts: item has "code": "EXACTCODE".
}

LONG = {
 # optional: thumbnail headline (else intro 'lines' are used)
 "thumb": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")],
 "scenes": [
  {"type": "intro", "bg": "purple", "acc": "yellow",
   "lines": [("ROBLOX NEWS", "white"), ("TODAY", "yellow")], "tag": "NOV 14",
   "vo": "Here's today's *Roblox news*. <one-line teaser of each block>, and I've got *five games* with *new codes*. Let's go."},
  {"type": "item", "n": 1, "bg": "blue", "acc": "blue", "game": "FEATURE", "icon": "bolt", "badge": "LIVE",
   "title": "HEADLINE",
   "bullets": ["FACT ONE", "FACT TWO", "FACT THREE"],
   "vo": "Number *one*. Three or four sentences: what, when, who it affects, why it matters."},
  # ... items 2-5 news, items 6-10 codes ("code": "MAINCODE", bullets "CODE: REWARD")
  {"type": "list", "bg": "red", "acc": "pink", "head": "THIS WEEK",
   "rows": [("EVENT ONE", "NOV 14"), ("EVENT TWO", "NOV 15")],
   "vo": "Here's your *week*. ..."},
  {"type": "outro", "bg": "purple", "acc": "yellow", "q": [("YOUR QUESTION", "white"), ("HERE?", "yellow")],
   "vo": "That's *today's* news. <question>? Tell me in the *comments*, and *subscribe* to *Secret Spawn* so you never miss a *Roblox update*. See you *tomorrow*."},
 ]}

# Upload metadata (used for file names + upload_manifest.json; the upload itself is a separate, approved step)
UPLOAD = {
 "short1": {"file": "SS_YYYY-MM-DD_1900_Short_Slug", "schedule_ist": "YYYY-MM-DD 19:00",
            "title": "Headline With Hook! 🎮 #roblox #shorts",
            "description": "2-3 sentence summary.\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #shorts"},
 "long":   {"file": "SS_YYYY-MM-DD_2300_Long_NewsToday", "schedule_ist": "YYYY-MM-DD 23:00",
            "title": "Roblox News Today: Topic A, Topic B & N New Codes 🚨 #roblox",
            "description": "Summary...\n\nChapters:\n0:00 Intro\n...\n\nCodes in this video:\n...\n\nCodes may expire at any time, so redeem them fast!\n\nSubscribe to Secret Spawn for daily Roblox news!\n\n#roblox #robloxnews #robloxcodes #robloxupdate",
            "tags": ["roblox", "roblox news", "roblox update", "roblox codes", "secret spawn", "roblox news today"],
            "language": "English", "category": "Gaming"},
 "short2": {"file": "SS_YYYY-MM-DD+1_0100_Short_Slug", "schedule_ist": "YYYY-MM-DD+1 01:00", "title": "...", "description": "..."},
 "short3": {"file": "SS_YYYY-MM-DD+1_0300_Short_Slug", "schedule_ist": "YYYY-MM-DD+1 03:00", "title": "...", "description": "..."},
}
