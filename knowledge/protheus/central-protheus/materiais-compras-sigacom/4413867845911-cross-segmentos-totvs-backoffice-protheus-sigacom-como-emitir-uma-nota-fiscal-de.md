---
article_id: 4413867845911
category: Materiais - Compras (SIGACOM)
content_hash: 18d1aacc24f5e56c9b03e1d099d7c485363f9146f1744d1932c049c05aab8503
fetched_at: '2026-06-28T22:41:15.834136+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como emitir uma nota
  fiscal de produtor rural eletrônica ?
type: support-article
updated_at: '2021-11-22T20:12:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413867845911-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-emitir-uma-nota-fiscal-de-produtor-rural-eletr%C3%B4nica
---

**Dúvida**Após a implantação da Norma Técnica 2020.006 aonde os campos **D1\_ITEMORI, D1\_SERIORI, D1\_NFORI**foram bloqueados, como realizar a emissão de uma nota fiscal para produtor rural?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões  
  
**Solução**Conforme a documentação Técnica, foi corrigido para que haja exceções no caso de emissão de documento para produtor rural ([NFP-e) sistema impede preenchimento do campos de nota fiscal origem manualmente](https://tdn.totvs.com/display/public/PROT/11853566+DMANMAT02-33814+DT+%28NFP-e%29+sistema+impede+preenchimento+do+campos+de+nota+fiscal+origem+manualmente))

Com isso é necessário informar no cadastro de fornecedor o campo A2\_INDRUR  igual a 1, 2 ou 3

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413867670423/mceclip0.png)

O sistema irá habilitar os campos **D1\_NFORI** (Docto. Orig.), **D1\_SERIORI** (Serie Orig.) e **D1\_ITEMORI** (Item Orig.) para edição, ficando bloqueado os campos **F1\_INDPRES e F1\_CODA1U.**

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
