---
article_id: 4427433650455
category: SIGAEST - CUSTOS
content_hash: d39613a61575ed80df16a9129bbdd4f97dd5134bf66163e78404bdd6dc0c0e7a
fetched_at: '2026-06-28T22:39:02.265417+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MV_USANPRC - Leitura
  do log sob a data de processamento MATA280
type: support-article
updated_at: '2023-11-16T19:13:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427433650455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-USANPRC-Leitura-do-log-sob-a-data-de-processamento-MATA280
---

**Dúvida**Como é feita a leitura do log de data, após processar a rotina MATA280 com o parâmetro MV\_USANPRC ativo?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Como configurar o parâmetro:**

<https://tdn.totvs.com/display/public/PROT/MV_USANPRC>

O log apresentado em tela que tem a data do sistema é feito através do método: **oCenterPanel:SaveLog()** e este é gravado na tabela SXU.

O log gravado na tabela CV8, onde a data é a data do servidor é gravado pela **M280PrcLog()**. Sendo assim, são 2 logs individuais e não um único log a ser apresentado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427424588823/mceclip0.png)

Para avaliar o log que é apresentado em tela deve ser avaliado com time de framework sobre a classe **tnewProcess** (<https://tdn.totvs.com/display/framework/tNewProcess>)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

*[FAQ Estoque/Custos](https://tdn.totvs.com/display/public/PROT/FAQs+-+Estoque+e+Custos)*
