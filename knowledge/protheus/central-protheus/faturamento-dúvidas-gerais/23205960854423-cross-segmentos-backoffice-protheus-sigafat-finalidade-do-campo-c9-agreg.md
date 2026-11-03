---
article_id: 23205960854423
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: a10db218dc6fbaf5aac3f2036bfaf3f4a168e2309ceb5ce0e059c684f45bf50f
fetched_at: '2026-06-28T22:38:29.812882+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Finalidade do campo C9_AGREG
type: support-article
updated_at: '2025-01-10T20:19:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23205960854423-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Finalidade-do-campo-C9-AGREG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23205960823831) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual a finalidade do campo C9\_AGREG?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**O campo **C9\_AGREG** serve para separar o faturamento da nota fiscal conforme o código deste campo. É feita a geração de Documento de saída do pedido todo.  
O sistema ao detectar que o campo **C9\_AGREG** tem diferentes valores nos itens, ele cria uma nota para cada valor de **C9\_AGREG**.  
  
Este campo é preenchido automaticamente quando o parâmetro: **(MV\_AGREG = SA1-A1\_AGREG)** e o campo **A1\_AGREG** está preenchido no cadastro de cliente.  
  
O sistema só separa os itens por nota fiscal quando os campos: **C9\_CARGA**, **C9\_SEQCAR** e **C9\_AGREG** estão preenchidos, mas este processo é realizado quando existe integração com o módulo de **WMS**.   
  
Neste caso, poderá utilizar os pontos de entrada abaixo:

* **[M440SC9I - Gravação de campos](https://tdn.totvs.com/pages/viewpage.action?pageId=6784165)**
* [M460QUEB - Define a quebra do documento de saída](https://tdn.totvs.com/pages/viewpage.action?pageId=6784198)
* [M460NITE - Quebra de NF de saída](https://tdn.totvs.com/pages/viewpage.action?pageId=6784191)

**Em Saiba Mais:**  
[Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - A1\_AGREG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053650553-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-A1-AGREG?source=search)
