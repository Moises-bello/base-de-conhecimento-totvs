---
article_id: 360028360771
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: cea6f734b4c0d07efe585814b5eb02bce036e0c259e248c71f9a42cb76a1e501
fetched_at: '2026-06-28T22:40:44.764141+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB -ECD : I155 Pelo menos
  um dos campos (saldo inicial, total de débitos, total de créditos ou saldo final)
  deve conter valor diferente de zero.'
type: support-article
updated_at: '2022-05-16T17:26:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028360771-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-I155-Pelo-menos-um-dos-campos-saldo-inicial-total-de-d%C3%A9bitos-total-de-cr%C3%A9ditos-ou-saldo-final-deve-conter-valor-diferente-de-zero
---

**Dúvida**

O registro I155 está sendo gerado com o saldo Zerado , com isso apresenta erro abaixo no validador

 I155 Pelo menos um dos campos (saldo inicial, total de débitos, total de créditos ou saldo final) deve conter valor diferente de zero.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028410172/mceclip3.png)

**Ambiente**  
Microsiga Protheus – Contabilidade – A partir da versão 11.80

**Causa**

Ao gerar o arquivo o sistema busca os dados existentes na tabela CSC.

Caso o tabela possua registros com valor zerado, os registro I155 será gerado com valor zero no TXT.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028410132/mceclip2.png)

**\*Solução Paliativa**

* Através da rotina de escrituração(CTBS001) - Gere uma revisão

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028411792/mceclip5.png)

* Através da tabela CSC realize um filtro pelo código da revisão gerada "CSC\_CODREV" onde os campos "CSC\_VALINI ; CSC\_VALDEB ;CSC\_VALCRE ; CSC\_VALMOV" estejam zerados
* Ao realizar o filtro delete os registros com valor zerado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028411852/mceclip6.png)

* Após limpeza da tabela CSC para essa revisão, clique em  "Gerar Arq"   e gere o arquivo , com isso o sistema não irá gerar mais o Registro I155 zerado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028408651/mceclip7.png)

**Importante:** Esse processo trata-se de um procedimento paliativo, disponibilizado em virtude da entrega ECD, a solução definitiva foi liberada através da Issue  DSERCTR1-21421, segue abaixo a solução liberada da Issue.

**Solução :**

A Solução encaminhada na Issue DSERCTR1-21421 foi , configurar o Appeserver conforme orientação descrita no link : <http://tdn.totvs.com/pages/releaseview.action?pageId=494991436>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029599052/mceclip0.png)
