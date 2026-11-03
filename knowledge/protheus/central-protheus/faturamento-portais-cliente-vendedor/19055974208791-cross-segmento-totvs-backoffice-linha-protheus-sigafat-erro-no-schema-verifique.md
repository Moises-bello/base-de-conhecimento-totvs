---
article_id: 19055974208791
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: abcd8b3ef1df6ec49f2d7bdfcd39b0040d2bbcf489b6463accced1ca3c6288c7
fetched_at: '2026-06-28T22:38:24.027587+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Erro no Schema
  (Verifique se a função SETUPTGV foi executada)
type: support-article
updated_at: '2023-11-14T12:31:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19055974208791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-no-Schema-Verifique-se-a-fun%C3%A7%C3%A3o-SETUPTGV-foi-executada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19055964754967) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Acessando o Portal de Vendas (PGV) apresenta o HELP Erro no Schema (Verifique se a função SETUPTGV foi executada).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.1.2210;  
  
**Solução**Ao acessar o Portal de Vendas (PGV) o sistema apresenta o HELP de **Erro no Schema** com a seguinte mensagem (*Não foram encontrados os schemas necessários para utilização do TGV. Verifique se a função SETUPTGV foi executada conforme a documentação: [TGV - Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=579468339#TOTVSGest%C3%A3odeVendas:GuiadeReferencia-CONFIG_PILOTO))*

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/19055960589591)

Hoje não é mais necessário executar o **SETUPTGV** para criar os schemas essa mensagem só é apresentada porque o ambiente está desatualizado.  
  
Para resolver tem que aplicar o patch de acumulados e rodar o UPDDISTR no ambiente, após atualização do sistema essa mensagem não vai ser mais apresentada.

[Pacotes de Atualização - Faturamento](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859#issues-17)
