---
article_id: 360025225652
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: 814293a00bd5931eab953a04d2480d270f33aa949902319678f97291a902386c
fetched_at: '2026-06-28T22:39:19.246245+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Código de Lançamento/Reflexo
  no TES Para ICMS Complementar/DIFAL + FECP
type: support-article
updated_at: '2021-09-28T19:15:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025225652-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%B3digo-de-Lan%C3%A7amento-Reflexo-no-TES-Para-ICMS-Complementar-DIFAL-FECP
---

**Dúvida**

Código de Lançamento/Reflexo na TES para ICMS Complementar/DIFAL + FECP

**Ambiente**Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Código de Lançamento/Reflexo na TES para ICMS Complementar/DIFAL + FECP

|  |  |
| --- | --- |
| **Produto:** | Microsiga Protheus |
| **Versões:** | 10, 11, e 12.1.7 |
| **Ocorrência:** | Preenchimento do Código de Reflexo para que as Bases/Alíquotas/Valores informados na ABA "Lançamentos de Apuração de ICMS" (MATA103) referente ao Diferencial de Alíquota e FECP sejam demonstrados corretamente. |
| **Ambiente:** | SIGAFIS |
| **Passo a passo:** | Para que a Base de Cálculo, Alíquota e Valores sejam considerados corretamente na ABA "Lançamentos de Apuração de ICMS" da rotina MATA103, é necessário que seja revisado o da TES (MATA080) que foi utilizada na operação, pontualmente a forma em que foi configurado o campo "Código de Reflexo" (CC7\_CODREF), verifique se os campos estão preenchidos da seguinte forma:     * **Configuração para o ICMS Complementar**:   - Base para Calc (CE0\_NFBASE) = Base ICMS  - Aliquota (CE0\_NFALIQ) = Alq.Compl.  - Vl.Aliquota (CE0\_NFALVA) = 0,00  - Valor (CE0\_VALO) = Complem.    OBS: O código de reflexo utilizado à cima destinado ao **ICMS Complementar** deve seguir o código de lançamento (Cod. Lanc - CC7\_CODLAN) utilizado.     * **Configuração para o FECP:**   No campo "Código de Reflexo", referente ao RJ7000006 (FECP) verifique se os campos estão preenchidos da seguinte forma:  - Base para Calc (CE0\_NFBASE) = Valor Contabil  - Aliquota (CE0\_NFALIQ) = FECP  - Vl.Aliquota (CE0\_NFALVA) = 0,00  - Valor (CE0\_VALO) = FECP    OBS: O código de reflexo utilizado à cima destinado ao **FECP** deve seguir o código de lançamento (Cod. Lanc - CC7\_CODLAN) utilizado. |
| **Observações:** | Validação de funcionamento realizado com os fontes:  IMPXFIS.PRW - 02/05/16  MATXFIS.PRX - 03/05/16 |
