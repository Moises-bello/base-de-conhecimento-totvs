---
article_id: 16745862124567
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3967be98fd447e11bc637d644dbbad36399bd603c5c293c4f436167d96f4ded3
fetched_at: '2026-06-28T22:42:47.130186+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Valor unitário na tela de resultados
  do MRP
type: support-article
updated_at: '2023-08-15T11:56:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16745862124567-Manufatura-Linha-Protheus-SIGAPCP-Valor-unit%C3%A1rio-na-tela-de-resultados-do-MRP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16745847123479) Tempo aproximado para leitura: **00:01:43 min** **Dúvida**Qual é a origem da informação apresentada no **Valor Unitário** da tela **RESULTADOMRP**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 1es]  
  
**Solução**A informação apresentada no campo **Valor Unitário** depende da configuração do parâmetro **MV\_CUSTPRD**, se esse parâmetro estiver com o valor **1** é apresentado o conteúdo do campo **B1\_CUSTD** ou **BZ\_CUSTD**, dependendo da configuração do parâmetro **MV\_ARQPROD**.  
Se estiver com conteúdo **2**, é apresentado o custo médio do item e armazém padrão do item, neste caso o conteúdo do campo **B2\_CM1**, caso **B2\_QATU** tenha o valor **0** ou do campo **B2\_VATU1** dividido pelo conteúdo do campo **B2\_QATU** caso **B2\_QATU** tenha um valor diferente de **0**.  
Já se estiver com o valor **3** é apresentado o conteúdo do campo **B1\_UPRC** ou **BZ\_UPRC**, dependendo da configuração do parâmetro **MV\_ARQPROD**.  
  
**Glossário**  
**RESULTADOMRP** - Resultados MRP   
**MV\_CUSTPRD** - Custo Produto 1-Custo Standard;2-Custo Médio;3-Preço de Compra  
**B1\_CUSTD** - Custo Standard  
**BZ\_CUSTD** - Custo Standard  
**MV\_ARQPROD** - O parâmetro configura se os dados de indicadores de produto serão considerados pela tabela SB1 ou se serão considerados pela da tabela SBZ  
**B2\_CM1 -** Custo Unitário do Produto  
**B2\_QATU** - Saldo Atual  
**B2\_VATU1** - Saldo Atual em Valor  
**B1\_UPRC** - Último Preço de Compra  
**BZ\_UPRC** - Último Preço de Compra
