---
article_id: 360048775974
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3c746f2d7ba59af1e48c5f40b9ba301c1771dedb9f935f5d19e3e10d579e1df6
fetched_at: '2026-06-28T22:42:47.154019+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Como agilizar a performance de Multi-Threads no MRP
type: support-article
updated_at: '2020-12-07T17:46:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048775974-MP-SIGAPCP-Como-agilizar-a-performance-de-Multi-Threads-no-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura:**00:00:42 min**  
 **Dúvida**Como agilizar a **performance** de **Multi-Threads** no **MRP - Material Requiriments Planning**?  
  
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**O resultado depende da configuração de **Servidor/Memória**, para que o processamento tenha um ganho real de **performance**.   
Configure o parâmetro **MV\_A710THR** **- Permite definir a quantidade de threads a serem processadas simultaneamente na rotina de MRP para montagem do arquivo de trabalho (1 a 20 threads)**, com o número de **threads**.  
  
**Importante**  
Esse parâmetro é válido para **MATA710 - MRP** e **MATA712 - MRP**.
