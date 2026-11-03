---
article_id: 360015904692
category: MDFe - Manifesto de Carga
content_hash: daef4c4dd5889e66dd0faee15c5a7e990d29d6dc4fd00689f35ff54a497a3f1b
fetched_at: '2026-06-28T22:40:08.322807+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Rejeição
  663: Percurso informado inválido'
type: support-article
updated_at: '2025-06-17T17:32:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015904692-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Rejei%C3%A7%C3%A3o-663-Percurso-informado-inv%C3%A1lido
---

**Dúvida**Como resolver a rejeição 663: Percurso informado inválido ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Solução**

Se modal Rodoviário, o grupo de informações de UF de percurso deverá ser preenchido na ordem Origem – Destino sempre que existir pelo menos uma ***UF entre a UF de carregamento e UF de descarregamento.***

1. Preencher a UF de percurso na aba ***Carregamento/Percurso*** -> **Municípios de carregamento e Percurso do veículo.** Para adicionar mais de uma UF, deve clicar a seta para baixo.

![20220801_161145.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7869932583191)

* ***Saiba mais:***

A regra será aplicada considerando as ***divisas possíveis na ordem definida*** para o percurso. A Tag <UFPer> - Não é necessário repetir as ***UF de Início e Fim, ou seja, na opção Percurso*** não é necessário repetir as ***UF de Início (Carregamento) e Fim (Descarregamento)*** informadas no cabeçalho.

* Exemplo de ***UF de Percurso:***

De RS para SP, informei a UF de SC e abaixo informei a UF de PA, o ***MDF-e foi autorizado.***
