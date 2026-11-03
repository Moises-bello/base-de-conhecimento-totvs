---
article_id: 17334620504983
category: TAF - REINF
content_hash: 0114c6ef345ca8ed508728f4328aaf4c9de460613be9fd6ca5ad6941e9696a89
fetched_at: '2026-06-28T22:41:34.781584+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Query greater than 32768
  bytes. on MPSYSOPENQUERY(MPSYSOPENTABLES.PRW)
type: support-article
updated_at: '2024-06-18T14:51:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17334620504983-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Query-greater-than-32768-bytes-on-MPSYSOPENQUERY-MPSYSOPENTABLES-PRW
---

#### **Produto**

#### TAF - SIGATAF - Release 12.1.33 e superior

**Causa**

O problema ocorre devido a falha das nomenclaturas das tabelas do menu, onde o browser faz a contagem de 3 em 3 caracteres, quando o nome está somente como 2 caracteres como B1 e A1, ele se perde não encontrando a tabela, aí entra no loop para encontrar, que acaba criando a query gigante na SX9 causando o error log.   
    
  
O problema ocorre nos menus que estiverem com o nome da tabela com 2 caracteres e tiver a chamada do extrator fiscal (EXTFISXTAF)

**Solução**

**Menu SIGAFIS.XNU**

1) Encontrar o arquivo SIGAFIS.XNU  
2) Buscar pela rotina FISR017  
3) Alterar no item <Tables> que consta a tabela B1, para SB1, ficando da seguinte forma:  
<TABLES>SB1</TABLES>.

**Menu SIGAFIN.XNU**

1) Encontrar o arquivo SIGAFIN.XNU  
2) Buscar pela rotina FINR960   
3) Alterar no item <Tables> que consta a tabela A1, para SA1, ficando da seguinte forma:  
<TABLES>SA1</TABLES>.

Faremos o ajuste no menu do módulo SIGAFIS e a expedição do menu atualizado acontece com a publicação da release 12.1.2310 em Outubro/2023.

Após efetuar o procedimento acima, caso o erro persista, efetue a configuração abaixo no appserver.ini:

[GENERAL]  
MaxQuerySize=65536  
   
Abaixo documentação:  
   
<https://tdn.totvs.com/pages/viewpage.action?pageId=372543595>
