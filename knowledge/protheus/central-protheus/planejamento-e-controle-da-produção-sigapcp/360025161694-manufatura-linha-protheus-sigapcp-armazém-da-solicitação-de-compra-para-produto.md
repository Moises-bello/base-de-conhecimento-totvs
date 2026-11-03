---
article_id: 360025161694
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 44148b8fa351cfc3521de45ec696f693437e08f14cbfad734c73047702c6a02b
fetched_at: '2026-06-28T22:42:40.847052+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Armazém da solicitação de compra para
  produto de apropriação indireta
type: support-article
updated_at: '2021-08-13T11:06:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025161694-Manufatura-Linha-Protheus-SIGAPCP-Armaz%C3%A9m-da-solicita%C3%A7%C3%A3o-de-compra-para-produto-de-apropria%C3%A7%C3%A3o-indireta
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Para qual armazém é gerada a solicitação de compra para item de apropriação indireta?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Por meio do parâmetro **MV\_GRVLOCP - Considerar o armazém de processos na geração da solicitação de compras** o Sistema identifica se a solicitação de compra deve ser gerada para o armazém padrão do produto, identificado pelo campo **B1\_LOCPAD - Armazém padrão** ou para o armazém identificado no parâmetro **MV\_LOCPROC - Local padrão a ser enviado os materiais indiretos em processo**. **Importante**  
Se o parâmetro **MV\_ARQPROD - O parâmetro configura se os dados de indicadores de produto serão considerados pela tabela SB1 ou se serão considerados pela tabela SBZ** possuir o conteúdo **SBZ - Indicadores de Produtos**, ao invés do campo **B1\_LOCPAD** será considerado o conteúdo do campo **BZ\_LOCPAD - Armazém padrão**.
