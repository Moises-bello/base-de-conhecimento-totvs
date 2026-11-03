---
article_id: 360052013533
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 98357842d0d244af3821349dc12504d5ee169881f1dd39b79b2416ab1ace696c
fetched_at: '2026-06-28T22:38:28.468842+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - Help FWNOWIDTH no
  CRM
type: support-article
updated_at: '2022-03-14T18:40:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052013533-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-Help-FWNOWIDTH-no-CRM
---

**Ocorrência**Help: FWNOWIDTH no CRM:  
![help.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081419693/help.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento – A partir da versão 12.

**Causa**O Help é apresentado quando existe diferença  entre o tamanho dos campos das tabelas citadas no [Help On-line Protheus](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/fata300_tabelas.htm) e colocamos como destaque para analise as tabelas **AD1**, **ADY**, **ADZ**, **SB1**, **SA1** e **SUS** e os tamanho dos campos das tabelas relacionadas a descrição. Geralmente Apresentado pela diferença entre os campos do código do produto.

**Solução**

Por gentileza, verificar se existe divergência de tamanho dos campos das tabelas citadas acima.

Para que o erro em questão não seja apresentado, é necessário que os campos tenham o mesmo tamanho entre si.

Exemplo:  
**B1\_DESC** seja igual a **ADZ\_DESCRI  
ADY\_DESENT**seja igual a **AD1\_DESCRI**

**OBS**: Caso tenha que alterar o tamanho de algum campo, por favor, faça-o via Configurador para que o campo seja alterado também na tabela no banco de dados, além de ser alterada no dicionário **SX3**.
