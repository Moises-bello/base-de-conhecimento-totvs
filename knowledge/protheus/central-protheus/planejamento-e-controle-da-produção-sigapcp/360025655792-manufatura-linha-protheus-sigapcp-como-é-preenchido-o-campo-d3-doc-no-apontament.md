---
article_id: 360025655792
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 356cb452ba073b22082b2921ea8a107f124c176f468b9c356e658889a187c584
fetched_at: '2026-06-28T22:42:41.085437+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como é preenchido o campo D3_DOC no
  apontamento de produção
type: support-article
updated_at: '2021-05-26T11:32:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025655792-Manufatura-Linha-Protheus-SIGAPCP-Como-%C3%A9-preenchido-o-campo-D3-DOC-no-apontamento-de-produ%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:50 min****Dúvida**Qual a regra para o preenchimento do campo **D3\_DOC - Número de Documento** no **Apontamento de produção - MATA250**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O Sistema tenta preencher o campo **D3\_DOC**com o número da ordem de produção, porém se ele encontrar algum outro registro na tabela **SD3 - Movimentação Internas** com esse número no campo **D3\_DOC**, ele faz o preenchimento do campo considerando o próximo número disponível na tabela **SD3**, para o campo**D3\_DOC**.  
Se houver necessidade de gerar um outro número para o campo **D3\_DOC**, o Sistema verifica através do índice **D3\_FILIAL - Filial + D3\_DOC + D3\_COD - Produto**, o valor do campo **D3\_DOC** para o último registro, e ao valor encontrado, soma mais 1.
