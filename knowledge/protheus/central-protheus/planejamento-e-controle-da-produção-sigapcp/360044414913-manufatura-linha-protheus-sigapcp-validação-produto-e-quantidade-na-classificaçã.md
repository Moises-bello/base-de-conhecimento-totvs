---
article_id: 360044414913
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 01ae04248c95ce71263bb5bb2bec64d1c62a2b1565763f91d5599e558eba078e
fetched_at: '2026-06-28T22:42:47.120274+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Validação produto e quantidade na classificação
  de perda
type: support-article
updated_at: '2021-09-14T14:17:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044414913-Manufatura-Linha-Protheus-SIGAPCP-Valida%C3%A7%C3%A3o-produto-e-quantidade-na-classifica%C3%A7%C3%A3o-de-perda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:07 min****Dúvida**Existe alguma forma de validar o produto e quantidade na tela de classificação de perda no momento do apontamento da **OP - Ordem de Produção**?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060209013/mceclip0.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O Sistema não valida a quantidade, pois por exemplo, é realizada a perda de 10 peças na **OP**, porém a unidade de medida do **Produto** informada na perda pode ser em quilos, então a quantidade perdida do **Produto** pode ser maior do que a informada na tela de apontamento.  
Porém o Sistema pode validar o **Produto** informado. Para que seja possível apenas a inclusão de produtos que foram empenhados para a **OP**, é necessário ativar o parâmetro **MV\_PERBPRD - Bloqueia apontamentos de perda de produtos que não fazem parte da lista de empenhos da ordem de produção?**.
