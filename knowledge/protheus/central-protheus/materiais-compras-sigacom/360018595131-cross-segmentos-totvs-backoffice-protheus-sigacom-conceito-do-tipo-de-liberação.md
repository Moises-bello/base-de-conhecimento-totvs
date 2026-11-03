---
article_id: 360018595131
category: Materiais - Compras (SIGACOM)
content_hash: f96d61f5da39f4e1a7d126c27fd2c07916ecccc1a81dcc9c0c6260d3e9a3cee1
fetched_at: '2026-06-28T22:41:08.717240+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Conceito do Tipo de
  Liberação no Grupo de Aprovação
type: support-article
updated_at: '2024-02-27T20:10:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018595131-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Conceito-do-Tipo-de-Libera%C3%A7%C3%A3o-no-Grupo-de-Aprova%C3%A7%C3%A3o
---

**Dúvida**Conceito do Tipo de Liberação no Grupo de Aprovação  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**Segue abaixo o conceito do tipo de liberação onde é configurado no cadastro de Grupo de Aprovação que define qual será o tratamento da liberação do aprovador perante ao grupo. Existem três opções: **Usuário, Nivel e Documento**

- O tipo de liberação de **Usuário** libera apenas a pendencia do aprovador. Exemplo:

APROVADOR 001 - Nível: 01 - Tipo Lib.: Usuário  
APROVADOR 002 - Nível: 01 - Tipo Lib.: Usuário  
APROVADOR 003 - Nível: 01 - Tipo Lib.: Usuário

Neste caso será necessário a aprovação de todos os aprovadores para que o nível seja liberado.

- O tipo de liberação de **Nível** libera a pendencia de todo o nivel que o aprovador faz parte. Exemplo:

APROVADOR 001 - Nível: 01 - Tipo Lib.: Nível  
APROVADOR 002 - Nível: 01 - Tipo Lib.: Nível  
APROVADOR 003 - Nível: 01 - Tipo Lib.: Nível

Neste caso qualquer um dos aprovadores que liberar o documento, libera a pendencia do nível 01.

- O tipo de liberação de **Documento** libera a pendencia de todo o documento independente da quantidade de níveis. Exemplo:

APROVADOR 001 - Nível: 01 - Tipo Lib.: Nível  
APROVADOR 002 - Nível: 01 - Tipo Lib.: Documento  
APROVADOR 003 - Nível: 02 - Tipo Lib.: Nível

Neste caso se o aprovador 02 liberar o documento, o pedido será totalmente desbloqueado sem a necessidade da aprovação do nível 02.

**Obs:**Tipo de liberação de **Documento** não pula a sequência de níveis estipulada no grupo, sendo assim, só estará disponível a aprovação no momento que o documento percorrer os níveis anteriores.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
