---
article_id: 1500012234902
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 422d78b495252bf498a6420e36b96946a8d74771b1632813cbfae7a66d438a3e
fetched_at: '2026-06-28T22:42:45.736540+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Previsão de Vendas no MRP Memória
type: support-article
updated_at: '2021-05-31T16:38:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012234902-Manufatura-Linha-Protheus-SIGAPCP-Previs%C3%A3o-de-Vendas-no-MRP-Mem%C3%B3ria
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:25 min**  
**Dúvida**Por que as previsões de vendas cadastradas no **MATA700 - Previsão de Vendas** não estão sendo consideradas no cálculo do **PCPA712 - MRP Memória** e não são listadas no **PCPA144 - Geração de Documentos MRP**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para ser considerada no cálculo realizado no **PCPA712** e por consequência listado no **PCPA144**, as previsões de venda devem ser importados para uma demanda, e esta deve ser considerada na execução do **MRP - Manufacturing Resource Planning**.  
Para solucionar essa questão, realize os seguintes passos:  
1. Inclua a previsão de vendas no **MATA700**;  
2. Inclua uma demanda no **PCPA136 - Demandas do MRP**;  
3. No botão **Importar** que há na tela de inclusão da demanda importe a previsão de vendas incluída no **MATA700**;  
4. Através do **PCPA139 - Parâmetros de Integração do MRP**, certifique-se que a **API - Application Programming Interface** **MRPDemands** está *online*  
5. Se estiver *online*, através do **PCPA142 - Pendências de Integração do MRP** verifique se há pendências de integração de demandas, e se tiver, faça os ajustes pertinentes e na sequência clique em **Reprocessar** para que ocorra a integração;  
6. Se não estiver *online*, através do **PCPA140 - Sincronização**, execute a sincronização das demandas  
7. Execute o **PCPA712**, considerando a demanda incluída.
