---
article_id: 4832102259479
category: Comércio Exterior - Easy Import Control - Miscelanea
content_hash: 9ba08484609b8dd347f26b2f99d579370b5c001a60f82a56a71fccc6429b7b66
fetched_at: '2026-06-28T22:39:42.057096+00:00'
product: protheus
section_id: 1500001549702
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Como preencher
  o cadastro de/para, para que seja substituído no arquivo de envio ao despachante
  o código do fornecedor?
type: support-article
updated_at: '2022-03-17T18:31:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4832102259479-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-preencher-o-cadastro-de-para-para-que-seja-substitu%C3%ADdo-no-arquivo-de-envio-ao-despachante-o-c%C3%B3digo-do-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como preencher o cadastro De/Para, para que seja substituído no arquivo de envio ao despachante o código do fornecedor?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**1. Selecione o menu Atualizações\Miscelânea\Tabela De\Para.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406506849559/mceclip2.png)  
  
2. Selecione incluir.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406506886935/mceclip3.png)

3. Preencha os  campos e o código do despachante que será enviado no arquivo de integração, deve ser preenchido com o código do fornecedor  exportador/fabricante descrito na Tabela De/Para campo **YU\_GIP\_1** para o importador corrente, se não existir a correspondência será utilizado o código digitado no pedido/embarque:  
fase PO campo **W3\_FORN-W3\_FABR**fase DI: **W7\_FORN-W7\_FABR** com invoice **W8\_FORN - W8\_FABR**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4831808745239/mceclip0.png)

**Saiba mais**  
[Erro no arquivo TXT SIGAEIC gerado para o despachante](https://tdn.totvs.com/display/public/PROT/13305798+DTRADE-7284+DT+Erro+no+arquivo+TXT+SIGAEIC+gerado+para+o+despachante)
