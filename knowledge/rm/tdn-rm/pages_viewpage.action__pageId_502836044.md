---
content_hash: 2a0486eed347a2cc4167af1da7241723ec65da7263ee5d699a6b5cbcc862427f
fetched_at: '2026-06-29T00:10:25.343078+00:00'
page_id: '502836044'
product: rm
source: tdn-rm
title: DT Classificacao Candidatos - Desconsiderar candidatos que não executaram a
  prova
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502836044
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Processo Seletivo |
| Função: | Processo de apuração - Classificar candidatos |
| Ticket: | 6146282 |
| Requisito/Story/Issue (informe o requisito relacionado) : | N/A |

## **02. SITUAÇÃO/REQUISITO**

O processo de classificar candidatos por notas utilizando as notas das provas do TOTVS Avaliação e Pesquisa sempre desclassificava os candidatos que não tiveram a prova executada ou o gabarito importado através do processo de importar gabaritos.

## **03. SOLUÇÃO**

Foi implementado um novo parâmetro na tela da classificação que irá possibilitar ignorar os candidatos que não tiveram a prova executada no TOTVS Avaliação e Pesquisa ou o gabarito não foi importado. Por definição o parâmetro sempre estará marcado para manter o comportamento atual do sistema, caso o usuário opte por ignorar os candidatos que não executaram a prova, será necessário somente desmarcar o parâmetro.
