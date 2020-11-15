import sqlite3
import pandas as pd
#connect to database

conn=sqlite3.connect('Jumbled_Words.db')
c=conn.cursor()
'''
c.execute("""
            CREATE TABLE words(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Word TEXT 
            ) 
""")'''

def add(word_list,number_of_words_in_the_list):
    conn=sqlite3.connect("Jumbled_Words.db")
    c=conn.cursor()
    for i in range(number_of_words_in_the_list):
        c.execute("INSERT INTO words VALUES (:ID,:word)",
        {
            'ID':i,
            'word':word_list[i]
        }
        )
    conn.commit()
    conn.close()

word_list=["philanthropist",
"antidote",
"strive",
"ambidextrous",
"retrospective",
"precursors",
"introvert",
"gerontocracy",
"ambiguous",
"braggart",
"aggravate",
"entice",
"alleviate",
"adorn",
"equilibrium",
"abhor",
"connote",
"endeavor",
"agile",
"renovate",
"curriculum",
"malevolent",
"amalgamate",
"drowsiness",
"stray",
"disrobe",
"acumen",
"suffocate",
"sporadic",
"scent",
"sequence",
"audacious",
"affinity",
"animosity",
"heterogeneous",
"fragile",
"legacy",
"massacre",
"appease",
"submerge",
"adulteration",
"combustion",
"premature",
"shunned",
"anguish",
"apt",
"conceal",
"grumble",
"indigenous",
"offhand",
"loll",
"correlate",
"somersault",
"abscond",
"edible",
"extinguish",
"inquest",
"surcharge",
"accolade",
"conjoin",
"timid",
"opaqueness",
"disallow",
"abide",
"impermeable",
"console",
"warrant",
"acclaimed",
"extinct",
"reminiscent",
"catalyst",
"embezzle",
"shallow",
"clientele",
"brittle",
"negligent",
"affable",
"salvage",
"moribund",
"relapse",
"dangle",
"ascend",
"asterisk",
"yarn",
"arrogance",
"divergence",
"allegiance",
"vigorous",
"dwarf",
"livid",
"rejuvenation",
"fragrant",
"judicious",
"hospitable",
"odor",
"scribble",
"ameliorate",
"poseur",
"sawdust",
"narcissism",
"dullard",
"succumb",
"sluggard",
"flop",
"ingest",
"reiterate",
"derivative",
"defer",
"eloquence",
"clot",
"commuter",
"weigh",
"steeply",
"torque",
"benefactor",
"moderation",
"plea",
"invincible",
"enduring",
"flimsy",
"tadpole",
"turmoil",
"sanity",
"cryptic",
"gallant",
"endorse",
"sponge",
"volatile",
"alloy",
"reconcile",
"fission",
"commemorate",
"gait",
"dormant",
"shard",
"chisel",
"encapsulate",
"complaisant",
"grievous",
"hypocrisy",
"enzyme",
"eradicate",
"infuriate",
"Lambaste",
"sanction",
"engulf",
"euphoria",
"renowned",
"colloquial",
"evoke",
"mischievous",
"implicit",
"abysmal",
"dote",
"riddle",
"misogynist",
"disproof",
"sadastic",
"impromptu",
"inclined",
"erratic",
"meticulous",
"ambivalent",
"pertain",
"auxiliary",
"constrict",
"luminary",
"ossified",
"tonic",
"perish",
"presentiment",
"indistinct",
"dupe",
"abstruse",
"turbulence",
"connoisseur",
"aberration",
"extralegal",
"pest",
"parenthesis",
"sophisticated",
"ail",
"limp",
"arcane",
"mite",
"edify",
"recuperate",
"satiate",
"yeoman",
"fidelity",
"pluck",
"perjury",
"paradigm",
"gullible",
"sobriety",
"tractable",
"writ",
"mesmerize",
"predominate",
"articulate",
"fleet",
"solvent",
"dislodge",
"partisan",
"spear",
"vivacious",
"beguile",
"coagulation",
"foolproof",
"liberality",
"elaborate",
"brass",
"permeate",
"malleable",
"suffice",
"lampoon",
"immutable",
"forgery",
"patron",
"cordial",
"retrograde",
"cumbersome",
"sheath",
"repel",
"unscathed",
"superimpose",
"boisterous",
"implosion",
"centurion",
"knit",
"pivotal",
"enigma",
"buoyant",
"jabber",
"treacherous",
"bewilder",
"stride",
"garrulous",
"redeem",
"calipers",
"impede",
"resuscitation",
"apartheid",
"concur",
"indulgent",
"recitals",
"woo",
"misanthrope",
"evasive",
"eulogy",
"foster",
"pilferer",
"refine",
"dexterity",
"bogus",
"incongruous",
"multifarious",
"skit",
"repulsive",
"hapless",
"convoluted",
"indefatigability",
"fawn",
"wince",
"feud",
"cognizant",
"substantiation",
"euthanasia",
"irate",
"underbid",
"alcove",
"frantic",
"peccadillo",
"pervade",
"decree",
"concoct",
"turquoise",
"miser",
"valiant",
"derogatory",
"tarnished",
"reverent",
"imminent",
"voluptuous",
"suppress",
"irrevocable",
"soggy",
"vindictive",
"wanton",
"pinch",
"earthenware",
"unearth",
"savor",
"hoax",
"vitriolic",
"loquacious",
"defiance",
"candid",
"warmonger",
"gust",
"coalescing",
"precursory",
"counterfeit",
"gush",
"quandary",
"chortle",
"compunction",
"plunge",
"revere",
"swerve",
"abraded",
"punitive",
"dawdler",
"noxious",
"torment",
"squander",
"exculpate",
"stifled",
"antithetical",
"deplete",
"apropos",
"recompense",
"coerce",
"aseptic",
"implacable",
"holster",
"proliferate",
"propagation",
"personable",
"reciprocity",
"vigilance",
"distraught",
"ineptitude",
"lustrous",
"condense",
"extol",
"forestall",
"stipulate",
"lament",
"provoke",
"plummet",
"subpoena",
"accrue",
"idolatry",
"apprehensive",
"nihilism",
"soot",
"valorous",
"complaisance",
"illicit",
"viscous",
"aversion",
"haughty",
"concord",
"latent",
"topple",
"supersede",
"entangle",
"variegate",
"inept",
"deviance",
"enunciate",
"polemic",
"pristine",
"impediment",
"floe",
"malevolence",
"prevalent",
"undermine",
"arduous",
"slack",
"calisthenics",
"placate",
"palate",
"regicide",
"iconoclast",
"pungency",
"aloof",
"indomitable",
"finesse",
"whimsical",
"tamper",
"recluse",
"hush",
"felon",
"frugal",
"shun",
"mendacious",
"apprise",
"muffler",
"bigot",
"imperative",
"enthral",
"smolder",
"dismal",
"perilous",
"lavish",
"trickle",
"diabolical",
"vehemence",
"disencumber",
"impending",
"stickler",
"stigma",
"avow",
"castigation",
"benevolence",
"incessant",
"squat",
"indulge",
"deter",
"incredulous",
"tenacity",
"exuberance",
"apostate",
"gist",
"transient",
"connotation",
"engrave",
"berate",
"conciliatory",
"subdue",
"soar",
"empirical",
"procrastination",
"tassel",
"immaculate",
"astute",
"flaunting",
"impair",
"prone",
"coy",
"pillage",
"incorrigibility",
"extrovert",
"approbation",
"efface",
"taciturn",
"mollify",
"exorbitant",
"sober",
"truce",
"conviction",
"bolster",
"precepts",
"castigate",
"curtail",
"fallacious",
"espouse",
"nonchalant",
"flamboyant",
"gorge",
"vex",
"grandiloquent",
"poncho",
"impassive",
"pitfall",
"coddle",
"inscrutable",
"shrill",
"arboreal",
"boorish",
"lull",
"timorous",
"imperturbable",
"perch",
"prudence",
"cohort",
"sagacious",
"ignoble",
"intersperse",
"oblivious",
"rescind",
"nebulous",
"disseminate",
"heed",
"laudatory",
"bask",
"fluke",
"ebullient",
"pliant",
"endearing",
"precarious",
"inferno",
"palpitate",
"embellish",
"ominous",
"fluster",
"matriculation",
"susceptibility",
"graze",
"quell",
"divulge",
"dubious",
"malapropism",
"maverick",
"irascible",
"incise",
"ostracism",
"ambrosial",
"sidestep",
"extort",
"cling",
"epitome",
"arabesque",
"ferocity",
"cantankerous",
"chaste",
"corroboration",
"expurgate",
"insensible",
"garner",
"fidget",
"impervious",
"rift",
"efficacy",
"Conduce",
"attune",
"convoke",
"enmity",
"credulous",
"palpability",

"plead",
"feral",
"gourmand",
"morbid",
"superfluous",
"equipoise",
"veer",
"benign",
"lackluster",
"chastisement",
"breach",
"rarefy",
"dissent",
"neophyte",
"reticence",
"pious",
"trudge",
"thrift",
"daunt",
"veneration",
"grave",
"frenetic",
"disheveled",
"temperate",
"impiety",
"blas�",
"scalding",
"irresolute",
"rave",
"heresy",
"guile",
"fret",
"chicanery",
"telltale",
"feckless",
"ardor",
"debacle",
"tawdry",
"striated",
"jocular",
"exoneration",
"contentious",
"cajole",
"resilience",
"disdain",
"taunt",
"alacrity",
"abeyance",
"apotheosis",
"hoodwink",
"glimmer",
"terse",
"ulterior",
"jagged",
"myriad",
"inimitable",
"conundrum",
"incite",
"falter",
"drawl",
"clamor",
"nexus",
"render",
"clinch",
"abet",
"decorum",
"quiescence",
"discreet",
"ale",
"sash",
"ruffian",
"tepid",
"itinerate",
"doleful",
"innocuous",
"exhaustive",
"abrogate",
"recant",
"crush",
"talon",
"quack",
"emaciate",
"sever",
"sodden",
"mephitic",
"sketchy",
"intrepid",
"preternatural",
"pariah",
"unfeigned",
"servile",
"ossify",
"prim",
"churlish",
"fixate",
"commodious",
"flinch",
"insurrection",
"recast",
"thwart",
"transgress",
"engrossing",
"vilify",
"intransigence",
"covert",
"heinous",
"infuse",
"ubiquitous",
"quixotic",
"fracas",
"putrefaction",
"torpid",
"assuage",
"insinuate",
"sycophant",
"urbane",
"ebullience",
"austere",
"inadvertent",
"assail",
"stingy",
"equivocal",
"proclivity",
"cower",
"colander",
"maul",
"provisional",
"burnish",
"penury",
"dirge",
"ire",
"vain",
"ruddy",
"forfeit",
"engender",
"occluded",
"rotund",
"puerile",
"savant",
"profuse",
"enervate",
"adamant",
"dynamo",
"equivocate",
"gnaw",
"wean",
"pry",
"beatify",
"discrete",
"hegemony",
"glut",
"crease",
"ascertain",
"foray",
"guileless",
"sting",
"splice",
"penitent",
"elegy",
"reticent",
"pusillanimous",
"obtuse",
"paucity",
"retinue",
"diatribe",
"cogitate",
"consummate",
"stolid",
"effrontery",
"dissolution",
"derision",
"indolence",
"pyre",
"erudite",
"mercurial",
"corporeal",
"pedestrian",
"equable",
"admonitory",
"luculent",
"coeval",
"insularity",
"auspicious",
"secular",
"streak",
"nascent",
"decry",
"penchant",
"pulchritude",
"onus",
"vanquish",
"extirpate",
"assiduous",
"privation",
"accretion",
"covetous",
"defalcate",
"baneful",
"indelible",
"palliate",
"cogent",
"dearth",
"pellucid",
"condone",
"lumber",
"discredit",
"recidivism",
"lurk",
"coda",
"cornucopia",
"veneer",
"petrify",
"censure",
"elicit",
"serration",
"dainty",
"caustic",
"highbrow",
"odious",
"abjure",
"chauvinist",
"tyro",
"inane",
"dilate",
"deprave",
"denigrate",
"duplicity",
"protracted",
"taut",
"turbid",
"fledgling",
"punctilious",
"bellicose",
"ignominious",
"interim",
"avid",
"florid",
"malign",
"inundate",
"attenuate",
"consume",
"phlegmatic",
"sanctimony",
"inimical",
"prevaricate",
"ingenuous",
"veracity",
"barren",
"plaque",
"lien",
"exigency",
"chagrin",
"aver",
"credulity",
"snub",
"libel",
"forbearance",
"volubility",
"conceit",
"idiosyncrasy",
"obdurate",
"dud",
"None",
"facile",
"contiguous",
"jejune",
"waft",
"resigned",
"abut",
"finagle",
"repudiate",
"tocsin",
"verisimilitude",
"fringe",
"chastened",
"somatic",
"pernicious",
"husk",
"insipid",
"coax",
"dolt",
"penurious",
"parley",
"effluvia",
"incursion",
"obfuscate",
"preclude",
"disingenuous",
"encumbrance",
"obtain",
"morose",
"gloat",
"quirk",
"extempore",
"disparate",
"regale",
"scorch",
"perpetrate",
"foil",
"salubrious",
"malinger",
"grouse",
"Palpable",
"discern",
"waffle",
"transitory",
"perfunctory",
"pundit",
"extant",
"mundane",
"deluge",
"visceral",
"lachrymose",
"ascribe",
"sullied",
"exscind",
"temerity",
"extenuate",
"grovel",
"collusion",
"squalid",
"undulate",
"fagged",
"shrewd",
"hollow",
"harbinger",
"august",
"conspicuous",
"epiphany",
"rife",
"evince",
"Pastiche",
"gaucherie",
"snare",
"rancorous",
"finical",
"mellifluous",
"macabre",
"uncouth",
"amortize",
"obviate",
"levity",
"ascetic",
"delineate",
"paean",
"nadir",
"emote",
"fervor",
"congeal",
"verve",
"gauche",
"lope",
"expostulate",
"discourse",
"lionize",
"dilettante",
"noisome",
"bandy",
"dogmatic",
"epicurean",
"sumptuous",
"craven",
"lassitude",
"ostentation",
"sanguine",
"irksome",
"prodigal",
"brash",
"requite",
"imperious",
"didactic",
"presage",
"sophomoric",
"trifling",
"drone",
"verdant",
"ensconce",
"intransigent",
"prodigious",
"palatial",
"agog",
"desiccant",
"philistine",
"broach",
"wile",
"heretic",
"supine",
"reactionary",
"raconteur",
"ferment",
"qualm",
"hauteur",
"perfidious",
"festoon",
"rumple",
"propitious",
"remonstrate",
"roll",
"curmudgeon",
"bequest",
"inchoate",
"facetious",
"fatuous",
"reproach",
"wan",
"rapacious",
"stymie",
"baleful",
"obtrusive",
"preen",
"jibe",
"extricable",
"figurehead",
"benison",
"provident",
"rivet",
"barrage",
"fetid",
"burgeon",
"overweening",
"discountenance",
"vacillation",
"eschew",
"pedantic",
"impetuous",
"rueful",
"equanimity",
"hubris",
"kibosh",
"mendicant",
"soporific",
"atonement",
"ford",
"forswear",
"excoriation",
"macerate",
"supplicate",
"saturnine",
"skiff",
"boggle",
"profundity",
"blithe",
"slur",
"contemn",
"blandness",
"cloture",
"hallow",
"tortuous",
"egress",
"scabbard",
"rant",
"vacuity",
"dereliction",
"seminal",
"petrous",
"prudish",
"mendacity",
"machination",
"restive",
"perspicacity",
"labyrinthine",
"esoteric",
"perfidy",
"entreat",
"prune",
"incumbents",
"contrite",
"maladroit",
"probity",
"manacle",
"indigence",
"fervid",
"imbroglio",
"stigmatize",
"molt",
"overhaul",
"germane",
"specious",
"goad",
"vestige",
"cravat",
"eddy",
"cordon",
"forage",
"poignant",
"depredation",
"flax",
"parsimonious",
"exploit",
"subsume",
"aleck",
"petulant",
"rubicund",
"severance",
"ineluctable",
"platitude",
"lugubrious",
"insouciant",
"halcyon",
"officious",
"gouge",
"interdict",
"onerous",
"predilection",
"flout",
"demagogue",
"belligerent",
"chary",
"feint",
"profligate",
"impute",
"upbraid",
"cabal",
"deprecate",
"obsequious",
"inveterate",
"retard",
"spurious",
"propitiatory",
"maudlin",
"shunt",
"aplomb",
"dulcet",
"tautology",
"inured",
"None",
"nemesis",
"gregarious",
"denouement",
"hone",
"cursory",
"forge",
"impecunious",
"sordid",
"argot",
"plethora",
"sinuous",
"vigilant",
"libertine",
"desultory",
"propinquity",
"salacious",
"augury",
"harangue",
"odium",
"turgid",
"recalcitrant",
"harrow",
"mulct",
"homiletics",
"eclat",
"foible",
"epistle",
"deposition",
"inculcate",
"tangential",
"gainsay",
"middling",
"countervail",
"moot",
"repertoire",
"nary",
"pinchbeck",
"stentorian",
"finicky",
"resort",
"profane",
"divestiture",
"gossamer",
"churl",
"temperance",
"truculence",
"inveigh",
"diffidence",
"atavistic",
"levee",
"astringent",
"pucker",
"trepidation",
"opprobrious",
"diaphanous",
"nugatory",
"rebuff",
"distrait",
"tenuous",
"detumescence",
"glean",
"disinter",
"vitiate",
"foppish",
"panegyric",
"flak",
"ramify",
"plod",
"refractory",
"fecund",
"encomium",
"expedient",
"pugnacious",
"vituperate",
"trenchant",
"disconcert",
"quail",
"obloquy",
"discomfit",
"impudent",
"quaff",
"untoward",
"sermon",
"voluble",
"sublime",
"rabble",
"calumny",
"peremptory",
"strut",
"blandishment",
"cant",
"bereft",
"fetter",
"prosaic",
"turpitude",
"glib",
"raffish",
"ensign",
"contumacious",
"asperity",
"meretricious",
"simper",
"idyll",
"teetotal",
"incense",
"veritable",
"invective",
"mien",
"implicate",
"endemic",
"hirsute",
"unencumbered",
"sophistry",
"impugned",
"surfeit",
"quotidian",
"umbrage",
"miseenscene",
"felicitous",
"hack",
"toady",
"peregrination",
"mettle",
"ineffable",
"ecumenical",
"incipient",
"canvass",
"plaintive",
"pine",
"ostensible",
"tout",
"piquant",
"tamp",
"forbear",
"slate",
"minatory",
"stanch",
"fledged",
"plumb",
"deferential",
"sundry",
"stipple",
"blatant",
"aspersion",
"demur",
"consternation",
"spurn",
"cadge",
"bedizen",
"purvey",
"desuetude",
"suppliant",
"presumption",
"brummagem",
"countenance",
"belabor",
"obstreperous",
"redoubtable",
"balk",
"supercilious",
"trite",
"virago",
"stygian",
"rebus",
"orison",
"preponderance",
"reprobate",
"hermetic",
"expiation",
"vagary",
"sententious",
"trencherman",
"hew",
"proscribe",
"dissemble",
"portent",
"imperviousness",
"picaresque",
"pileous",
"venal",
"doggerel",
"splenetic",
"peripatetic",
"imprecation",
"froward",
"profligacy",
"lithe",
"mettlesome",
"petrified",
"succor",
"fulsome",
"ferret",
"travesty",
"duress",
"puissance",
"acarpous",
"pied",
"effete",
"edacious",
"constrain",
"sobriquet",
"wend",
"fulmination",
"nibble",
"ponderous",
"brook",
"palaver",
"pique",
"slake",
"salutary",
"detraction",
"welter",
"repast",
"abraid",
"nostrum",
"stint",
"pith",
"suborn",
"nonplused",
"refulgent",
"expatiate",
"fustian",
"garble",
"recondite",
"scurvy",
"mince",
"epithet",
"sedulous",
"prolix",
"importune",
"involute",
"bilge",
"cavalcade",
"sere",
"droll",
"descry",
"brazen",
"repine",
"limn",
"wag",
"lucubrate",
"coruscate",
"crass",
"consequential",
"foment",
"testiness",
"recreancy",
"arrant",
"quibble",
"lam",
"Archaic",
"imbibe"
]

def show_database():
    conn=sqlite3.connect('Jumbled_Words.db')
    c=conn.cursor()
    c.execute("SELECT * FROM words")
    records=c.fetchall()

    for record in records:
        print(record)

number=len(word_list)
show_database()





conn.commit()
conn.close()