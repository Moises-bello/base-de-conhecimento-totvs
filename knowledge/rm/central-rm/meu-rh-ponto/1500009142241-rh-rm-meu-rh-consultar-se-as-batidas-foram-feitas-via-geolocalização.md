---
article_id: 1500009142241
category: Meu RH - Ponto
content_hash: 7967c7135700bb1cdf8ea9304804cee34271aef456f4ca2104915d9e317edd69
fetched_at: '2026-06-28T22:47:30.378219+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Consultar se as batidas foram feitas via geolocalização
type: support-article
updated_at: '2025-03-06T14:31:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009142241-RH-RM-Meu-RH-Consultar-se-as-batidas-foram-feitas-via-geolocaliza%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25907518295447) Tempo aproximado para leitura: 00:00:36 min**

**Dúvida**

Consultar se as batidas foram feitas via geolocalização?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.27  
  
**Solução**

Ao ser efetuada a batida de ponto através do menu **"Relógio"** no Meu RH são alimentadas algumas tabelas no banco de dados que podem ser consultadas através de uma consulta SQL.  
  
Com a consulta no SQL você irá visualizar diversos campos referentes a batida que foi realizada. As batidas registradas por geolocalização ficam armazenadas na tabela **APORTARIA373.**   
  
Seu registro na tabela **ABATFUN** terá na coluna **IDAPORTARIA373** valor referente ao seu ID informado na tabela **APORTARIA373**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7500370399639)  
  
Ao consultar a tabela **ABATFUN** as batidas que tiverem o campo preenchido como **NULL** na coluna **IDAPORTARIA373** não foram realizadas utilizando o menu **"Relógio"**, foram inseridas manualmente no espelho de ponto via sistema RM e/ou Portais ou foram importadas de um arquivo **AFD(Arquivo de fonte de dados)**.
