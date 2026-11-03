---
article_id: 17023428523287
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c6cfe97b563f4919ccb1ba79691ee4d8f05c0cc514d07d956f81f182b948740e
fetched_at: '2026-06-28T22:42:47.021543+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Sincronização na execução do MRP
type: support-article
updated_at: '2024-10-17T11:57:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17023428523287-Manufatura-Linha-Protheus-SIGAPCP-Sincroniza%C3%A7%C3%A3o-na-execu%C3%A7%C3%A3o-do-MRP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17023419880343) Tempo aproximado para leitura: **00:01:11 min** **Dúvida**Como ocorre a sincronização na execução do **MRP - Manufacturing Resource Planning?**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**A sincronização na execução do **MRP** pode ocorrer de três formas, a depender do preenchimento do parâmetro **MV\_MRPSINC - Sincronização Automática de tabelas ao rodar o MRP**. Se o conteúdo desse parâmetro for **1**, ao acessar a rotina **PCPA712  - MRP Memória** será apresentada uma tela indicando os cadastros que tem pendência de sincronização, permitindo ao usuário escolher se deseja ou não sincronizar os dados.  
Se esse parâmetro tiver o conteúdo **2**, não será apresentada a tela e as pendências serão sincronizadas automaticamente ao iniciar o processamento do **MRP**.  
Se esse parâmetro tiver o conteúdo **3**, serão sincronizados todos os dados, não somente as pendências.
