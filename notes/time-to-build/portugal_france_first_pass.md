# Portugal and France: first pass on data-centre project lifecycles

Research note, September 2026. Companion to `DataCenterTTB.tex`. Sources are web research by two subagents (Grok 4.6); dates carry a link and should be spot-checked before use in the paper. Unverified items are flagged.

## Purpose

Test whether the seven gates and the two-track clock found for Spain (about 3 years announcement-to-service with public land, spare grid capacity and an uncontested file; 5–7 years otherwise) hold in two neighbouring jurisdictions.

## Step mapping

| Spain step | Portugal | France |
| --- | --- | --- |
| 1. Regional strategic label (DIGA/DIR) | National PIN (*Potencial Interesse Nacional*, [DL 154/2013](https://portugal.gov.pt/pt/gc22/comunicacao/noticias/sines-recebera-o-maior-investimento-estrangeiro-das-ultimas-decadas)): CPAI decides in 30 days; process manager, deadlines cut up to half, 90-day EIA clock. Does not rezone or reserve MW. | PINM (*projet d'intérêt national majeur*) extended to data centres by [loi 2026-403 of 26 May 2026](https://www.conseil-constitutionnel.fr/decision/2026/2026903DC.htm): designation by decree, no numeric thresholds; prefect instructs the building permit, faster PLU compatibility, RTE capacity reservation. ZAN exemption struck down. No DC decree issued yet. Plus the Feb 2025 list of [35 pre-qualified sites](https://www.elysee.fr/admin/upload/default/0001/17/23058aa82354edfd8a30ff11b57b36f2801504f3.pdf). |
| 2. Regional land-use plan (PIGA/PSI) | No regional layer. Municipal PDM; a full revision averages over five years. Public industrial estates (ZILS Sines, aicep Global Parques) skip it: investor buys a 50-year surface right. | PLU/PLUi held by commune or EPCI; *déclaration de projet emportant mise en compatibilité* (6–18 months) when the use is not allowed; prefect can take over under PINM. ZAN still applies. |
| 3. Environmental permits | APA runs the EIA; DIA 150 days (90 for PIN), tacit if silent, valid 4 years. Campus not automatically listed; large generator parks trip Annex II. PCIP environmental licence for generators, no expiry since DL 11/2023. | ICPE regime on auxiliaries: generators >50 MW → *autorisation environnementale* (prefect, DREAL). Statutory ~9 months pre-2024; since Oct 2024 fixed 3-month consultation then ~2 months. Real large files 9–18 months (trade press). |
| 4. Land assembly | Skipped on ZILS. Elsewhere RAN/REN declassification (20-day binding opinion for RAN). | Incremental campuses on assembled land (Data4). State-packaged sites carry land EIA done. |
| 5. Grid connection | REN transmission, E-Redes distribution; DGEG oversight. Saturation handled by *zonas de grande procura* ([DL 80/2023](https://www.e-redes.pt/pt-pt/noticias/2024/01/08/informacao-prevista-no-dl-no-802023-sobre-capacidade-atribuida-nao-utilizada-na)): bond, unused-capacity sweep, competitive award; PIN ranks first. REN quotes up to 4 years for a 400 kV line. | RTE for 225/400 kV: study → PTF → convention. Connection 2–7 years (was 2–3). [CRE Fast Track](https://www.cre.fr/fileadmin/Documents/Deliberations/2025/250507_2025-120_Procedure_raccordement_Fast_track_annexe.pdf) (May 2025): State pre-reserves capacity on a few sites. "First ready, first served" from June 2026. |
| 6. Municipal licence | *Câmara* licence 120–200 days by floor area, tacit since DL 10/2024; *comunicação prévia* for some works. Minister (Oct 2025): legal deadlines routinely missed. | *Permis de construire* 3 months from complete file (mayor, or prefect under PINM). Third-party appeal window 2 months; merits 12–24 months; a stay can freeze works within months. |
| 7. Construction | Start Campus SIN01: works Apr 2022 → operation Q4 2024 (~30 months, 15 MW). SIN02 planned 24 months. | Data4 Marcoussis permits: 22–24 months permit-to-completion. |

Portugal has six gates in effect (no regional plan layer). France has all seven, with the State able to absorb steps 1, 2 and part of 5 under PINM or the Fast Track.

## Grid queues

- Portugal: Sines zone opened Sep 2023; 7.9 GVA of interest, 4.9 GVA bonded by 17 projects, reinforcements insufficient ([ECO](https://eco.sapo.pt/2023/11/20/17-projetos-reservam-direito-a-capacidade-eletrica-em-sines-no-ambito-do-despacho-do-bar-aberto/)). Continental call Feb–Mar 2026: 29 valid requests, 5.6 GW, mostly data centres ([ECO](https://eco.pt/2026/03/06/governo-recebe-29-pedidos-de-ligacao-a-rede-eletrica/)). Minister (Jan 2026): ~41 GW of informal requests ([Jornal Económico](https://jornaleconomico.sapo.pt/noticias/portugal-tem-40-gigas-de-projetos-a-espera-de-serem-ligados-a-rede/)). PDIRT 2025–2034 plans ~7 GVA of new Sines demand: a build programme, not spare capacity.
- France: RTE reserved ~5 GW / 40 projects at end-2024 and ~18 GW / 80 projects by May 2026; Île-de-France ~7 GW reserved ([RTE](https://www.rte-france.com/bases-electricite/consommation-electricite/essor-data-centers-france)). The "10 GW Île-de-France" figure in circulation is not RTE's.
- Spain (for reference): >43 GW of demand access rights vs 38.2 GW peak; first competitive call Jul 2025 → Feb 2026.

## Case clocks

| Case | Type | Start | Milestones | First MW | Elapsed |
| --- | --- | --- | --- | --- | --- |
| Start Campus SIN01, Sines (PT) | Public industrial land, PIN, EIA-exempt first hall, distribution-grid connection | PIN Mar 2021; announced 23 Apr 2021 | Case-by-case EIA exemption 17 Dec 2021; works 26 Apr 2022; water licence 8 Jun 2022 | Q4 2024 (14–26 MW) | ~43 months |
| Start Campus SIN02–06 (PT) | 1.2 GW campus on 400 kV | DIA 10 Aug 2023 | RECAPE Nov 2024; SIN02 works Feb 2026, finish 2027; campus "early 2030s" | not yet | >5 years and counting |
| Altice Covilhã (PT, historical) | Brownfield aerodrome | Announced 5 Feb 2011 | Works 21 Oct 2011 | 23 Sep 2013 | ~31 months |
| AtlasEdge LIS001 (PT) | Colocation, urban | Ground-break 24 Apr 2024 | | 28 Oct 2025 (~5 MW) | ~18 months |
| Equinix LS2 (PT) | Colocation, adjacent hall | Announced 4 Jun 2024 | | 2 Jun 2025 | ~12 months |
| Data4 Marcoussis (FR) | Incremental, assembled land | PC 7 Jul 2021 / 21 Feb 2022 | | DAACT 25 Jul 2023 / 15 Dec 2023 | 22–24 months per building |
| Campus IA Fouju (FR) | 1 GW greenfield, State Fast Track | Announced 6 Feb 2025 | CNDP Oct–Nov 2025; RTE Fast Track Jan 2026 (240 MW end-2027, 700 MW end-2029); enquête Apr–May 2026; PLU + prefect AE 23–29 Jul 2026; works Sep 2026 | planned end-2029 (company said 2028 in May 2025) | ~17 months to permits; 3.5–4.5 years to first MW if held |
| Microsoft Petit-Landau, Alsace (FR) | Greenfield, contested, new 400/225 kV substation | Announced 13 May 2024 | PLU procedure Dec 2024; PC filed Oct 2025; enquête Jun–Jul 2026 (80% of comments opposed); prefect expected Oct 2026 | planned 2030; full site 2032 | ~6 years |
| Sesterce Alixan (FR) | 40 MW, contested | PC 18 Dec 2025 | Appeal Feb 2026; PC stayed by TA Grenoble 10 Jul 2026; Conseil d'État pending | frozen | appeal → stay in ~7 months |
| AWS Paris region (FR) | Colocation | Announced 29 Sep 2016 | | GA 18 Dec 2017 | ~15 months |
| Microsoft Paris/Marseille (FR) | Colocation | Announced 3 Oct 2016 | | GA 14 Mar 2018 | ~17 months |

Sources: Start Campus ([government note 2021](https://portugal.gov.pt/pt/gc22/comunicacao/noticias/sines-recebera-o-maior-investimento-estrangeiro-das-ultimas-decadas), [APA process 3633](https://siaia.apambiente.pt/ProcessoAIA/Detalhes/3633), [company Aug 2024](https://www.startcampus.pt/press_release_august_2024_1gw), [Observador Jan 2026](https://observador.pt/2026/01/13/start-campus-avanca-em-fevereiro-com-segundo-edificio-do-centro-de-dados-de-sines/)); Fouju ([RTE Fast Track contract](https://lafibre.info/images/datacenter/202601_fouju_campus_ia_rte_raccordement_fasttrack_400000volts.pdf), [prefecture decisions](https://www.seine-et-marne.gouv.fr/Publications/Enquetes-publiques/FOUJU-PROJET-CAMPUS-IA/DECISIONS), [Le Parisien Aug 2026](https://www.leparisien.fr/seine-et-marne-77/data-centers-plus-cher-que-le-grand-paris-express-le-projet-de-campus-ia-geant-valide-en-seine-et-marne-11-08-2026-AUCLSXM7CFHOZFPLDLUHJSPRUI.php)); Microsoft Alsace ([Petit-Landau council](http://petit-landau.fr/wp-content/uploads/2016/01/PV-CM-7-juillet-2026.pdf), [L'Alsace Aug 2026](https://www.lalsace.fr/economie/2026/08/24/centre-de-donnees-un-avis-favorable-malgre-80-de-contributions-defavorables)); Sesterce ([ZDNet Jul 2026](https://www.zdnet.fr/actualites/coup-darret-pour-le-datacenter-sesterce-a-valence-498653.htm)); Data4 ([permit base](https://basedespermis.fr/autorisation-pc-0913632110030-2021-07-07), [MRAe 2023](https://www.mrae.developpement-durable.gouv.fr/IMG/pdf/2023-08-09_marcoussis_91__projet_extension_data_center4_avis_delibere_.pdf)).

## Reading against Spain

- The two-track pattern repeats. Fast track with State-packaged land and pre-reserved grid: Amazon Aragón 36 months, Start Campus first hall 43 months, Fouju 3.5–4.5 years planned. Contested greenfield with a new substation: Meta Talavera 54 months and no licence, Microsoft Aragón ~7 years planned, Microsoft Alsace ~6 years planned, Start Campus gigawatt phase >5 years and unbuilt.
- The fast Portuguese and French first halls are small (15–26 MW at Sines on a distribution connection; colocation halls of 5–10 MW in Lisbon and Paris). The gigawatt phases everywhere wait for transmission works. The "first MW" clock and the "campus" clock should be reported separately.
- Grid is the binding step in all three countries, and all three changed allocation rules in 2023–2026 (Spain concursos, Portugal zonas de grande procura, France Fast Track then first-ready-first-served). All three carry request queues far above plausible build (Spain 43 GW, Portugal 41 GW informal, France 18 GW reserved).
- France adds a step Spain lacks in practice: the third-party appeal against the building permit, which can stay a granted permit within months (Sesterce). Spain's equivalent litigation targets expropriation (Microsoft Puerto Venecia), not the licence.
- Portugal removes a step: no regional plan layer, and public industrial estates are the default location for large projects, so land assembly rarely appears.
- Construction of the first buildings is 22–30 months everywhere (Amazon 27, Data4 22–24, SIN01 30).

## Corrections to common claims found in the research

- Operação Influencer was November 2023, not 2024. The company says it did not move the campus target.
- Microsoft Alsace: EUR 4bn is France-wide; the campus is >EUR 2bn; first building 2030, not 2027–28; land is Petit-Landau and Hombourg.
- Fouju: no PINM decree requested; the Fast Track is an RTE/CRE instrument, not the PINM law.
- Data4's EUR 2bn expansion is PAR03 Nozay, not Marcoussis.
- Start Campus's "1.2 GW secured" is a company claim; ERSE documents cite 1,436 MVA allocated, mostly future transmission capacity under an exceptional procedure; SIN01 runs on 25–37.5 MVA of distribution.

## Unverified

- Sines surface-right date; Start Campus municipal licence dates for SIN02; Data4 zone 2 Nord environmental authorisation grant; outcome of the Fouju appeal announced by opponents; the Microsoft Alsace prefectoral decision (expected Oct 2026).
- Real-duration statistics for Portuguese municipal licences and French *autorisation environnementale* for data centres specifically.

## Next

- If used in the paper: one paragraph in the caveats or a short section "Out-of-sample checks" with the clock table above, after spot-checking the Fouju, Start Campus and Microsoft Alsace dates against the primary documents linked.
- Track: Fouju appeal; Microsoft Alsace prefect decision (Oct 2026); Start Campus SIN02 completion (2027); first PINM decree for a data centre; Portugal PNCD revision of the PIN regime (RCM 70/2026).
