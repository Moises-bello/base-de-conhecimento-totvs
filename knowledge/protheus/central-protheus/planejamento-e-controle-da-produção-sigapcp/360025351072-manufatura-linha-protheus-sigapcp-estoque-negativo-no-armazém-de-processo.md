---
article_id: 360025351072
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 0eabc08711d6b909c6c641b1e498d5284c66bba3de4110d59a8b4e5913385922
fetched_at: '2026-06-28T22:42:42.316830+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Estoque negativo no armazém de processo
type: support-article
updated_at: '2021-09-24T12:26:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025351072-Manufatura-Linha-Protheus-SIGAPCP-Estoque-negativo-no-armaz%C3%A9m-de-processo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min  
  
Dúvida**Por que está permitindo estoque negativo no armazém de processo se o parâmetro **MV\_ESTNEG - Identifica se o sistema permitira que os saldos em estoque dos produtos fique negativo através de movimentação** está desativado?  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
 **Solução**Isso ocorre porque o parâmetro **MV\_INDNEG - Indica se permite deixar estoque negativo quando material de apropriação indireta** está igual a **S - Sim**, desta forma o Sistema permitirá que o estoque fique negativo no armazém de processo.   
  
Se for **N - Não**, não permitirá que o estoque de produto com apropriação indireta fique negativo e se a opção no parâmetro for **E - Respeita MV\_ESTNEG** o Sistema obedecerá a mesma regra do parâmetro **MV\_ESTNEG** para o armazém de processo.
