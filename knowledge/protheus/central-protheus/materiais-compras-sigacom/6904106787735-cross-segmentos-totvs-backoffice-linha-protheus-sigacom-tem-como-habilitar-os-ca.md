---
article_id: 6904106787735
category: Materiais - Compras (SIGACOM)
content_hash: 5b512770adcc32c82d0dfd4d86556d76be58b6c64b5649d16e0076ab23b30db0
fetched_at: '2026-06-28T22:41:12.764306+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGACOM - Tem como habilitar
  os campos C1_PRECO e C1_TOTAL da tabela de Solicitação de Compras ?
type: support-article
updated_at: '2024-11-13T12:19:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6904106787735-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Tem-como-habilitar-os-campos-C1-PRECO-e-C1-TOTAL-da-tabela-de-Solicita%C3%A7%C3%A3o-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25483745494807) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como habilitar os campos Campos C1\_PRECO e C1\_TOTAL ?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

Os campos ***C1\_PRECO*** e ***C1\_TOTAL*** não possuem por padrão o flag de Exibição no browse da rotina de Solicitaçaõ de Compras habilitado, pois na Solicitação de Compras será considerada somente a quantidade de itens (C1\_QUANT) da Solicitação.

Apesar de ser possivel habilitar sua exibição no browse da rotina ***MATA110***, pelo padrão do sistema não é possível habilitar estes campos para aparecer ou para o preenchimento de informação no grid/itens na rotina de Solicitação de Compras (***MATA110***).

Esta não exibição dos campos ***C1\_PRECO*** e ***C1\_TOTAL*** nos Itens da Solicitação de compras se trata de fato da forma como o sistema padrão trabalha.

Estes campos não possuem utilização no processo do Compras padrão do Brasil, possuindo utilização apenas em processos/fonte do "Protheus Mercado Internacional (Localizações)".

Caso haja necessidade de inserção de informações nos itens da SC conforme os processos da empresa, orienta-se a criação de campos customizados de acordo a necessidade existente.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
