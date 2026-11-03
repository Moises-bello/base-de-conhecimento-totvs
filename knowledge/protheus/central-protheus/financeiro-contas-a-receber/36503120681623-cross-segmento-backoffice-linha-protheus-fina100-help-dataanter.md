---
article_id: 36503120681623
category: Financeiro - Contas a Receber
content_hash: aec1dc3a340a31bae2d8e9261c31f92964da7342121db8f5944b3baeadea8ecb
fetched_at: '2026-06-28T22:38:12.476482+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - FINA100 - HELP: DATAANTER'
type: support-article
updated_at: '2026-01-28T12:40:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36503120681623-Cross-Segmento-Backoffice-Linha-Protheus-FINA100-HELP-DATAANTER
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36503120656023) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Problema: Não é permitido que seja feita movimentação financeira em períodos anteriores.  
  
**Solução**

O parâmetro [MV\_DTMOVRE](https://tdn.totvs.com/pages/viewpage.action?pageId=638721921) faz parte do conjunto de configurações que, através da rotina Movimento Bancário (**FINA100**), permitem incluir movimentações bancárias informando uma data (**E5\_DATA**) anterior à *database* do sistema.

Para que esse processo seja permitido, é necessário habilitar o parâmetro **MV\_DTMOVRE** e, com isso, através do **MV\_DTMOVDR** possa ser definida a quantidade de dias (corridos) que a data pode ser informada (em relação à *database*).

Estes parâmetros continuam sujeitos ao controle de data do parâmetro [MV\_DATAFIN](https://tdn.totvs.com/pages/viewpage.action?pageId=514730929), não permitindo a inclusão de registros em data igual ou anterior à informada neste parâmetro.

**Importante**

Para correta atualização de saldo bancário (SE8), ao incluir um movimento bancário com data retroativa, o campo **E5\_VENCTO**é preenchido com a mesma data informada no campo **E5\_DATA.**

**Saiba mais**

[Utilização do parâmetro MV\_DTMOVDR](https://tdn.totvs.com/pages/viewpage.action?pageId=653424946)

[Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550522-Financeiro)
