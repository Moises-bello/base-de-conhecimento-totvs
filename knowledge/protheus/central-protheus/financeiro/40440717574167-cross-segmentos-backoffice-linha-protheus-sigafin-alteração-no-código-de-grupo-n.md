---
article_id: 40440717574167
category: Financeiro
content_hash: b289e844f8f088a821f04539f77a048d334be641b10b5c9af81e3e6542c1ec62
fetched_at: '2026-06-28T22:38:00.882254+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Alteração no código
  de grupo no campo X2_ARQUIVO da tabela SX2 diferente do código do grupo do logado
type: support-article
updated_at: '2026-05-14T17:40:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40440717574167-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Altera%C3%A7%C3%A3o-no-c%C3%B3digo-de-grupo-no-campo-X2-ARQUIVO-da-tabela-SX2-diferente-do-c%C3%B3digo-do-grupo-do-logado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40440717554199)**Tempo aproximado para leitura:**00:02:00 min**  
  
**Dúvida**  
No módulo financeiro pode alterar o código de grupo no campo X2\_ARQUIVO da tabela SX2 diferente do código do grupo do logado.

**Exemplo:**

Estou logado no grupo 01, e um campo fictício está com o conteúdo X2\_ARQUIVO=SE5**01**0, e posso realizar uma alteração no conteúdo do campo para o grupo 03, deixando com o conteúdo X2\_ARQUIVO=SE5**03**0?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Não é recomendável realizar a alteração do grupo na tabela SX2 (campo X2\_ARQUIVO).

O sistema Protheus é projetado para que as tabelas referenciadas no dicionário de dados pertençam ao mesmo grupo da empresa/filial logada. Ao realizar uma alteração manual para um grupo distinto, podem ocorrer inconsistências graves, tais como:

Falhas em consultas SQL (Querys);

Erros em pesquisas no banco de dados;

Comportamentos inesperados em rotinas de processamento;

Erros de integridade de dados não previstos e demais inconsistências não previstas.

#KCSBuilder
