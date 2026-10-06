# Time to Build: next steps

Working list for `DataCenterTTB.tex`. Not part of the paper.

## Data

- Received the Castilla-La Mancha working file (`centros_datos_expedientes_CLM.xlsx`, see `clm_workbook_notes.md`). It documents the method and adds resolution dates (8–14 days before gazette) but not the Aragón clocks. Ask for the Aragón and Madrid workbooks (`centros_datos_expedientes_AR.xlsx`, `_MA.xlsx` if they follow the same naming) and the `datos/crudos/boletines/` PDFs for Amazon and Microsoft.
- Use the REE access-request status page listed in the workbook's `Fuentes` to date the grid step for Amazon, Microsoft and Meta.
- Reconcile the census Amazon AAI row (`ARF-71`, Feb 2020) with the official Aragón page (DIA+AAI 27 Jul 2020). Read the BOA document behind `ARF-71`.
- Re-merge Amazon (`AR-P01`, `AR-P01-2`, `AR-P01-3`, `AR-P02`) and Microsoft (`AR-P03`, `AR-P06-2`, `AR-P01-4`, `AR-P08-3`) rows once the authors confirm their grouping.

## Cases

- Amazon expansion: watch for energisation of the Huesca and Villanueva buildings (staging plan says Q2 2027). That will be the second completed greenfield observation and the test of whether the 3-year fast track repeats under a congested grid.
- Meta: watch for the Talavera building licence and any urbanisation contract. Read the third environmental monitoring report if it appears on the CLM PSI page.
- Microsoft Aragón: definitive PIGA date; outcome of the 349 objections; CNMC/REE decision on the 300 MW per site requests.
- Calatorao: AAI decision and first municipal licence; whether Q2 2026 works start held.
- Add one Madrid colocation campus with a full permit stack (Data4 Alcobendas or Digital Realty MAD4) by pulling BOCM and municipal records, to give a clean industrial-land clock with dates rather than press.

## Out-of-sample comparators

- Portugal and France: first pass done, see `portugal_france_first_pass.md`. Spot-check Fouju, Start Campus and Microsoft Alsace dates against primary documents before adding to the paper. Ireland (Dublin moratorium) still open.
- Compare with US time-to-build estimates already in `us_dc_boom_macro_ballpark.tex`.

## Regulation to track

- Final text of the Royal Decree on data-centre sustainability (consultation closed 10 Sep 2026): does the 6-month lapse for unconnected permits survive; transition for Meta and Microsoft.
- Orden TED setting the demand-capacity concurso criteria (still unpublished as of Sep 2026).
- Approval of the 2025–2030 grid plan and which Aragón / Madrid nodes get new capacity.
- Ley de Industria "proyectos industriales estratégicos" fast track, if enacted.

## Modelling

- Replace the single SpainDC delay with two tracks (industrial land vs greenfield) and a grid indicator; re-run the 2026–2030 GFCF path in `ai_capital_report_spaindc.tex`.
- Put Meta in 2028+, Microsoft Aragón in 2028–2030+, Calatorao not before 2027 in `ai_capital_report_upside.tex`.
