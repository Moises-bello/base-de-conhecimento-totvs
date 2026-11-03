---
article_id: 360044416153
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5e584c820015478f0a58150e2de6a6560fb0fd0d8593358f2f626caefa3ab511
fetched_at: '2026-06-28T22:42:43.231757+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Filtro no MRP por produtos que fazem
  parte de uma demanda
type: support-article
updated_at: '2023-04-26T19:01:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044416153-Manufatura-Linha-Protheus-SIGAPCP-Filtro-no-MRP-por-produtos-que-fazem-parte-de-uma-demanda
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:21 min**  
**Dúvida**Por que o **MRP - Manufacturing Resource Planning** não calcula somente as necessidades dos produtos que fazem parte da demanda informada no campo **Demanda**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
O **PCPA712 -** **MRP** **Memória** sempre realiza uma busca completa de todos os produtos da tabela **SB1** **- Produtos**, descartando somente os produto que estiverem com o campo **B1\_MRP - MPR** como **Não**, e que não façam parte dos grupos e tipos de materiais selecionados para processamento.  
Após esse levantamento, o Sistema avalia a necessidade de estoque dos produtos envolvidos e a essa necessidade soma a previsão de vendas.  
Portanto o **MRP** não faz a leitura somente do produto constante na demanda, seja esta demanda do tipo **1 - Pedido de Venda**, **2 - Plano de Vendas**, 3 - **Plano Mestre**, **4 - Empenhos de Projeto**, **5 - Importação CSV** ou **9 - Manual**.  
  
**Saiba mais**  
Na documentação [Manufatura - Linha Protheus - SIGAPCP - Filtros dos produtos no MRP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024933113-MP-SIGAPCP-Filtros-dos-produtos-no-MRP?source=search) explica sobre como realizar filtro por produto no cálculo do **MRP**.
