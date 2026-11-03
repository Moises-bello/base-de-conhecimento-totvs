---
article_id: 16693352223127
category: Contabilidade Gerencial - Relatórios Razões
content_hash: 8a138a26a90b681e941a82c625fec6d93c5390bf0472ac76100d660cde04079e
fetched_at: '2026-06-28T22:40:41.139195+00:00'
product: protheus
section_id: 1500001548782
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBR400 - GERAÇÃO DOS
  RAZÃO CONTÁBIL COM O HISTORICO EM UMA LINHA UNICA
type: support-article
updated_at: '2023-08-14T14:36:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16693352223127-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR400-GERA%C3%87%C3%83O-DOS-RAZ%C3%83O-CONT%C3%81BIL-COM-O-HISTORICO-EM-UMA-LINHA-UNICA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16693383125911) Tempo aproximado para leitura: 00:03:00 min **Dúvida**Como realizar a unificação do Histórico do Lançamento no Razão Contábil, quando a quebra de histórico?

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**Para que a quebra do Histórico (CT2\_HIST) fique somente em uma única linha no Razão Contábil (CTBR400), será necessário deixar o parâmetro MV\_CTBRAZB igual a .T. (true).

com o parâmetro MV\_CTBRAZB igual a .T. o sistema concatena o histórico em uma só linha, veja:  
-O cadastro do lançamento:  
![](https://totvssuporte.zendesk.com/attachments/token/d2a61qNe0a9NqJORQcH8hfWyi/?name=image.png)  
   
-Com parâmetro MV\_CTBRAZB  igual a .T.:  
![](https://totvssuporte.zendesk.com/attachments/token/Fesz1QEJIFoQqrQzjw5pUcgvW/?name=image.png)  
   
-Com parâmetro igual a .F. ou inexistente na base:  
![](https://totvssuporte.zendesk.com/attachments/token/XSrWoozXLAGN6aSrrNukh99mD/?name=image.png)
