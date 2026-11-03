---
article_id: 360042160514
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 5b67d0c0fdf2ba1d724776c5503c1a3c8cbfb8545f0695de1b0a98682aeb79ad
fetched_at: '2026-06-28T22:39:36.868543+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Campos N1_ALIQPIS
  e N1_ALIQCOF estão bloqueados, qual procedimento devo realizar?
type: support-article
updated_at: '2021-06-29T12:37:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042160514-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Campos-N1-ALIQPIS-e-N1-ALIQCOF-est%C3%A3o-bloqueados-qual-procedimento-devo-realizar
---

**Dúvida**As alíquotas dos campos N1\_ALIQPIS e N1\_ALIQCOF eram inseridas de forma manual, porém atualmente estão bloqueados. Qual procedimento para desbloquear?

**Ambiente**

PROTHEUS - Ativo Fixo - A partir da versão 12.1.7  
  
**Solução**Atualmente não há uma maneira de liberar os campos e foram bloqueados pela seguinte situação:

“A edição dos Campos N1\_ALIQPIS e N1\_ALIQCOF, foram desabilitados para que os mesmos sejam originados de uma nota fiscal de entrada, através de um TES que atualiza ativo. Os campos impactam diretamente no cálculo de PIS/COFINS e influenciam negativamente no EFD-Contribuições (Pis/Cofins) se alterados manualmente."

Sendo assim o TES deve estar configurada para o calculo de PIS/COFINS que será preenchido as Alíquotas no Ativo.

O procedimento que deseja realizar deve ter relação com crédito sobre Depreciação PIS e COFINS, caso sim há duas documentações da equipe de Arquivos Magnéticos referente o assunto:

MP - FIS - EFD CONTRIBUIÇÕES - Como gerar o registro F120 do Sped Contribuições

MP - FIS - EFD CONTRIBUIÇÕES - Como gerar o registro F130

Teoricamente somente preenchendo o campo Atual. Ativo = Sim e calcular PIS e COFINS no documento de entrada, deve levar informações para os campos N1\_ALIQPIS e N1\_ALIQCOF automaticamente.

PIS/ COFINS (F4\_PISCOF) = Ambos  
Cred.PIS/COF (F4\_PISCRED) = Credita
