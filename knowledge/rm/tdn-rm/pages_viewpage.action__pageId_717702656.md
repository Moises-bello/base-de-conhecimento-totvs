---
content_hash: f77916a9080991709ba6e381efffe8f82f04db26248120e213732d27e76386f5
fetched_at: '2026-06-29T00:11:26.452616+00:00'
page_id: '717702656'
product: rm
source: tdn-rm
title: FISCAL01-18801 - DT - Órgão Público vinculado à União - Filial é Órgão Público
  Federal, Municipal ou Estadual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=717702656
version: 5
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro Filial - Dados Fiscais |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18832 |

## **02. SITUAÇÃO/REQUISITO**

Atualmente no cadastro da Filial, existe um campo para indicar que a Filial é "**Filial é Órgão Público"** (Anexo – Dados Fiscais - SubPasta Tipo de Estabelecimento). Devemos evoluir este campo para indicar se trata-se de um órgão público Federal (colocar as 3 esferas - Municipal, Estadual e Federal) ou criar outro meio que permita tal identificação.

## **03. SOLUÇÃO**

Realizada a inclusão de um CheckListBox no cadastro da Filial, para que seja definido se a Filial é Órgão Público Federal, Estadual ou Municipal.

Regras:

* As opções Federal, Estadual e Municipal só podem ser selecionadas caso a opção "Filial é Órgão Público" esteja marcada.

* Caso a opção "Filial é Órgão Público" seja desmarcada, os campos Federal, Estadual e Municipal serão limpos.

* A nova opção só será exibida após atualização da Base de Dados onde será criado o novo campo DFILIAL.TIPOORGAOPUBLICO

IMAGEM

Disponível a partir da biblioteca 12.1.2205
