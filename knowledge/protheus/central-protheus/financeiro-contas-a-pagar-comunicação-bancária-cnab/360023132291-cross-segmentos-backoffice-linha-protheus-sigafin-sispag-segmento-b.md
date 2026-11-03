---
article_id: 360023132291
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: d30edeae1e3b3aaad6ac547a98d513b5a0a7b3e9d9c5dffe870479ec86b06097
fetched_at: '2026-06-28T22:37:55.086795+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - SISPAG - SEGMENTO B
type: support-article
updated_at: '2022-05-31T02:21:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023132291-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-SISPAG-SEGMENTO-B
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**

Não esta gerando o SEGMENTO B, mesmo quando o tipo do borderô é 03, 07, 41 e 47 conforme instruções da documentação <http://tdn.totvs.com/pages/releaseview.action?pageId=233743712>,  e o leiaute devidamente configurado.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Não esta definido no Detalhe do SEGMENTO A, posição 230, de forma correta. Veja o exemplo, incorreto abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020859772/mceclip0.png)

Forma correta:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020785491/mceclip1.png)

TXT abaixo após o ajuste acima.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020786211/mceclip0.png)  
  
**Solução**Conforme instruções da **página 13**, da documentação do SISPAG-ITAU:

Este segmento só é obrigatório quando:  
o Houver a necessidade de emissão de aviso ao favorecido, conforme definido no Segmento  
A (posição 230 igual a 3 ou 5 - ver nota 16)

Íntegra da documentação no link abaixo:

<http://download.itau.com.br/bankline/SISPAG_CNAB.pdf>

Dessa forma o SEGMENTO B será gerado.
