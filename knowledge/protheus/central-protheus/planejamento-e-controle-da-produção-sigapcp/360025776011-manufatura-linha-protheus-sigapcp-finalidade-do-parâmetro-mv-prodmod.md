---
article_id: 360025776011
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6548ba358a66c6ba018f9e13b2c6672ff28b180cddbfde9200de518e08290aa9
fetched_at: '2026-06-28T22:42:43.261925+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Finalidade do parâmetro MV_PRODMOD
type: support-article
updated_at: '2023-10-05T19:18:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025776011-Manufatura-Linha-Protheus-SIGAPCP-Finalidade-do-par%C3%A2metro-MV-PRODMOD
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Qual a finalidade do campo **MV\_PRODMOD - Indicado para clientes que não utilizam produtos mão de obra e desejam melhorar a performance das rotinas de fechamento**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Por padrão o Sistema considera como produto correspondente a centro de custos aquele que estiver com o campo **B1\_COD** **- Código** preenchido com as letras **MOD** seguidas pelo código do centro de custo.  
  
Além disso, o Sistema também pode considerar o produto que estiver com o campo **B1\_CCCUSTO - Centro de Custo Custeio** preenchido, porém para que o Sistema considere este produto é necessário que o parâmetro **MV\_PRODMOD** esteja preenchido com **.T.**.
