---
article_id: 360040549473
category: Materiais - Compras (SIGACOM)
content_hash: 04410a571687b41f95cd0dbed6055de69faeac328cccf16c7c112bf055d0b28e
fetched_at: '2026-06-28T22:41:08.771518+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Data de validação da
  cotação (C8_VALIDA) busca a informação de onde?
type: support-article
updated_at: '2022-05-12T21:09:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549473-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Data-de-valida%C3%A7%C3%A3o-da-cota%C3%A7%C3%A3o-C8-VALIDA-busca-a-informa%C3%A7%C3%A3o-de-onde
---

**Dúvida**

Data de validação da cotação (**C8\_VALIDA)**busca a informação de onde?  
  
**Ambiente**Protheus – Compras – A partir da versão 12

**Solução**

O sistema busca a informação para preencher o campo **C8\_VALIDA**com base nos perguntes da rotina Gera Cotação (**MATA131**) na abertura da rotina conforme exemplo abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/OTVrBsJ8PsFipkQePsD3XjgAK/?name=inline1891158312.png)​​  
A partir da Atualização da Cotação o campo é apresentado no grid conforme exemplo abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053091874/mceclip0.png)​

Se o campo Necessidade estiver preenchido com informação diferente da data base o campo calcula a partir dessa informação.

No exemplo deste artigo consta:

**Data de Emissão:** 13/12/2019

**Necessidade:** 20/12/2019

**Validade:** 30/12/2019 ( calculada com base no pergunte "**N. dias p/ validade"** - MATA131)

![](https://totvssuporte.zendesk.com/attachments/token/vfR28DHTM0r0JykqCNwBhU0Wi/?name=inline345485935.png)​

![](https://totvssuporte.zendesk.com/attachments/token/zY2WlbQXewJR403CWKIgQ1IaI/?name=inline1335793149.png)​

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
