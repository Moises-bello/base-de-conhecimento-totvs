---
article_id: 1500012314521
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8566501ebb79fcb5021a225a2800697a21189b10136d6b8e29876fead0d4f5e8
fetched_at: '2026-06-28T22:42:45.584867+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Plano mestre de produção no MRP Memória
type: support-article
updated_at: '2021-05-31T14:58:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012314521-Manufatura-Linha-Protheus-SIGAPCP-Plano-mestre-de-produ%C3%A7%C3%A3o-no-MRP-Mem%C3%B3ria
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Por que os planos mestres de produção cadastrados no **MATA750 - Manutenção do Plano Mestre de Produção** não estão sendo considerados no cálculo do **PCPA712 - MRP Memória** e não são listados no **PCPA144 - Geração de Documentos MRP**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para ser considerado no cálculo realizado no **PCPA712** e por consequência listado no **PCPA144**, os planos mestres de produção devem ser importados para uma demanda, e esta deve ser considerada na execução do **MRP - Manufacturing Resource Planning**.  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Inclua o plano mestre de produção no **MATA750**;  
2. Inclua uma demanda no **PCPA136 - Demandas do MRP**;  
3. No botão **Importar** que há na tela de inclusão da demanda importe o plano mestre incluído no **MATA750**;  
4. Através do **PCPA139 - Parâmetros de Integração do MRP**, certifique-se que a **API - Application Programming Interface** **MRPDemands** está *online*  
5. Se estiver *online*, através do **PCPA142 - Pendências de Integração do MRP** verifique se há pendências de integração de demandas, e se tiver, faça os ajustes pertinentes e na sequência clique em **Reprocessar** para que ocorra a integração;  
6. Se não estiver *online*, através do **PCPA140 - Sincronização**, execute a sincronização das demandas  
7. Execute o **PCPA712**, considerando a demanda incluída.
