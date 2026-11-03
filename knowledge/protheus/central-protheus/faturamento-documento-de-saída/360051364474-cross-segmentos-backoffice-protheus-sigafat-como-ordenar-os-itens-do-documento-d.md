---
article_id: 360051364474
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 85a0e65ee172c9f0c30bbb95151eb1860d102211576fc40a0eb3ecaec81ac2c5
fetched_at: '2026-06-28T22:38:44.021058+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como ordenar os itens do
  documento de saída
type: support-article
updated_at: '2026-04-13T19:55:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051364474-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-ordenar-os-itens-do-documento-de-sa%C3%ADda
---

**Dúvida**

Como ordenar os itens do documento de saída?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**  
Os fontes que realizam a transmissão da NF-e, a gravação do XML e a impressão do DANFE, não realizam alteração na ordem dos itens.  
A ordem é definida na Preparação do Documento de Saída para gravação das linhas de itens na tabela SD2.

Para definir a ordem de gravação acesse a Rotina "Documentos de Saída (MATA460A)" em "Outras Ações > Ordem":

![](https://tdn.totvs.com/download/attachments/338374819/image2018-2-19_16-22-27.png?version=1&modificationDate=1519068799000&api=v2)

Selecione a ordem desejada e gere o Documento de Saída:

![](https://tdn.totvs.com/download/attachments/338374819/image2018-2-19_16-26-38.png?version=1&modificationDate=1519068799000&api=v2)

Caso deseje editar os Índices (Cadastrar novos ou definir uma única opção a ser utilizada) pode-se realizar a manutenção no Dicionário SIX da Tabela SC9:

![](https://tdn.totvs.com/download/attachments/338374819/image2018-2-21_11-22-47.png?version=1&modificationDate=1519222967000&api=v2)

No entanto, é importante ressaltar que alterações no índice refletirão também na consulta do índice pela função de Pesquisar desta e de demais rotinas que exibem a Tabela SC9:

![](https://tdn.totvs.com/download/attachments/338374819/image2018-2-21_11-25-48.png?version=1&modificationDate=1519223148000&api=v2)

![](https://tdn.totvs.com/download/attachments/338374819/image2018-2-21_11-29-51.png?version=1&modificationDate=1519223392000&api=v2)

**Observações:**

Caso a Preparação do Documento de Saída seja realizado pela rotina "**Pedidos de Venda (MATA410)"**  em “Outras Ações > Prep. Doc. Saída", o sistema não ordena seu índice pela SC9 (e sim pela SC6).

Só é possível definir a ordem de Faturamento pela rotina **"Documentos de Saída (MATA460A)".**

O botão "Ordem" não tem efeito na visualização do browser da rotina, ele tem efeito somente na ordem da preparação do docto de saída, ou seja, no documento gerado, o que determina a ordem de exibição no browser da rotina são os filtros.

**Saiba Mais:**

[**Ordem dos itens / produtos no Documento de Saída (Nota Fiscal)**](https://tdn.totvs.com/x/ozArF)
