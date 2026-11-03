---
article_id: 360061930033
category: ADVPL - Rotina Automática
content_hash: a6c91804da63632cccd223dd72cf6a568bea38384a4f97d9d8a7a0c8a7eb318d
fetched_at: '2026-06-28T22:40:23.852362+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL -  É possível incluir grade
  de produtos através de rotina automática MATA010? '
type: support-article
updated_at: '2021-12-29T13:05:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061930033-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-incluir-grade-de-produtos-atrav%C3%A9s-de-rotina-autom%C3%A1tica-MATA010
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**É possível incluir grade de produtos através de rotina automática MATA010?   
  
**Ambiente**Protheus - ADVPL – A partir da versão 11.80  
  
**Solução**

Não é possível realizar automaticamente a inclusão do registro de um produto grade na **SB1**.

O procedimento de marcar uma coluna/linha, previamente atrelada no cadastro de grade **MATA550**, realmente gera um registro na **SB1**, porém mesmo que o registro(**B1\_COD/B1\_DESC/B1\_GRADE**) não exista na tabela, a rotina **MATA010** realizará uma validação, ao identificar que trata-se de um produto grade, entre a tabela **SB4** e não será permitido apresentando um *help;*   
Isso ocorre pois a manipulação desse registro deve ser realizada na rotina **MATA550**,  atualmente a rotina **MATA550** não esta preparada para execução automática.  
  
**Saiba mais:**  
[Rotina automática MATA010](https://tdn.totvs.com/display/PROT/Produtos+-+MATA010+-+Estoque+-+P12)
