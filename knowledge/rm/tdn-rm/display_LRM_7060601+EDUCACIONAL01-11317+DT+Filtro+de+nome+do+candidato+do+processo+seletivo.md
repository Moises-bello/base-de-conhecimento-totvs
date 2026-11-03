---
content_hash: 2277f1244a56ce362e26abbb3b227e6accfde5a29d2c132b763255308b4f6f84
fetched_at: '2026-06-29T00:10:27.098558+00:00'
page_id: '516217302'
product: rm
source: tdn-rm
title: 7060601 EDUCACIONAL01-11317 DT Filtro de nome do candidato do processo seletivo
type: documentation
url: https://tdn.totvs.com/display/LRM/7060601+EDUCACIONAL01-11317+DT+Filtro+de+nome+do+candidato+do+processo+seletivo
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Processo Seletivo |
| Função: | Inscrição do candidato  Local de prova do candidato  Arquivos do candidato  Documentação do candidato |
| Ticket: | 7060601 7047708 |
| Requisito/Story/Issue (informe o requisito relacionado) : | N/A |

## **02. SITUAÇÃO/REQUISITO**

Ao utilizar o filtro do nome do candidato nas visões de candidatos inscritos, documentação do candidato, local de prova do candidato e arquivos do candidato o sistema não retornava nenhum registro.

## **03. SOLUÇÃO**

Foi identificado uma inconsistência no filtro que invalidava os dados, sendo assim este teve que ser alterado e desmembrando em dois, agora existe o item nome do candidato e nome do candidato (Novo Portal), assim como já existe com os respectivos códigos de pessoa e código da pessoa (Novo Portal).
