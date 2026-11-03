---
article_id: 360056016574
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8f5e41b3b6537b398cddbcfe2184c847d3b472beb39e173c60db246f6e0c0a59
fetched_at: '2026-06-28T22:42:41.000289+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Campo G2_ROTALT
type: support-article
updated_at: '2021-09-30T14:53:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056016574-Manufatura-Linha-Protheus-SIGAPCP-Campo-G2-ROTALT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Para que serve o campo **G2\_ROTALT** do **MATA632 - Roteiro de Operações**? **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O campo **G2\_ROTALT - Roteiro de Operações Alternativo** refere-se ao **roteiro alternativo** utilizado no **MATA690 - Carga Máquina**, se uma **operação** não pode ser alocada no recurso determinado no **roteiro principal**, mas tem o campo **G2\_ROTALT** preenchido o Sistema considerará todas as **operações** deste **roteiro alternativo** como substitutas da **operação** em questão.  
 **Exemplo  
Roteiro** 01 com **operações** A, B e C  
**Roteiro** 03 com **operações** M e N  
  
Se para o **roteiro** 01, **operação** A for determinado como alternativo o **roteiro** 03 o Sistema alocará:  
M  
N  
B  
C  
  
Sendo M e N provenientes do **roteiro alternativo** 03.
