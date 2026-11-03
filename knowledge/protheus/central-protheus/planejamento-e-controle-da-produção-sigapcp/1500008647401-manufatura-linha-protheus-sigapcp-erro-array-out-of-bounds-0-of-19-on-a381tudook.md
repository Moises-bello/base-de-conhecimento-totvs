---
article_id: 1500008647401
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 499eeede4e960e24cf43631f0a48395befa57ed0895043b2756bcc7c13ea2827
fetched_at: '2026-06-28T22:42:42.268859+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Erro array out of bounds ( 0 of 19
  ) on A381TUDOOK(MATA381.PRX)
type: support-article
updated_at: '2023-07-13T17:33:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008647401-Manufatura-Linha-Protheus-SIGAPCP-Erro-array-out-of-bounds-0-of-19-on-A381TUDOOK-MATA381-PRX
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min**  
**Ocorrência**No módulo **SIGAPCP - Planejamento e Controle da Produção** é apresentado o erro **array out of bounds ( 0 of 19 ) on A381TUDOOK(MATA381.PRX)**ao salvar ou excluir os empenhos.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Existe campos que não estão marcados como **Usado** no **SIGACFG - Configurador**.  
  
**Solução**É necessário que os campos abaixo estão presentes no ambiente estejam marcados como **Usado** através do **Configurador**:

* **D4\_COD - Produto**
* **D4\_TRT - Seq. Estrutura**
* **D4\_LOCAL - Armazém**
* **D4\_QUANT - Sal. Empenho**
* **D4\_QTDEORI - Qtd. Empenho**
* **D4\_QTSEGUM - Sld.Emp 2aUM**
* **D4\_LOTECTL - Lote**
* **D4\_NUMLOTE - Sub-Lote**
* **D4\_DTVALID - Data Validade**
* **D4\_POTENCI - Potencia Lote**
* **D4\_DATA - Dt. Emepnho**
* **D4\_OPORIG - OP Origem**
