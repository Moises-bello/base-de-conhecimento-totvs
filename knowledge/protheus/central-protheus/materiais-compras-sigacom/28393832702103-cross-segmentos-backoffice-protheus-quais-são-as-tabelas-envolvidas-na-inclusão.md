---
article_id: 28393832702103
category: Materiais - Compras (SIGACOM)
content_hash: 0bfd4aeaeadb1605af57182d75da1b3108bdf7af5df781160b0695be93790637
fetched_at: '2026-06-28T22:41:11.863222+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Quais são as tabelas envolvidas na
  Inclusão do Documento de Entrada?
type: support-article
updated_at: '2024-12-09T19:32:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28393832702103-Cross-Segmentos-Backoffice-Protheus-Quais-s%C3%A3o-as-tabelas-envolvidas-na-Inclus%C3%A3o-do-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28393862608407) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais são as tabelas envolvidas na Incusão do Documento de Entrada?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as Versões  
  
**Solução**

A inclusão de um documento de entrada envolve, principalmente, duas tabelas: **SD1** (itens do documento de entrada) e **SF1** (cabeçalho do documento de entrada). No entanto, dependendo da configuração do TES (Tipo de Entrada Selecionado), outras tabelas podem ser alimentadas, refletindo a integração com diversos módulos do sistema. Por exemplo:

* Se o documento for relacionado aos livros fiscais, as tabelas **SFT** e **SF3** podem ser atualizadas.
* Caso envolva o **ativo fixo**, as tabelas **SN1** e **SN3** podem ser preenchidas.
* Se houver rateio por centro de custo, registros podem ser gerados na tabela **SDE**.
* Se um título a pagar for gerado a partir dessa nota fiscal, informações serão inseridas na tabela **SE2**.

Portanto, embora as tabelas **SD1** e **SF1** sejam as principais responsáveis pela inclusão do documento de entrada, a integração com outros módulos pode gerar registros em diversas outras tabelas, dependendo das configurações do TES.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
