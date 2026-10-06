"""Stage 1 named assumptions. Change numbers here, not in the builder.

Units in the VLW object are millions of current dollars. Rates are annual.
D3b (17 Sep 2026): owned hyperscale campuses are treated as rentals, so
structures and owner-furnished power/cooling sit in DC_facilities.
"""

# --- model ---
BETA = 0.96
R = 1.0 / BETA - 1.0  # 0.041666...

# --- sector indices, 0-based, VLW 37 then 38=DC_facilities, 39=Compute ---
UTIL = 1
CONSTR = 2
MACH = 7
COMP = 8
ELEC = 9
WT = 22
RT = 23
TRANSP = 24
INFO = 25
RE = 27
PT = 28
ADMIN = 30
DC = 37
CMP = 38
N37 = 37
N39 = 39

SECTOR_NAMES_37 = [
    "Mining_Oil_and_Gas",
    "Utilities",
    "Construction",
    "Wood",
    "Minerals",
    "Primary_Metals",
    "Fabricated_Metals",
    "Machinery",
    "Computers",
    "Electrical",
    "Vehicles",
    "Transport",
    "Furniture",
    "Misc_Mfg",
    "Food_Mfg",
    "Textile",
    "Apparel",
    "Paper",
    "Printing",
    "Petroleum",
    "Chemical",
    "Plastics",
    "Wholesale_Trade",
    "Retail",
    "Transp_and_Wareh",
    "Info",
    "Finance",
    "Real_estate",
    "Prof_Tech",
    "Mgmt",
    "Admin",
    "Educ",
    "Health",
    "Arts",
    "Accom",
    "Food_Services",
    "Other",
]
SECTOR_NAMES_39 = SECTOR_NAMES_37 + ["DC_facilities", "Compute"]

# MATLAB LoadIOMat_37sec.m Depindcell: 1-based FA industry indices (63 sheets).
DEPIND = [
    (3, 5),
    6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
    (29, 36),
    (37, 40),
    (41, 45),
    (46, 47),
    (48, 50),
    51,
    (52, 53),
    54,
    (55, 58),
    (59, 60),
    61,
    62,
    63,
]

# --- facility capital (one stock from C30 construction, split shell / plant) ---
# Census C30 construction cost includes installed mechanical and electrical
# plant and excludes racks and servers. Split the flow with the Turner &
# Townsend 2025 US cost index: shell and architectural 14%, mechanical 22%,
# electrical 54%, general conditions 10% (pro-rated) -> shell ~0.15.
FACILITY_SHELL_SHARE = 0.15
DELTA_SHELL = 0.0247  # BEA geometric rate, office buildings (36-year life)
DELTA_PLANT = 0.10  # borrowed BEA industrial-equipment rate; alternatives in stage1_plan.md §2.6
DELTA_IT = 0.30  # near BEA implied computer rate in 514 (~0.33)
DELTA_SOFT = 0.22  # slower than BEA IPP (~0.32); small stock, low leverage

# Pre-sample C30 growth used only to start the 2014 PIM (series begins Jan 2014).
# Weight of this anchor in the stock: ~1/3 in 2018, <1/10 from 2022 on.
C30_PRESAMPLE_G = 0.10

# Orchestration / systems software of Compute vs its server stock. Hosting's
# official software stock is 3–4× servers (search, social, other products) and
# is not this object. 0.04 is a small explicit add-on (old 8/210 ≈ 0.038);
# band 0 and 0.10 is reported, not used. See notes/us-national-accounts/dc_it_stock.tex.
SOFT_TO_IT_RATIO = 0.04

# --- electricity: LBNL TWh (all US data centers) × node share × price ---
# 2018 and 2023–24 TWh are published (Shehabi 2024; Smith 2025 update).
# 2022 ≈ 145 is interpolated in our notes, not a published LBNL point.
# Node share: 0.65 in 2018 (assumed); 0.74 in 2023 is LBNL's share of *servers*
# (they also say >90% of server energy). 2022/2024 interpolated toward 85% in 2028.
LBNL_TWH = {2018: 76.0, 2022: 145.0, 2023: 176.0, 2024: 192.0}
NODE_ENERGY_SHARE = {2018: 0.65, 2022: 0.72, 2023: 0.74, 2024: 0.76}
ELEC_PRICE_PER_KWH = 0.085  # 2018 midpoint industrial~6.8c / commercial~10.5c; held
LBNL_TWH_2018 = LBNL_TWH[2018]  # alias
NODE_ENERGY_SHARE_2018 = NODE_ENERGY_SHARE[2018]

# Facility other-M and labour relative to electricity (notes facility services:
# elec 25–30%, other M ~10%, labour ~5%).
FACILITY_OTHER_M_OVER_ELEC = 10.0 / 27.0
FACILITY_L_OVER_ELEC = 5.0 / 27.0

# Compute other intermediates and labour as shares of Compute GO (notes all-in
# computing: other M 5–8%, labour 3–5%), after powered-space is its own cell.
COMPUTE_OTHER_M_SHARE = 0.06
COMPUTE_L_SHARE = 0.04
COMPUTE_OTHER_M_INFO_SHARE = 2.0 / 3.0  # rest from Prof_Tech

# --- D5 row ---
OWN_USE_INFO_SHARE = 0.30
LABS_PT_SHARE = 0.15
CONS_COMPUTE_SHARE = 0.10

# --- D6 Compute invmat (servers; PEQ retail is PCs, not racks) ---
COMPUTERS_PRODUCERS_SHARE = 0.92
IT_MARGIN_WT = 0.05
IT_MARGIN_TRANSP = 0.02
IT_MARGIN_RT = 0.01

# Colo tenant rent previously in RE→Info. 2017 detail Before 518200←531ORE
# $5.45bn, scaled by C30 2018/2017.
COLO_RENT_2017_M = 5450.0
C30_SCALE_RENT = 6928.8 / 4661.8

# Facility construction currently recorded in Info vs Real_estate invmat.
STRUCTURES_FROM_INFO_SHARE = 0.75  # remainder from Real_estate (colo developers)

# Server-like FA types (not PCs/printers/terminals). Networking EP20 is a check.
SERVER_ASSET_CODES = ("EP1A", "EP1G", "EP1H")
PC_ASSET_CODES = ("EP1B",)
NETWORK_ASSET_CODES = ("EP20",)
COMPUTER_ASSET_CODES = ("EP1A", "EP1B", "EP1C", "EP1D", "EP1E", "EP1F", "EP1G", "EP1H")
SOFTWARE_ASSET_CODES = ("ENS1", "ENS2", "ENS3")
INFO_FA_CODES = ("5110", "5120", "5130", "5140")
HOSTING_FA = ("5140",)  # baseline: data processing / hosting / internet publishing
PUBLISHING_FA = ("5110",)  # Microsoft-inclusive ceiling when added to HOSTING_FA
PUBLISH_AND_HOSTING_FA = HOSTING_FA + PUBLISHING_FA  # check only, not the SS
