---
article_id: 360006849432
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: de2384f35d571211bcbad3061501d7da16852c896f4974f22b10b1b94c505938
fetched_at: '2026-06-28T22:40:32.285581+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGACTB - CTBA102 type mismatch
  on compare on CTBA102 
type: support-article
updated_at: '2022-07-18T18:55:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006849432-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-type-mismatch-on-compare-on-CTBA102
---

**Ocorrência**

Error log : type mismatch on compare on CTBA102(CTBA102.PRW)

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80 **Causa**

Ausência pergunta na rotina  "CTB102A".

**Solução**  
Trate o preenchimento selecionando via F12 na rotina CTBA102.prw a pergunta Modo de Exibição? Igual à "1" ou "2"?  
Verifique se a pergunta existe no Dicionário de Dados, via Configurador  grupo de perguntas CTB102A.  
  
Para a correção desta inconsistência, é necessário a atualização do Dicionário de Dados disponível no portal e execute o UPDDISTR.  
  
![](https://totvssuporte.zendesk.com/attachments/token/c1BihPIkO7YNLNQYzL2FMrWKA/?name=inline-1105129562.png)​
