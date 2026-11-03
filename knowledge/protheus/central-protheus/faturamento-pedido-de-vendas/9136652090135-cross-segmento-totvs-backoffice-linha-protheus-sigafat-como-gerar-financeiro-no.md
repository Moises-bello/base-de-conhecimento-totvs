---
article_id: 9136652090135
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b2ca058ebcac04c5b79d6e4b1c69a986ef203164036c47654a5d585dc9d3dcfb
fetched_at: '2026-06-28T22:38:42.346026+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Como gerar Financeiro
  no Beneficiamento / Poder de Terceiros
type: support-article
updated_at: '2023-10-06T20:16:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9136652090135-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Como-gerar-Financeiro-no-Beneficiamento-Poder-de-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Preciso cobrar mão de obra em uma operação de Poder de Terceiros, como fazer ?   
  
Inciso I do Art 404 do RICMS/SP  
https://legislacao.fazenda.sp.gov.br/Paginas/art404.aspx  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Solução**  
Exemplo de operação :

Entrada de NF com controle de Poder de Terceiros não vai gerar financeiro (F4\_PODER3 como Remessa)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9136231873431/mceclip0.png)

Na Devolução, no modulo Faturamento, devolver o produto do Poder de terceiros com a TES F4\_PODER3 tipo D (para baixar o saldo da tabela SB6) e incluir mais um item de mão de obra onde a TES vai gerar financeiro, não atualiza estoque e não vai gerar Poder de Terceiros

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9136459529879/mceclip2.png)  
Esta é a TES do Produto Mão de Obra

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9136555315607/mceclip3.png)
