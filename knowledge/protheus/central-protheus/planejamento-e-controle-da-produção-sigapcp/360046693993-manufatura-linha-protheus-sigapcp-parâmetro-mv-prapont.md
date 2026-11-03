---
article_id: 360046693993
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6bf67ea4dbfbbf58ec5121a4d1fd601c9d57cc36b619b9984b27d92ec6446ea3
fetched_at: '2026-06-28T22:42:44.733171+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Parâmetro MV_PRAPONT
type: support-article
updated_at: '2025-12-19T18:48:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046693993-Manufatura-Linha-Protheus-SIGAPCP-Par%C3%A2metro-MV-PRAPONT
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37151843487639)*** Tempo aproximado para leitura:**00:01:08 min**  
  
**Dúvida**  
Para que serve o parâmetro **MV\_PRAPONT - Configura prioridade no Apontamento de Produção: 1-Tipo de Movimentação / 2-Cadastro de Produto**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Quando o parâmetro **MV\_PRAPONT** possui o conteúdo**2**, o sistema considera que o produto determina se a quantidade produzida será encaminhado para **Qualidade**, validando se o campo **B1\_NUMCQPR - Produções CQ** da aba **CQ** do **MATA010 - Cadastro de Produtos** tem conteúdo diferente de zero.  
Já quando o parâmetro **MV\_PRAPONT** possui o conteúdo **1**, é a **TM - Tipo de movimento**que determina se será encaminhado. Ou seja, verifica no **MATA230 - Tipo de Movimentação** o campo **F5\_ENVCQPR -** **Envia p/ CQ?**.   
  
**Importante**  
O objetivo do **MV\_PRAPONT** é permitir diferenciar produtos que serão enviados para **CQ - Controle de Qualidade** dos produtos que não precisam de inspeção após apontamento, mesmo utilizando a mesma **TM** padrão informada no parâmetro **MV\_TMPAD - Tipo de movimentação padrão para produção PCP**.
