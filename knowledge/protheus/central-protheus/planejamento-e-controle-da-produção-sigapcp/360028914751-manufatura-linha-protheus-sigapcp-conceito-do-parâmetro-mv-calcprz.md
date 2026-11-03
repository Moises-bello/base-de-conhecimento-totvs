---
article_id: 360028914751
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 060cbb8ea769cb129663b3da20b4b2425a7a1831426a32b986f7c6a8642f1943
fetched_at: '2026-06-28T22:42:42.093218+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Conceito do parâmetro MV_CALCPRZ
type: support-article
updated_at: '2021-08-27T17:34:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028914751-Manufatura-Linha-Protheus-SIGAPCP-Conceito-do-par%C3%A2metro-MV-CALCPRZ
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Como e onde é utilizado o parâmetro **MV\_CALCPRZ - Define os dias da semana a considerar no Prazo de Entrega**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O Sistema utiliza a informação preenchida no parâmetro **MV\_CALCPRZ** para definir a **C2\_DATPRI** **- Previsão Inicial** ou **C2\_DATPRF - Entrega** de uma determinada **OP - Ordem de Produção**.  
  
Se o conteúdo do parâmetro **MV\_CALCPRZ** for:

* **0**: baseado no prazo de entrega do produto, considera todos os dias da semana como produtivos;
* **1**: considera de segunda a sábado;
* **2**: considera de segunda a sexta.

**Importante**  
Esse parâmetro é utilizado na geração de **OP's** por meio da rotina **MATA650 - Ordem de Produção** e também por meio das rotinas de **MRP -**Material Requirements Planning.
