
import sys
from mtga.models.card import Card
from mtga.models.card_set import Set
import inspect


ActofHeroism = Card("act_of_heroism", "Act of Heroism", ['1', 'W'], ['W'], "Instant", "", "HOU", "Common", 1, 65479)
AdornedPouncer = Card("adorned_pouncer", "Adorned Pouncer", ['1', 'W'], ['W'], "Creature", "Cat", "HOU", "Rare", 2, 65481)
AngelofCondemnation = Card("angel_of_condemnation", "Angel of Condemnation", ['2', 'W', 'W'], ['W'], "Creature", "Angel", "HOU", "Rare", 3, 65483)
AngeloftheGodPharaoh = Card("angel_of_the_godpharaoh", "Angel of the God-Pharaoh", ['4', 'W', 'W'], ['W'], "Creature", "Angel", "HOU", "Uncommon", 4, 65485)
AvenofEnduringHope = Card("aven_of_enduring_hope", "Aven of Enduring Hope", ['4', 'W'], ['W'], "Creature", "Bird Cleric", "HOU", "Common", 5, 65487)
CrestedSunmare = Card("crested_sunmare", "Crested Sunmare", ['3', 'W', 'W'], ['W'], "Creature", "Horse", "HOU", "Mythic Rare", 6, 65489)
DauntlessAven = Card("dauntless_aven", "Dauntless Aven", ['2', 'W'], ['W'], "Creature", "Bird Warrior", "HOU", "Common", 7, 65491)
DesertsHold = Card("deserts_hold", "Desert's Hold", ['2', 'W'], ['W'], "Enchantment", "Aura", "HOU", "Uncommon", 8, 65493)
# mixup start
DisposalMummy = Card("disposal_mummy", "Disposal Mummy", ['2', 'W'], ['W'], "Creature", "Zombie Jackal", "HOU", "Common", 9, 65957)
DjeruWithEyesOpen = Card("djeru_with_eyes_open", "Djeru, With Eyes Open", ['3', 'W', 'W'], ['W'], "Legendary Creature", "Human Warrior", "HOU", "Rare", 10, 65495)
DjerusRenunciation = Card("djerus_renunciation", "Djeru's Renunciation", ['1', 'W'], ['W'], "Instant", "", "HOU", "Common", 11, 65497)
DutifulServants = Card("dutiful_servants", "Dutiful Servants", ['3', 'W'], ['W'], "Creature", "Zombie", "HOU", "Common", 12, 65499)
# mixup end
GideonsDefeat = Card("gideons_defeat", "Gideon's Defeat", ['W'], ['W'], "Instant", "", "HOU", "Uncommon", 13, 65503)
GodPharaohsFaithful = Card("godpharaohs_faithful", "God-Pharaoh's Faithful", ['W'], ['W'], "Creature", "Human Wizard", "HOU", "Common", 14, 65505)
HourofRevelation = Card("hour_of_revelation", "Hour of Revelation", ['3', 'W', 'W', 'W'], ['W'], "Sorcery", "", "HOU", "Rare", 15, 65507)
MummyParamount = Card("mummy_paramount", "Mummy Paramount", ['1', 'W'], ['W'], "Creature", "Zombie", "HOU", "Common", 16, 65509)
OketrasAvenger = Card("oketras_avenger", "Oketra's Avenger", ['1', 'W'], ['W'], "Creature", "Human Warrior", "HOU", "Common", 17, 65511)
OketrasLastMercy = Card("oketras_last_mercy", "Oketra's Last Mercy", ['1', 'W', 'W'], ['W'], "Sorcery", "", "HOU", "Rare", 18, 65513)
OverwhelmingSplendor = Card("overwhelming_splendor", "Overwhelming Splendor", ['6', 'W', 'W'], ['W'], "Enchantment", "Aura Curse", "HOU", "Mythic Rare", 19, 65515)
Sandblast = Card("sandblast", "Sandblast", ['2', 'W'], ['W'], "Instant", "", "HOU", "Common", 20, 65517)
SavingGrace = Card("saving_grace", "Saving Grace", ['1', 'W'], ['W'], "Enchantment", "Aura", "HOU", "Uncommon", 21, 65519)
Solemnity = Card("solemnity", "Solemnity", ['2', 'W'], ['W'], "Enchantment", "", "HOU", "Rare", 22, 65521)
SolitaryCamel = Card("solitary_camel", "Solitary Camel", ['2', 'W'], ['W'], "Creature", "Camel", "HOU", "Common", 23, 65523)
SteadfastSentinel = Card("steadfast_sentinel", "Steadfast Sentinel", ['3', 'W'], ['W'], "Creature", "Human Cleric", "HOU", "Common", 24, 65525)
StewardofSolidarity = Card("steward_of_solidarity", "Steward of Solidarity", ['1', 'W'], ['W'], "Creature", "Human Warrior", "HOU", "Uncommon", 25, 65527)
SunscourgeChampion = Card("sunscourge_champion", "Sunscourge Champion", ['2', 'W'], ['W'], "Creature", "Human Wizard", "HOU", "Uncommon", 26, 65529)
UnconventionalTactics = Card("unconventional_tactics", "Unconventional Tactics", ['2', 'W'], ['W'], "Sorcery", "", "HOU", "Uncommon", 27, 65531)
VizieroftheTrue = Card("vizier_of_the_true", "Vizier of the True", ['3', 'W'], ['W'], "Creature", "Human Cleric", "HOU", "Uncommon", 28, 65533)
AerialGuide = Card("aerial_guide", "Aerial Guide", ['2', 'U'], ['U'], "Creature", "Drake", "HOU", "Common", 29, 65535)
AvenReedstalker = Card("aven_reedstalker", "Aven Reedstalker", ['3', 'U'], ['U'], "Creature", "Bird Warrior", "HOU", "Common", 30, 65537)
ChampionofWits = Card("champion_of_wits", "Champion of Wits", ['2', 'U'], ['U'], "Creature", "Naga Wizard", "HOU", "Rare", 31, 65539)
CountervailingWinds = Card("countervailing_winds", "Countervailing Winds", ['2', 'U'], ['U'], "Instant", "", "HOU", "Common", 32, 65541)
CunningSurvivor = Card("cunning_survivor", "Cunning Survivor", ['1', 'U'], ['U'], "Creature", "Human Warrior", "HOU", "Common", 33, 65543)
EternalofHarshTruths = Card("eternal_of_harsh_truths", "Eternal of Harsh Truths", ['2', 'U'], ['U'], "Creature", "Zombie Cleric", "HOU", "Uncommon", 34, 65545)
FrayingSanity = Card("fraying_sanity", "Fraying Sanity", ['2', 'U'], ['U'], "Enchantment", "Aura Curse", "HOU", "Rare", 35, 65547)
HourofEternity = Card("hour_of_eternity", "Hour of Eternity", ['X', 'X', 'U', 'U', 'U'], ['U'], "Sorcery", "", "HOU", "Rare", 36, 65549)
ImaginaryThreats = Card("imaginary_threats", "Imaginary Threats", ['2', 'U', 'U'], ['U'], "Instant", "", "HOU", "Uncommon", 37, 65551)
JacesDefeat = Card("jaces_defeat", "Jace's Defeat", ['1', 'U'], ['U'], "Instant", "", "HOU", "Uncommon", 38, 65553)
KefnetsLastWord = Card("kefnets_last_word", "Kefnet's Last Word", ['2', 'U', 'U'], ['U'], "Sorcery", "", "HOU", "Rare", 39, 65555)
NimbleObstructionist = Card("nimble_obstructionist", "Nimble Obstructionist", ['2', 'U'], ['U'], "Creature", "Bird Wizard", "HOU", "Rare", 40, 65557)
OminousSphinx = Card("ominous_sphinx", "Ominous Sphinx", ['3', 'U', 'U'], ['U'], "Creature", "Sphinx", "HOU", "Uncommon", 41, 65559)
ProvenCombatant = Card("proven_combatant", "Proven Combatant", ['U'], ['U'], "Creature", "Human Warrior", "HOU", "Common", 42, 65561)
Riddleform = Card("riddleform", "Riddleform", ['1', 'U'], ['U'], "Enchantment", "", "HOU", "Uncommon", 43, 65563)
SeeroftheLastTomorrow = Card("seer_of_the_last_tomorrow", "Seer of the Last Tomorrow", ['2', 'U'], ['U'], "Creature", "Naga Cleric", "HOU", "Common", 44, 65565)
SinuousStriker = Card("sinuous_striker", "Sinuous Striker", ['2', 'U'], ['U'], "Creature", "Naga Warrior", "HOU", "Uncommon", 45, 65567)
SpellweaverEternal = Card("spellweaver_eternal", "Spellweaver Eternal", ['1', 'U'], ['U'], "Creature", "Zombie Naga Wizard", "HOU", "Common", 46, 65569)
StrategicPlanning = Card("strategic_planning", "Strategic Planning", ['1', 'U'], ['U'], "Sorcery", "", "HOU", "Common", 47, 65571)
StripedRiverwinder = Card("striped_riverwinder", "Striped Riverwinder", ['6', 'U'], ['U'], "Creature", "Serpent", "HOU", "Common", 48, 65573)
SupremeWill = Card("supreme_will", "Supreme Will", ['2', 'U'], ['U'], "Instant", "", "HOU", "Uncommon", 49, 65575)
SwarmIntelligence = Card("swarm_intelligence", "Swarm Intelligence", ['6', 'U'], ['U'], "Enchantment", "", "HOU", "Rare", 50, 65577)
TragicLesson = Card("tragic_lesson", "Tragic Lesson", ['2', 'U'], ['U'], "Instant", "", "HOU", "Common", 51, 65579)
UneshCriosphinxSovereign = Card("unesh_criosphinx_sovereign", "Unesh, Criosphinx Sovereign", ['4', 'U', 'U'], ['U'], "Legendary Creature", "Sphinx", "HOU", "Mythic Rare", 52, 65581)
UnquenchableThirst = Card("unquenchable_thirst", "Unquenchable Thirst", ['1', 'U'], ['U'], "Enchantment", "Aura", "HOU", "Common", 53, 65583)
Unsummon = Card("unsummon", "Unsummon", ['U'], ['U'], "Instant", "", "HOU", "Common", 54, 65585)
VizieroftheAnointed = Card("vizier_of_the_anointed", "Vizier of the Anointed", ['3', 'U'], ['U'], "Creature", "Human Cleric", "HOU", "Uncommon", 55, 65587)
AccursedHorde = Card("accursed_horde", "Accursed Horde", ['3', 'B'], ['B'], "Creature", "Zombie", "HOU", "Uncommon", 56, 65589)
AmmitEternal = Card("ammit_eternal", "Ammit Eternal", ['2', 'B'], ['B'], "Creature", "Zombie Crocodile Demon", "HOU", "Rare", 57, 65591)
# mixup start
ApocalypseDemon = Card("apocalypse_demon", "Apocalypse Demon", ['4', 'B', 'B'], ['B'], "Creature", "Demon", "HOU", "Rare", 58, 65595)
BanewhipPunisher = Card("banewhip_punisher", "Banewhip Punisher", ['2', 'B'], ['B'], "Creature", "Human Warrior", "HOU", "Uncommon", 59, 65593)
# mixup end
BontusLastReckoning = Card("bontus_last_reckoning", "Bontu's Last Reckoning", ['1', 'B', 'B'], ['B'], "Sorcery", "", "HOU", "Rare", 60, 65597)
CarrionScreecher = Card("carrion_screecher", "Carrion Screecher", ['3', 'B'], ['B'], "Creature", "Zombie Bird", "HOU", "Common", 61, 65599)
Doomfall = Card("doomfall", "Doomfall", ['2', 'B'], ['B'], "Sorcery", "", "HOU", "Uncommon", 62, 65601)
Dreamstealer = Card("dreamstealer", "Dreamstealer", ['2', 'B'], ['B'], "Creature", "Human Wizard", "HOU", "Rare", 63, 65603)
GrislySurvivor = Card("grisly_survivor", "Grisly Survivor", ['2', 'B'], ['B'], "Creature", "Minotaur Warrior", "HOU", "Common", 64, 65605)
HourofGlory = Card("hour_of_glory", "Hour of Glory", ['3', 'B'], ['B'], "Instant", "", "HOU", "Rare", 65, 65607)
KhenraEternal = Card("khenra_eternal", "Khenra Eternal", ['1', 'B'], ['B'], "Creature", "Zombie Jackal Warrior", "HOU", "Common", 66, 65609)
LethalSting = Card("lethal_sting", "Lethal Sting", ['2', 'B'], ['B'], "Sorcery", "", "HOU", "Common", 67, 65611)
LilianasDefeat = Card("lilianas_defeat", "Liliana's Defeat", ['B'], ['B'], "Sorcery", "", "HOU", "Uncommon", 68, 65613)
LurchingRotbeast = Card("lurching_rotbeast", "Lurching Rotbeast", ['3', 'B'], ['B'], "Creature", "Zombie Beast", "HOU", "Common", 69, 65615)
MaraudingBoneslasher = Card("marauding_boneslasher", "Marauding Boneslasher", ['2', 'B'], ['B'], "Creature", "Zombie Minotaur", "HOU", "Common", 70, 65617)
MercilessEternal = Card("merciless_eternal", "Merciless Eternal", ['2', 'B'], ['B'], "Creature", "Zombie Cleric", "HOU", "Uncommon", 71, 65619)
MoaningWall = Card("moaning_wall", "Moaning Wall", ['2', 'B'], ['B'], "Creature", "Zombie Wall", "HOU", "Common", 72, 65621)
RazakeththeFoulblooded = Card("razaketh_the_foulblooded", "Razaketh, the Foulblooded", ['5', 'B', 'B', 'B'], ['B'], "Legendary Creature", "Demon", "HOU", "Mythic Rare", 73, 65623)
RazakethsRite = Card("razakeths_rite", "Razaketh's Rite", ['3', 'B', 'B'], ['B'], "Sorcery", "", "HOU", "Uncommon", 74, 65625)
RuinRat = Card("ruin_rat", "Ruin Rat", ['1', 'B'], ['B'], "Creature", "Rat", "HOU", "Common", 75, 65627)
ScroungerofSouls = Card("scrounger_of_souls", "Scrounger of Souls", ['4', 'B'], ['B'], "Creature", "Horror", "HOU", "Common", 76, 65629)
TormentofHailfire = Card("torment_of_hailfire", "Torment of Hailfire", ['X', 'B', 'B'], ['B'], "Sorcery", "", "HOU", "Rare", 77, 65631)
TormentofScarabs = Card("torment_of_scarabs", "Torment of Scarabs", ['3', 'B'], ['B'], "Enchantment", "Aura Curse", "HOU", "Uncommon", 78, 65633)
TormentofVenom = Card("torment_of_venom", "Torment of Venom", ['2', 'B', 'B'], ['B'], "Instant", "", "HOU", "Common", 79, 65635)
VileManifestation = Card("vile_manifestation", "Vile Manifestation", ['1', 'B'], ['B'], "Creature", "Horror", "HOU", "Uncommon", 80, 65637)
WithoutWeakness = Card("without_weakness", "Without Weakness", ['1', 'B'], ['B'], "Instant", "", "HOU", "Common", 81, 65639)
WretchedCamel = Card("wretched_camel", "Wretched Camel", ['1', 'B'], ['B'], "Creature", "Zombie Camel", "HOU", "Common", 82, 65641)
Abrade = Card("abrade", "Abrade", ['1', 'R'], ['R'], "Instant", "", "HOU", "Uncommon", 83, 65643)
BlurofBlades = Card("blur_of_blades", "Blur of Blades", ['1', 'R'], ['R'], "Instant", "", "HOU", "Common", 84, 65645)
BurningFistMinotaur = Card("burningfist_minotaur", "Burning-Fist Minotaur", ['1', 'R'], ['R'], "Creature", "Minotaur Wizard", "HOU", "Uncommon", 85, 65647)
ChandrasDefeat = Card("chandras_defeat", "Chandra's Defeat", ['R'], ['R'], "Instant", "", "HOU", "Uncommon", 86, 65649)
ChaosMaw = Card("chaos_maw", "Chaos Maw", ['5', 'R', 'R'], ['R'], "Creature", "Hellion", "HOU", "Rare", 87, 65651)
CrashThrough = Card("crash_through", "Crash Through", ['R'], ['R'], "Sorcery", "", "HOU", "Common", 88, 65653)
DefiantKhenra = Card("defiant_khenra", "Defiant Khenra", ['1', 'R'], ['R'], "Creature", "Jackal Warrior", "HOU", "Common", 89, 65655)
EarthshakerKhenra = Card("earthshaker_khenra", "Earthshaker Khenra", ['1', 'R'], ['R'], "Creature", "Jackal Warrior", "HOU", "Rare", 90, 65657)
FerventPaincaster = Card("fervent_paincaster", "Fervent Paincaster", ['2', 'R'], ['R'], "Creature", "Human Wizard", "HOU", "Uncommon", 91, 65659)
FirebrandArcher = Card("firebrand_archer", "Firebrand Archer", ['1', 'R'], ['R'], "Creature", "Human Archer", "HOU", "Common", 92, 65661)
FrontlineDevastator = Card("frontline_devastator", "Frontline Devastator", ['3', 'R'], ['R'], "Creature", "Zombie Minotaur Warrior", "HOU", "Common", 93, 65663)
InfernoJet = Card("inferno_jet", "Inferno Jet", ['5', 'R'], ['R'], "Sorcery", "", "HOU", "Uncommon", 99, 65673)
KhenraScrapper = Card("khenra_scrapper", "Khenra Scrapper", ['2', 'R'], ['R'], "Creature", "Jackal Warrior", "HOU", "Common", 100, 65675)
KindledFury = Card("kindled_fury", "Kindled Fury", ['R'], ['R'], "Instant", "", "HOU", "Common", 101, 65677)
Magmaroth = Card("magmaroth", "Magmaroth", ['3', 'R'], ['R'], "Creature", "Elemental", "HOU", "Uncommon", 102, 65679)
# mixup start
ThornedMoloch = Card("thorned_moloch", "Thorned Moloch", ['2', 'R'], ['R'], "Creature", "Lizard", "HOU", "Common", 108, 65665)
HazoretsUndyingFury = Card("hazorets_undying_fury", "Hazoret's Undying Fury", ['4', 'R', 'R'], ['R'], "Sorcery", "", "HOU", "Rare", 96, 65667)
HourofDevastation = Card("hour_of_devastation", "Hour of Devastation", ['3', 'R', 'R'], ['R'], "Sorcery", "", "HOU", "Rare", 97, 65669)
ImminentDoom = Card("imminent_doom", "Imminent Doom", ['2', 'R'], ['R'], "Enchantment", "", "HOU", "Rare", 98, 65671)
ManticoreEternal = Card("manticore_eternal", "Manticore Eternal", ['3', 'R', 'R'], ['R'], "Creature", "Zombie Manticore", "HOU", "Uncommon", 103, 65681)
NehebtheEternal = Card("neheb_the_eternal", "Neheb, the Eternal", ['3', 'R', 'R'], ['R'], "Legendary Creature", "Zombie Minotaur Warrior", "HOU", "Mythic Rare", 104, 65683)
OpenFire = Card("open_fire", "Open Fire", ['2', 'R'], ['R'], "Instant", "", "HOU", "Common", 105, 65685)
PuncturingBlow = Card("puncturing_blow", "Puncturing Blow", ['2', 'R', 'R'], ['R'], "Sorcery", "", "HOU", "Common", 106, 65687)
SandStrangler = Card("sand_strangler", "Sand Strangler", ['3', 'R'], ['R'], "Creature", "Beast", "HOU", "Uncommon", 107, 65689)
GraniticTitan = Card("granitic_titan", "Granitic Titan", ['4', 'R', 'R'], ['R'], "Creature", "Elemental", "HOU", "Common", 95, 65691)
GildedCerodon = Card("gilded_cerodon", "Gilded Cerodon", ['4', 'R'], ['R'], "Creature", "Beast", "HOU", "Common", 94, 65693)
WildfireEternal = Card("wildfire_eternal", "Wildfire Eternal", ['3', 'R'], ['R'], "Creature", "Zombie Jackal Cleric", "HOU", "Rare", 109, 65695)
Ambuscade = Card("ambuscade", "Ambuscade", ['2', 'G'], ['G'], "Instant", "", "HOU", "Common", 110, 65697)
BeneaththeSands = Card("beneath_the_sands", "Beneath the Sands", ['2', 'G'], ['G'], "Sorcery", "", "HOU", "Common", 111, 65699)
BitterbowSharpshooters = Card("bitterbow_sharpshooters", "Bitterbow Sharpshooters", ['4', 'G'], ['G'], "Creature", "Jackal Archer", "HOU", "Common", 112, 65701)
DevoteeofStrength = Card("devotee_of_strength", "Devotee of Strength", ['2', 'G'], ['G'], "Creature", "Naga Wizard", "HOU", "Uncommon", 113, 65703)
DuneDiviner = Card("dune_diviner", "Dune Diviner", ['2', 'G'], ['G'], "Creature", "Naga Cleric", "HOU", "Uncommon", 114, 65705)
FeralProwler = Card("feral_prowler", "Feral Prowler", ['1', 'G'], ['G'], "Creature", "Cat", "HOU", "Common", 115, 65707)
FrilledSandwalla = Card("frilled_sandwalla", "Frilled Sandwalla", ['G'], ['G'], "Creature", "Lizard", "HOU", "Common", 116, 65709)
GiftofStrength = Card("gift_of_strength", "Gift of Strength", ['1', 'G'], ['G'], "Instant", "", "HOU", "Common", 117, 65711)
HarrierNaga = Card("harrier_naga", "Harrier Naga", ['2', 'G'], ['G'], "Creature", "Naga Warrior", "HOU", "Common", 118, 65713)
HopeTender = Card("hope_tender", "Hope Tender", ['1', 'G'], ['G'], "Creature", "Human Druid", "HOU", "Uncommon", 119, 65717)
HourofPromise = Card("hour_of_promise", "Hour of Promise", ['4', 'G'], ['G'], "Sorcery", "", "HOU", "Rare", 120, 65715)
LifeGoesOn = Card("life_goes_on", "Life Goes On", ['G'], ['G'], "Instant", "", "HOU", "Common", 121, 65719)
MajesticMyriarch = Card("majestic_myriarch", "Majestic Myriarch", ['4', 'G'], ['G'], "Creature", "Chimera", "HOU", "Mythic Rare", 122, 65721)
NissasDefeat = Card("nissas_defeat", "Nissa's Defeat", ['2', 'G'], ['G'], "Sorcery", "", "HOU", "Uncommon", 123, 65723)
OasisRitualist = Card("oasis_ritualist", "Oasis Ritualist", ['3', 'G'], ['G'], "Creature", "Naga Druid", "HOU", "Common", 124, 65725)
Overcome = Card("overcome", "Overcome", ['3', 'G', 'G'], ['G'], "Sorcery", "", "HOU", "Uncommon", 125, 65727)
PrideSovereign = Card("pride_sovereign", "Pride Sovereign", ['2', 'G'], ['G', 'W'], "Creature", "Cat", "HOU", "Rare", 126, 65729)
QuarryBeetle = Card("quarry_beetle", "Quarry Beetle", ['4', 'G'], ['G'], "Creature", "Insect", "HOU", "Uncommon", 127, 65731)
RampagingHippo = Card("rampaging_hippo", "Rampaging Hippo", ['4', 'G', 'G'], ['G'], "Creature", "Hippo", "HOU", "Common", 128, 65733)
RamunapExcavator = Card("ramunap_excavator", "Ramunap Excavator", ['2', 'G'], ['G'], "Creature", "Naga Cleric", "HOU", "Rare", 129, 65735)
RamunapHydra = Card("ramunap_hydra", "Ramunap Hydra", ['3', 'G'], ['G'], "Creature", "Snake Hydra", "HOU", "Rare", 130, 65737)
ResilientKhenra = Card("resilient_khenra", "Resilient Khenra", ['1', 'G'], ['G'], "Creature", "Jackal Wizard", "HOU", "Rare", 131, 65739)
RhonassLastStand = Card("rhonass_last_stand", "Rhonas's Last Stand", ['G', 'G'], ['G'], "Sorcery", "", "HOU", "Rare", 132, 65741)
RhonassStalwart = Card("rhonass_stalwart", "Rhonas's Stalwart", ['1', 'G'], ['G'], "Creature", "Human Warrior", "HOU", "Common", 133, 65743)
SidewinderNaga = Card("sidewinder_naga", "Sidewinder Naga", ['2', 'G'], ['G'], "Creature", "Naga Warrior", "HOU", "Common", 134, 65745)
SifterWurm = Card("sifter_wurm", "Sifter Wurm", ['5', 'G', 'G'], ['G'], "Creature", "Wurm", "HOU", "Uncommon", 135, 65747)
TenaciousHunter = Card("tenacious_hunter", "Tenacious Hunter", ['2', 'G', 'G'], ['G'], "Creature", "Crocodile", "HOU", "Uncommon", 136, 65749)
UncagetheMenagerie = Card("uncage_the_menagerie", "Uncage the Menagerie", ['X', 'G', 'G'], ['G'], "Sorcery", "", "HOU", "Mythic Rare", 137, 65751)
BloodwaterEntity = Card("bloodwater_entity", "Bloodwater Entity", ['1', 'U', 'R'], ['U', 'R'], "Creature", "Elemental", "HOU", "Uncommon", 138, 65753)
# START God mixup
TheScorpionGod = Card("the_scorpion_god", "The Scorpion God", ['3', 'B', 'R'], ['B', 'R'], "Legendary Creature", "God", "HOU", "Mythic Rare", 146, 65755)  # WRONG: was 65769
TheLocustGod = Card("the_locust_god", "The Locust God", ['4', 'U', 'R'], ['U', 'R'], "Legendary Creature", "God", "HOU", "Mythic Rare", 139, 65757)  # WRONG: was 65755
NicolBolasGodPharaoh = Card("nicol_bolas_godpharaoh", "Nicol Bolas, God-Pharaoh", ['4', 'U', 'B', 'R'], ['U', 'B', 'R'], "Legendary Planeswalker", "Bolas", "HOU", "Mythic Rare", 140, 65759)  # WRONG: was 65757
ObeliskSpider = Card("obelisk_spider", "Obelisk Spider", ['1', 'B', 'G'], ['B', 'G'], "Creature", "Spider", "HOU", "Uncommon", 141, 65761)  # WRONG: was 65759
ResoluteSurvivors = Card("resolute_survivors", "Resolute Survivors", ['1', 'R', 'W'], ['W', 'R'], "Creature", "Human Warrior", "HOU", "Uncommon", 142, 65763)  # WRONG: was 65761
RiverHoopoe = Card("river_hoopoe", "River Hoopoe", ['G', 'U'], ['U', 'G'], "Creature", "Bird", "HOU", "Uncommon", 143, 65765)  # WRONG: was 65763
SamuttheTested = Card("samut_the_tested", "Samut, the Tested", ['2', 'R', 'G'], ['R', 'G'], "Legendary Planeswalker", "Samut", "HOU", "Mythic Rare", 144, 65767)  # WRONG: was 65765
TheScarabGod = Card("the_scarab_god", "The Scarab God", ['3', 'U', 'B'], ['U', 'B'], "Legendary Creature", "God", "HOU", "Mythic Rare", 145, 65769)  # WRONG: was 65767
# END God mixup
UnravelingMummy = Card("unraveling_mummy", "Unraveling Mummy", ['1', 'W', 'B'], ['W', 'B'], "Creature", "Zombie", "HOU", "Uncommon", 147, 65771)
Farm = Card("farm", "Farm", ['2', 'W'], ['U', 'W'], "Instant", "", "HOU", "Uncommon", 148, 65773)
Market = Card("market", "Market", ['2', 'U'], ['U', 'W'], "Sorcery", "", "HOU", "Uncommon", 148, 65776)
Consign = Card("consign", "Consign", ['1', 'U'], ['B', 'U'], "Instant", "", "HOU", "Uncommon", 149, 65779)
Oblivion = Card("oblivion", "Oblivion", ['4', 'B'], ['B', 'U'], "Sorcery", "", "HOU", "Uncommon", 149, 65782)
Claim = Card("claim", "Claim", ['B'], ['R', 'B'], "Sorcery", "", "HOU", "Uncommon", 150, 65785)
Fame = Card("fame", "Fame", ['1', 'R'], ['R', 'B'], "Sorcery", "", "HOU", "Uncommon", 150, 65788)
Struggle = Card("struggle", "Struggle", ['2', 'R'], ['G', 'R'], "Instant", "", "HOU", "Uncommon", 151, 65791)
Survive = Card("survive", "Survive", ['1', 'G'], ['G', 'R'], "Sorcery", "", "HOU", "Uncommon", 151, 65794)
Appeal = Card("appeal", "Appeal", ['G'], ['W', 'G'], "Sorcery", "", "HOU", "Uncommon", 152, 65797)
Authority = Card("authority", "Authority", ['1', 'W'], ['W', 'G'], "Sorcery", "", "HOU", "Uncommon", 152, 65800)
Leave = Card("leave", "Leave", ['1', 'W'], ['W', 'R'], "Instant", "", "HOU", "Rare", 153, 65803)
Chance = Card("chance", "Chance", ['3', 'R'], ['W', 'R'], "Sorcery", "", "HOU", "Rare", 153, 65806)
Reason = Card("reason", "Reason", ['U'], ['U', 'G'], "Sorcery", "", "HOU", "Rare", 154, 65809)
Believe = Card("believe", "Believe", ['4', 'G'], ['U', 'G'], "Sorcery", "", "HOU", "Rare", 154, 65812)
Grind = Card("grind", "Grind", ['1', 'B'], ['B', 'W'], "Sorcery", "", "HOU", "Rare", 155, 65815)
Dust = Card("dust", "Dust", ['3', 'W'], ['B', 'W'], "Sorcery", "", "HOU", "Rare", 155, 65818)
Refuse = Card("refuse", "Refuse", ['3', 'R'], ['R', 'U'], "Instant", "", "HOU", "Rare", 156, 65821)
Cooperate = Card("cooperate", "Cooperate", ['2', 'U'], ['R', 'U'], "Instant", "", "HOU", "Rare", 156, 65824)
Driven = Card("driven", "Driven", ['1', 'G'], ['G', 'B'], "Sorcery", "", "HOU", "Rare", 157, 65827)
Despair = Card("despair", "Despair", ['1', 'B'], ['G', 'B'], "Sorcery", "", "HOU", "Rare", 157, 65830)
AbandonedSarcophagus = Card("abandoned_sarcophagus", "Abandoned Sarcophagus", ['3'], [], "Artifact", "", "HOU", "Rare", 158, 65833)
CrookofCondemnation = Card("crook_of_condemnation", "Crook of Condemnation", ['2'], [], "Artifact", "", "HOU", "Uncommon", 159, 65835)
DaggeroftheWorthy = Card("dagger_of_the_worthy", "Dagger of the Worthy", ['2'], [], "Artifact", "Equipment", "HOU", "Uncommon", 160, 65837)
GodPharaohsGift = Card("godpharaohs_gift", "God-Pharaoh's Gift", ['7'], [], "Artifact", "", "HOU", "Rare", 161, 65839)
GravenAbomination = Card("graven_abomination", "Graven Abomination", ['3'], [], "Artifact Creature", "Horror", "HOU", "Common", 162, 65841)
HollowOne = Card("hollow_one", "Hollow One", ['5'], [], "Artifact Creature", "Golem", "HOU", "Rare", 163, 65843)
Manalith = Card("manalith", "Manalith", ['3'], [], "Artifact", "", "HOU", "Common", 164, 65845)
MirageMirror = Card("mirage_mirror", "Mirage Mirror", ['3'], [], "Artifact", "", "HOU", "Rare", 165, 65847)
SunsetPyramid = Card("sunset_pyramid", "Sunset Pyramid", ['2'], [], "Artifact", "", "HOU", "Uncommon", 166, 65849)
TravelersAmulet = Card("travelers_amulet", "Traveler's Amulet", ['1'], [], "Artifact", "", "HOU", "Common", 167, 65851)
WallofForgottenPharaohs = Card("wall_of_forgotten_pharaohs", "Wall of Forgotten Pharaohs", ['2'], [], "Artifact Creature", "Wall", "HOU", "Common", 168, 65853)
# wat
CryptoftheEternals = Card("crypt_of_the_eternals", "Crypt of the Eternals", [], ['U', 'B', 'R'], "Land", "", "HOU", "Uncommon", 169, 65959)
# end wat
DesertoftheFervent = Card("desert_of_the_fervent", "Desert of the Fervent", [], ['R'], "Land", "Desert", "HOU", "Common", 170, 65857)
DesertoftheGlorified = Card("desert_of_the_glorified", "Desert of the Glorified", [], ['B'], "Land", "Desert", "HOU", "Common", 171, 65859)
DesertoftheIndomitable = Card("desert_of_the_indomitable", "Desert of the Indomitable", [], ['G'], "Land", "Desert", "HOU", "Common", 172, 65861)
DesertoftheMindful = Card("desert_of_the_mindful", "Desert of the Mindful", [], ['U'], "Land", "Desert", "HOU", "Common", 173, 65863)
DesertoftheTrue = Card("desert_of_the_true", "Desert of the True", [], ['W'], "Land", "Desert", "HOU", "Common", 174, 65865)
DunesoftheDead = Card("dunes_of_the_dead", "Dunes of the Dead", [], [], "Land", "Desert", "HOU", "Uncommon", 175, 65867)
EndlessSands = Card("endless_sands", "Endless Sands", [], [], "Land", "Desert", "HOU", "Rare", 176, 65869)
HashepOasis = Card("hashep_oasis", "Hashep Oasis", [], ['G'], "Land", "Desert", "HOU", "Uncommon", 177, 65871)
HostileDesert = Card("hostile_desert", "Hostile Desert", [], [], "Land", "Desert", "HOU", "Rare", 178, 65873)
IfnirDeadlands = Card("ifnir_deadlands", "Ifnir Deadlands", [], ['B'], "Land", "Desert", "HOU", "Uncommon", 179, 65875)
IpnuRivulet = Card("ipnu_rivulet", "Ipnu Rivulet", [], ['U'], "Land", "Desert", "HOU", "Uncommon", 180, 65877)
RamunapRuins = Card("ramunap_ruins", "Ramunap Ruins", [], ['R'], "Land", "Desert", "HOU", "Uncommon", 181, 65879)
ScavengerGrounds = Card("scavenger_grounds", "Scavenger Grounds", [], [], "Land", "Desert", "HOU", "Rare", 182, 65881)
ShefetDunes = Card("shefet_dunes", "Shefet Dunes", [], ['W'], "Land", "Desert", "HOU", "Uncommon", 183, 65883)
SurvivorsEncampment = Card("survivors_encampment", "Survivors' Encampment", [], [], "Land", "Desert", "HOU", "Common", 184, 65885)
Plains = Card("plains", "Plains", [], ['W'], "Basic Land", "Plains", "HOU", "Basic Land", 185, 65887)
Island = Card("island", "Island", [], ['U'], "Basic Land", "Island", "HOU", "Basic Land", 186, 65889)
Swamp = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "HOU", "Basic Land", 187, 65891)
Mountain = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "HOU", "Basic Land", 188, 65893)
Forest = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "HOU", "Basic Land", 189, 65895)
Plains2 = Card("plains", "Plains", [], ['W'], "Basic Land", "Plains", "HOU", "Basic Land", 190, 65897)
Plains3 = Card("plains", "Plains", [], ['W'], "Basic Land", "Plains", "HOU", "Basic Land", 191, 65899)
Island2 = Card("island", "Island", [], ['U'], "Basic Land", "Island", "HOU", "Basic Land", 192, 65901)
Island3 = Card("island", "Island", [], ['U'], "Basic Land", "Island", "HOU", "Basic Land", 193, 65903)
Swamp2 = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "HOU", "Basic Land", 194, 65905)
Swamp3 = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "HOU", "Basic Land", 195, 65907)
Mountain2 = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "HOU", "Basic Land", 196, 65909)
Mountain3 = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "HOU", "Basic Land", 197, 65911)
Forest2 = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "HOU", "Basic Land", 198, 65913)
Forest3 = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "HOU", "Basic Land", 199, 65915)
# start mixup
NissaGenesisMage = Card("nissa_genesis_mage", "Nissa, Genesis Mage", ['5', 'G', 'G'], ['G'], "Legendary Planeswalker", "Nissa", "HOU", "Mythic Rare", 200, 65937)
AvidReclaimer = Card("avid_reclaimer", "Avid Reclaimer", ['2', 'G'], ['G', 'U'], "Creature", "Human Druid", "HOU", "Uncommon", 201, 65939)
BrambleweftBehemoth = Card("brambleweft_behemoth", "Brambleweft Behemoth", ['4', 'G', 'G'], ['G'], "Creature", "Elemental", "HOU", "Common", 202, 65941)
NissasEncouragement = Card("nissas_encouragement", "Nissa's Encouragement", ['4', 'G'], ['G'], "Sorcery", "", "HOU", "Rare", 203, 65943)
WoodlandStream = Card("woodland_stream", "Woodland Stream", [], ['G', 'U'], "Land", "", "HOU", "Common", 204, 65945)
NicolBolastheDeceiver = Card("nicol_bolas_the_deceiver", "Nicol Bolas, the Deceiver", ['5', 'U', 'B', 'R'], ['U', 'B', 'R'], "Legendary Planeswalker", "Bolas", "HOU", "Mythic Rare", 205, 65947)
WaspoftheBitterEnd = Card("wasp_of_the_bitter_end", "Wasp of the Bitter End", ['1', 'B'], ['B'], "Creature", "Insect Horror", "HOU", "Uncommon", 206, 65949)
ZealotoftheGodPharaoh = Card("zealot_of_the_godpharaoh", "Zealot of the God-Pharaoh", ['3', 'R'], ['R'], "Creature", "Minotaur Archer", "HOU", "Common", 207, 65951)
VisageofBolas = Card("visage_of_bolas", "Visage of Bolas", ['4'], ['U', 'B', 'R'], "Artifact", "", "HOU", "Rare", 208, 65953)
CinderBarrens = Card("cinder_barrens", "Cinder Barrens", [], ['B', 'R'], "Land", "", "HOU", "Common", 209, 65955)
# end mixup

clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
HourOfDevastation = Set("hour_of_devastation", cards=clsmembers)

