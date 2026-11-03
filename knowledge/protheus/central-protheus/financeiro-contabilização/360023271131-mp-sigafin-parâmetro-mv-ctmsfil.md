---
article_id: 360023271131
category: Financeiro - Contabilização
content_hash: 8b2e9869937e684337e0d9d8cd3c5caaa47b6c685fafa8d9e51d931a34d65f3a
fetched_at: '2026-06-28T22:38:05.239002+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: MP - SIGAFIN - Parâmetro MV_CTMSFIL
type: support-article
updated_at: '2021-04-28T15:56:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023271131-MP-SIGAFIN-Par%C3%A2metro-MV-CTMSFIL
---

**Dúvida**Ao utilizar a rotina CTBAFIN (Contabilização Offline) com a pergunta **Considera Filial Original?** igual a  "**Sim**", qual campo é considerado?

**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 12.1.17.  
  
   
**Solução**A rotina irá verificar o conteúdo do parâmetro MV\_CTMSFIL.

Este parâmetro possibilita mudar o campo de **filial origem**a ser pesquisado pela rotina.

Campos de **filial origem**que serão considerados com MV\_CTMSFIL = .F. ou caso o parâmetro não tenha sido cadastrado (padrão do sistema):

* E1\_MSFIL, E2\_MSFIL, E5\_MSFIL e EF\_MSFIL

Campos de **filial origem**que serão considerados com MV\_CTMSFIL = .T.

* E1\_FILORIG, E2\_FILORIG, E5\_FILORIG e EF\_FILORIG
